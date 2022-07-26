# -*- coding: utf-8 -*-
from collections import Iterable

import numpy as np

from dewloosh.mesh import PointCloud, CartesianFrame
from dewloosh.mesh.topo import TopologyArray

import axisvm
from .core.wrap import AxWrapper, AxisVMModelItems
from .core.utils import RDisplacementValues2list
from .axdomain import IAxisVMDomains
from .axmember import IAxisVMMembers
from .axsurface import IAxisVMSurfaces
from .axline import IAxisVMLines
from .axwindow import IAxisVMWindows


__all__ = ['IAxisVMModels', 'IAxisVMModel']


class IAxisVMCalculation(AxisVMModelItems):
    """Wrapper for the `IAxisVMCalculation` COM interface."""

    def LinearAnalysis(self, *args, interact=False, show=False, autocorrect=True):
        if len(args) > 0 and isinstance(args[0], int):
            itype = args[0]
        else:
            import axisvm.com.tlb as axtlb
            if interact:
                itype = axtlb.cuiUserInteraction
            else:
                if show and autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithAutoCorrect
                elif not show and autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithoutAutoCorrect
                elif not show and autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithAutoCorrectNoShow
                elif not show and not autocorrect:
                    itype = axtlb.cuiNoUserInteractionWithoutAutoCorrectNoShow
                else:
                    raise NotImplementedError
        return self._wrapped.LinearAnalysis(itype)


class IAxisVMModel(AxWrapper):
    """Wrapper for the `IAxisVMModel` COM interface."""

    def __init__(self, *args, parent=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

    @property
    def Members(self) -> IAxisVMMembers:
        return IAxisVMMembers(model=self, wrap=self._wrapped.Members)

    @property
    def Domains(self) -> IAxisVMDomains:
        return IAxisVMDomains(model=self, wrap=self._wrapped.Domains)

    @property
    def Lines(self) -> IAxisVMLines:
        return IAxisVMLines(model=self, wrap=self._wrapped.Lines)

    @property
    def Surfaces(self) -> IAxisVMSurfaces:
        return IAxisVMSurfaces(model=self, wrap=self._wrapped.Surfaces)

    @property
    def Windows(self) -> IAxisVMWindows:
        return IAxisVMWindows(model=self, wrap=self._wrapped.Windows)

    @property
    def Calculation(self) -> IAxisVMCalculation:
        return IAxisVMCalculation(model=self, wrap=self._wrapped.Calculation)

    @property
    def MeshSurfaceIds(self):
        d = self.Domains
        dc = d.Count
        def fnc(i): return d[i+1].MeshSurfaceIds
        return np.vstack(list(map(fnc, range(dc)))).flatten().astype(np.int64)

    def points(self, ids=None) -> PointCloud:
        frame = CartesianFrame(dim=3)
        if isinstance(ids, np.ndarray):
            ids = ids.astype(np.int32)
        elif isinstance(ids, int):
            ids = [ids]
        if ids is not None:
            coords = self.Nodes.BulkGetCoord(ids)[0]
        else:
            lines = self.Lines
            lc, mpc = lines.Count, self.Lines.MidPointCount
            ids = np.array(list(range(self.Nodes.Count))) + 1
            coords = self.Nodes.BulkGetCoord(ids)[0]
            coords = np.array([[n.x, n.y, n.z] for n in coords])
            if lc > 0 and mpc > 0:
                def fnc(i): return lines.GetMidpoint(i+1)[0]
                def xyz(n): return [n.x, n.y, n.z]
                coords_mid = np.array(list(map(xyz, map(fnc, range(lc)))))
                def fnc(i): return lines.MidpointId[i+1]
                mIDs = np.array(list(map(fnc, range(lc))))
                i = np.where(mIDs > 0)[0]
                mIDs = mIDs[i]
                coords_mid = coords_mid[i]
                coords = np.vstack([coords, coords_mid])
                ids = np.concatenate([ids, mIDs])
        return PointCloud(coords, inds=ids, frame=frame)

    def coordinates(self, ids=None) -> np.ndarray:
        return self.points(ids).show()

    def topology(self) -> TopologyArray:
        res = []

        if self.Members.Count > 0:
            res.append(self.Members.topology())
        if self.Surfaces.Count > 0:
            res.append(self.Surfaces.topology())
            """s = self.Surfaces
            sIDs = self.MeshSurfaceIds
            def fnc_corner(i): return list(s[i].GetContourPoints()[0])
            def fnc_mid(i): return list(s[i].GetMidPoints()[0])
            def fnc(i): return fnc_corner(i) + fnc_mid(i)
            res.append(TopologyArray(ak.Array(list(map(fnc, sIDs)))))"""

        if len(res) >= 2:
            return np.vstack(res)
        return res[0] if len(res) == 1 else None
    
    def dof_solution(self, DisplacementSystem=1, LoadCaseId=1, 
                     LoadLevelOrModeShapeOrTimeStep=1):
        disps = self.Results.Displacements
        disps.DisplacementSystem = DisplacementSystem
        disps.LoadCaseId = LoadCaseId
        disps.LoadLevelOrModeShapeOrTimeStep = LoadLevelOrModeShapeOrTimeStep
        recs = disps.AllNodalDisplacementsByLoadCaseId()[0]
        return np.array(list(map(RDisplacementValues2list, recs)))

    def __enter__(self):
        if self._wrapped is not None:
            self._wrapped.BeginUpdate()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self._wrapped is not None:
            self._wrapped.EndUpdate()

    def _get_attrs(self):
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("N Nodes", self.Nodes.Count, "{}"))
        attrs.append(("N Lines", self.Lines.Count, "{}"))
        attrs.append(("N Members", self.Members.Count, "{}"))
        attrs.append(("N Surfaces", self.Surfaces.Count, "{}"))
        attrs.append(("N Domains", self.Domains.Count, "{}"))
        """bds = self.bounds
        fmt = f"{axisvm.FLOAT_FORMAT}, {axisvm.FLOAT_FORMAT}"
        attrs.append(("X Bounds", (bds[0], bds[1]), fmt))
        attrs.append(("Y Bounds", (bds[2], bds[3]), fmt))
        attrs.append(("Z Bounds", (bds[4], bds[5]), fmt))"""
        return attrs


class IAxisVMModels(AxWrapper):
    """Wrapper for the `IAxisVMModels` COM interface."""

    __itemcls__ = IAxisVMModel

    def __init__(self, *args, app=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
