# -*- coding: utf-8 -*-
from typing import Iterable

import numpy as np
import awkward as ak
from numpy import ndarray as Array

import matplotlib.tri as tri

from dewloosh.math.linalg import Vector
from dewloosh.mesh import PointCloud, CartesianFrame
from dewloosh.mesh.tri import triplot
from dewloosh.mesh.topo import TopologyArray, rewire
from dewloosh.mesh.utils import decompose

import axisvm
from .core.wrap import AxisVMModelItem, AxisVMModelItems
from .core.utils import (RMatrix3x3toNumPy, RMatrix2x2toNumPy,
                         RSurfaceCoordinates2list, triangulate as triang,
                         dcomp2int)
from .attr import AxisVMAttributes
from .axsurface import SurfaceMixin, get_surface_attributes, surface_attr_fields


__all__ = ['IAxisVMDomain', 'IAxisVMDomains']


class IAxisVMDomain(AxisVMModelItem, SurfaceMixin):
    """Wrapper for the `IAxisVMDomain` COM interface."""

    @property
    def model(self):
        return self.parent.model

    @property
    def attributes(self):
        return self.parent.get_attributes(self.Index)

    @property
    def domain_attributes(self):
        return self.parent.get_domain_attributes(self.Index)

    @property
    def tr(self):
        return self.transformation_matrix()

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
        topo = self.topology().to_array() - 1
        ecoords = self.surface_coordinates()
        inds = np.unique(topo)
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

    def plot_dof_solution(self, component='ez', mpl_kw: dict = None,
                          DisplacementSystem=1, LoadCaseId=1,
                          LoadLevelOrModeShapeOrTimeStep=1):
        axm = self.model
        dofsol = axm.dof_solution(DisplacementSystem=1, LoadCaseId=LoadCaseId,
                                  LoadLevelOrModeShapeOrTimeStep=LoadLevelOrModeShapeOrTimeStep)
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
        return triplot(triobj, data=dofsol[:, i], **mpl_kw)

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
            ids = np.array([i])
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
            fields = surface_attr_fields
        elif isinstance(fields, str):
            fields = [fields]
        elif isinstance(fields, Iterable):
            fields = list(filter(lambda i: i in surface_attr_fields, fields))
        if rec is None:
            i = i if len(args) == 0 else args[0]
            rec = self._get_attributes_raw(i)
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

    def records(self, *args, **kwargs):
        return self.get_domain_attributes(*args, raw=True, **kwargs)
