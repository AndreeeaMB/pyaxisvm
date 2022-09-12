# -*- coding: utf-8 -*-
from typing import Iterable, Callable
from functools import partial

import numpy as np
import awkward as ak
from numpy import ndarray as Array

import matplotlib.tri as tri

from dewloosh.core import issequence
from dewloosh.core.tools import float_to_str_sig

from neumann.linalg import Vector
from neumann.array import minmax
from polymesh import PointCloud, CartesianFrame
from dewloosh.mpl import triplot
from polymesh.topo import TopologyArray, rewire
from polymesh.utils import decompose
from neumann.linalg.sparse.utils import count_cols

import axisvm
from .core.wrap import AxisVMModelItem, AxisVMModelItems, AxItemCollection
from .core.utils import (RMatrix3x3toNumPy, RMatrix2x2toNumPy,
                         RSurfaceCoordinates2list, triangulate as triang,
                         dcomp2int, fcomp2int, scomp2int, xlmscomp2int,
                         RXLAMSurfaceStresses2list, RSurfaceStresses2list,
                         get_xlam_strs_case, get_xlam_strs_comb,
                         get_xlam_effs_crit, RXLAMSurfaceEfficiencies2list)
from .attr import AxisVMAttributes, squeeze_attributes as dsqueeze
from .axsurface import SurfaceMixin, get_surface_attributes, surface_attr_fields


__all__ = ['IAxisVMDomain', 'IAxisVMDomains']


class AxDomainCollection(AxItemCollection):

    def __getattribute__(self, attr):
        if hasattr(self[0], attr):
            _attr = getattr(self[0], attr)
            if isinstance(_attr, Callable):
                def getter(i): return getattr(i, attr)
                funcs = map(getter, self)

                def inner(*args, **kwargs):
                    return list(map(lambda f: f(*args, **kwargs), funcs))
                return inner
            else:
                return list(map(lambda i: getattr(i, attr), self))
        else:
            return super().__getattribute__(attr)


class IAxisVMDomain(AxisVMModelItem, SurfaceMixin):
    """Wrapper for the `IAxisVMDomain` COM interface."""

    @property
    def model(self):
        return self.parent.model

    @property
    def attributes(self):
        return dsqueeze(self.parent.get_attributes(i=self.Index))

    @property
    def domain_attributes(self):
        return dsqueeze(self.parent.get_domain_attributes(i=self.Index))

    @property
    def tr(self):
        return self.transformation_matrix()

    @property
    def IsXLAM(self):
        return self.parent.IsXLAM[self.Index]

    def transformation_matrix(self) -> Array:
        return np.array(RMatrix3x3toNumPy(self.GetTrMatrix()[0]), dtype=float)

    def record(self):
        return self.parent.records(self.Index)

    def ABDS(self, *args, compose=True, **kwargs):
        A, B, D, S, *_ = self._wrapped.GetCustomStiffnessMatrix()
        A, B, D = [RMatrix3x3toNumPy(x) for x in (A, B, D)]
        S = RMatrix2x2toNumPy(S)
        if compose:
            res = np.zeros((8, 8), dtype=float)
            res[0:3, 0:3] = A
            res[0:3, 3:6] = B
            res[3:6, 0:3] = B
            res[3:6, 3:6] = D
            res[6:8, 6:8] = S
            return res
        else:
            return A, B, D, S

    def GetCustomStiffnessMatrix(self, to_numpy=False, compose=True):
        if to_numpy:
            return self.ABDS(compose=compose)
        else:
            return self._wrapped.GetCustomStiffnessMatrix()

    def coordinates(self, frame='global'):
        coords = self.model.coordinates()
        topo = self.topology()
        i = np.unique(topo) - 1
        if frame == 'global':
            return coords[i]
        elif frame == 'local':
            source = CartesianFrame(dim=3)
            target = CartesianFrame(self.transformation_matrix())
            return PointCloud(coords[i], frame=source).show(target)
        else:
            raise NotImplementedError

    def topology(self) -> TopologyArray:
        axms = self.model.Surfaces._wrapped
        sIDs = self.MeshSurfaceIds
        def fnc_corner(i): return list(axms.Item[i].GetContourPoints()[0])
        def fnc_mid(i): return list(axms.Item[i].GetMidPoints()[0])
        def fnc(i): return fnc_corner(i) + fnc_mid(i)
        return TopologyArray(ak.Array(list(map(fnc, sIDs))))

    def surface_coordinates(self):
        recs = self.GetMeshSurfacesCoordinates()[0]
        return ak.Array(list(map(RSurfaceCoordinates2list, recs)))

    def detach_mesh(self, triangulate=False, return_indices=False):
        topo = self.topology()
        inds = np.unique(topo) - 1
        topo = topo.to_array() - 1
        ecoords = self.surface_coordinates()
        topo = rewire(topo, inds, invert=True)
        coords = np.zeros((np.max(topo) + 1, 3), dtype=float)
        decompose(ecoords, topo, coords)
        source = CartesianFrame(dim=3)
        target = CartesianFrame(self.transformation_matrix())
        coords = PointCloud(coords, frame=source).show(target)[:, :2]
        if triangulate:
            topo = triang(topo)
        if return_indices:
            return coords, topo, inds + 1
        return coords, topo

    def plot(self, *args, **mpl_kw):
        coords, topo, _ = self.detach_mesh(
            return_indices=True, triangulate=True)
        triobj = tri.Triangulation(coords[:, 0], coords[:, 1], triangles=topo)
        if mpl_kw is None:
            mpl_kw = dict(axis='on')
        triplot(triobj, **mpl_kw)

    def plot_dof_solution(self, *args, component='ez', mpl_kw: dict = None,
                          DisplacementSystem=1, **kwargs):
        axm = self.model
        dofsol = axm.dof_solution(*args, DisplacementSystem=1, **kwargs)
        coords, topo, inds = self.detach_mesh(return_indices=True,
                                              triangulate=True)
        triobj = tri.Triangulation(coords[:, 0], coords[:, 1], triangles=topo)
        dofsol = dofsol[inds-1]
        if mpl_kw is None:
            mpl_kw = dict(nlevels=15, cmap='jet', axis='on',
                          offset=0., cbpad='10%', cbsize='10%',
                          cbpos='right')
        if isinstance(DisplacementSystem, str):
            if DisplacementSystem == 'local':
                DisplacementSystem = 0
        if DisplacementSystem == 0:
            source = CartesianFrame(dim=3)
            target = CartesianFrame(self.transformation_matrix())
            dofsol[:, :3] = Vector(dofsol[:, :3], frame=source).show(target)
            dofsol[:, 3:6] = Vector(dofsol[:, 3:6], frame=source).show(target)
        i = dcomp2int(component)
        #min, max = minmax(dofsol[:, i])
        compstr = component.upper()
        params = [self.Index, compstr]
        tmpl = "Domain {} - {}"
        mpl_kw['title'] = tmpl.format(*params)
        triplot(triobj, data=dofsol[:, i], **mpl_kw)

    def plot_forces(self, *args, component='nx', mpl_kw: dict = None,
                    smoothen=False, **kwargs):
        assert not smoothen, "Smoothing is not available at the moment."
        axm = self.model
        sids = np.array(self.MeshSurfaceIds) - 1
        forces = axm.generalized_surface_forces(*args, **kwargs)[sids]
        coords, topo = self.detach_mesh(triangulate=False)
        topo, forces = triang(topo, data=forces)  # triangulate with data
        triobj = tri.Triangulation(coords[:, 0], coords[:, 1], triangles=topo)
        if mpl_kw is None:
            mpl_kw = dict(nlevels=15, cmap='jet', axis='on',
                          offset=0., cbpad='10%', cbsize='10%',
                          cbpos='right')
        i = fcomp2int(component)
        #min, max = minmax(forces[:, :3, i])
        compstr = component.upper()
        params = [self.Index, compstr]
        tmpl = "Domain {} - {}"
        mpl_kw['title'] = tmpl.format(*params)
        triplot(triobj, data=forces[:, :3, i], **mpl_kw)

    def plot_stresses(self, *args, component=None, mpl_kw: dict = None,
                      smoothen=False, z='m', **kwargs):
        assert not smoothen, "Smoothing is not available at the moment."
        stresses = self.surface_stresses(*args, z=z, **kwargs)
        coords, topo = self.detach_mesh(triangulate=False)
        topo, stresses = triang(topo, data=stresses)  # triangulate with data
        triobj = tri.Triangulation(coords[:, 0], coords[:, 1], triangles=topo)
        if mpl_kw is None:
            mpl_kw = dict(nlevels=15, cmap='jet', axis='on',
                          offset=0., cbpad='10%', cbsize='10%',
                          cbpos='right')
        if self.IsXLAM:
            c = component if component is not None else 'sxx_m_t'
            ci = xlmscomp2int(c)
        else:
            c = component if component is not None else 'sxx'
            ci = scomp2int(c)
        #min, max = minmax(stresses[:, :3, ci])
        compstr = component.upper()
        params = [self.Index, compstr, z.lower()]
        tmpl = "Domain {} - {} - {}"
        mpl_kw['title'] = tmpl.format(*params)
        triplot(triobj, data=stresses[:, :3, ci], **mpl_kw)

    def surface_stresses(self, case=None, combination=None, z='m',
                         LoadCaseId=None, LoadCombinationId=None,
                         DisplacementSystem=0, LoadLevelOrModeShapeOrTimeStep=1):
        if self.IsXLAM:
            return self.xlam_surface_stresses(case=case, combination=combination,
                                              LoadCaseId=LoadCaseId,
                                              LoadCombinationId=LoadCombinationId,
                                              DisplacementSystem=DisplacementSystem,
                                              LoadLevelOrModeShapeOrTimeStep=LoadLevelOrModeShapeOrTimeStep)
        axm = self.model
        stresses = axm.Results.Stresses
        sids = self.MeshSurfaceIds

        LoadCaseId, LoadCombinationId = \
            stresses._get_case_or_component(case=case, combination=combination,
                                            LoadCaseId=LoadCaseId,
                                            LoadCombinationId=LoadCombinationId)

        config = dict(
            LoadCaseId=LoadCaseId,
            LoadCombinationId=LoadCombinationId,
            LoadLevelOrModeShapeOrTimeStep=LoadLevelOrModeShapeOrTimeStep,
            DisplacementSystem=DisplacementSystem
        )
        stresses.config(**config)

        if LoadCaseId is not None:
            def getter(i): return stresses.SurfaceStressesByLoadCaseId(i)[0]
        elif LoadCombinationId is not None:
            def getter(
                i): return stresses.SurfaceStressesByLoadCombinationId(i)[0]
        foo = partial(RSurfaceStresses2list, mode=z)
        return ak.Array(list(map(foo, map(getter, sids))))

    def xlam_surface_stresses(self, case=None, combination=None,
                              LoadCaseId=None, LoadCombinationId=None,
                              DisplacementSystem=0, LoadLevelOrModeShapeOrTimeStep=1,
                              AnalysisType=0, frmt='array', factor=None):
        assert self.IsXLAM, "This is not an XLAM domain!"
        
        def ak2np(r, i): return ak.flatten(r[:, :, i]).to_numpy()
        def ad2d(arr): return {i: ak2np(arr, i) for i in range(13)}
        
        if issequence(case):
            if factor is not None:
                assert issequence(factor), \
                    "If 'case' is an Iterable, 'factor' must be an Iterable of the same shape."
                assert len(case) == len(factor), \
                    "Lists 'case' and 'factor' must have equal lengths."
                res = sum([self.xlam_surface_stresses(
                    case=c,
                    frmt='array',
                    factor=f,
                    AnalysisType=AnalysisType,
                    LoadLevelOrModeShapeOrTimeStep=LoadLevelOrModeShapeOrTimeStep,
                    DisplacementSystem=DisplacementSystem
                ) for c, f in zip(case, factor)])
            else:
                res = [self.xlam_surface_stresses(
                    case=c,
                    frmt=frmt,
                    factor=1.0,
                    AnalysisType=AnalysisType,
                    LoadLevelOrModeShapeOrTimeStep=LoadLevelOrModeShapeOrTimeStep,
                    DisplacementSystem=DisplacementSystem
                ) for c in case]
            if frmt == 'dict':
                return ad2d(res)
            return res

        axm = self.model
        stresses = axm.Results.Stresses
        sids = self.MeshSurfaceIds

        LoadCaseId, LoadCombinationId = \
            stresses._get_case_or_component(case=case, combination=combination,
                                            LoadCaseId=LoadCaseId,
                                            LoadCombinationId=LoadCombinationId)

        config = dict(
            LoadCaseId=LoadCaseId,
            LoadCombinationId=LoadCombinationId,
            LoadLevelOrModeShapeOrTimeStep=LoadLevelOrModeShapeOrTimeStep,
            DisplacementSystem=DisplacementSystem
        )
        stresses.config(**config)

        if LoadCaseId is not None:
            getter = partial(get_xlam_strs_case, stresses, LoadCaseId,
                             LoadLevelOrModeShapeOrTimeStep, AnalysisType)
        elif LoadCombinationId is not None:
            getter = partial(get_xlam_strs_comb, stresses, LoadCombinationId,
                             LoadLevelOrModeShapeOrTimeStep, AnalysisType)
        foo = partial(RXLAMSurfaceStresses2list)
        factor = 1.0 if factor is None else float(factor)
        res = factor * ak.Array(list(map(foo, map(getter, sids))))
        if frmt == 'dict':
            return ad2d(res)
        return res

    def critical_xlam_surface_efficiencies(self, *args, CombinationType=None,
                                           AnalysisType=None, Component=None,
                                           MinMaxType=None, **kwargs):
        axm = self.model
        stresses = axm.Results.Stresses

        def inner(sid):
            params = dict(
                SurfaceId=sid, MinMaxType=MinMaxType,
                CombinationType=CombinationType,
                AnalysisType=AnalysisType, Component=Component,
            )
            rec = get_xlam_effs_crit(stresses, **params)
            return np.array(RXLAMSurfaceEfficiencies2list(rec))

        return ak.Array(list(map(inner, self.MeshSurfaceIds)))

    def critical_xlam_data(self, *args, CombinationType=None,
                           AnalysisType=0, **kwargs):
        Surfaces = self.model.Surfaces
        dparams = dict(
            MinMaxType=1,
            CombinationType=CombinationType,
            AnalysisType=AnalysisType,
            Component=4  # xse_Max
        )

        sid, nid, f, lc = (None,) * 4
        data = self.critical_xlam_surface_efficiencies(**dparams)
        cuts = count_cols(data)
        eff_max = ak.flatten(data[:, :, -1]).to_numpy()
        imax = np.argmax(eff_max)
        csum = np.cumsum(cuts)
        iS = np.where(csum > imax)[0][0]
        iN = imax - csum[iS-1]
        sid = self.MeshSurfaceIds[iS]
        nid = self.topology()[iS, iN]

        if cuts[iS] == 6:
            SurfaceVertexType = 0 if iN < 3 else 1
        elif cuts[iS] == 8:
            SurfaceVertexType = 0 if iN < 4 else 1
        else:
            raise NotImplementedError

        sparams = dict(
            SurfaceVertexType=SurfaceVertexType,
            SurfaceVertexId=nid,
            MinMaxType=1,
            CombinationType=CombinationType,
            AnalysisType=AnalysisType,
            Component=4
        )
        _, f, lc = Surfaces[sid].critical_xlam_efficiency(**sparams)
        return f, lc, (sid, nid)

    def _get_attrs(self):
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("Name", self.Name, "{}"))
        attrs.append(("Index", self.Index, "{}"))
        attrs.append(("UID", self._wrapped.UID, "{}"))
        attrs.append(("N Surfaces", len(self.MeshSurfaceIds), "{}"))
        attrs.append(("Area", self.Area, axisvm.FLOAT_FORMAT))
        attrs.append(("Volume", self.Volume, axisvm.FLOAT_FORMAT))
        attrs.append(("Weight", self.Weight, axisvm.FLOAT_FORMAT))
        return attrs


class IAxisVMDomains(AxisVMModelItems, SurfaceMixin):
    """Wrapper for the `IAxisVMDomains` COM interface."""

    __itemcls__ = IAxisVMDomain
    __collectioncls__ = AxDomainCollection

    def __getitem__(self, *args) -> IAxisVMDomain:
        return super().__getitem__(*args)

    @property
    def tr(self) -> Array:
        return self.transformation_matrices()

    @property
    def frames(self) -> Array:
        return self.transformation_matrices()

    @property
    def attributes(self):
        return self.get_attributes()

    @property
    def domain_attributes(self):
        return self.get_domain_attributes()

    @property
    def XLAMItems(self):
        return filter(lambda i: self.IsXLAM[i.Index], self[:])

    @property
    def XLAMCount(self):
        return len(self.XLAMItems)

    def topology(self, *args,  i=None) -> TopologyArray:
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            return self[i].topology()
        if isinstance(i, np.ndarray):
            ids = i
        else:
            if isinstance(i, Iterable):
                ids = np.array(i, dtype=int)
            else:
                ids = np.array(list(range(self.Count))) + 1
        return np.vstack(list(map(lambda i: self[i].topology(), ids)))

    def _get_attributes_raw(self, *args, i=None, **kwargs) -> Iterable:
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            return self.BulkGetDomains([i])
        if isinstance(i, np.ndarray):
            ids = i
        else:
            if isinstance(i, Iterable):
                ids = np.array(i, dtype=int)
            else:
                ids = np.array(list(range(self.Count))) + 1
        return self.BulkGetDomains(ids)

    def get_domain_attributes(self, *args, i=None, raw=False, fields=None,
                              rec=None, **kwargs) -> AxisVMAttributes:
        if fields is None:
            fields = surface_attr_fields + ['LineIdCounts', 'BulkLineIds']
        elif isinstance(fields, str):
            fields = [fields]
        elif isinstance(fields, Iterable):
            fields = list(filter(lambda i: i in surface_attr_fields, fields))
        if rec is None:
            i = i if len(args) == 0 else args[0]
            rec = self._get_attributes_raw(i=i)
        if raw:
            return rec
        else:
            LineIdCounts, BulkLineIds, SurfaceAttrs, *_ = rec
            data = get_surface_attributes(self, *args, i=i, attr=SurfaceAttrs,
                                          fields=fields, raw=False, **kwargs)
            if 'LineIdCounts' in fields:
                data['LineIdCounts'] = LineIdCounts
            if 'BulkLineIds' in fields:
                data['BulkLineIds'] = BulkLineIds
            return AxisVMAttributes(data)

    def get_attributes(self, *args, **kwargs) -> AxisVMAttributes:
        return self.get_domain_attributes(*args, **kwargs)

    def get_xlam_domain_indices(self):
        return list(map(lambda i: i.Index, self.XLAMItems))

    def records(self, *args, **kwargs):
        return self.get_domain_attributes(*args, raw=True, **kwargs)
