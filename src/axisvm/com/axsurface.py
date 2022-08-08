# -*- coding: utf-8 -*-
import numpy as np
import awkward as ak
from numpy import ndarray as Array
from typing import Iterable
from functools import partial

import awkward as ak

from sigmaepsilon.mesh.topo import TopologyArray, unique_topo_data
from sigmaepsilon.mesh.topo.topodata import edges_Q4
from sigmaepsilon.mesh.tri.triutils import edges_tri
from sigmaepsilon.mesh.plotting.plotly import plot_triangles_3d
from sigmaepsilon.mesh.topo import detach as detach_mesh

import axisvm
from .core.wrap import AxisVMModelItem, AxisVMModelItems
from .core.utils import (RMatrix3x3toNumPy, triangulate, RSurfaceForces2list, 
                         RSurfaceStresses2list)
from .attr import AxisVMAttributes

surfacetype_to_str = {
    0: 'Hole',
    1: 'MembraneStress',
    2: 'MembraneStrain',
    3: 'Plate',
    4: 'Shell',
}

surface_attr_fields = ['Thickness', 'SurfaceType', 'RefZId', 'RefXId',
                       'MaterialId', 'Characteristics', 'ElasticFoundation',
                       'NonLinearity', 'Resistance']

surface_data_fields = ['N', 'Attr', 'DomainIndex', 'LineIndex1',
                       'LineIndex2', 'LineIndex3', 'LineIndex4']

def xyz(p): 
    return [p.x, p.y, p.z]

def get_surface_attributes(obj, *args, i=None, fields=None, raw=False,
                           rec=None, attr=None, **kwargs):
    if fields is None:
        fields = surface_attr_fields
    elif isinstance(fields, str):
        fields = [fields]
    elif isinstance(fields, Iterable):
        fields = list(filter(lambda i: i in surface_attr_fields, fields))
    if attr is None:
        if rec is None:
            i = i if len(args) == 0 else args[0]
            rec = obj._get_attributes_raw(i)
        if raw:
            return rec
        else:
            rec = rec[0]
        attr = list(map(lambda r: r.Attr, rec))

    data = {}
    if 'Thickness' in fields:
        data['Thickness'] = list(map(lambda a: a.Thickness, attr))
    if 'SurfaceType' in fields:
        data['SurfaceType'] = list(
            map(lambda a: surfacetype_to_str[a.SurfaceType], attr))
    if 'RefXId' in fields:
        data['RefXId'] = list(map(lambda a: a.RefXId, attr))
    if 'RefZId' in fields:
        data['RefZId'] = list(map(lambda a: a.RefZId, attr))
    if 'MaterialId' in fields:
        data['MaterialId'] = list(map(lambda a: a.MaterialId, attr))
    if 'Characteristics' in fields:
        data['Characteristics'] = list(map(lambda a: a.Charactersitics, attr))
    if 'ElasticFoundation' in fields:
        data['ElasticFoundation'] = list(
            map(lambda a: xyz(a.ElasticFoundation), attr))
    if 'NonLinearity' in fields:
        data['NonLinearity'] = list(
            map(lambda a: xyz(a.NonLinearity), attr))
    if 'Resistance' in fields:
        data['Resistance'] = list(map(lambda a: xyz(a.Resistance), attr))
    return AxisVMAttributes(data)


class SurfaceMixin:

    def surface_edges(self, topology=None):
        topo = self.topology() if topology is None else topology
        w = topo.widths()
        i6 = np.where(w == 6)[0]
        i8 = np.where(w == 8)[0]
        try:
            eT, _ = unique_topo_data(edges_tri(topo[i6, :3].to_numpy()))
        except Exception:
            eT, _ = unique_topo_data(edges_tri(topo[i6, :3]))
        try:
            eQ, _ = unique_topo_data(edges_Q4(topo[i8, :4].to_numpy()))
        except Exception:
            eQ, _ = unique_topo_data(edges_Q4(topo[i8, :4]))        
        return np.vstack([eT, eQ])

    def triangles(self, topology=None):
        topo = self.topology() if topology is None else topology
        return triangulate(topo)
        
    def plot(self, *args, scalars=None, plot_edges=True, detach=False, 
             backend='mpl', **kwargs):
        topo = self.topology()
        triangles = self.triangles(topo) - 1
        edges = None
        if plot_edges:
            edges = self.surface_edges(topo) - 1
        if detach:
            #ids = np.unique(triangles) + 1
            coords = self.model.coordinates()
            coords, triangles = detach_mesh(coords, triangles)
        else:
            coords = self.model.coordinates()
        if backend == 'mpl':
            pass
        return plot_triangles_3d(coords, triangles, data=scalars,
                                 plot_edges=plot_edges, edges=edges)


class IAxisVMSurface(AxisVMModelItem, SurfaceMixin):
    """Wrapper for the `IAxisVMSurface` COM interface."""

    def topology(self) -> TopologyArray:
        return self.parent.topology(self.Index)

    def record(self):
        return self.parent.records(self.Index)

    def normal(self) -> Array:
        return self.parent.normals(self.Index)

    def transformation_matrix(self) -> Array:
        return self.parent.transformation_matrices(self.Index)

    @property
    def tr(self):
        return self.transformation_matrix()

    @property
    def attributes(self):
        return self.parent.get_attributes(self.Index)

    @property
    def surface_attributes(self):
        return self.parent.get_surface_attributes(self.Index)

    def _get_attrs(self) -> Iterable:
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("Index", self.Index, "{}"))
        attrs.append(("UID", self._wrapped.UID, "{}"))
        attrs.append(("Area", self.Area, axisvm.FLOAT_FORMAT))
        attrs.append(("Volume", self.Volume, axisvm.FLOAT_FORMAT))
        attrs.append(("Weight", self.Weight, axisvm.FLOAT_FORMAT))
        return attrs


class IAxisVMSurfaces(AxisVMModelItems, SurfaceMixin):
    """Wrapper for the `IAxisVMSurfaces` COM interface."""

    __itemcls__ = IAxisVMSurface

    @property
    def tr(self) -> Array:
        return self.transformation_matrices()

    @property
    def t(self) -> Array:
        k = 'Thickness'
        return np.array(self.get_surface_attributes(fields=[k])[k])

    @property
    def n(self) -> Array:
        return self.normals()

    @property
    def frames(self) -> Array:
        return self.transformation_matrices()

    @property
    def attributes(self):
        return self.get_attributes()

    @property
    def surface_attributes(self):
        return self.get_surface_attributes()

    def topology(self, *args,  i=None) -> TopologyArray:
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            s = self[i]._wrapped
            data = list(s.GetContourPoints()[0]) + list(s.GetMidPoints()[0])
            return np.array(data, dtype=int)
        ids = None
        if isinstance(i, np.ndarray):
            ids = i
        else:
            if isinstance(i, Iterable):
                ids = np.array(i, dtype=int)
            else:
                ids = np.array(list(range(self.Count))) + 1
        if ids is not None:
            s = self._wrapped
            def fnc_corner(i): return list(s[i].GetContourPoints()[0])
            def fnc_mid(i): return list(s[i].GetMidPoints()[0])
            def fnc(i): return fnc_corner(i) + fnc_mid(i)
            return TopologyArray(ak.Array(list(map(fnc, ids))))
        return None

    def records(self, *args, **kwargs) -> Iterable:
        return self._get_attributes_raw(*args, **kwargs)[0]

    def get_attributes(self, *args, i=None, fields=None, raw=False, **kwargs):
        i = i if len(args) == 0 else args[0]
        dfields, afields = [], []
        if fields is None:
            afields = surface_attr_fields
            dfields = surface_data_fields
        else:
            if isinstance(fields, str):
                fields = [fields]
            if isinstance(fields, Iterable):
                afields = list(
                    filter(lambda i: i in surface_attr_fields, fields))
                dfields = list(
                    filter(lambda i: i in surface_data_fields, fields))
        fields = dfields + afields
        rec_raw = self._get_attributes_raw(i)
        if raw:
            return rec_raw
        else:
            rec = rec_raw[0]
        data = {}
        if 'Attr' in fields:
            data.update(self.get_surface_attributes(_rec=rec_raw))
        else:
            if len(afields) > 0:
                attr = self.get_surface_attributes(
                    _rec=rec_raw, fields=afields)
                for f in afields:
                    data[f] = attr[f]
        if 'N' in dfields:
            data['N'] = list(map(lambda r: r.N, rec))
        if 'DomainIndex' in dfields:
            data['DomainIndex'] = list(map(lambda r: r.DomainIndex, rec))
        if 'LineIndex1' in dfields:
            data['LineIndex1'] = list(map(lambda r: r.LineIndex1, rec))
        if 'LineIndex2' in dfields:
            data['LineIndex2'] = list(map(lambda r: r.LineIndex2, rec))
        if 'LineIndex3' in dfields:
            data['LineIndex3'] = list(map(lambda r: r.LineIndex3, rec))
        if 'LineIndex4' in dfields:
            data['LineIndex4'] = list(map(lambda r: r.LineIndex4, rec))
        return AxisVMAttributes(data)

    def _get_attributes_raw(self, *args, i=None) -> Iterable:
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
        return self.model.Surfaces.BulkGetSurfaces(ids)

    def get_surface_attributes(self, *args, **kwargs) -> AxisVMAttributes:
        return get_surface_attributes(self, *args, **kwargs)

    def normals(self, *args, i=None) -> Array:
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            s = self[i]._wrapped
            def xyz(p): return [p.x, p.y, p.z]
            return np.array(xyz(s.GetNormalVector()[0]), dtype=float)
        if isinstance(i, np.ndarray):
            inds = i
        else:
            if isinstance(i, Iterable):
                inds = np.array(i, dtype=int)
            else:
                inds = np.array(list(range(self.Count))) + 1
        s = self._wrapped
        m = map(lambda i: s.Item[i].GetNormalVector()[0], inds)
        xyz = map(lambda p: [p.x, p.y, p.z], m)
        return np.array(list(xyz), dtype=float)

    def transformation_matrices(self, *args, i=None) -> Array:
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            s = self[i]._wrapped
            return np.array(RMatrix3x3toNumPy(s.GetTrMatrix()[0]), dtype=float)
        if isinstance(i, np.ndarray):
            inds = i
        else:
            if isinstance(i, Iterable):
                inds = np.array(i, dtype=int)
            else:
                inds = np.array(list(range(self.Count))) + 1
        s = self._wrapped
        rec = list(map(lambda i: s.Item[i].GetTrMatrix()[0], inds))
        return np.array(list(map(RMatrix3x3toNumPy, rec)), dtype=float)
    
    def generalized_surface_forces(self, *args, case=None, combination=None,
                                   DisplacementSystem=None, LoadCaseId=None,
                                   LoadLevelOrModeShapeOrTimeStep=None, 
                                   LoadCombinationId=None,**kwargs):
        axm = self.model
        if case is not None:
            LoadCombinationId = None
            if isinstance(case, str):
                LoadCases = axm.LoadCases
                imap = {LoadCases.Name[i]: i for i in range(
                    1, LoadCases.Count+1)}
                if case in imap:
                    LoadCaseId = imap[case]
                else:
                    raise KeyError("Unknown case with name '{}'".format(case))
            elif isinstance(case, int):
                LoadCaseId = case
        elif combination is not None:
            LoadCaseId = None
            if isinstance(combination, str):
                LoadCombinations = axm.LoadCombinations
                imap = {LoadCombinations.Name[i]: i for i in range(
                    1, LoadCombinations.Count+1)}
                if combination in imap:
                    LoadCombinationId = imap[combination]
                else:
                    raise KeyError(
                        "Unknown combination with name '{}'".format(combination))
            elif isinstance(combination, int):
                LoadCombinationId = combination
        forces = axm.Results.Forces
        if DisplacementSystem is None:
            DisplacementSystem = 1  # global
        if isinstance(DisplacementSystem, int):
            forces.DisplacementSystem = DisplacementSystem
        if LoadCaseId is not None:
            forces.LoadCaseId = LoadCaseId
        if LoadCombinationId is not None:
            forces.LoadCombinationId = LoadCombinationId
        if LoadLevelOrModeShapeOrTimeStep is None:
            LoadLevelOrModeShapeOrTimeStep = 1
        forces.LoadLevelOrModeShapeOrTimeStep = LoadLevelOrModeShapeOrTimeStep
        if LoadCaseId is not None:
            recs = forces.AllSurfaceForcesByLoadCaseId()[0]
        elif LoadCombinationId is not None:
            recs = forces.AllSurfaceForcesByLoadCombinationId()[0]
        return ak.Array(list(map(RSurfaceForces2list, recs)))
    
    def surface_stresses(self, *args, case=None, combination=None,
                         DisplacementSystem=None, LoadCaseId=None,
                         LoadLevelOrModeShapeOrTimeStep=None, 
                         LoadCombinationId=None, z='m', **kwargs):
        axm = self.model
        if case is not None:
            LoadCombinationId = None
            if isinstance(case, str):
                LoadCases = axm.LoadCases
                imap = {LoadCases.Name[i]: i for i in range(
                    1, LoadCases.Count+1)}
                if case in imap:
                    LoadCaseId = imap[case]
                else:
                    raise KeyError("Unknown case with name '{}'".format(case))
            elif isinstance(case, int):
                LoadCaseId = case
        elif combination is not None:
            LoadCaseId = None
            if isinstance(combination, str):
                LoadCombinations = axm.LoadCombinations
                imap = {LoadCombinations.Name[i]: i for i in range(
                    1, LoadCombinations.Count+1)}
                if combination in imap:
                    LoadCombinationId = imap[combination]
                else:
                    raise KeyError(
                        "Unknown combination with name '{}'".format(combination))
            elif isinstance(combination, int):
                LoadCombinationId = combination
        resobj = axm.Results.Stresses
        if DisplacementSystem is None:
            DisplacementSystem = 1  # global
        if isinstance(DisplacementSystem, int):
            resobj.DisplacementSystem = DisplacementSystem
        if LoadCaseId is not None:
            resobj.LoadCaseId = LoadCaseId
        if LoadCombinationId is not None:
            resobj.LoadCombinationId = LoadCombinationId
        if LoadLevelOrModeShapeOrTimeStep is None:
            LoadLevelOrModeShapeOrTimeStep = 1
        resobj.LoadLevelOrModeShapeOrTimeStep = LoadLevelOrModeShapeOrTimeStep
        if LoadCaseId is not None:
            recs = resobj.AllSurfaceStressesByLoadCaseId()[0]
        elif LoadCombinationId is not None:
            recs = resobj.AllSurfaceStressesByLoadCombinationId()[0]
        foo = partial(RSurfaceStresses2list, mode=z)
        return ak.Array(list(map(foo, recs)))

    def _get_attrs(self) -> Iterable:
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("Index", self.Index, "{}"))
        attrs.append(("UID", self._wrapped.UID, "{}"))
        attrs.append(("Area", self.Area, axisvm.FLOAT_FORMAT))
        attrs.append(("Volume", self.Volume, axisvm.FLOAT_FORMAT))
        attrs.append(("Weight", self.Weight, axisvm.FLOAT_FORMAT))
        return attrs
