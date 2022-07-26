# -*- coding: utf-8 -*-
import numpy as np

from dewloosh.mesh.topo.tr import Q8_to_T3, T6_to_T3


def RMatrix2x2toNumPy(RMatrix):
    res = np.zeros((2, 2))
    res[0, 0] = RMatrix.e11
    res[0, 1] = RMatrix.e12
    res[1, 0] = RMatrix.e21
    res[1, 1] = RMatrix.e22
    return res


def RMatrix3x3toNumPy(RMatrix):
    res = np.zeros((3, 3))
    res[0, 0] = RMatrix.e11
    res[0, 1] = RMatrix.e12
    res[0, 2] = RMatrix.e13
    res[1, 0] = RMatrix.e21
    res[1, 1] = RMatrix.e22
    res[1, 2] = RMatrix.e23
    res[2, 0] = RMatrix.e31
    res[2, 1] = RMatrix.e32
    res[2, 2] = RMatrix.e33
    return res


def RStiffness2dict(r):
    return dict(x=r.x, y=r.y, z=r.z,
                xx=r.xx, yy=r.yy, zz=r.zz)


def xyz(r): return [r.x, r.y, r.z]


def sfcT6(r):
    return list(map(xyz, [
        r.pContourPoint1, r.pContourPoint2, r.pContourPoint3,
        r.pContourLineMidPoint1, r.pContourLineMidPoint2,
        r.pContourLineMidPoint3
    ]))


def sfcQ8(r):
    return list(map(xyz, [
        r.pContourPoint1, r.pContourPoint2, r.pContourPoint3,
        r.pContourPoint4, r.pContourLineMidPoint1, r.pContourLineMidPoint2,
        r.pContourLineMidPoint3, r.pContourLineMidPoint4
    ]))


def RSurfaceCoordinates2list(r):
    return sfcT6(r) if r.ContourPointCount == 3 else sfcQ8(r)


def RDisplacementValues2list(r):
    return [r.ex, r.ey, r.ez, r.Fx, r.Fy, r.Fz]


def triangulate(topo):
    if isinstance(topo, np.ndarray):
        _, nNE = topo.shape
        if nNE == 6:
            _, T3 = T6_to_T3(None, topo)
            return T3
        elif nNE == 8:
            _, T3 = Q8_to_T3(None, topo)
            return T3
        else:
            raise NotImplementedError
    else:
        w = topo.widths()
        i6 = np.where(w == 6)[0]
        i8 = np.where(w == 8)[0]
        try:
            _, T3a = Q8_to_T3(None, topo[i8].to_numpy())
        except Exception:
            _, T3a = Q8_to_T3(None, topo[i8])
        try:
            _, T3b = T6_to_T3(None, topo[i6].to_numpy())
        except Exception:
            _, T3b = T6_to_T3(None, topo[i6])
        return np.vstack([T3a, T3b])
    
    
def dcomp2int(dcomp : str):
    assert isinstance(dcomp, str)
    dc = dcomp.lower()
    if dc in ['ex', 'ux']:
        return 0
    if dc in ['ey', 'uy']:
        return 1
    if dc in ['ez', 'uz']:
        return 2
    if dc in ['fx', 'rotx']:
        return 3
    if dc in ['fy', 'roty']:
        return 4
    if dc in ['fz', 'rotz']:
        return 5
    raise ValueError("Invalid displacement component '{}'".format(dcomp))