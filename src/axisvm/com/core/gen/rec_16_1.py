# -*- coding: utf-8 -*-
from dewloosh.core.wrapping import Wrapper
from ctypes import *
from comtypes import BSTR


class RCrossSectionTable(Wrapper):

    @property
    def CrossSectionShape(self) -> c_long:
        return self._wrapped.CrossSectionShape

    @property
    def ProviderID(self) -> c_long:
        return self._wrapped.ProviderID

    @property
    def CrossSectionRegion(self) -> c_long:
        return self._wrapped.CrossSectionRegion

    @property
    def Id(self) -> c_long:
        return self._wrapped.Id


class RRebarSteelGrade(Wrapper):

    @property
    def NationalDesignCode(self) -> c_long:
        return self._wrapped.NationalDesignCode

    @property
    def E(self) -> c_double:
        return self._wrapped.E

    @property
    def RebarSteelGrade_EC_ITA(self) -> 'RRebarSteelGrade_EC_ITA':
        return self._wrapped.RebarSteelGrade_EC_ITA

    @property
    def RebarSteelGrade_MSZ(self) -> 'RRebarSteelGrade_MSZ':
        return self._wrapped.RebarSteelGrade_MSZ

    @property
    def RebarSteelGrade_STAS(self) -> 'RRebarSteelGrade_STAS':
        return self._wrapped.RebarSteelGrade_STAS

    @property
    def RebarSteelGrade_DIN(self) -> 'RRebarSteelGrade_DIN':
        return self._wrapped.RebarSteelGrade_DIN

    @property
    def RebarSteelGrade_SIA(self) -> 'RRebarSteelGrade_SIA':
        return self._wrapped.RebarSteelGrade_SIA

    @property
    def RebarSteelGrade_NEN(self) -> 'RRebarSteelGrade_NEN':
        return self._wrapped.RebarSteelGrade_NEN


class RStiffnesses(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z

    @property
    def xx(self) -> c_double:
        return self._wrapped.xx

    @property
    def yy(self) -> c_double:
        return self._wrapped.yy

    @property
    def zz(self) -> c_double:
        return self._wrapped.zz


class RNonLinearity(Wrapper):

    @property
    def x(self) -> c_long:
        return self._wrapped.x

    @property
    def y(self) -> c_long:
        return self._wrapped.y

    @property
    def z(self) -> c_long:
        return self._wrapped.z

    @property
    def xx(self) -> c_long:
        return self._wrapped.xx

    @property
    def yy(self) -> c_long:
        return self._wrapped.yy

    @property
    def zz(self) -> c_long:
        return self._wrapped.zz


class RResistances(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z

    @property
    def xx(self) -> c_double:
        return self._wrapped.xx

    @property
    def yy(self) -> c_double:
        return self._wrapped.yy

    @property
    def zz(self) -> c_double:
        return self._wrapped.zz


class RMatrix3x3(Wrapper):

    @property
    def e11(self) -> c_double:
        return self._wrapped.e11

    @property
    def e12(self) -> c_double:
        return self._wrapped.e12

    @property
    def e13(self) -> c_double:
        return self._wrapped.e13

    @property
    def e21(self) -> c_double:
        return self._wrapped.e21

    @property
    def e22(self) -> c_double:
        return self._wrapped.e22

    @property
    def e23(self) -> c_double:
        return self._wrapped.e23

    @property
    def e31(self) -> c_double:
        return self._wrapped.e31

    @property
    def e32(self) -> c_double:
        return self._wrapped.e32

    @property
    def e33(self) -> c_double:
        return self._wrapped.e33


class RNodalSupportSpringParams(Wrapper):

    @property
    def SpringParamIndexes(self) -> 'RSpringParamIndexes':
        return self._wrapped.SpringParamIndexes

    @property
    def IsolatorParamIndex(self) -> c_long:
        return self._wrapped.IsolatorParamIndex

    @property
    def IsolatorD2(self) -> c_double:
        return self._wrapped.IsolatorD2


class RMemberMeshParameters(Wrapper):

    @property
    def MeshType(self) -> c_long:
        return self._wrapped.MeshType

    @property
    def MeshParam(self) -> c_double:
        return self._wrapped.MeshParam


class RLineAttr(Wrapper):

    @property
    def LineType(self) -> c_long:
        return self._wrapped.LineType

    @property
    def MaterialIndex(self) -> c_long:
        return self._wrapped.MaterialIndex

    @property
    def StartCrossSectionIndex(self) -> c_long:
        return self._wrapped.StartCrossSectionIndex

    @property
    def EndCrossSectionIndex(self) -> c_long:
        return self._wrapped.EndCrossSectionIndex

    @property
    def AutoEccentricityType(self) -> c_long:
        return self._wrapped.AutoEccentricityType

    @property
    def StartEccentricity(self) -> 'RPoint3d':
        return self._wrapped.StartEccentricity

    @property
    def EndEccentricity(self) -> 'RPoint3d':
        return self._wrapped.EndEccentricity

    @property
    def TrussType(self) -> c_long:
        return self._wrapped.TrussType

    @property
    def Resistance(self) -> c_double:
        return self._wrapped.Resistance

    @property
    def ServiceClass(self) -> c_long:
        return self._wrapped.ServiceClass

    @property
    def kdef(self) -> c_double:
        return self._wrapped.kdef

    @property
    def kx(self) -> c_double:
        return self._wrapped.kx

    @property
    def Domain1(self) -> c_long:
        return self._wrapped.Domain1

    @property
    def Domain2(self) -> c_long:
        return self._wrapped.Domain2

    @property
    def GapType(self) -> c_long:
        return self._wrapped.GapType

    @property
    def ActiveStiffness(self) -> c_double:
        return self._wrapped.ActiveStiffness

    @property
    def InactiveStiffness(self) -> c_double:
        return self._wrapped.InactiveStiffness

    @property
    def InitialOpening(self) -> c_double:
        return self._wrapped.InitialOpening

    @property
    def MinPenetration(self) -> c_double:
        return self._wrapped.MinPenetration

    @property
    def MaxPenetration(self) -> c_double:
        return self._wrapped.MaxPenetration

    @property
    def AdjustmentRatio(self) -> c_double:
        return self._wrapped.AdjustmentRatio

    @property
    def SpringDirection(self) -> c_long:
        return self._wrapped.SpringDirection

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses


class RPoint3d(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z


class RLineAttr_V161(Wrapper):

    @property
    def LineType(self) -> c_long:
        return self._wrapped.LineType

    @property
    def MaterialIndex(self) -> c_long:
        return self._wrapped.MaterialIndex

    @property
    def StartCrossSectionIndex(self) -> c_long:
        return self._wrapped.StartCrossSectionIndex

    @property
    def EndCrossSectionIndex(self) -> c_long:
        return self._wrapped.EndCrossSectionIndex

    @property
    def LocalXOrientation(self) -> c_long:
        return self._wrapped.LocalXOrientation

    @property
    def StartRelease(self) -> 'RReleases_V161':
        return self._wrapped.StartRelease

    @property
    def EndRelease(self) -> 'RReleases_V161':
        return self._wrapped.EndRelease

    @property
    def Reference(self) -> c_long:
        return self._wrapped.Reference

    @property
    def RibAutoEccentricityType(self) -> c_long:
        return self._wrapped.RibAutoEccentricityType

    @property
    def StartEccentricity(self) -> 'RPoint3d':
        return self._wrapped.StartEccentricity

    @property
    def EndEccentricity(self) -> 'RPoint3d':
        return self._wrapped.EndEccentricity

    @property
    def StartEccentricityType(self) -> c_long:
        return self._wrapped.StartEccentricityType

    @property
    def EndEccentricityType(self) -> c_long:
        return self._wrapped.EndEccentricityType

    @property
    def StartAlignementPoint(self) -> c_long:
        return self._wrapped.StartAlignementPoint

    @property
    def EndAlignementPoint(self) -> c_long:
        return self._wrapped.EndAlignementPoint

    @property
    def EccGroupIndex(self) -> c_long:
        return self._wrapped.EccGroupIndex

    @property
    def StartRefLine(self) -> c_long:
        return self._wrapped.StartRefLine

    @property
    def EndRefLine(self) -> c_long:
        return self._wrapped.EndRefLine

    @property
    def RefStartAlignementPoint(self) -> c_long:
        return self._wrapped.RefStartAlignementPoint

    @property
    def RefEndAlignementPoint(self) -> c_long:
        return self._wrapped.RefEndAlignementPoint

    @property
    def StartEccRelease(self) -> 'REccReleases':
        return self._wrapped.StartEccRelease

    @property
    def EndEccRelease(self) -> 'REccReleases':
        return self._wrapped.EndEccRelease

    @property
    def TrussType(self) -> c_long:
        return self._wrapped.TrussType

    @property
    def Resistance(self) -> c_double:
        return self._wrapped.Resistance

    @property
    def ServiceClass(self) -> c_long:
        return self._wrapped.ServiceClass

    @property
    def kdef(self) -> c_double:
        return self._wrapped.kdef

    @property
    def kx(self) -> c_double:
        return self._wrapped.kx

    @property
    def Domain1(self) -> c_long:
        return self._wrapped.Domain1

    @property
    def Domain2(self) -> c_long:
        return self._wrapped.Domain2

    @property
    def Beam7DOF(self) -> c_long:
        return self._wrapped.Beam7DOF

    @property
    def MaterialColor(self) -> c_long:
        return self._wrapped.MaterialColor

    @property
    def ContourColor(self) -> c_long:
        return self._wrapped.ContourColor

    @property
    def GapType(self) -> c_long:
        return self._wrapped.GapType

    @property
    def ActiveStiffness(self) -> c_double:
        return self._wrapped.ActiveStiffness

    @property
    def InactiveStiffness(self) -> c_double:
        return self._wrapped.InactiveStiffness

    @property
    def InitialOpening(self) -> c_double:
        return self._wrapped.InitialOpening

    @property
    def MinPenetration(self) -> c_double:
        return self._wrapped.MinPenetration

    @property
    def MaxPenetration(self) -> c_double:
        return self._wrapped.MaxPenetration

    @property
    def AdjustmentRatio(self) -> c_double:
        return self._wrapped.AdjustmentRatio

    @property
    def SpringType(self) -> c_long:
        return self._wrapped.SpringType

    @property
    def SpringCharacteristics(self) -> 'RSpringCharacteristics':
        return self._wrapped.SpringCharacteristics

    @property
    def SeismicIsolatorIndex(self) -> c_long:
        return self._wrapped.SeismicIsolatorIndex

    @property
    def IsolatorD2(self) -> c_double:
        return self._wrapped.IsolatorD2


class RReleases_V161(Wrapper):

    @property
    def x(self) -> 'RRelease_V161':
        return self._wrapped.x

    @property
    def y(self) -> 'RRelease_V161':
        return self._wrapped.y

    @property
    def z(self) -> 'RRelease_V161':
        return self._wrapped.z

    @property
    def xx(self) -> 'RRelease_V161':
        return self._wrapped.xx

    @property
    def yy(self) -> 'RRelease_V161':
        return self._wrapped.yy

    @property
    def zz(self) -> 'RRelease_V161':
        return self._wrapped.zz

    @property
    def ew(self) -> 'RRelease_V161':
        return self._wrapped.ew


class RRelease_V161(Wrapper):

    @property
    def ReleaseType(self) -> c_long:
        return self._wrapped.ReleaseType

    @property
    def FunctionId(self) -> c_long:
        return self._wrapped.FunctionId


class REccReleases(Wrapper):

    @property
    def x(self) -> c_long:
        return self._wrapped.x

    @property
    def y(self) -> c_long:
        return self._wrapped.y

    @property
    def z(self) -> c_long:
        return self._wrapped.z

    @property
    def xx(self) -> c_long:
        return self._wrapped.xx

    @property
    def yy(self) -> c_long:
        return self._wrapped.yy

    @property
    def zz(self) -> c_long:
        return self._wrapped.zz

    @property
    def PosType(self) -> c_long:
        return self._wrapped.PosType

    @property
    def Pos(self) -> c_double:
        return self._wrapped.Pos


class RSpringCharacteristics(Wrapper):

    @property
    def x(self) -> c_long:
        return self._wrapped.x

    @property
    def y(self) -> c_long:
        return self._wrapped.y

    @property
    def z(self) -> c_long:
        return self._wrapped.z

    @property
    def xx(self) -> c_long:
        return self._wrapped.xx

    @property
    def yy(self) -> c_long:
        return self._wrapped.yy

    @property
    def zz(self) -> c_long:
        return self._wrapped.zz


class RLoadRibMemberConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def Fgx(self) -> c_double:
        return self._wrapped.Fgx

    @property
    def Fgy(self) -> c_double:
        return self._wrapped.Fgy

    @property
    def Fgz(self) -> c_double:
        return self._wrapped.Fgz

    @property
    def Mgx(self) -> c_double:
        return self._wrapped.Mgx

    @property
    def Mgy(self) -> c_double:
        return self._wrapped.Mgy

    @property
    def Mgz(self) -> c_double:
        return self._wrapped.Mgz

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR


class RPoint2d(Wrapper):

    @property
    def Coord1(self) -> c_double:
        return self._wrapped.Coord1

    @property
    def Coord2(self) -> c_double:
        return self._wrapped.Coord2


class RWindLoadParams_V161(Wrapper):

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def v_b0(self) -> c_double:
        return self._wrapped.v_b0

    @property
    def c_dir_xp(self) -> c_double:
        return self._wrapped.c_dir_xp

    @property
    def c_dir_xm(self) -> c_double:
        return self._wrapped.c_dir_xm

    @property
    def c_dir_yp(self) -> c_double:
        return self._wrapped.c_dir_yp

    @property
    def c_dir_ym(self) -> c_double:
        return self._wrapped.c_dir_ym

    @property
    def c_season(self) -> c_double:
        return self._wrapped.c_season

    @property
    def TerrainCategoryDifferent(self) -> c_long:
        return self._wrapped.TerrainCategoryDifferent

    @property
    def CustomDirectionalFactors(self) -> c_long:
        return self._wrapped.CustomDirectionalFactors

    @property
    def TerrainCat_Xp(self) -> c_long:
        return self._wrapped.TerrainCat_Xp

    @property
    def TerrainCat_Xm(self) -> c_long:
        return self._wrapped.TerrainCat_Xm

    @property
    def TerrainCat_Yp(self) -> c_long:
        return self._wrapped.TerrainCat_Yp

    @property
    def TerrainCat_Ym(self) -> c_long:
        return self._wrapped.TerrainCat_Ym

    @property
    def c_o(self) -> c_double:
        return self._wrapped.c_o

    @property
    def Iw(self) -> c_double:
        return self._wrapped.Iw

    @property
    def Zone(self) -> c_long:
        return self._wrapped.Zone

    @property
    def AltitudeFactor(self) -> c_double:
        return self._wrapped.AltitudeFactor

    @property
    def TurbulenceFactor(self) -> c_double:
        return self._wrapped.TurbulenceFactor


class RWindSubStructParams(Wrapper):

    @property
    def Name(self) -> BSTR:
        return self._wrapped.Name

    @property
    def RoofType(self) -> c_long:
        return self._wrapped.RoofType

    @property
    def TorsionalEffect(self) -> c_long:
        return self._wrapped.TorsionalEffect

    @property
    def InternalPressure(self) -> c_long:
        return self._wrapped.InternalPressure

    @property
    def Mu_Xp(self) -> c_double:
        return self._wrapped.Mu_Xp

    @property
    def Mu_Xm(self) -> c_double:
        return self._wrapped.Mu_Xm

    @property
    def Mu_Yp(self) -> c_double:
        return self._wrapped.Mu_Yp

    @property
    def Mu_Ym(self) -> c_double:
        return self._wrapped.Mu_Ym

    @property
    def cpi_Xp(self) -> c_double:
        return self._wrapped.cpi_Xp

    @property
    def cpi_Xm(self) -> c_double:
        return self._wrapped.cpi_Xm

    @property
    def cpi_Yp(self) -> c_double:
        return self._wrapped.cpi_Yp

    @property
    def cpi_Ym(self) -> c_double:
        return self._wrapped.cpi_Ym

    @property
    def FricionEffect(self) -> c_long:
        return self._wrapped.FricionEffect

    @property
    def CustomFriction(self) -> c_double:
        return self._wrapped.CustomFriction

    @property
    def IsRelativeElevation(self) -> c_long:
        return self._wrapped.IsRelativeElevation

    @property
    def RelativeElevation(self) -> c_double:
        return self._wrapped.RelativeElevation

    @property
    def IsMultiSpan(self) -> c_long:
        return self._wrapped.IsMultiSpan

    @property
    def MultiSpanPos(self) -> c_long:
        return self._wrapped.MultiSpanPos

    @property
    def MultiSpanDir(self) -> c_long:
        return self._wrapped.MultiSpanDir

    @property
    def FlatRoofEdgeType(self) -> c_long:
        return self._wrapped.FlatRoofEdgeType

    @property
    def FlatRoofEdgeParam(self) -> c_double:
        return self._wrapped.FlatRoofEdgeParam

    @property
    def Blockage_Xp(self) -> c_double:
        return self._wrapped.Blockage_Xp

    @property
    def Blockage_Xm(self) -> c_double:
        return self._wrapped.Blockage_Xm

    @property
    def Blockage_Yp(self) -> c_double:
        return self._wrapped.Blockage_Yp

    @property
    def Blockage_Ym(self) -> c_double:
        return self._wrapped.Blockage_Ym

    @property
    def Solidity(self) -> c_double:
        return self._wrapped.Solidity


class RSurfaceAttr(Wrapper):

    @property
    def Thickness(self) -> c_double:
        return self._wrapped.Thickness

    @property
    def SurfaceType(self) -> c_long:
        return self._wrapped.SurfaceType

    @property
    def RefZId(self) -> c_long:
        return self._wrapped.RefZId

    @property
    def RefXId(self) -> c_long:
        return self._wrapped.RefXId

    @property
    def MaterialId(self) -> c_long:
        return self._wrapped.MaterialId

    @property
    def ElasticFoundation(self) -> 'RElasticFoundationXYZ':
        return self._wrapped.ElasticFoundation

    @property
    def NonLinearity(self) -> 'RNonLinearityXYZ':
        return self._wrapped.NonLinearity

    @property
    def Resistance(self) -> 'RResistancesXYZ':
        return self._wrapped.Resistance

    @property
    def Charactersitics(self) -> c_long:
        return self._wrapped.Charactersitics


class RDomainMeshParameters(Wrapper):

    @property
    def MeshSize(self) -> c_double:
        return self._wrapped.MeshSize

    @property
    def MeshType(self) -> c_long:
        return self._wrapped.MeshType

    @property
    def IsFitToPointLoad(self) -> c_long:
        return self._wrapped.IsFitToPointLoad

    @property
    def FitToPointLoadValue(self) -> c_double:
        return self._wrapped.FitToPointLoadValue

    @property
    def IsFitToLineLoad(self) -> c_long:
        return self._wrapped.IsFitToLineLoad

    @property
    def FitToLineLoadValue(self) -> c_double:
        return self._wrapped.FitToLineLoadValue

    @property
    def IsFitToSurfaceLoad(self) -> c_long:
        return self._wrapped.IsFitToSurfaceLoad

    @property
    def FitToSurfaceLoadValue(self) -> c_double:
        return self._wrapped.FitToSurfaceLoadValue

    @property
    def MeshGeometryType(self) -> c_long:
        return self._wrapped.MeshGeometryType

    @property
    def QuadMeshQuality(self) -> c_long:
        return self._wrapped.QuadMeshQuality


class RSurfaceCoordinates(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def pContourPoint1(self) -> 'RPoint3d':
        return self._wrapped.pContourPoint1

    @property
    def pContourPoint2(self) -> 'RPoint3d':
        return self._wrapped.pContourPoint2

    @property
    def pContourPoint3(self) -> 'RPoint3d':
        return self._wrapped.pContourPoint3

    @property
    def pContourPoint4(self) -> 'RPoint3d':
        return self._wrapped.pContourPoint4

    @property
    def pContourLineMidPoint1(self) -> 'RPoint3d':
        return self._wrapped.pContourLineMidPoint1

    @property
    def pContourLineMidPoint2(self) -> 'RPoint3d':
        return self._wrapped.pContourLineMidPoint2

    @property
    def pContourLineMidPoint3(self) -> 'RPoint3d':
        return self._wrapped.pContourLineMidPoint3

    @property
    def pContourLineMidPoint4(self) -> 'RPoint3d':
        return self._wrapped.pContourLineMidPoint4


class RReinforcementParameters(Wrapper):

    @property
    def ConcreteId(self) -> c_long:
        return self._wrapped.ConcreteId

    @property
    def RebarSteelGradeId(self) -> c_long:
        return self._wrapped.RebarSteelGradeId

    @property
    def Thickness(self) -> c_double:
        return self._wrapped.Thickness


class RStiffnessesXYZ(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z


class RNonLinearityXYZ(Wrapper):

    @property
    def x(self) -> c_long:
        return self._wrapped.x

    @property
    def y(self) -> c_long:
        return self._wrapped.y

    @property
    def z(self) -> c_long:
        return self._wrapped.z


class RResistancesXYZ(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z


class RSurfaceStiffnessFactors(Wrapper):

    @property
    def k_torsion(self) -> c_double:
        return self._wrapped.k_torsion

    @property
    def k_shear(self) -> c_double:
        return self._wrapped.k_shear

    @property
    def k_bending(self) -> c_double:
        return self._wrapped.k_bending


class RMatrix2x2(Wrapper):

    @property
    def e11(self) -> c_double:
        return self._wrapped.e11

    @property
    def e12(self) -> c_double:
        return self._wrapped.e12

    @property
    def e21(self) -> c_double:
        return self._wrapped.e21

    @property
    def e22(self) -> c_double:
        return self._wrapped.e22


class RLoadNodalForce(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def NodeId(self) -> c_long:
        return self._wrapped.NodeId

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RNode(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z

    @property
    def dof(self) -> c_long:
        return self._wrapped.dof


class RResultTreeIteratorRec(Wrapper):

    @property
    def AnalysisType(self) -> c_long:
        return self._wrapped.AnalysisType

    @property
    def ResultCase(self) -> c_long:
        return self._wrapped.ResultCase

    @property
    def LoadLevelOrTimeStep(self) -> c_long:
        return self._wrapped.LoadLevelOrTimeStep

    @property
    def Creep(self) -> c_long:
        return self._wrapped.Creep


class RTableCrossSectionID(Wrapper):

    @property
    def TableID(self) -> c_long:
        return self._wrapped.TableID

    @property
    def CrossSectionID(self) -> c_long:
        return self._wrapped.CrossSectionID


class RVelocityValues(Wrapper):

    @property
    def vvX(self) -> c_double:
        return self._wrapped.vvX

    @property
    def vvY(self) -> c_double:
        return self._wrapped.vvY

    @property
    def vvZ(self) -> c_double:
        return self._wrapped.vvZ

    @property
    def vvXX(self) -> c_double:
        return self._wrapped.vvXX

    @property
    def vvYY(self) -> c_double:
        return self._wrapped.vvYY

    @property
    def vvZZ(self) -> c_double:
        return self._wrapped.vvZZ

    @property
    def vvR(self) -> c_double:
        return self._wrapped.vvR

    @property
    def vvRR(self) -> c_double:
        return self._wrapped.vvRR


class RSpringParam_V161(Wrapper):

    @property
    def SpringType(self) -> c_long:
        return self._wrapped.SpringType

    @property
    def NNType(self) -> c_long:
        return self._wrapped.NNType

    @property
    def DOFType(self) -> c_long:
        return self._wrapped.DOFType

    @property
    def NLESimplified(self) -> c_long:
        return self._wrapped.NLESimplified

    @property
    def K(self) -> c_double:
        return self._wrapped.K

    @property
    def KVib(self) -> c_double:
        return self._wrapped.KVib

    @property
    def DampingType(self) -> c_long:
        return self._wrapped.DampingType

    @property
    def C(self) -> c_double:
        return self._wrapped.C

    @property
    def NonLinearity(self) -> c_long:
        return self._wrapped.NonLinearity

    @property
    def NLDefType(self) -> c_long:
        return self._wrapped.NLDefType

    @property
    def K_T(self) -> c_double:
        return self._wrapped.K_T

    @property
    def K_C(self) -> c_double:
        return self._wrapped.K_C

    @property
    def ResistanceDef_T(self) -> c_long:
        return self._wrapped.ResistanceDef_T

    @property
    def ResistanceDef_C(self) -> c_long:
        return self._wrapped.ResistanceDef_C

    @property
    def TangentStiffness_T(self) -> c_double:
        return self._wrapped.TangentStiffness_T

    @property
    def TangentStiffness_C(self) -> c_double:
        return self._wrapped.TangentStiffness_C

    @property
    def Resistance_T(self) -> c_double:
        return self._wrapped.Resistance_T

    @property
    def Resistance_C(self) -> c_double:
        return self._wrapped.Resistance_C

    @property
    def HardeningRule(self) -> c_long:
        return self._wrapped.HardeningRule

    @property
    def MatrixType(self) -> c_long:
        return self._wrapped.MatrixType

    @property
    def C_t(self) -> c_double:
        return self._wrapped.C_t

    @property
    def C_C(self) -> c_double:
        return self._wrapped.C_C

    @property
    def VerticalStiffness(self) -> c_double:
        return self._wrapped.VerticalStiffness

    @property
    def IsolatorType(self) -> c_long:
        return self._wrapped.IsolatorType

    @property
    def K1(self) -> c_double:
        return self._wrapped.K1

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def F1(self) -> c_double:
        return self._wrapped.F1

    @property
    def Mu(self) -> c_double:
        return self._wrapped.Mu

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def HorizontalStiffness(self) -> c_double:
        return self._wrapped.HorizontalStiffness

    @property
    def Ksi(self) -> c_double:
        return self._wrapped.Ksi

    @property
    def WF(self) -> c_double:
        return self._wrapped.WF


class RIFCExportReinforcementParams(Wrapper):

    @property
    def EdgeReinforcementNeeded(self) -> c_long:
        return self._wrapped.EdgeReinforcementNeeded

    @property
    def AdditionalHoleReinforcement(self) -> c_long:
        return self._wrapped.AdditionalHoleReinforcement

    @property
    def TypicalLapLengthByDesignCode(self) -> c_long:
        return self._wrapped.TypicalLapLengthByDesignCode

    @property
    def ConcaveCornerLapLengthByDesignCode(self) -> c_long:
        return self._wrapped.ConcaveCornerLapLengthByDesignCode

    @property
    def TypicalLapLengthByUser(self) -> c_double:
        return self._wrapped.TypicalLapLengthByUser

    @property
    def ConcaveCornerLapLengthByUser(self) -> c_double:
        return self._wrapped.ConcaveCornerLapLengthByUser

    @property
    def AdditionalHoleRebarDiameter(self) -> c_double:
        return self._wrapped.AdditionalHoleRebarDiameter

    @property
    def DomainReinforcementLinkType(self) -> c_long:
        return self._wrapped.DomainReinforcementLinkType

    @property
    def QuestionableDomainLink(self) -> c_long:
        return self._wrapped.QuestionableDomainLink

    @property
    def DomainOverlap_Larger(self) -> c_long:
        return self._wrapped.DomainOverlap_Larger

    @property
    def DomainOverlap_Smaller(self) -> c_long:
        return self._wrapped.DomainOverlap_Smaller

    @property
    def ModifyClosedLinks(self) -> c_long:
        return self._wrapped.ModifyClosedLinks

    @property
    def ClosedLinkRatio(self) -> c_double:
        return self._wrapped.ClosedLinkRatio


class RShearCapacities(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def scvCenterPoint(self) -> 'RShearCapacityValues':
        return self._wrapped.scvCenterPoint

    @property
    def scvContourPoint1(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourPoint1

    @property
    def scvContourPoint2(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourPoint2

    @property
    def scvContourPoint3(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourPoint3

    @property
    def scvContourPoint4(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourPoint4

    @property
    def scvContourLineMidPoint1(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourLineMidPoint1

    @property
    def scvContourLineMidPoint2(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourLineMidPoint2

    @property
    def scvContourLineMidPoint3(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourLineMidPoint3

    @property
    def scvContourLineMidPoint4(self) -> 'RShearCapacityValues':
        return self._wrapped.scvContourLineMidPoint4


class RShearCapacityValues(Wrapper):

    @property
    def VRdc(self) -> c_double:
        return self._wrapped.VRdc

    @property
    def VEdMinusVRdc(self) -> c_double:
        return self._wrapped.VEdMinusVRdc

    @property
    def VRdmax(self) -> c_double:
        return self._wrapped.VRdmax

    @property
    def VEdDivVRdmax(self) -> c_double:
        return self._wrapped.VEdDivVRdmax

    @property
    def aVEd(self) -> c_double:
        return self._wrapped.aVEd


class RCrossSectionSFB(Wrapper):

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def b2(self) -> c_double:
        return self._wrapped.b2

    @property
    def v2(self) -> c_double:
        return self._wrapped.v2

    @property
    def Process(self) -> c_long:
        return self._wrapped.Process


class RStructuralGridLineParams(Wrapper):

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2

    @property
    def NormalVector(self) -> 'RPoint3d':
        return self._wrapped.NormalVector

    @property
    def Colour(self) -> c_long:
        return self._wrapped.Colour

    @property
    def Extension(self) -> c_double:
        return self._wrapped.Extension

    @property
    def ShowTitle(self) -> c_long:
        return self._wrapped.ShowTitle

    @property
    def ToLogicalPart(self) -> c_long:
        return self._wrapped.ToLogicalPart

    @property
    def PlaneTolerance(self) -> c_double:
        return self._wrapped.PlaneTolerance


class RBulkLineSupport(Wrapper):

    @property
    def SupportType(self) -> c_long:
        return self._wrapped.SupportType

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def NonLinearity(self) -> 'RNonLinearity':
        return self._wrapped.NonLinearity

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances

    @property
    def SurfaceId1(self) -> c_long:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> c_long:
        return self._wrapped.SurfaceId2

    @property
    def DomainId1(self) -> c_long:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> c_long:
        return self._wrapped.DomainId2

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RLoadSupportDisplacement(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def SupportId(self) -> c_long:
        return self._wrapped.SupportId

    @property
    def ex(self) -> c_double:
        return self._wrapped.ex

    @property
    def ey(self) -> c_double:
        return self._wrapped.ey

    @property
    def ez(self) -> c_double:
        return self._wrapped.ez

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz


class RSeismicParams(Wrapper):

    @property
    def VibrType(self) -> c_long:
        return self._wrapped.VibrType

    @property
    def kg(self) -> c_double:
        return self._wrapped.kg

    @property
    def ks(self) -> c_double:
        return self._wrapped.ks

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def psi(self) -> c_double:
        return self._wrapped.psi

    @property
    def SeismicCombType(self) -> c_long:
        return self._wrapped.SeismicCombType

    @property
    def qd(self) -> c_double:
        return self._wrapped.qd

    @property
    def ksiV(self) -> c_double:
        return self._wrapped.ksiV

    @property
    def ModalCombType(self) -> c_long:
        return self._wrapped.ModalCombType

    @property
    def Torsion(self) -> c_long:
        return self._wrapped.Torsion

    @property
    def ExcCoeff(self) -> c_double:
        return self._wrapped.ExcCoeff

    @property
    def C(self) -> c_double:
        return self._wrapped.C

    @property
    def nu(self) -> c_double:
        return self._wrapped.nu

    @property
    def LoadCaseLoadCombination(self) -> c_long:
        return self._wrapped.LoadCaseLoadCombination

    @property
    def Eta(self) -> c_double:
        return self._wrapped.Eta


class RDXFimportParameters(Wrapper):

    @property
    def CoordinateUnit(self) -> c_long:
        return self._wrapped.CoordinateUnit

    @property
    def MaxDeviation(self) -> c_double:
        return self._wrapped.MaxDeviation

    @property
    def GeometryCheckTolerance(self) -> c_double:
        return self._wrapped.GeometryCheckTolerance

    @property
    def CoordinateScaleFactor(self) -> c_double:
        return self._wrapped.CoordinateScaleFactor

    @property
    def ImportAs(self) -> c_long:
        return self._wrapped.ImportAs

    @property
    def ImportMode(self) -> c_long:
        return self._wrapped.ImportMode

    @property
    def BasePlane(self) -> c_long:
        return self._wrapped.BasePlane

    @property
    def WorkPlaneIndex(self) -> c_long:
        return self._wrapped.WorkPlaneIndex

    @property
    def PlaceOffset(self) -> 'RPoint3d':
        return self._wrapped.PlaceOffset

    @property
    def VisibleLayersOnly(self) -> c_long:
        return self._wrapped.VisibleLayersOnly

    @property
    def ImportHatch(self) -> c_long:
        return self._wrapped.ImportHatch

    @property
    def ActivateDXFonAllDrawings(self) -> c_long:
        return self._wrapped.ActivateDXFonAllDrawings


class RPDFimportParameters(Wrapper):

    @property
    def PageNumber(self) -> c_long:
        return self._wrapped.PageNumber

    @property
    def MaxDeviation(self) -> c_double:
        return self._wrapped.MaxDeviation

    @property
    def GeometryCheckTolerance(self) -> c_double:
        return self._wrapped.GeometryCheckTolerance

    @property
    def Scale(self) -> c_double:
        return self._wrapped.Scale

    @property
    def ImportLineWidth(self) -> c_long:
        return self._wrapped.ImportLineWidth

    @property
    def ImportText(self) -> c_long:
        return self._wrapped.ImportText

    @property
    def BasePlane(self) -> c_long:
        return self._wrapped.BasePlane

    @property
    def WorkPlaneIndex(self) -> c_long:
        return self._wrapped.WorkPlaneIndex

    @property
    def ImportAs(self) -> c_long:
        return self._wrapped.ImportAs

    @property
    def ImportMode(self) -> c_long:
        return self._wrapped.ImportMode

    @property
    def PlaceOffset(self) -> 'RPoint3d':
        return self._wrapped.PlaceOffset


class RIFCimportParameters(Wrapper):

    @property
    def ImportMode(self) -> c_long:
        return self._wrapped.ImportMode

    @property
    def ImportMethod(self) -> c_long:
        return self._wrapped.ImportMethod

    @property
    def MaxDeviation(self) -> c_double:
        return self._wrapped.MaxDeviation

    @property
    def ByAngle(self) -> c_double:
        return self._wrapped.ByAngle

    @property
    def JoinIfObjectsAreCloserThan(self) -> c_double:
        return self._wrapped.JoinIfObjectsAreCloserThan

    @property
    def ImportAs(self) -> c_long:
        return self._wrapped.ImportAs

    @property
    def OpeningsAlignedToDomainEdge(self) -> c_long:
        return self._wrapped.OpeningsAlignedToDomainEdge


class RCompanyLogoParameters(Wrapper):

    @property
    def ShowInHeader(self) -> c_long:
        return self._wrapped.ShowInHeader

    @property
    def HeaderPosition(self) -> c_long:
        return self._wrapped.HeaderPosition

    @property
    def HeaderSizeOption(self) -> c_long:
        return self._wrapped.HeaderSizeOption

    @property
    def HeaderSize(self) -> c_double:
        return self._wrapped.HeaderSize

    @property
    def ShowOnCover(self) -> c_long:
        return self._wrapped.ShowOnCover

    @property
    def CoverAlignment(self) -> c_long:
        return self._wrapped.CoverAlignment

    @property
    def TopMargin(self) -> c_double:
        return self._wrapped.TopMargin

    @property
    def SpacingAfter(self) -> c_double:
        return self._wrapped.SpacingAfter

    @property
    def CoverSizeOption(self) -> c_long:
        return self._wrapped.CoverSizeOption

    @property
    def CoverSize(self) -> c_double:
        return self._wrapped.CoverSize


class RAXSimportParameters(Wrapper):

    @property
    def Place(self) -> 'RPoint3d':
        return self._wrapped.Place

    @property
    def CheckTolerance(self) -> c_double:
        return self._wrapped.CheckTolerance

    @property
    def MergeLoadCases(self) -> c_long:
        return self._wrapped.MergeLoadCases

    @property
    def UserInteraction(self) -> c_long:
        return self._wrapped.UserInteraction

    @property
    def IgnoreDesignCode(self) -> c_long:
        return self._wrapped.IgnoreDesignCode

    @property
    def MergeLayers(self) -> c_long:
        return self._wrapped.MergeLayers

    @property
    def CustomParts(self) -> c_long:
        return self._wrapped.CustomParts


class RDomainHollowCore(Wrapper):

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def d(self) -> c_double:
        return self._wrapped.d

    @property
    def Origin(self) -> 'RPoint3d':
        return self._wrapped.Origin

    @property
    def HoleType(self) -> c_long:
        return self._wrapped.HoleType

    @property
    def fi(self) -> c_double:
        return self._wrapped.fi

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def h(self) -> c_double:
        return self._wrapped.h


class RSpringParam(Wrapper):

    @property
    def SpringType(self) -> c_long:
        return self._wrapped.SpringType

    @property
    def NNType(self) -> c_long:
        return self._wrapped.NNType

    @property
    def DOFType(self) -> c_long:
        return self._wrapped.DOFType

    @property
    def NLESimplified(self) -> c_long:
        return self._wrapped.NLESimplified

    @property
    def K(self) -> c_double:
        return self._wrapped.K

    @property
    def KVib(self) -> c_double:
        return self._wrapped.KVib

    @property
    def DampingType(self) -> c_long:
        return self._wrapped.DampingType

    @property
    def C(self) -> c_double:
        return self._wrapped.C

    @property
    def NonLinearity(self) -> c_long:
        return self._wrapped.NonLinearity

    @property
    def NLDefType(self) -> c_long:
        return self._wrapped.NLDefType

    @property
    def K_T(self) -> c_double:
        return self._wrapped.K_T

    @property
    def K_C(self) -> c_double:
        return self._wrapped.K_C

    @property
    def ResistanceDef_T(self) -> c_long:
        return self._wrapped.ResistanceDef_T

    @property
    def ResistanceDef_C(self) -> c_long:
        return self._wrapped.ResistanceDef_C

    @property
    def TangentStiffness_T(self) -> c_double:
        return self._wrapped.TangentStiffness_T

    @property
    def TangentStiffness_C(self) -> c_double:
        return self._wrapped.TangentStiffness_C

    @property
    def Resistance_T(self) -> c_double:
        return self._wrapped.Resistance_T

    @property
    def Resistance_C(self) -> c_double:
        return self._wrapped.Resistance_C

    @property
    def HardeningRule(self) -> c_long:
        return self._wrapped.HardeningRule

    @property
    def MatrixType(self) -> c_long:
        return self._wrapped.MatrixType

    @property
    def C_t(self) -> c_double:
        return self._wrapped.C_t

    @property
    def C_C(self) -> c_double:
        return self._wrapped.C_C

    @property
    def VerticalStiffness(self) -> c_double:
        return self._wrapped.VerticalStiffness

    @property
    def IsolatorType(self) -> c_long:
        return self._wrapped.IsolatorType

    @property
    def K1(self) -> c_double:
        return self._wrapped.K1

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def F1(self) -> c_double:
        return self._wrapped.F1

    @property
    def Mu(self) -> c_double:
        return self._wrapped.Mu

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def HorizontalStiffness(self) -> c_double:
        return self._wrapped.HorizontalStiffness

    @property
    def Ksi(self) -> c_double:
        return self._wrapped.Ksi


class RSpringParamIndexes(Wrapper):

    @property
    def x(self) -> c_long:
        return self._wrapped.x

    @property
    def y(self) -> c_long:
        return self._wrapped.y

    @property
    def z(self) -> c_long:
        return self._wrapped.z

    @property
    def xx(self) -> c_long:
        return self._wrapped.xx

    @property
    def yy(self) -> c_long:
        return self._wrapped.yy

    @property
    def zz(self) -> c_long:
        return self._wrapped.zz


class RLoadBeamThermal(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Tref(self) -> c_double:
        return self._wrapped.Tref

    @property
    def Ttop(self) -> c_double:
        return self._wrapped.Ttop

    @property
    def Tbot(self) -> c_double:
        return self._wrapped.Tbot

    @property
    def Axis(self) -> c_long:
        return self._wrapped.Axis


class RColumnRebarPos(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def d(self) -> c_double:
        return self._wrapped.d


class RSnowLoadParams(Wrapper):

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def C_e(self) -> c_double:
        return self._wrapped.C_e

    @property
    def C_t(self) -> c_double:
        return self._wrapped.C_t

    @property
    def C_esl(self) -> c_double:
        return self._wrapped.C_esl

    @property
    def s_k(self) -> c_double:
        return self._wrapped.s_k

    @property
    def s_Ad(self) -> c_double:
        return self._wrapped.s_Ad

    @property
    def Iw(self) -> c_double:
        return self._wrapped.Iw

    @property
    def Zone(self) -> c_long:
        return self._wrapped.Zone


class RLoadSurfaceThermal(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def SurfaceId(self) -> c_long:
        return self._wrapped.SurfaceId

    @property
    def Tref(self) -> c_double:
        return self._wrapped.Tref

    @property
    def Ttop(self) -> c_double:
        return self._wrapped.Ttop

    @property
    def Tbot(self) -> c_double:
        return self._wrapped.Tbot


class RMovingLoadOnBeamItem(Wrapper):

    @property
    def ItemType(self) -> c_long:
        return self._wrapped.ItemType

    @property
    def Concentrated(self) -> 'RConcentratedMovingLoadOnBeam':
        return self._wrapped.Concentrated

    @property
    def Distributed(self) -> 'RDistributedMovingLoadOnBeam':
        return self._wrapped.Distributed


class RLoadBeamInfluence(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def ex(self) -> c_double:
        return self._wrapped.ex

    @property
    def ey(self) -> c_double:
        return self._wrapped.ey

    @property
    def ez(self) -> c_double:
        return self._wrapped.ez

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position


class RLoadBeamStress(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def P(self) -> c_double:
        return self._wrapped.P


class RNodalSupportForceValues(Wrapper):

    @property
    def Rx(self) -> c_double:
        return self._wrapped.Rx

    @property
    def Ry(self) -> c_double:
        return self._wrapped.Ry

    @property
    def Rz(self) -> c_double:
        return self._wrapped.Rz

    @property
    def Rxx(self) -> c_double:
        return self._wrapped.Rxx

    @property
    def Ryy(self) -> c_double:
        return self._wrapped.Ryy

    @property
    def Rzz(self) -> c_double:
        return self._wrapped.Rzz

    @property
    def Rr(self) -> c_double:
        return self._wrapped.Rr

    @property
    def Rrr(self) -> c_double:
        return self._wrapped.Rrr


class RBulkWSLineSupport(Wrapper):

    @property
    def SupportType(self) -> c_long:
        return self._wrapped.SupportType

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def NonLinearity(self) -> 'RNonLinearity':
        return self._wrapped.NonLinearity

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances

    @property
    def ShearStiffness(self) -> c_double:
        return self._wrapped.ShearStiffness

    @property
    def SurfaceId1(self) -> c_long:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> c_long:
        return self._wrapped.SurfaceId2

    @property
    def DomainId1(self) -> c_long:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> c_long:
        return self._wrapped.DomainId2

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RLoadDomainThermal(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId

    @property
    def Tref(self) -> c_double:
        return self._wrapped.Tref

    @property
    def Tsup(self) -> c_double:
        return self._wrapped.Tsup

    @property
    def Tinf(self) -> c_double:
        return self._wrapped.Tinf


class RLineSupportForceValues(Wrapper):

    @property
    def Rx(self) -> c_double:
        return self._wrapped.Rx

    @property
    def Ry(self) -> c_double:
        return self._wrapped.Ry

    @property
    def Rz(self) -> c_double:
        return self._wrapped.Rz

    @property
    def Rxx(self) -> c_double:
        return self._wrapped.Rxx

    @property
    def Ryy(self) -> c_double:
        return self._wrapped.Ryy

    @property
    def Rzz(self) -> c_double:
        return self._wrapped.Rzz

    @property
    def Rr(self) -> c_double:
        return self._wrapped.Rr

    @property
    def Rrr(self) -> c_double:
        return self._wrapped.Rrr


class RLoadPanelEdgeParams(Wrapper):

    @property
    def LoadPanelEdgeType(self) -> c_long:
        return self._wrapped.LoadPanelEdgeType

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def Alpha(self) -> c_double:
        return self._wrapped.Alpha

    @property
    def b_1(self) -> c_double:
        return self._wrapped.b_1


class RShowLocalSystems(Wrapper):

    @property
    def Beam(self) -> c_long:
        return self._wrapped.Beam

    @property
    def Rib(self) -> c_long:
        return self._wrapped.Rib

    @property
    def Surface(self) -> c_long:
        return self._wrapped.Surface

    @property
    def Domain(self) -> c_long:
        return self._wrapped.Domain

    @property
    def Support(self) -> c_long:
        return self._wrapped.Support

    @property
    def Spring(self) -> c_long:
        return self._wrapped.Spring

    @property
    def Gap(self) -> c_long:
        return self._wrapped.Gap

    @property
    def Link(self) -> c_long:
        return self._wrapped.Link

    @property
    def EdgeHinge(self) -> c_long:
        return self._wrapped.EdgeHinge


class RLoadSurfaceToBeamAssoc(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Px(self) -> c_double:
        return self._wrapped.Px

    @property
    def Py(self) -> c_double:
        return self._wrapped.Py

    @property
    def Pz(self) -> c_double:
        return self._wrapped.Pz


class RReinforcements(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def rvCenterPoint(self) -> 'RReinforcementValues':
        return self._wrapped.rvCenterPoint

    @property
    def rvContourPoint1(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourPoint1

    @property
    def rvContourPoint2(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourPoint2

    @property
    def rvContourPoint3(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourPoint3

    @property
    def rvContourPoint4(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourPoint4

    @property
    def rvContourLineMidPoint1(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourLineMidPoint1

    @property
    def rvContourLineMidPoint2(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourLineMidPoint2

    @property
    def rvContourLineMidPoint3(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourLineMidPoint3

    @property
    def rvContourLineMidPoint4(self) -> 'RReinforcementValues':
        return self._wrapped.rvContourLineMidPoint4


class RReinforcementValues(Wrapper):

    @property
    def Asbx(self) -> c_double:
        return self._wrapped.Asbx

    @property
    def Asby(self) -> c_double:
        return self._wrapped.Asby

    @property
    def Astx(self) -> c_double:
        return self._wrapped.Astx

    @property
    def Asty(self) -> c_double:
        return self._wrapped.Asty

    @property
    def AsbxStatus(self) -> c_long:
        return self._wrapped.AsbxStatus

    @property
    def AsbyStatus(self) -> c_long:
        return self._wrapped.AsbyStatus

    @property
    def AstxStatus(self) -> c_long:
        return self._wrapped.AstxStatus

    @property
    def AstyStatus(self) -> c_long:
        return self._wrapped.AstyStatus


class RTimberDesignParameters(Wrapper):

    @property
    def BreakAtElements(self) -> c_long:
        return self._wrapped.BreakAtElements

    @property
    def EC_SIA_ITA(self) -> 'RTimberDesignParameters_EC_SIA_ITA':
        return self._wrapped.EC_SIA_ITA


class RTimberDesignParameters_V153(Wrapper):

    @property
    def BreakAtElements(self) -> c_long:
        return self._wrapped.BreakAtElements

    @property
    def EC(self) -> 'RTimberDesignParameters_EC_V153':
        return self._wrapped.EC


class REdgeConnectionRec(Wrapper):

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances


class RRCBeamDesignParameters(Wrapper):

    @property
    def ConcreteMaterial(self) -> c_long:
        return self._wrapped.ConcreteMaterial

    @property
    def Dmax(self) -> c_double:
        return self._wrapped.Dmax

    @property
    def RebarMaterial(self) -> c_long:
        return self._wrapped.RebarMaterial

    @property
    def RebarType(self) -> c_long:
        return self._wrapped.RebarType

    @property
    def StirrupMaterial(self) -> c_long:
        return self._wrapped.StirrupMaterial

    @property
    def StirrupDiameter(self) -> c_double:
        return self._wrapped.StirrupDiameter

    @property
    def StirrupLegs(self) -> c_long:
        return self._wrapped.StirrupLegs

    @property
    def Shape(self) -> c_long:
        return self._wrapped.Shape

    @property
    def c_top(self) -> c_double:
        return self._wrapped.c_top

    @property
    def c_bottom(self) -> c_double:
        return self._wrapped.c_bottom

    @property
    def ds_top(self) -> c_double:
        return self._wrapped.ds_top

    @property
    def ds_bottom(self) -> c_double:
        return self._wrapped.ds_bottom

    @property
    def TakeConcTensileStrengthNL(self) -> c_long:
        return self._wrapped.TakeConcTensileStrengthNL

    @property
    def UseFctmflNL(self) -> c_long:
        return self._wrapped.UseFctmflNL

    @property
    def ShrinkageEpsNL(self) -> c_double:
        return self._wrapped.ShrinkageEpsNL


class RAccelerationValues(Wrapper):

    @property
    def avX(self) -> c_double:
        return self._wrapped.avX

    @property
    def avY(self) -> c_double:
        return self._wrapped.avY

    @property
    def avZ(self) -> c_double:
        return self._wrapped.avZ

    @property
    def avXX(self) -> c_double:
        return self._wrapped.avXX

    @property
    def avYY(self) -> c_double:
        return self._wrapped.avYY

    @property
    def avZZ(self) -> c_double:
        return self._wrapped.avZZ

    @property
    def avR(self) -> c_double:
        return self._wrapped.avR

    @property
    def avRR(self) -> c_double:
        return self._wrapped.avRR


class RSteelDesignParameters_EC_SIA_ITA_V153(Wrapper):

    @property
    def BreakAtElements(self) -> c_long:
        return self._wrapped.BreakAtElements

    @property
    def Ky(self) -> c_double:
        return self._wrapped.Ky

    @property
    def Kz(self) -> c_double:
        return self._wrapped.Kz

    @property
    def Kw(self) -> c_double:
        return self._wrapped.Kw

    @property
    def C1(self) -> c_double:
        return self._wrapped.C1

    @property
    def C2(self) -> c_double:
        return self._wrapped.C2

    @property
    def C3(self) -> c_double:
        return self._wrapped.C3

    @property
    def Za(self) -> c_double:
        return self._wrapped.Za

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def akr(self) -> c_double:
        return self._wrapped.akr

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def Stiffeners(self) -> c_long:
        return self._wrapped.Stiffeners

    @property
    def SDP_Class(self) -> c_long:
        return self._wrapped.SDP_Class

    @property
    def YBraced(self) -> c_long:
        return self._wrapped.YBraced

    @property
    def ZBraced(self) -> c_long:
        return self._wrapped.ZBraced

    @property
    def McrMethod(self) -> c_long:
        return self._wrapped.McrMethod

    @property
    def DesignApproach(self) -> c_long:
        return self._wrapped.DesignApproach

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def Cantilever(self) -> c_long:
        return self._wrapped.Cantilever

    @property
    def CantileverFixedEnd(self) -> c_long:
        return self._wrapped.CantileverFixedEnd

    @property
    def FlexuralBuckling(self) -> c_long:
        return self._wrapped.FlexuralBuckling

    @property
    def LateralTorsionalBuckling(self) -> c_long:
        return self._wrapped.LateralTorsionalBuckling

    @property
    def WebShearBuckling(self) -> c_long:
        return self._wrapped.WebShearBuckling

    @property
    def BucklingLengthModeY(self) -> c_long:
        return self._wrapped.BucklingLengthModeY

    @property
    def BucklingLengthModeZ(self) -> c_long:
        return self._wrapped.BucklingLengthModeZ

    @property
    def Ly(self) -> c_double:
        return self._wrapped.Ly

    @property
    def Lz(self) -> c_double:
        return self._wrapped.Lz

    @property
    def ConsiderN(self) -> c_long:
        return self._wrapped.ConsiderN

    @property
    def Eta(self) -> c_double:
        return self._wrapped.Eta

    @property
    def LateralSupports(self) -> c_long:
        return self._wrapped.LateralSupports

    @property
    def Mcr(self) -> c_double:
        return self._wrapped.Mcr

    @property
    def FireResistDef(self) -> c_long:
        return self._wrapped.FireResistDef

    @property
    def fpOnlyPrescribed(self) -> c_long:
        return self._wrapped.fpOnlyPrescribed

    @property
    def fpKy(self) -> c_double:
        return self._wrapped.fpKy

    @property
    def fpKz(self) -> c_double:
        return self._wrapped.fpKz

    @property
    def fpKw(self) -> c_double:
        return self._wrapped.fpKw

    @property
    def fpC1(self) -> c_double:
        return self._wrapped.fpC1

    @property
    def fpC2(self) -> c_double:
        return self._wrapped.fpC2

    @property
    def fpC3(self) -> c_double:
        return self._wrapped.fpC3

    @property
    def fpLy(self) -> c_double:
        return self._wrapped.fpLy

    @property
    def fpLz(self) -> c_double:
        return self._wrapped.fpLz

    @property
    def fpMcr(self) -> c_double:
        return self._wrapped.fpMcr

    @property
    def fpBetaMethod(self) -> c_long:
        return self._wrapped.fpBetaMethod

    @property
    def fpBetaMy(self) -> c_double:
        return self._wrapped.fpBetaMy

    @property
    def fpBetaMz(self) -> c_double:
        return self._wrapped.fpBetaMz

    @property
    def fpBetaLT(self) -> c_double:
        return self._wrapped.fpBetaLT

    @property
    def slsAngle(self) -> c_double:
        return self._wrapped.slsAngle

    @property
    def slsEyLimitDef(self) -> c_long:
        return self._wrapped.slsEyLimitDef

    @property
    def slsEzLimitDef(self) -> c_long:
        return self._wrapped.slsEzLimitDef

    @property
    def slsHxLimitDef(self) -> c_long:
        return self._wrapped.slsHxLimitDef

    @property
    def slsHyLimitDef(self) -> c_long:
        return self._wrapped.slsHyLimitDef

    @property
    def slsUyDef(self) -> c_long:
        return self._wrapped.slsUyDef

    @property
    def slsUzDef(self) -> c_long:
        return self._wrapped.slsUzDef

    @property
    def slsHGlob(self) -> c_long:
        return self._wrapped.slsHGlob

    @property
    def slsHMode(self) -> c_long:
        return self._wrapped.slsHMode

    @property
    def slsEMode(self) -> c_long:
        return self._wrapped.slsEMode

    @property
    def slsLMode(self) -> c_long:
        return self._wrapped.slsLMode

    @property
    def slsPreCamberCurve(self) -> c_long:
        return self._wrapped.slsPreCamberCurve

    @property
    def slsEyLimit(self) -> c_double:
        return self._wrapped.slsEyLimit

    @property
    def slsEzLimit(self) -> c_double:
        return self._wrapped.slsEzLimit

    @property
    def slsHxLimit(self) -> c_double:
        return self._wrapped.slsHxLimit

    @property
    def slsHyLimit(self) -> c_double:
        return self._wrapped.slsHyLimit

    @property
    def slsUy(self) -> c_double:
        return self._wrapped.slsUy

    @property
    def slsUz(self) -> c_double:
        return self._wrapped.slsUz

    @property
    def slsCustomLy(self) -> c_double:
        return self._wrapped.slsCustomLy

    @property
    def slsCustomLz(self) -> c_double:
        return self._wrapped.slsCustomLz

    @property
    def slsCustomH(self) -> c_double:
        return self._wrapped.slsCustomH

    @property
    def slsRatio(self) -> c_double:
        return self._wrapped.slsRatio


class RNodalSupportStiffParams(Wrapper):

    @property
    def Top(self) -> 'RColumnStiffnessParams':
        return self._wrapped.Top

    @property
    def Bottom(self) -> 'RColumnStiffnessParams':
        return self._wrapped.Bottom


class RPadFootingDimensions(Wrapper):

    @property
    def UpperThickness(self) -> c_double:
        return self._wrapped.UpperThickness

    @property
    def LowerThickness(self) -> c_double:
        return self._wrapped.LowerThickness

    @property
    def UpperCornerA(self) -> 'RPoint2d':
        return self._wrapped.UpperCornerA

    @property
    def UpperCornerB(self) -> 'RPoint2d':
        return self._wrapped.UpperCornerB

    @property
    def LowerCornerA(self) -> 'RPoint2d':
        return self._wrapped.LowerCornerA

    @property
    def LowerCornerB(self) -> 'RPoint2d':
        return self._wrapped.LowerCornerB


class RPadFootingParams(Wrapper):

    @property
    def HeightTop(self) -> c_double:
        return self._wrapped.HeightTop

    @property
    def HeightBottom(self) -> c_double:
        return self._wrapped.HeightBottom

    @property
    def BaseThickness(self) -> c_double:
        return self._wrapped.BaseThickness

    @property
    def bx(self) -> c_double:
        return self._wrapped.bx

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def by(self) -> c_double:
        return self._wrapped.by

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def dy1(self) -> c_double:
        return self._wrapped.dy1

    @property
    def dy2(self) -> c_double:
        return self._wrapped.dy2

    @property
    def MaterialId(self) -> c_long:
        return self._wrapped.MaterialId


class RPadFootingParams_V153(Wrapper):

    @property
    def FootingType(self) -> c_long:
        return self._wrapped.FootingType

    @property
    def VerticalType(self) -> c_long:
        return self._wrapped.VerticalType

    @property
    def MaterialId(self) -> c_long:
        return self._wrapped.MaterialId

    @property
    def GroundToBottom(self) -> c_double:
        return self._wrapped.GroundToBottom

    @property
    def HeightMain(self) -> c_double:
        return self._wrapped.HeightMain

    @property
    def HeightStep(self) -> c_double:
        return self._wrapped.HeightStep

    @property
    def BlindThickness(self) -> c_double:
        return self._wrapped.BlindThickness

    @property
    def RectangularFootingSpec(self) -> 'RRectangularFootingSpec':
        return self._wrapped.RectangularFootingSpec

    @property
    def RectangularFootingCalced(self) -> 'RRectanularFootingCalced':
        return self._wrapped.RectangularFootingCalced

    @property
    def CircularFootingSpec(self) -> 'RCircularFootingSpec':
        return self._wrapped.CircularFootingSpec

    @property
    def CircularFootingCalced(self) -> 'RCircularFootingCalced':
        return self._wrapped.CircularFootingCalced


class RShowGraphicSymbols(Wrapper):

    @property
    def Mesh(self) -> c_long:
        return self._wrapped.Mesh

    @property
    def Node(self) -> c_long:
        return self._wrapped.Node

    @property
    def SurfaceCentre(self) -> c_long:
        return self._wrapped.SurfaceCentre

    @property
    def CentreOfCircle(self) -> c_long:
        return self._wrapped.CentreOfCircle

    @property
    def Domain(self) -> c_long:
        return self._wrapped.Domain

    @property
    def NodalSupport(self) -> c_long:
        return self._wrapped.NodalSupport

    @property
    def LineSupport(self) -> c_long:
        return self._wrapped.LineSupport

    @property
    def SurfaceSupport(self) -> c_long:
        return self._wrapped.SurfaceSupport

    @property
    def Foundation(self) -> c_long:
        return self._wrapped.Foundation

    @property
    def AutoFoundationDimension(self) -> c_long:
        return self._wrapped.AutoFoundationDimension

    @property
    def Links(self) -> c_long:
        return self._wrapped.Links

    @property
    def Rigids(self) -> c_long:
        return self._wrapped.Rigids

    @property
    def Diaphragm(self) -> c_long:
        return self._wrapped.Diaphragm

    @property
    def Reference(self) -> c_long:
        return self._wrapped.Reference

    @property
    def CrossSectionShape(self) -> c_long:
        return self._wrapped.CrossSectionShape

    @property
    def EndReleases(self) -> c_long:
        return self._wrapped.EndReleases

    @property
    def StructuralMembers(self) -> c_long:
        return self._wrapped.StructuralMembers

    @property
    def ReinfParams(self) -> c_long:
        return self._wrapped.ReinfParams

    @property
    def ReinfDomain(self) -> c_long:
        return self._wrapped.ReinfDomain

    @property
    def Mass(self) -> c_long:
        return self._wrapped.Mass

    @property
    def StoreyCentGrav(self) -> c_long:
        return self._wrapped.StoreyCentGrav

    @property
    def StoreyShearCent(self) -> c_long:
        return self._wrapped.StoreyShearCent

    @property
    def ARBO_CRETelems(self) -> c_long:
        return self._wrapped.ARBO_CRETelems

    @property
    def COBIAXelems(self) -> c_long:
        return self._wrapped.COBIAXelems

    @property
    def Trusses(self) -> c_long:
        return self._wrapped.Trusses

    @property
    def Beams(self) -> c_long:
        return self._wrapped.Beams

    @property
    def Ribs(self) -> c_long:
        return self._wrapped.Ribs

    @property
    def Springs(self) -> c_long:
        return self._wrapped.Springs

    @property
    def IsolineLabels(self) -> c_long:
        return self._wrapped.IsolineLabels

    @property
    def RoundIsoValues(self) -> c_long:
        return self._wrapped.RoundIsoValues

    @property
    def Gaps(self) -> c_long:
        return self._wrapped.Gaps

    @property
    def StructuralGrids(self) -> c_long:
        return self._wrapped.StructuralGrids


class RShowLoads(Wrapper):

    @property
    def Concentrated(self) -> c_long:
        return self._wrapped.Concentrated

    @property
    def Line(self) -> c_long:
        return self._wrapped.Line

    @property
    def Surface(self) -> c_long:
        return self._wrapped.Surface

    @property
    def Temperature(self) -> c_long:
        return self._wrapped.Temperature

    @property
    def SelfWeight(self) -> c_long:
        return self._wrapped.SelfWeight

    @property
    def Miscel(self) -> c_long:
        return self._wrapped.Miscel

    @property
    def LoadDistrScheme(self) -> c_long:
        return self._wrapped.LoadDistrScheme

    @property
    def DerivedBeamLoad(self) -> c_long:
        return self._wrapped.DerivedBeamLoad

    @property
    def MovingLoadPhases(self) -> c_long:
        return self._wrapped.MovingLoadPhases


class RSteelDesignParameters_EC_SIA_ITA(Wrapper):

    @property
    def BreakAtElements(self) -> c_long:
        return self._wrapped.BreakAtElements

    @property
    def Ky(self) -> c_double:
        return self._wrapped.Ky

    @property
    def Kz(self) -> c_double:
        return self._wrapped.Kz

    @property
    def Kw(self) -> c_double:
        return self._wrapped.Kw

    @property
    def C1(self) -> c_double:
        return self._wrapped.C1

    @property
    def C2(self) -> c_double:
        return self._wrapped.C2

    @property
    def C3(self) -> c_double:
        return self._wrapped.C3

    @property
    def Za(self) -> c_double:
        return self._wrapped.Za

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def akr(self) -> c_double:
        return self._wrapped.akr

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def Stiffeners(self) -> c_long:
        return self._wrapped.Stiffeners

    @property
    def SDP_Class(self) -> c_long:
        return self._wrapped.SDP_Class

    @property
    def YBraced(self) -> c_long:
        return self._wrapped.YBraced

    @property
    def ZBraced(self) -> c_long:
        return self._wrapped.ZBraced

    @property
    def McrMethod(self) -> c_long:
        return self._wrapped.McrMethod

    @property
    def DesignApproach(self) -> c_long:
        return self._wrapped.DesignApproach

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def Cantilever(self) -> c_long:
        return self._wrapped.Cantilever

    @property
    def CantileverFixedEnd(self) -> c_long:
        return self._wrapped.CantileverFixedEnd

    @property
    def FlexuralBuckling(self) -> c_long:
        return self._wrapped.FlexuralBuckling

    @property
    def LateralTorsionalBuckling(self) -> c_long:
        return self._wrapped.LateralTorsionalBuckling

    @property
    def WebShearBuckling(self) -> c_long:
        return self._wrapped.WebShearBuckling

    @property
    def BucklingLengthModeY(self) -> c_long:
        return self._wrapped.BucklingLengthModeY

    @property
    def BucklingLengthModeZ(self) -> c_long:
        return self._wrapped.BucklingLengthModeZ

    @property
    def Ly(self) -> c_double:
        return self._wrapped.Ly

    @property
    def Lz(self) -> c_double:
        return self._wrapped.Lz

    @property
    def ConsiderN(self) -> c_long:
        return self._wrapped.ConsiderN

    @property
    def Eta(self) -> c_double:
        return self._wrapped.Eta

    @property
    def LateralSupports(self) -> c_long:
        return self._wrapped.LateralSupports

    @property
    def Mcr(self) -> c_double:
        return self._wrapped.Mcr


class RSteelDesignParameters_MSZ_STAS(Wrapper):

    @property
    def BreakAtElements(self) -> c_long:
        return self._wrapped.BreakAtElements

    @property
    def nuy(self) -> c_double:
        return self._wrapped.nuy

    @property
    def nuz(self) -> c_double:
        return self._wrapped.nuz

    @property
    def nuw(self) -> c_double:
        return self._wrapped.nuw

    @property
    def d(self) -> c_double:
        return self._wrapped.d

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def Stiffeners(self) -> c_long:
        return self._wrapped.Stiffeners


class RLoadPanelConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LoadPanelId(self) -> c_long:
        return self._wrapped.LoadPanelId

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RRebarSteelGrade_EC_ITA(Wrapper):

    @property
    def fyd(self) -> c_double:
        return self._wrapped.fyd

    @property
    def es1(self) -> c_double:
        return self._wrapped.es1

    @property
    def esu(self) -> c_double:
        return self._wrapped.esu


class RNNLinkElementRec(Wrapper):

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def MasterPoint(self) -> c_long:
        return self._wrapped.MasterPoint

    @property
    def RefZId(self) -> c_long:
        return self._wrapped.RefZId

    @property
    def PositionType(self) -> c_long:
        return self._wrapped.PositionType

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances

    @property
    def NonLinearity(self) -> 'RNonLinearity':
        return self._wrapped.NonLinearity


class RLLLinkElementRec(Wrapper):

    @property
    def MasterLine(self) -> c_long:
        return self._wrapped.MasterLine

    @property
    def SlaveLine(self) -> c_long:
        return self._wrapped.SlaveLine

    @property
    def MasterStartLink(self) -> c_long:
        return self._wrapped.MasterStartLink

    @property
    def MasterEndLink(self) -> c_long:
        return self._wrapped.MasterEndLink

    @property
    def PositionType(self) -> c_long:
        return self._wrapped.PositionType

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances

    @property
    def NonLinearity(self) -> 'RNonLinearity':
        return self._wrapped.NonLinearity


class RLinkElementRec(Wrapper):

    @property
    def NNLinkElementRec(self) -> 'RNNLinkElementRec':
        return self._wrapped.NNLinkElementRec

    @property
    def LLLinkElementRec(self) -> 'RLLLinkElementRec':
        return self._wrapped.LLLinkElementRec


class REdgeConnectionForces(Wrapper):

    @property
    def ecfSection1(self) -> 'REdgeConnectionForceValues':
        return self._wrapped.ecfSection1

    @property
    def ecfSection2(self) -> 'REdgeConnectionForceValues':
        return self._wrapped.ecfSection2

    @property
    def ecfSection3(self) -> 'REdgeConnectionForceValues':
        return self._wrapped.ecfSection3


class REdgeConnectionForceValues(Wrapper):

    @property
    def ecfvNx(self) -> c_double:
        return self._wrapped.ecfvNx

    @property
    def ecfvVy(self) -> c_double:
        return self._wrapped.ecfvVy

    @property
    def ecfvVz(self) -> c_double:
        return self._wrapped.ecfvVz

    @property
    def ecfvTx(self) -> c_double:
        return self._wrapped.ecfvTx

    @property
    def ecfvMy(self) -> c_double:
        return self._wrapped.ecfvMy

    @property
    def ecfvMz(self) -> c_double:
        return self._wrapped.ecfvMz


class RRebarSteelGrade_MSZ(Wrapper):

    @property
    def ssh(self) -> c_double:
        return self._wrapped.ssh

    @property
    def es0(self) -> c_double:
        return self._wrapped.es0

    @property
    def esh(self) -> c_double:
        return self._wrapped.esh


class RReinforcementParameters_ITA(Wrapper):

    @property
    def AggregateSize(self) -> c_double:
        return self._wrapped.AggregateSize

    @property
    def StructClass(self) -> c_long:
        return self._wrapped.StructClass

    @property
    def EnvClass_T(self) -> c_long:
        return self._wrapped.EnvClass_T

    @property
    def EnvClass_B(self) -> c_long:
        return self._wrapped.EnvClass_B

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def UnfavorableEccentricity_Npos(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Npos

    @property
    def UnfavorableEccentricity_Nneg(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Nneg

    @property
    def dxt(self) -> c_double:
        return self._wrapped.dxt

    @property
    def dxb(self) -> c_double:
        return self._wrapped.dxb

    @property
    def dyt(self) -> c_double:
        return self._wrapped.dyt

    @property
    def dyb(self) -> c_double:
        return self._wrapped.dyb

    @property
    def SlabLoadTransfer(self) -> c_long:
        return self._wrapped.SlabLoadTransfer

    @property
    def SlabLoadTransferDirection(self) -> c_long:
        return self._wrapped.SlabLoadTransferDirection

    @property
    def MainDirectionTop(self) -> c_long:
        return self._wrapped.MainDirectionTop

    @property
    def MainDirectionBottom(self) -> c_long:
        return self._wrapped.MainDirectionBottom

    @property
    def ct(self) -> c_double:
        return self._wrapped.ct

    @property
    def cb(self) -> c_double:
        return self._wrapped.cb

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def ShortTerm(self) -> c_long:
        return self._wrapped.ShortTerm

    @property
    def ShearReinforcementAngle(self) -> c_double:
        return self._wrapped.ShearReinforcementAngle

    @property
    def ShearCrackAngle(self) -> c_double:
        return self._wrapped.ShearCrackAngle

    @property
    def TakeConcTensileStrengthNL(self) -> c_long:
        return self._wrapped.TakeConcTensileStrengthNL

    @property
    def UseFctmfl(self) -> c_long:
        return self._wrapped.UseFctmfl

    @property
    def ShrinkageEps(self) -> c_double:
        return self._wrapped.ShrinkageEps

    @property
    def RCNonlinearSurfType(self) -> c_long:
        return self._wrapped.RCNonlinearSurfType

    @property
    def ReinforcementType(self) -> c_long:
        return self._wrapped.ReinforcementType

    @property
    def AlphaAngle(self) -> c_double:
        return self._wrapped.AlphaAngle

    @property
    def BetaAngle(self) -> c_double:
        return self._wrapped.BetaAngle

    @property
    def CalcFromLimitingCrackWidth(self) -> c_long:
        return self._wrapped.CalcFromLimitingCrackWidth

    @property
    def wk_b(self) -> c_double:
        return self._wrapped.wk_b

    @property
    def wk2_b(self) -> c_double:
        return self._wrapped.wk2_b

    @property
    def wk_t(self) -> c_double:
        return self._wrapped.wk_t

    @property
    def wk2_t(self) -> c_double:
        return self._wrapped.wk2_t

    @property
    def ApproximateLevelArm(self) -> c_long:
        return self._wrapped.ApproximateLevelArm

    @property
    def SeelhoferMartiEquation(self) -> c_long:
        return self._wrapped.SeelhoferMartiEquation

    @property
    def TrapSheetOnlyFormWork(self) -> c_long:
        return self._wrapped.TrapSheetOnlyFormWork

    @property
    def TrapSheetOneLayerReinf(self) -> c_long:
        return self._wrapped.TrapSheetOneLayerReinf

    @property
    def TrapSheetConsidered(self) -> c_long:
        return self._wrapped.TrapSheetConsidered


class RLinkElementForces(Wrapper):

    @property
    def lefLinkElementType(self) -> c_long:
        return self._wrapped.lefLinkElementType

    @property
    def lefSection1(self) -> 'RLinkElementForceValues':
        return self._wrapped.lefSection1

    @property
    def lefSection2(self) -> 'RLinkElementForceValues':
        return self._wrapped.lefSection2

    @property
    def lefSection3(self) -> 'RLinkElementForceValues':
        return self._wrapped.lefSection3


class RLinkElementForceValues(Wrapper):

    @property
    def lefvNx(self) -> c_double:
        return self._wrapped.lefvNx

    @property
    def lefvVy(self) -> c_double:
        return self._wrapped.lefvVy

    @property
    def lefvVz(self) -> c_double:
        return self._wrapped.lefvVz

    @property
    def lefvTx(self) -> c_double:
        return self._wrapped.lefvTx

    @property
    def lefvMy(self) -> c_double:
        return self._wrapped.lefvMy

    @property
    def lefvMz(self) -> c_double:
        return self._wrapped.lefvMz


class RSurface(Wrapper):

    @property
    def N(self) -> c_long:
        return self._wrapped.N

    @property
    def LineIndex1(self) -> c_long:
        return self._wrapped.LineIndex1

    @property
    def LineIndex2(self) -> c_long:
        return self._wrapped.LineIndex2

    @property
    def LineIndex3(self) -> c_long:
        return self._wrapped.LineIndex3

    @property
    def LineIndex4(self) -> c_long:
        return self._wrapped.LineIndex4

    @property
    def Attr(self) -> 'RSurfaceAttr':
        return self._wrapped.Attr

    @property
    def DomainIndex(self) -> c_long:
        return self._wrapped.DomainIndex


class RElasticFoundationXYZ(Wrapper):

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z


class RLoadBeamDistributed(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def qx1(self) -> c_double:
        return self._wrapped.qx1

    @property
    def qy1(self) -> c_double:
        return self._wrapped.qy1

    @property
    def qz1(self) -> c_double:
        return self._wrapped.qz1

    @property
    def mx1(self) -> c_double:
        return self._wrapped.mx1

    @property
    def my1(self) -> c_double:
        return self._wrapped.my1

    @property
    def mz1(self) -> c_double:
        return self._wrapped.mz1

    @property
    def qx2(self) -> c_double:
        return self._wrapped.qx2

    @property
    def qy2(self) -> c_double:
        return self._wrapped.qy2

    @property
    def qz2(self) -> c_double:
        return self._wrapped.qz2

    @property
    def mx2(self) -> c_double:
        return self._wrapped.mx2

    @property
    def my2(self) -> c_double:
        return self._wrapped.my2

    @property
    def mz2(self) -> c_double:
        return self._wrapped.mz2

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def Position1(self) -> c_double:
        return self._wrapped.Position1

    @property
    def Position2(self) -> c_double:
        return self._wrapped.Position2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Trapezoid(self) -> c_long:
        return self._wrapped.Trapezoid


class RSurfaceStressValues(Wrapper):

    @property
    def ssvSxx(self) -> c_double:
        return self._wrapped.ssvSxx

    @property
    def ssvSyy(self) -> c_double:
        return self._wrapped.ssvSyy

    @property
    def ssvSxy(self) -> c_double:
        return self._wrapped.ssvSxy

    @property
    def ssvSxz(self) -> c_double:
        return self._wrapped.ssvSxz

    @property
    def ssvSyz(self) -> c_double:
        return self._wrapped.ssvSyz

    @property
    def ssvSVM(self) -> c_double:
        return self._wrapped.ssvSVM

    @property
    def ssvS1(self) -> c_double:
        return self._wrapped.ssvS1

    @property
    def ssvS2(self) -> c_double:
        return self._wrapped.ssvS2

    @property
    def ssvAs(self) -> c_double:
        return self._wrapped.ssvAs


class RLine3d(Wrapper):

    @property
    def LineType(self) -> c_long:
        return self._wrapped.LineType

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2

    @property
    def ArcCenter(self) -> 'RPoint3d':
        return self._wrapped.ArcCenter

    @property
    def ArcOrientation(self) -> c_long:
        return self._wrapped.ArcOrientation

    @property
    def NormVect(self) -> 'RPoint3d':
        return self._wrapped.NormVect


class RRCBeamCrossSections(Wrapper):

    @property
    def StartSection(self) -> 'RRCBeamSection':
        return self._wrapped.StartSection

    @property
    def EndSection(self) -> 'RRCBeamSection':
        return self._wrapped.EndSection


class RRCBeamSection(Wrapper):

    @property
    def bw(self) -> c_double:
        return self._wrapped.bw

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def hf(self) -> c_double:
        return self._wrapped.hf

    @property
    def beff(self) -> c_double:
        return self._wrapped.beff


class RLoadRibDistributed(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def qx1(self) -> c_double:
        return self._wrapped.qx1

    @property
    def qy1(self) -> c_double:
        return self._wrapped.qy1

    @property
    def qz1(self) -> c_double:
        return self._wrapped.qz1

    @property
    def mx1(self) -> c_double:
        return self._wrapped.mx1

    @property
    def my1(self) -> c_double:
        return self._wrapped.my1

    @property
    def mz1(self) -> c_double:
        return self._wrapped.mz1

    @property
    def qx2(self) -> c_double:
        return self._wrapped.qx2

    @property
    def qy2(self) -> c_double:
        return self._wrapped.qy2

    @property
    def qz2(self) -> c_double:
        return self._wrapped.qz2

    @property
    def mx2(self) -> c_double:
        return self._wrapped.mx2

    @property
    def my2(self) -> c_double:
        return self._wrapped.my2

    @property
    def mz2(self) -> c_double:
        return self._wrapped.mz2

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def Position1(self) -> c_double:
        return self._wrapped.Position1

    @property
    def Position2(self) -> c_double:
        return self._wrapped.Position2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Trapezoid(self) -> c_long:
        return self._wrapped.Trapezoid


class RResultBlock(Wrapper):

    @property
    def ResultType(self) -> c_long:
        return self._wrapped.ResultType

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LoadCombinationId(self) -> c_long:
        return self._wrapped.LoadCombinationId

    @property
    def LoadLevel(self) -> c_long:
        return self._wrapped.LoadLevel

    @property
    def AnalysisType(self) -> c_long:
        return self._wrapped.AnalysisType

    @property
    def MinMaxType(self) -> c_long:
        return self._wrapped.MinMaxType

    @property
    def EnvelopeUID(self) -> c_long:
        return self._wrapped.EnvelopeUID

    @property
    def CombinationType(self) -> c_long:
        return self._wrapped.CombinationType


class RRebarSteelGrade_DIN(Wrapper):

    @property
    def fyk(self) -> c_double:
        return self._wrapped.fyk

    @property
    def Epsuk(self) -> c_double:
        return self._wrapped.Epsuk

    @property
    def GammaS(self) -> c_double:
        return self._wrapped.GammaS


class RLineStressValues(Wrapper):

    @property
    def lsvLineType(self) -> c_long:
        return self._wrapped.lsvLineType

    @property
    def lsvPointCount(self) -> c_long:
        return self._wrapped.lsvPointCount

    @property
    def lsvS1(self) -> c_double:
        return self._wrapped.lsvS1

    @property
    def lsvS2(self) -> c_double:
        return self._wrapped.lsvS2

    @property
    def lsvS3(self) -> c_double:
        return self._wrapped.lsvS3

    @property
    def lsvS4(self) -> c_double:
        return self._wrapped.lsvS4

    @property
    def lsvS5(self) -> c_double:
        return self._wrapped.lsvS5

    @property
    def lsvS6(self) -> c_double:
        return self._wrapped.lsvS6

    @property
    def lsvS7(self) -> c_double:
        return self._wrapped.lsvS7

    @property
    def lsvS8(self) -> c_double:
        return self._wrapped.lsvS8

    @property
    def lsvS9(self) -> c_double:
        return self._wrapped.lsvS9

    @property
    def lsvV1(self) -> c_double:
        return self._wrapped.lsvV1

    @property
    def lsvV2(self) -> c_double:
        return self._wrapped.lsvV2

    @property
    def lsvV3(self) -> c_double:
        return self._wrapped.lsvV3

    @property
    def lsvV4(self) -> c_double:
        return self._wrapped.lsvV4

    @property
    def lsvV5(self) -> c_double:
        return self._wrapped.lsvV5

    @property
    def lsvV6(self) -> c_double:
        return self._wrapped.lsvV6

    @property
    def lsvV7(self) -> c_double:
        return self._wrapped.lsvV7

    @property
    def lsvV8(self) -> c_double:
        return self._wrapped.lsvV8

    @property
    def lsvV9(self) -> c_double:
        return self._wrapped.lsvV9

    @property
    def lsvSo1(self) -> c_double:
        return self._wrapped.lsvSo1

    @property
    def lsvSo2(self) -> c_double:
        return self._wrapped.lsvSo2

    @property
    def lsvSo3(self) -> c_double:
        return self._wrapped.lsvSo3

    @property
    def lsvSo4(self) -> c_double:
        return self._wrapped.lsvSo4

    @property
    def lsvSo5(self) -> c_double:
        return self._wrapped.lsvSo5

    @property
    def lsvSo6(self) -> c_double:
        return self._wrapped.lsvSo6

    @property
    def lsvSo7(self) -> c_double:
        return self._wrapped.lsvSo7

    @property
    def lsvSo8(self) -> c_double:
        return self._wrapped.lsvSo8

    @property
    def lsvSo9(self) -> c_double:
        return self._wrapped.lsvSo9

    @property
    def lsvSeff1(self) -> c_double:
        return self._wrapped.lsvSeff1

    @property
    def lsvSeff2(self) -> c_double:
        return self._wrapped.lsvSeff2

    @property
    def lsvSeff3(self) -> c_double:
        return self._wrapped.lsvSeff3

    @property
    def lsvSeff4(self) -> c_double:
        return self._wrapped.lsvSeff4

    @property
    def lsvSeff5(self) -> c_double:
        return self._wrapped.lsvSeff5

    @property
    def lsvSeff6(self) -> c_double:
        return self._wrapped.lsvSeff6

    @property
    def lsvSeff7(self) -> c_double:
        return self._wrapped.lsvSeff7

    @property
    def lsvSeff8(self) -> c_double:
        return self._wrapped.lsvSeff8

    @property
    def lsvSeff9(self) -> c_double:
        return self._wrapped.lsvSeff9

    @property
    def lsvfy1(self) -> c_double:
        return self._wrapped.lsvfy1

    @property
    def lsvfy2(self) -> c_double:
        return self._wrapped.lsvfy2

    @property
    def lsvfy3(self) -> c_double:
        return self._wrapped.lsvfy3

    @property
    def lsvfy4(self) -> c_double:
        return self._wrapped.lsvfy4

    @property
    def lsvfy5(self) -> c_double:
        return self._wrapped.lsvfy5

    @property
    def lsvfy6(self) -> c_double:
        return self._wrapped.lsvfy6

    @property
    def lsvfy7(self) -> c_double:
        return self._wrapped.lsvfy7

    @property
    def lsvfy8(self) -> c_double:
        return self._wrapped.lsvfy8

    @property
    def lsvfy9(self) -> c_double:
        return self._wrapped.lsvfy9

    @property
    def lsvKih1(self) -> c_double:
        return self._wrapped.lsvKih1

    @property
    def lsvKih2(self) -> c_double:
        return self._wrapped.lsvKih2

    @property
    def lsvKih3(self) -> c_double:
        return self._wrapped.lsvKih3

    @property
    def lsvKih4(self) -> c_double:
        return self._wrapped.lsvKih4

    @property
    def lsvKih5(self) -> c_double:
        return self._wrapped.lsvKih5

    @property
    def lsvKih6(self) -> c_double:
        return self._wrapped.lsvKih6

    @property
    def lsvKih7(self) -> c_double:
        return self._wrapped.lsvKih7

    @property
    def lsvKih8(self) -> c_double:
        return self._wrapped.lsvKih8

    @property
    def lsvKih9(self) -> c_double:
        return self._wrapped.lsvKih9

    @property
    def lsvVymean(self) -> c_double:
        return self._wrapped.lsvVymean

    @property
    def lsvVzmean(self) -> c_double:
        return self._wrapped.lsvVzmean

    @property
    def lsvSmin(self) -> c_long:
        return self._wrapped.lsvSmin

    @property
    def lsvSmax(self) -> c_long:
        return self._wrapped.lsvSmax

    @property
    def lsvVmin(self) -> c_long:
        return self._wrapped.lsvVmin

    @property
    def lsvVmax(self) -> c_long:
        return self._wrapped.lsvVmax

    @property
    def lsvSomin(self) -> c_long:
        return self._wrapped.lsvSomin

    @property
    def lsvSomax(self) -> c_long:
        return self._wrapped.lsvSomax


class RSurfaceStressValuesTMB(Wrapper):

    @property
    def ssvTop(self) -> 'RSurfaceStressValues':
        return self._wrapped.ssvTop

    @property
    def ssvMiddle(self) -> 'RSurfaceStressValues':
        return self._wrapped.ssvMiddle

    @property
    def ssvBottom(self) -> 'RSurfaceStressValues':
        return self._wrapped.ssvBottom


class RRebarSteelGrade_STAS(Wrapper):

    @property
    def Ra(self) -> c_double:
        return self._wrapped.Ra

    @property
    def es1(self) -> c_double:
        return self._wrapped.es1

    @property
    def esu(self) -> c_double:
        return self._wrapped.esu

    @property
    def mat(self) -> c_double:
        return self._wrapped.mat


class RRCBeamSupport(Wrapper):

    @property
    def OverWrite(self) -> c_long:
        return self._wrapped.OverWrite

    @property
    def ActualHalfWidth(self) -> c_double:
        return self._wrapped.ActualHalfWidth

    @property
    def TheoreticalHalfWidth(self) -> c_double:
        return self._wrapped.TheoreticalHalfWidth

    @property
    def ShearReduction(self) -> c_long:
        return self._wrapped.ShearReduction


class RReinforcementParameters_SIA(Wrapper):

    @property
    def AggregateSize(self) -> c_double:
        return self._wrapped.AggregateSize

    @property
    def StructClass(self) -> c_long:
        return self._wrapped.StructClass

    @property
    def EnvClass_T(self) -> c_long:
        return self._wrapped.EnvClass_T

    @property
    def EnvClass_B(self) -> c_long:
        return self._wrapped.EnvClass_B

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def dxt(self) -> c_double:
        return self._wrapped.dxt

    @property
    def dxb(self) -> c_double:
        return self._wrapped.dxb

    @property
    def dyt(self) -> c_double:
        return self._wrapped.dyt

    @property
    def dyb(self) -> c_double:
        return self._wrapped.dyb

    @property
    def SlabLoadTransfer(self) -> c_long:
        return self._wrapped.SlabLoadTransfer

    @property
    def SlabLoadTransferDirection(self) -> c_long:
        return self._wrapped.SlabLoadTransferDirection

    @property
    def MainDirectionTop(self) -> c_long:
        return self._wrapped.MainDirectionTop

    @property
    def MainDirectionBottom(self) -> c_long:
        return self._wrapped.MainDirectionBottom

    @property
    def ct(self) -> c_double:
        return self._wrapped.ct

    @property
    def cb(self) -> c_double:
        return self._wrapped.cb

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def MaxCompressionHeight(self) -> c_double:
        return self._wrapped.MaxCompressionHeight

    @property
    def kc_compression(self) -> c_double:
        return self._wrapped.kc_compression

    @property
    def kc_tension(self) -> c_double:
        return self._wrapped.kc_tension

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def ShortTerm(self) -> c_long:
        return self._wrapped.ShortTerm

    @property
    def ShearReinforcementAngle(self) -> c_double:
        return self._wrapped.ShearReinforcementAngle

    @property
    def ShearCrackAngle(self) -> c_double:
        return self._wrapped.ShearCrackAngle

    @property
    def TakeConcTensileStrengthNL(self) -> c_long:
        return self._wrapped.TakeConcTensileStrengthNL

    @property
    def ShrinkageEps(self) -> c_double:
        return self._wrapped.ShrinkageEps

    @property
    def RCNonlinearSurfType(self) -> c_long:
        return self._wrapped.RCNonlinearSurfType

    @property
    def ReinforcementType(self) -> c_long:
        return self._wrapped.ReinforcementType

    @property
    def AlphaAngle(self) -> c_double:
        return self._wrapped.AlphaAngle

    @property
    def BetaAngle(self) -> c_double:
        return self._wrapped.BetaAngle

    @property
    def CalcFromLimitingCrackWidth(self) -> c_long:
        return self._wrapped.CalcFromLimitingCrackWidth

    @property
    def wk_b(self) -> c_double:
        return self._wrapped.wk_b

    @property
    def wk2_b(self) -> c_double:
        return self._wrapped.wk2_b

    @property
    def wk_t(self) -> c_double:
        return self._wrapped.wk_t

    @property
    def wk2_t(self) -> c_double:
        return self._wrapped.wk2_t

    @property
    def ApproximateLevelArm(self) -> c_long:
        return self._wrapped.ApproximateLevelArm

    @property
    def SeelhoferMartiEquation(self) -> c_long:
        return self._wrapped.SeelhoferMartiEquation

    @property
    def TrapSheetOnlyFormWork(self) -> c_long:
        return self._wrapped.TrapSheetOnlyFormWork

    @property
    def TrapSheetOneLayerReinf(self) -> c_long:
        return self._wrapped.TrapSheetOneLayerReinf

    @property
    def TrapSheetConsidered(self) -> c_long:
        return self._wrapped.TrapSheetConsidered


class RRebarSteelGrade_SIA(Wrapper):

    @property
    def fsk(self) -> c_double:
        return self._wrapped.fsk

    @property
    def ks(self) -> c_double:
        return self._wrapped.ks

    @property
    def Epsuk(self) -> c_double:
        return self._wrapped.Epsuk

    @property
    def Epsud(self) -> c_double:
        return self._wrapped.Epsud

    @property
    def GammaS(self) -> c_double:
        return self._wrapped.GammaS


class RLoadBeamConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Fgx(self) -> c_double:
        return self._wrapped.Fgx

    @property
    def Fgy(self) -> c_double:
        return self._wrapped.Fgy

    @property
    def Fgz(self) -> c_double:
        return self._wrapped.Fgz

    @property
    def Mgx(self) -> c_double:
        return self._wrapped.Mgx

    @property
    def Mgy(self) -> c_double:
        return self._wrapped.Mgy

    @property
    def Mgz(self) -> c_double:
        return self._wrapped.Mgz

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR


class RLineSupportStiffParams(Wrapper):

    @property
    def Top(self) -> 'RWallStiffnessParams':
        return self._wrapped.Top

    @property
    def Bottom(self) -> 'RWallStiffnessParams':
        return self._wrapped.Bottom


class RLinearFootingParams(Wrapper):

    @property
    def VerticalType(self) -> c_long:
        return self._wrapped.VerticalType

    @property
    def MaterialId(self) -> c_long:
        return self._wrapped.MaterialId

    @property
    def GroundToBottom(self) -> c_double:
        return self._wrapped.GroundToBottom

    @property
    def HeightMain(self) -> c_double:
        return self._wrapped.HeightMain

    @property
    def HeightStep(self) -> c_double:
        return self._wrapped.HeightStep

    @property
    def BlindThickness(self) -> c_double:
        return self._wrapped.BlindThickness

    @property
    def FootingSpec(self) -> 'RLinearFootingSpec':
        return self._wrapped.FootingSpec

    @property
    def FootingCalced(self) -> 'RLinearFootingCalced':
        return self._wrapped.FootingCalced


class RBulkMemberSupport(Wrapper):

    @property
    def SupportType(self) -> c_long:
        return self._wrapped.SupportType

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def NonLinearity(self) -> 'RNonLinearity':
        return self._wrapped.NonLinearity

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances

    @property
    def SurfaceId1(self) -> c_long:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> c_long:
        return self._wrapped.SurfaceId2

    @property
    def DomainId1(self) -> c_long:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> c_long:
        return self._wrapped.DomainId2

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RBulkMemberWSSupport(Wrapper):

    @property
    def SupportType(self) -> c_long:
        return self._wrapped.SupportType

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def Stiffnesses(self) -> 'RStiffnesses':
        return self._wrapped.Stiffnesses

    @property
    def NonLinearity(self) -> 'RNonLinearity':
        return self._wrapped.NonLinearity

    @property
    def Resistances(self) -> 'RResistances':
        return self._wrapped.Resistances

    @property
    def ShearStiffness(self) -> c_double:
        return self._wrapped.ShearStiffness

    @property
    def SurfaceId1(self) -> c_long:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> c_long:
        return self._wrapped.SurfaceId2

    @property
    def DomainId1(self) -> c_long:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> c_long:
        return self._wrapped.DomainId2

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RSectionSegmentIntegratedResultant(Wrapper):

    @property
    def N(self) -> c_double:
        return self._wrapped.N

    @property
    def M(self) -> c_double:
        return self._wrapped.M

    @property
    def V(self) -> c_double:
        return self._wrapped.V


class RReference(Wrapper):

    @property
    def ReferenceType(self) -> c_long:
        return self._wrapped.ReferenceType

    @property
    def ReferenceData(self) -> 'RRefData':
        return self._wrapped.ReferenceData


class RSteelLateralSupport(Wrapper):

    @property
    def Pos(self) -> c_double:
        return self._wrapped.Pos

    @property
    def Ecc(self) -> c_double:
        return self._wrapped.Ecc

    @property
    def Ry(self) -> c_double:
        return self._wrapped.Ry

    @property
    def Rxx(self) -> c_double:
        return self._wrapped.Rxx

    @property
    def Rzz(self) -> c_double:
        return self._wrapped.Rzz

    @property
    def Rw(self) -> c_double:
        return self._wrapped.Rw


class RRCBeamDesignDeflectionResult(Wrapper):

    @property
    def CombinationOrLoadCaseID(self) -> c_long:
        return self._wrapped.CombinationOrLoadCaseID

    @property
    def ez(self) -> c_double:
        return self._wrapped.ez


class RLineForceValues(Wrapper):

    @property
    def lfvLineType(self) -> c_long:
        return self._wrapped.lfvLineType

    @property
    def lfvNx(self) -> c_double:
        return self._wrapped.lfvNx

    @property
    def lfvVy(self) -> c_double:
        return self._wrapped.lfvVy

    @property
    def lfvVz(self) -> c_double:
        return self._wrapped.lfvVz

    @property
    def lfvTx(self) -> c_double:
        return self._wrapped.lfvTx

    @property
    def lfvMy(self) -> c_double:
        return self._wrapped.lfvMy

    @property
    def lfvMz(self) -> c_double:
        return self._wrapped.lfvMz

    @property
    def lfvMyD(self) -> c_double:
        return self._wrapped.lfvMyD


class RResultBlockInfo(Wrapper):

    @property
    def ResultCase(self) -> c_long:
        return self._wrapped.ResultCase

    @property
    def LoadLevelOrModeShapeOrTimeStep(self) -> c_long:
        return self._wrapped.LoadLevelOrModeShapeOrTimeStep


class RSurfaceForceValues(Wrapper):

    @property
    def sfvNx(self) -> c_double:
        return self._wrapped.sfvNx

    @property
    def sfvNy(self) -> c_double:
        return self._wrapped.sfvNy

    @property
    def sfvNxy(self) -> c_double:
        return self._wrapped.sfvNxy

    @property
    def sfvMx(self) -> c_double:
        return self._wrapped.sfvMx

    @property
    def sfvMy(self) -> c_double:
        return self._wrapped.sfvMy

    @property
    def sfvMxy(self) -> c_double:
        return self._wrapped.sfvMxy

    @property
    def sfvVxz(self) -> c_double:
        return self._wrapped.sfvVxz

    @property
    def sfvVyz(self) -> c_double:
        return self._wrapped.sfvVyz

    @property
    def sfvVSz(self) -> c_double:
        return self._wrapped.sfvVSz

    @property
    def sfvN1(self) -> c_double:
        return self._wrapped.sfvN1

    @property
    def sfvN2(self) -> c_double:
        return self._wrapped.sfvN2

    @property
    def sfvAn(self) -> c_double:
        return self._wrapped.sfvAn

    @property
    def sfvM1(self) -> c_double:
        return self._wrapped.sfvM1

    @property
    def sfvM2(self) -> c_double:
        return self._wrapped.sfvM2

    @property
    def sfvAm(self) -> c_double:
        return self._wrapped.sfvAm

    @property
    def sfvNxD(self) -> c_double:
        return self._wrapped.sfvNxD

    @property
    def sfvNyD(self) -> c_double:
        return self._wrapped.sfvNyD

    @property
    def sfvMxDp(self) -> c_double:
        return self._wrapped.sfvMxDp

    @property
    def sfvMxDm(self) -> c_double:
        return self._wrapped.sfvMxDm

    @property
    def sfvMyDp(self) -> c_double:
        return self._wrapped.sfvMyDp

    @property
    def sfvMyDm(self) -> c_double:
        return self._wrapped.sfvMyDm


class RSurfaceForces(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def sfvCenterPoint(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvCenterPoint

    @property
    def sfvContourPoint1(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourPoint1

    @property
    def sfvContourPoint2(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourPoint2

    @property
    def sfvContourPoint3(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourPoint3

    @property
    def sfvContourPoint4(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourPoint4

    @property
    def sfvContourLineMidPoint1(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourLineMidPoint1

    @property
    def sfvContourLineMidPoint2(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourLineMidPoint2

    @property
    def sfvContourLineMidPoint3(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourLineMidPoint3

    @property
    def sfvContourLineMidPoint4(self) -> 'RSurfaceForceValues':
        return self._wrapped.sfvContourLineMidPoint4


class RSurfaceSupportForceValues(Wrapper):

    @property
    def Rx(self) -> c_double:
        return self._wrapped.Rx

    @property
    def Ry(self) -> c_double:
        return self._wrapped.Ry

    @property
    def Rz(self) -> c_double:
        return self._wrapped.Rz


class RSurfaceSupportForces(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def ssfvCenterPoint(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvCenterPoint

    @property
    def ssfvContourPoint1(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourPoint1

    @property
    def ssfvContourPoint2(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourPoint2

    @property
    def ssfvContourPoint3(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourPoint3

    @property
    def ssfvContourPoint4(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourPoint4

    @property
    def ssfvContourLineMidPoint1(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourLineMidPoint1

    @property
    def ssfvContourLineMidPoint2(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourLineMidPoint2

    @property
    def ssfvContourLineMidPoint3(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourLineMidPoint3

    @property
    def ssfvContourLineMidPoint4(self) -> 'RSurfaceSupportForceValues':
        return self._wrapped.ssfvContourLineMidPoint4


class RSpringForceValues(Wrapper):

    @property
    def Rx(self) -> c_double:
        return self._wrapped.Rx

    @property
    def Ry(self) -> c_double:
        return self._wrapped.Ry

    @property
    def Rz(self) -> c_double:
        return self._wrapped.Rz

    @property
    def Rxx(self) -> c_double:
        return self._wrapped.Rxx

    @property
    def Ryy(self) -> c_double:
        return self._wrapped.Ryy

    @property
    def Rzz(self) -> c_double:
        return self._wrapped.Rzz


class RVirtualBeamForceValues(Wrapper):

    @property
    def vbfvNx(self) -> c_double:
        return self._wrapped.vbfvNx

    @property
    def vbfvVy(self) -> c_double:
        return self._wrapped.vbfvVy

    @property
    def vbfvVz(self) -> c_double:
        return self._wrapped.vbfvVz

    @property
    def vbfvTx(self) -> c_double:
        return self._wrapped.vbfvTx

    @property
    def vbfvMy(self) -> c_double:
        return self._wrapped.vbfvMy

    @property
    def vbfvMz(self) -> c_double:
        return self._wrapped.vbfvMz


class RCombinationElement(Wrapper):

    @property
    def LoadCase(self) -> c_long:
        return self._wrapped.LoadCase

    @property
    def Factor(self) -> c_double:
        return self._wrapped.Factor


class RRCBeamDesignDeflectionResults(Wrapper):

    @property
    def Min(self) -> 'RRCBeamDesignDeflectionResult':
        return self._wrapped.Min

    @property
    def Max(self) -> 'RRCBeamDesignDeflectionResult':
        return self._wrapped.Max


class RWallStiffnessParams(Wrapper):

    @property
    def CalcParams(self) -> 'RElementStiffnessParams':
        return self._wrapped.CalcParams

    @property
    def WallThickness(self) -> c_double:
        return self._wrapped.WallThickness


class RElementStiffnessParams(Wrapper):

    @property
    def MaterialId(self) -> c_long:
        return self._wrapped.MaterialId

    @property
    def Height(self) -> c_double:
        return self._wrapped.Height

    @property
    def EndReleaseXTop(self) -> c_long:
        return self._wrapped.EndReleaseXTop

    @property
    def EndReleaseXBottom(self) -> c_long:
        return self._wrapped.EndReleaseXBottom


class RRefPoint(Wrapper):

    @property
    def P(self) -> 'RPoint3d':
        return self._wrapped.P


class RLoadBeamMemberDistributed(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def qx1(self) -> c_double:
        return self._wrapped.qx1

    @property
    def qy1(self) -> c_double:
        return self._wrapped.qy1

    @property
    def qz1(self) -> c_double:
        return self._wrapped.qz1

    @property
    def mx1(self) -> c_double:
        return self._wrapped.mx1

    @property
    def my1(self) -> c_double:
        return self._wrapped.my1

    @property
    def mz1(self) -> c_double:
        return self._wrapped.mz1

    @property
    def qx2(self) -> c_double:
        return self._wrapped.qx2

    @property
    def qy2(self) -> c_double:
        return self._wrapped.qy2

    @property
    def qz2(self) -> c_double:
        return self._wrapped.qz2

    @property
    def mx2(self) -> c_double:
        return self._wrapped.mx2

    @property
    def my2(self) -> c_double:
        return self._wrapped.my2

    @property
    def mz2(self) -> c_double:
        return self._wrapped.mz2

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def Position1(self) -> c_double:
        return self._wrapped.Position1

    @property
    def Position2(self) -> c_double:
        return self._wrapped.Position2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Trapezoid(self) -> c_long:
        return self._wrapped.Trapezoid


class RMyMzFi(Wrapper):

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def fi(self) -> c_double:
        return self._wrapped.fi


class RColumnReinforcementParameters(Wrapper):

    @property
    def ColumnRebarsId(self) -> c_long:
        return self._wrapped.ColumnRebarsId

    @property
    def ConcreteMaterialId(self) -> c_long:
        return self._wrapped.ConcreteMaterialId

    @property
    def RebarSteelGradeId(self) -> c_long:
        return self._wrapped.RebarSteelGradeId

    @property
    def CheckingParameters(self) -> 'RColumnCheckingParameters':
        return self._wrapped.CheckingParameters

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def UseFctmfl(self) -> c_long:
        return self._wrapped.UseFctmfl

    @property
    def ShrinkageEps(self) -> c_double:
        return self._wrapped.ShrinkageEps

    @property
    def SpiralStirrup(self) -> c_long:
        return self._wrapped.SpiralStirrup

    @property
    def StirrupSpacing(self) -> 'RColumnStirrupSpacing':
        return self._wrapped.StirrupSpacing

    @property
    def StirrupDiameters(self) -> 'RColumnStirrupDiameters':
        return self._wrapped.StirrupDiameters

    @property
    def StirrupZones(self) -> 'RColumnStirrupZones':
        return self._wrapped.StirrupZones

    @property
    def StirrupLegNumY(self) -> c_long:
        return self._wrapped.StirrupLegNumY

    @property
    def StirrupLegNumZ(self) -> c_long:
        return self._wrapped.StirrupLegNumZ

    @property
    def ShearCrackAngle(self) -> c_long:
        return self._wrapped.ShearCrackAngle

    @property
    def CapacityDesignParams(self) -> 'RRCColumnCapacityDesignParams':
        return self._wrapped.CapacityDesignParams

    @property
    def CBDetailingRules(self) -> c_long:
        return self._wrapped.CBDetailingRules

    @property
    def SteelMaterialId(self) -> c_long:
        return self._wrapped.SteelMaterialId

    @property
    def ShearRhoFactor(self) -> c_double:
        return self._wrapped.ShearRhoFactor


class RMyMz(Wrapper):

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz


class RNMInteractionDiagMinMax(Wrapper):

    @property
    def NMin(self) -> c_double:
        return self._wrapped.NMin

    @property
    def NMax(self) -> c_double:
        return self._wrapped.NMax

    @property
    def MyMin(self) -> c_double:
        return self._wrapped.MyMin

    @property
    def MyMax(self) -> c_double:
        return self._wrapped.MyMax

    @property
    def MzMin(self) -> c_double:
        return self._wrapped.MzMin

    @property
    def MzMax(self) -> c_double:
        return self._wrapped.MzMax


class RColumnCheckResult(Wrapper):

    @property
    def xRelPos(self) -> c_double:
        return self._wrapped.xRelPos

    @property
    def Passed(self) -> c_long:
        return self._wrapped.Passed

    @property
    def Eff_Const_N(self) -> c_double:
        return self._wrapped.Eff_Const_N

    @property
    def Eff_Const_e(self) -> c_double:
        return self._wrapped.Eff_Const_e

    @property
    def My_c(self) -> c_double:
        return self._wrapped.My_c

    @property
    def My_e2y_P(self) -> c_double:
        return self._wrapped.My_e2y_P

    @property
    def My_e2y_N(self) -> c_double:
        return self._wrapped.My_e2y_N

    @property
    def My_e2z_P(self) -> c_double:
        return self._wrapped.My_e2z_P

    @property
    def My_e2z_N(self) -> c_double:
        return self._wrapped.My_e2z_N

    @property
    def Mz_c(self) -> c_double:
        return self._wrapped.Mz_c

    @property
    def Mz_e2y_P(self) -> c_double:
        return self._wrapped.Mz_e2y_P

    @property
    def Mz_e2y_N(self) -> c_double:
        return self._wrapped.Mz_e2y_N

    @property
    def Mz_e2z_P(self) -> c_double:
        return self._wrapped.Mz_e2z_P

    @property
    def Mz_e2z_N(self) -> c_double:
        return self._wrapped.Mz_e2z_N


class RColumnForces(Wrapper):

    @property
    def Nx(self) -> c_double:
        return self._wrapped.Nx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def Vy(self) -> c_double:
        return self._wrapped.Vy

    @property
    def Vz(self) -> c_double:
        return self._wrapped.Vz

    @property
    def Tx(self) -> c_double:
        return self._wrapped.Tx


class RColumnVTCheckResult(Wrapper):

    @property
    def xRelPos(self) -> c_double:
        return self._wrapped.xRelPos

    @property
    def Passed(self) -> c_long:
        return self._wrapped.Passed

    @property
    def VyR(self) -> c_double:
        return self._wrapped.VyR

    @property
    def VzR(self) -> c_double:
        return self._wrapped.VzR

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def Ast(self) -> c_double:
        return self._wrapped.Ast

    @property
    def Eff_Vy(self) -> c_double:
        return self._wrapped.Eff_Vy

    @property
    def Eff_Vz(self) -> c_double:
        return self._wrapped.Eff_Vz

    @property
    def Eff_Vy_Vz(self) -> c_double:
        return self._wrapped.Eff_Vy_Vz

    @property
    def Eff_Vy_Vz_Tx(self) -> c_double:
        return self._wrapped.Eff_Vy_Vz_Tx

    @property
    def Eff_Vy_Vz_Tx_max(self) -> c_double:
        return self._wrapped.Eff_Vy_Vz_Tx_max


class RRefVector(Wrapper):

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2


class RInfoWindowSwitch(Wrapper):

    @property
    def Coordinates(self) -> c_long:
        return self._wrapped.Coordinates

    @property
    def Info(self) -> c_long:
        return self._wrapped.Info

    @property
    def ColourCoding(self) -> c_long:
        return self._wrapped.ColourCoding

    @property
    def ColourLegend(self) -> c_long:
        return self._wrapped.ColourLegend


class RPartialRCBeamDesignParameters(Wrapper):

    @property
    def RCBeamCrossSections(self) -> 'RRCBeamCrossSections':
        return self._wrapped.RCBeamCrossSections

    @property
    def RCBeamSupports(self) -> 'RRCBeamSupports':
        return self._wrapped.RCBeamSupports


class RRCBeamSupports(Wrapper):

    @property
    def StartSupport(self) -> 'RRCBeamSupport':
        return self._wrapped.StartSupport

    @property
    def EndSupport(self) -> 'RRCBeamSupport':
        return self._wrapped.EndSupport


class RColumnStiffnessParams(Wrapper):

    @property
    def CalcParams(self) -> 'RElementStiffnessParams':
        return self._wrapped.CalcParams

    @property
    def CrossSectionID(self) -> c_long:
        return self._wrapped.CrossSectionID

    @property
    def EndReleaseYTop(self) -> c_long:
        return self._wrapped.EndReleaseYTop

    @property
    def EndReleaseYBottom(self) -> c_long:
        return self._wrapped.EndReleaseYBottom


class RImperfectionParams(Wrapper):

    @property
    def SwayDirection(self) -> c_long:
        return self._wrapped.SwayDirection

    @property
    def SwayAngle(self) -> c_double:
        return self._wrapped.SwayAngle

    @property
    def BaseHeightType(self) -> c_long:
        return self._wrapped.BaseHeightType

    @property
    def BaseHeight(self) -> c_double:
        return self._wrapped.BaseHeight

    @property
    def StructureAutoHeight(self) -> c_long:
        return self._wrapped.StructureAutoHeight

    @property
    def StructureHeight(self) -> c_double:
        return self._wrapped.StructureHeight

    @property
    def ColumnsInvolved(self) -> c_long:
        return self._wrapped.ColumnsInvolved

    @property
    def Alpha_h(self) -> c_double:
        return self._wrapped.Alpha_h

    @property
    def Alpha_m(self) -> c_double:
        return self._wrapped.Alpha_m

    @property
    def Phi0(self) -> c_double:
        return self._wrapped.Phi0


class RTextBoxParameters(Wrapper):

    @property
    def NodeId(self) -> c_long:
        return self._wrapped.NodeId

    @property
    def LayerID(self) -> c_long:
        return self._wrapped.LayerID

    @property
    def Position(self) -> 'RPoint3d':
        return self._wrapped.Position

    @property
    def LabelOrientation(self) -> c_long:
        return self._wrapped.LabelOrientation

    @property
    def TextBoxStyle(self) -> c_long:
        return self._wrapped.TextBoxStyle


class RCSOptimizationParamsGeneral(Wrapper):

    @property
    def ObjectiveOfOptimization(self) -> c_long:
        return self._wrapped.ObjectiveOfOptimization

    @property
    def Constraint_h_min(self) -> c_double:
        return self._wrapped.Constraint_h_min

    @property
    def Constraint_h_max(self) -> c_double:
        return self._wrapped.Constraint_h_max

    @property
    def Constraint_b_min(self) -> c_double:
        return self._wrapped.Constraint_b_min

    @property
    def Constraint_b_max(self) -> c_double:
        return self._wrapped.Constraint_b_max

    @property
    def MaximumEfficiency(self) -> c_double:
        return self._wrapped.MaximumEfficiency

    @property
    def Custom(self) -> c_long:
        return self._wrapped.Custom

    @property
    def NumberOfIterations(self) -> c_long:
        return self._wrapped.NumberOfIterations

    @property
    def Beams(self) -> c_long:
        return self._wrapped.Beams


class RNodalMass(Wrapper):

    @property
    def Node(self) -> c_long:
        return self._wrapped.Node

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz


class RRefAxis(Wrapper):

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2


class RLoadCombinationGenParameters(Wrapper):

    @property
    def ConsiderImperfections(self) -> c_long:
        return self._wrapped.ConsiderImperfections

    @property
    def OverwriteGeneratedCombos(self) -> c_long:
        return self._wrapped.OverwriteGeneratedCombos

    @property
    def OverWriteDuplComboSameType(self) -> c_long:
        return self._wrapped.OverWriteDuplComboSameType


class RRefData(Wrapper):

    @property
    def Point(self) -> 'RRefPoint':
        return self._wrapped.Point

    @property
    def Vector(self) -> 'RRefVector':
        return self._wrapped.Vector

    @property
    def Axis(self) -> 'RRefAxis':
        return self._wrapped.Axis

    @property
    def Plane(self) -> 'RRefPlane':
        return self._wrapped.Plane

    @property
    def Beta(self) -> 'RRefBeta':
        return self._wrapped.Beta


class RRefPlane(Wrapper):

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2

    @property
    def P3(self) -> 'RPoint3d':
        return self._wrapped.P3


class RRefBeta(Wrapper):

    @property
    def Beta(self) -> c_double:
        return self._wrapped.Beta


class RDisplaySwitch(Wrapper):

    @property
    def Parts(self) -> c_long:
        return self._wrapped.Parts

    @property
    def NonVisiblePartsGreyed(self) -> c_long:
        return self._wrapped.NonVisiblePartsGreyed

    @property
    def Guidlines(self) -> c_long:
        return self._wrapped.Guidlines

    @property
    def StructuralGrid(self) -> c_long:
        return self._wrapped.StructuralGrid


class RDomainTrapezoidal(Wrapper):

    @property
    def PlateMaterial(self) -> c_long:
        return self._wrapped.PlateMaterial

    @property
    def InfillMaterial(self) -> c_long:
        return self._wrapped.InfillMaterial

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def Origin(self) -> 'RPoint3d':
        return self._wrapped.Origin

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def t(self) -> c_double:
        return self._wrapped.t

    @property
    def V(self) -> c_double:
        return self._wrapped.V

    @property
    def d(self) -> c_double:
        return self._wrapped.d

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def w(self) -> c_double:
        return self._wrapped.w

    @property
    def P(self) -> c_double:
        return self._wrapped.P

    @property
    def Eta(self) -> c_double:
        return self._wrapped.Eta


class RSteelDesignResult(Wrapper):

    @property
    def PosX(self) -> c_double:
        return self._wrapped.PosX

    @property
    def DesignValue(self) -> c_double:
        return self._wrapped.DesignValue

    @property
    def LimitValue(self) -> c_double:
        return self._wrapped.LimitValue


class RSectionSegmentChainIntegratedParameters(Wrapper):

    @property
    def StartPoint(self) -> 'RPoint3d':
        return self._wrapped.StartPoint

    @property
    def EndPoint(self) -> 'RPoint3d':
        return self._wrapped.EndPoint

    @property
    def CentreRatio(self) -> c_double:
        return self._wrapped.CentreRatio


class RGlobalForces(Wrapper):

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz


class RMiscellaneousSettings(Wrapper):

    @property
    def Smoothing(self) -> c_long:
        return self._wrapped.Smoothing

    @property
    def MaxAngleLocZ(self) -> c_double:
        return self._wrapped.MaxAngleLocZ

    @property
    def MaxAngleLocX(self) -> c_double:
        return self._wrapped.MaxAngleLocX

    @property
    def IntensityRefVal(self) -> c_long:
        return self._wrapped.IntensityRefVal

    @property
    def CustomVal(self) -> c_double:
        return self._wrapped.CustomVal

    @property
    def SupportsAvgResultsPerMember(self) -> c_long:
        return self._wrapped.SupportsAvgResultsPerMember


class RCommonDisplayParameters(Wrapper):

    @property
    def CriticalResSettings(self) -> 'RCommonCriticalResultsSettings':
        return self._wrapped.CriticalResSettings

    @property
    def CutMomentPeaks(self) -> c_long:
        return self._wrapped.CutMomentPeaks

    @property
    def DrawInPlane(self) -> c_long:
        return self._wrapped.DrawInPlane

    @property
    def MiscelSettings(self) -> 'RMiscellaneousSettings':
        return self._wrapped.MiscelSettings


class RCommonCriticalResultsSettings(Wrapper):

    @property
    def InvestigateAllCombos(self) -> c_long:
        return self._wrapped.InvestigateAllCombos

    @property
    def CritComboFormula(self) -> c_long:
        return self._wrapped.CritComboFormula

    @property
    def InPersistentAndTransientDesignSituations(self) -> c_long:
        return self._wrapped.InPersistentAndTransientDesignSituations


class RCircleArcGeomData(Wrapper):

    @property
    def Center(self) -> 'RPoint3d':
        return self._wrapped.Center

    @property
    def NormalVector(self) -> 'RPoint3d':
        return self._wrapped.NormalVector

    @property
    def Alfa(self) -> c_double:
        return self._wrapped.Alfa


class RShowSwitches(Wrapper):

    @property
    def InfoWindowSwitch(self) -> 'RInfoWindowSwitch':
        return self._wrapped.InfoWindowSwitch

    @property
    def DisplaySwitch(self) -> 'RDisplaySwitch':
        return self._wrapped.DisplaySwitch


class RFrequencyParameters(Wrapper):

    @property
    def Frequency(self) -> c_double:
        return self._wrapped.Frequency

    @property
    def EigenValConv(self) -> c_double:
        return self._wrapped.EigenValConv

    @property
    def EigenVecConv(self) -> c_double:
        return self._wrapped.EigenVecConv

    @property
    def EigenValConvLimit(self) -> c_double:
        return self._wrapped.EigenValConvLimit

    @property
    def EigenVecConvLimit(self) -> c_double:
        return self._wrapped.EigenVecConvLimit

    @property
    def Iteration(self) -> c_long:
        return self._wrapped.Iteration


class RSteelDesignParameters(Wrapper):

    @property
    def MSZ_STAS(self) -> 'RSteelDesignParameters_MSZ_STAS':
        return self._wrapped.MSZ_STAS

    @property
    def EC_SIA_ITA(self) -> 'RSteelDesignParameters_EC_SIA_ITA':
        return self._wrapped.EC_SIA_ITA

    @property
    def NEN(self) -> 'RSteelDesignParameters_NEN':
        return self._wrapped.NEN


class RSteelDesignParameters_NEN(Wrapper):

    @property
    def BreakAtElements(self) -> c_long:
        return self._wrapped.BreakAtElements

    @property
    def Kapy(self) -> c_double:
        return self._wrapped.Kapy

    @property
    def Kapz(self) -> c_double:
        return self._wrapped.Kapz

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def l1F(self) -> c_double:
        return self._wrapped.l1F

    @property
    def l1A(self) -> c_double:
        return self._wrapped.l1A

    @property
    def lgF(self) -> c_double:
        return self._wrapped.lgF

    @property
    def lgA(self) -> c_double:
        return self._wrapped.lgA

    @property
    def ak(self) -> c_double:
        return self._wrapped.ak

    @property
    def Fytot(self) -> c_double:
        return self._wrapped.Fytot

    @property
    def Fztot(self) -> c_double:
        return self._wrapped.Fztot

    @property
    def YBraced(self) -> c_long:
        return self._wrapped.YBraced

    @property
    def ZBraced(self) -> c_long:
        return self._wrapped.ZBraced

    @property
    def Torsion(self) -> c_long:
        return self._wrapped.Torsion


class RCursorSnap(Wrapper):

    @property
    def MouseSnap(self) -> c_long:
        return self._wrapped.MouseSnap

    @property
    def DeltaX(self) -> c_double:
        return self._wrapped.DeltaX

    @property
    def DeltaY(self) -> c_double:
        return self._wrapped.DeltaY

    @property
    def DeltaZ(self) -> c_double:
        return self._wrapped.DeltaZ

    @property
    def CtrlX(self) -> c_double:
        return self._wrapped.CtrlX


class RTimberDesignParameters_EC_SIA_ITA(Wrapper):

    @property
    def Ky(self) -> c_double:
        return self._wrapped.Ky

    @property
    def Kz(self) -> c_double:
        return self._wrapped.Kz

    @property
    def Klt(self) -> c_double:
        return self._wrapped.Klt

    @property
    def LoadPosition(self) -> c_long:
        return self._wrapped.LoadPosition

    @property
    def Grain(self) -> c_long:
        return self._wrapped.Grain

    @property
    def LayerThickness(self) -> c_double:
        return self._wrapped.LayerThickness


class RCSOptimizationResultsParametric(Wrapper):

    @property
    def OptimizationEfficiency(self) -> c_double:
        return self._wrapped.OptimizationEfficiency

    @property
    def Efficiency(self) -> c_double:
        return self._wrapped.Efficiency

    @property
    def M(self) -> c_double:
        return self._wrapped.M

    @property
    def DeltaM(self) -> c_double:
        return self._wrapped.DeltaM

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf

    @property
    def b2(self) -> c_double:
        return self._wrapped.b2

    @property
    def tf2(self) -> c_double:
        return self._wrapped.tf2

    @property
    def a(self) -> c_double:
        return self._wrapped.a


class REllipseArcGeomData(Wrapper):

    @property
    def Center(self) -> 'RPoint3d':
        return self._wrapped.Center

    @property
    def NormalVector(self) -> 'RPoint3d':
        return self._wrapped.NormalVector

    @property
    def Alfa(self) -> c_double:
        return self._wrapped.Alfa

    @property
    def MajorEndPoint(self) -> 'RPoint3d':
        return self._wrapped.MajorEndPoint

    @property
    def Ratio(self) -> c_double:
        return self._wrapped.Ratio

    @property
    def StartAlfa(self) -> c_double:
        return self._wrapped.StartAlfa

    @property
    def EndAlfa(self) -> c_double:
        return self._wrapped.EndAlfa


class RNcrParameters(Wrapper):

    @property
    def Ncr(self) -> c_double:
        return self._wrapped.Ncr

    @property
    def EigenValConv(self) -> c_double:
        return self._wrapped.EigenValConv

    @property
    def EigenVecConv(self) -> c_double:
        return self._wrapped.EigenVecConv

    @property
    def EigenValConvLimit(self) -> c_double:
        return self._wrapped.EigenValConvLimit

    @property
    def EigenVecConvLimit(self) -> c_double:
        return self._wrapped.EigenVecConvLimit

    @property
    def Iteration(self) -> c_long:
        return self._wrapped.Iteration


class RReinforcementCheckValues(Wrapper):

    @property
    def rmxdmin_ULS(self) -> c_double:
        return self._wrapped.rmxdmin_ULS

    @property
    def rmxdmax_ULS(self) -> c_double:
        return self._wrapped.rmxdmax_ULS

    @property
    def rmydmin_ULS(self) -> c_double:
        return self._wrapped.rmydmin_ULS

    @property
    def rmydmax_ULS(self) -> c_double:
        return self._wrapped.rmydmax_ULS

    @property
    def rmxumin_ULS(self) -> c_double:
        return self._wrapped.rmxumin_ULS

    @property
    def rmxumax_ULS(self) -> c_double:
        return self._wrapped.rmxumax_ULS

    @property
    def rmyumin_ULS(self) -> c_double:
        return self._wrapped.rmyumin_ULS

    @property
    def rmyumax_ULS(self) -> c_double:
        return self._wrapped.rmyumax_ULS

    @property
    def rmxdmin_SLS(self) -> c_double:
        return self._wrapped.rmxdmin_SLS

    @property
    def rmxdmax_SLS(self) -> c_double:
        return self._wrapped.rmxdmax_SLS

    @property
    def rmydmin_SLS(self) -> c_double:
        return self._wrapped.rmydmin_SLS

    @property
    def rmydmax_SLS(self) -> c_double:
        return self._wrapped.rmydmax_SLS

    @property
    def rmxumin_SLS(self) -> c_double:
        return self._wrapped.rmxumin_SLS

    @property
    def rmxumax_SLS(self) -> c_double:
        return self._wrapped.rmxumax_SLS

    @property
    def rmyumin_SLS(self) -> c_double:
        return self._wrapped.rmyumin_SLS

    @property
    def rmyumax_SLS(self) -> c_double:
        return self._wrapped.rmyumax_SLS

    @property
    def Status(self) -> c_long:
        return self._wrapped.Status


class RCSParametricOptimizationParams(Wrapper):

    @property
    def General(self) -> 'RCSOptimizationParamsGeneral':
        return self._wrapped.General

    @property
    def fixed_h(self) -> c_long:
        return self._wrapped.fixed_h

    @property
    def delta_h(self) -> c_double:
        return self._wrapped.delta_h

    @property
    def fixed_b(self) -> c_long:
        return self._wrapped.fixed_b

    @property
    def delta_b(self) -> c_double:
        return self._wrapped.delta_b

    @property
    def fixed_tw(self) -> c_long:
        return self._wrapped.fixed_tw

    @property
    def delta_tw(self) -> c_double:
        return self._wrapped.delta_tw

    @property
    def fixed_tf(self) -> c_long:
        return self._wrapped.fixed_tf

    @property
    def delta_tf(self) -> c_double:
        return self._wrapped.delta_tf

    @property
    def fixed_b2(self) -> c_long:
        return self._wrapped.fixed_b2

    @property
    def b2_min(self) -> c_double:
        return self._wrapped.b2_min

    @property
    def b2_max(self) -> c_double:
        return self._wrapped.b2_max

    @property
    def delta_b2(self) -> c_double:
        return self._wrapped.delta_b2

    @property
    def fixed_tf2(self) -> c_long:
        return self._wrapped.fixed_tf2

    @property
    def tf2_min(self) -> c_double:
        return self._wrapped.tf2_min

    @property
    def tf2_max(self) -> c_double:
        return self._wrapped.tf2_max

    @property
    def delta_tf2(self) -> c_double:
        return self._wrapped.delta_tf2

    @property
    def fixed_a(self) -> c_long:
        return self._wrapped.fixed_a

    @property
    def a_min(self) -> c_double:
        return self._wrapped.a_min

    @property
    def a_max(self) -> c_double:
        return self._wrapped.a_max

    @property
    def delta_a(self) -> c_double:
        return self._wrapped.delta_a


class RSteelLTBSupport(Wrapper):

    @property
    def AbsPos(self) -> c_double:
        return self._wrapped.AbsPos

    @property
    def Ecc(self) -> c_double:
        return self._wrapped.Ecc

    @property
    def Ry(self) -> c_double:
        return self._wrapped.Ry

    @property
    def Rxx(self) -> c_double:
        return self._wrapped.Rxx

    @property
    def Rzz(self) -> c_double:
        return self._wrapped.Rzz

    @property
    def Rw(self) -> c_double:
        return self._wrapped.Rw


class RLoadEmptySurfaceLine(Wrapper):

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def SegmentId(self) -> c_long:
        return self._wrapped.SegmentId

    @property
    def GlbStartx(self) -> c_double:
        return self._wrapped.GlbStartx

    @property
    def GlbStarty(self) -> c_double:
        return self._wrapped.GlbStarty

    @property
    def GlbStartz(self) -> c_double:
        return self._wrapped.GlbStartz

    @property
    def GlbEndx(self) -> c_double:
        return self._wrapped.GlbEndx

    @property
    def GlbEndy(self) -> c_double:
        return self._wrapped.GlbEndy

    @property
    def GlbEndz(self) -> c_double:
        return self._wrapped.GlbEndz


class RTimberDesignParameters_EC_V153(Wrapper):

    @property
    def Ky(self) -> c_double:
        return self._wrapped.Ky

    @property
    def Kz(self) -> c_double:
        return self._wrapped.Kz

    @property
    def Klt(self) -> c_double:
        return self._wrapped.Klt

    @property
    def LoadPosition(self) -> c_long:
        return self._wrapped.LoadPosition

    @property
    def Grain(self) -> c_long:
        return self._wrapped.Grain

    @property
    def LayerThickness(self) -> c_double:
        return self._wrapped.LayerThickness

    @property
    def slsEyLimitDef(self) -> c_long:
        return self._wrapped.slsEyLimitDef

    @property
    def slsEzLimitDef(self) -> c_long:
        return self._wrapped.slsEzLimitDef

    @property
    def slsUyDef(self) -> c_long:
        return self._wrapped.slsUyDef

    @property
    def slsUzDef(self) -> c_long:
        return self._wrapped.slsUzDef

    @property
    def slsEMode(self) -> c_long:
        return self._wrapped.slsEMode

    @property
    def slsLMode(self) -> c_long:
        return self._wrapped.slsLMode

    @property
    def slsPreCamberCurve(self) -> c_long:
        return self._wrapped.slsPreCamberCurve

    @property
    def slsEyLimit(self) -> c_double:
        return self._wrapped.slsEyLimit

    @property
    def slsEzLimit(self) -> c_double:
        return self._wrapped.slsEzLimit

    @property
    def slsCustomLy(self) -> c_double:
        return self._wrapped.slsCustomLy

    @property
    def slsCustomLz(self) -> c_double:
        return self._wrapped.slsCustomLz

    @property
    def slsUy(self) -> c_double:
        return self._wrapped.slsUy

    @property
    def slsUz(self) -> c_double:
        return self._wrapped.slsUz

    @property
    def slsCreepMode(self) -> c_long:
        return self._wrapped.slsCreepMode

    @property
    def slsPhi(self) -> c_double:
        return self._wrapped.slsPhi

    @property
    def FireResistDef(self) -> c_long:
        return self._wrapped.FireResistDef

    @property
    def fpKy(self) -> c_double:
        return self._wrapped.fpKy

    @property
    def fpKz(self) -> c_double:
        return self._wrapped.fpKz

    @property
    def fpKLT(self) -> c_double:
        return self._wrapped.fpKLT


class RCrackWidths(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def cwvCenterPoint_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvCenterPoint_Bottom

    @property
    def cwvCenterPoint_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvCenterPoint_Top

    @property
    def cwvContourPoint1_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint1_Bottom

    @property
    def cwvContourPoint1_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint1_Top

    @property
    def cwvContourPoint2_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint2_Bottom

    @property
    def cwvContourPoint2_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint2_Top

    @property
    def cwvContourPoint3_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint3_Bottom

    @property
    def cwvContourPoint3_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint3_Top

    @property
    def cwvContourPoint4_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint4_Bottom

    @property
    def cwvContourPoint4_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourPoint4_Top

    @property
    def cwvContourLineMidPoint1_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint1_Bottom

    @property
    def cwvContourLineMidPoint1_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint1_Top

    @property
    def cwvContourLineMidPoint2_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint2_Bottom

    @property
    def cwvContourLineMidPoint2_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint2_Top

    @property
    def cwvContourLineMidPoint3_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint3_Bottom

    @property
    def cwvContourLineMidPoint3_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint3_Top

    @property
    def cwvContourLineMidPoint4_Bottom(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint4_Bottom

    @property
    def cwvContourLineMidPoint4_Top(self) -> 'RCrackWidthValues':
        return self._wrapped.cwvContourLineMidPoint4_Top


class RCrackWidthValues(Wrapper):

    @property
    def Asbx(self) -> c_double:
        return self._wrapped.Asbx

    @property
    def Asby(self) -> c_double:
        return self._wrapped.Asby

    @property
    def Astx(self) -> c_double:
        return self._wrapped.Astx

    @property
    def Asty(self) -> c_double:
        return self._wrapped.Asty

    @property
    def Nx(self) -> c_double:
        return self._wrapped.Nx

    @property
    def Ny(self) -> c_double:
        return self._wrapped.Ny

    @property
    def Nxy(self) -> c_double:
        return self._wrapped.Nxy

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mxy(self) -> c_double:
        return self._wrapped.Mxy

    @property
    def wR_p(self) -> c_double:
        return self._wrapped.wR_p

    @property
    def wR_s(self) -> c_double:
        return self._wrapped.wR_s

    @property
    def wk_p(self) -> c_double:
        return self._wrapped.wk_p

    @property
    def wk_s(self) -> c_double:
        return self._wrapped.wk_s

    @property
    def wk2_p(self) -> c_double:
        return self._wrapped.wk2_p

    @property
    def wk2_s(self) -> c_double:
        return self._wrapped.wk2_s

    @property
    def xs2_p(self) -> c_double:
        return self._wrapped.xs2_p

    @property
    def xs2_s(self) -> c_double:
        return self._wrapped.xs2_s

    @property
    def Ss2_p(self) -> c_double:
        return self._wrapped.Ss2_p

    @property
    def Ss2_s(self) -> c_double:
        return self._wrapped.Ss2_s

    @property
    def Sb1_p(self) -> c_double:
        return self._wrapped.Sb1_p

    @property
    def Sb1_s(self) -> c_double:
        return self._wrapped.Sb1_s


class RCommonCriticalResultsSettings_V161(Wrapper):

    @property
    def InvestigateAllCombos(self) -> c_long:
        return self._wrapped.InvestigateAllCombos

    @property
    def CritComboFormula(self) -> c_long:
        return self._wrapped.CritComboFormula

    @property
    def InPersistentAndTransientDesignSituations(self) -> c_long:
        return self._wrapped.InPersistentAndTransientDesignSituations

    @property
    def SemiAutoSLS(self) -> c_long:
        return self._wrapped.SemiAutoSLS


class RGridOptions(Wrapper):

    @property
    def DisplayGrid(self) -> c_long:
        return self._wrapped.DisplayGrid

    @property
    def DeltaX(self) -> c_double:
        return self._wrapped.DeltaX

    @property
    def DeltaY(self) -> c_double:
        return self._wrapped.DeltaY

    @property
    def DeltaZ(self) -> c_double:
        return self._wrapped.DeltaZ

    @property
    def GridType(self) -> c_long:
        return self._wrapped.GridType


class RLoadSurfaceLine(Wrapper):

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def SegmentId(self) -> c_long:
        return self._wrapped.SegmentId

    @property
    def GlbStartx(self) -> c_double:
        return self._wrapped.GlbStartx

    @property
    def GlbStarty(self) -> c_double:
        return self._wrapped.GlbStarty

    @property
    def GlbStartz(self) -> c_double:
        return self._wrapped.GlbStartz

    @property
    def GlbEndx(self) -> c_double:
        return self._wrapped.GlbEndx

    @property
    def GlbEndy(self) -> c_double:
        return self._wrapped.GlbEndy

    @property
    def GlbEndz(self) -> c_double:
        return self._wrapped.GlbEndz


class REditingOptions(Wrapper):

    @property
    def ConstAngle_DeltaAlpha(self) -> c_double:
        return self._wrapped.ConstAngle_DeltaAlpha

    @property
    def ConstAngle_CustomAlpha(self) -> c_double:
        return self._wrapped.ConstAngle_CustomAlpha

    @property
    def EditingToler(self) -> c_double:
        return self._wrapped.EditingToler


class RTotalLoads(Wrapper):

    @property
    def ExternalForces(self) -> 'RGlobalForces':
        return self._wrapped.ExternalForces

    @property
    def UnbalancedLoads(self) -> 'RGlobalForces':
        return self._wrapped.UnbalancedLoads


class RLoadDomainPolyArea(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def LoadDistributionType(self) -> c_long:
        return self._wrapped.LoadDistributionType

    @property
    def Component(self) -> c_long:
        return self._wrapped.Component

    @property
    def P1(self) -> c_double:
        return self._wrapped.P1

    @property
    def P2(self) -> c_double:
        return self._wrapped.P2

    @property
    def P3(self) -> c_double:
        return self._wrapped.P3

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def x3(self) -> c_double:
        return self._wrapped.x3

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def y3(self) -> c_double:
        return self._wrapped.y3

    @property
    def z1(self) -> c_double:
        return self._wrapped.z1

    @property
    def z2(self) -> c_double:
        return self._wrapped.z2

    @property
    def z3(self) -> c_double:
        return self._wrapped.z3

    @property
    def WindowLoad(self) -> c_long:
        return self._wrapped.WindowLoad


class RSegmentChainPointCrackWidthValues(Wrapper):

    @property
    def covBottom(self) -> 'RSegmentChainCrackWidthValues':
        return self._wrapped.covBottom

    @property
    def covTop(self) -> 'RSegmentChainCrackWidthValues':
        return self._wrapped.covTop


class RSegmentChainCrackWidthValues(Wrapper):

    @property
    def wk_p(self) -> c_double:
        return self._wrapped.wk_p

    @property
    def wk_s(self) -> c_double:
        return self._wrapped.wk_s

    @property
    def wk2_p(self) -> c_double:
        return self._wrapped.wk2_p

    @property
    def wk2_s(self) -> c_double:
        return self._wrapped.wk2_s


class RActualReinforcement(Wrapper):

    @property
    def ds(self) -> c_double:
        return self._wrapped.ds

    @property
    def spacing(self) -> c_double:
        return self._wrapped.spacing

    @property
    def RebarType(self) -> c_long:
        return self._wrapped.RebarType

    @property
    def Cover(self) -> c_double:
        return self._wrapped.Cover

    @property
    def Alpha(self) -> c_double:
        return self._wrapped.Alpha


class RSteelDesignParameters_V153(Wrapper):

    @property
    def EC_SIA_ITA(self) -> 'RSteelDesignParameters_EC_SIA_ITA_V153':
        return self._wrapped.EC_SIA_ITA

    @property
    def MSZ_STAS(self) -> 'RSteelDesignParameters_MSZ_STAS':
        return self._wrapped.MSZ_STAS

    @property
    def NEN(self) -> 'RSteelDesignParameters_NEN':
        return self._wrapped.NEN


class RCircularFootingCalced(Wrapper):

    @property
    def Calculated(self) -> c_long:
        return self._wrapped.Calculated

    @property
    def Diam(self) -> c_double:
        return self._wrapped.Diam

    @property
    def StepMeasureSource(self) -> c_long:
        return self._wrapped.StepMeasureSource

    @property
    def DeltaR(self) -> c_double:
        return self._wrapped.DeltaR


class RLineGeomData(Wrapper):

    @property
    def CircleArc(self) -> 'RCircleArcGeomData':
        return self._wrapped.CircleArc

    @property
    def EllipseArc(self) -> 'REllipseArcGeomData':
        return self._wrapped.EllipseArc


class RLineData(Wrapper):

    @property
    def NodeId1(self) -> c_long:
        return self._wrapped.NodeId1

    @property
    def NodeId2(self) -> c_long:
        return self._wrapped.NodeId2

    @property
    def GeomType(self) -> c_long:
        return self._wrapped.GeomType

    @property
    def CircleArc(self) -> 'RCircleArcGeomData':
        return self._wrapped.CircleArc

    @property
    def EllipseArc(self) -> 'REllipseArcGeomData':
        return self._wrapped.EllipseArc


class RRCBeamDesignParameters_ITA(Wrapper):

    @property
    def VariableAngleTrussMethod(self) -> c_long:
        return self._wrapped.VariableAngleTrussMethod

    @property
    def Theta(self) -> c_double:
        return self._wrapped.Theta

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def CrackWidthCheck(self) -> c_long:
        return self._wrapped.CrackWidthCheck

    @property
    def MaxCrackWidth_Top(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Top

    @property
    def MaxCrackWidth_Bottom(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Bottom

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def ShortTerm(self) -> c_long:
        return self._wrapped.ShortTerm

    @property
    def Deflection_Beam_L_div(self) -> c_double:
        return self._wrapped.Deflection_Beam_L_div

    @property
    def Deflection_Cantilever_L_div(self) -> c_double:
        return self._wrapped.Deflection_Cantilever_L_div

    @property
    def SeismicZone(self) -> c_long:
        return self._wrapped.SeismicZone

    @property
    def PlasticHinges(self) -> 'RRCBeamPlasticHinges':
        return self._wrapped.PlasticHinges


class RRCBeamPlasticHinges(Wrapper):

    @property
    def EnablePlasticHinges(self) -> c_long:
        return self._wrapped.EnablePlasticHinges

    @property
    def Hinge1(self) -> 'RRCBeamPlasticHingeParams':
        return self._wrapped.Hinge1

    @property
    def Hinge2(self) -> 'RRCBeamPlasticHingeParams':
        return self._wrapped.Hinge2

    @property
    def Pos_Hinge1(self) -> c_double:
        return self._wrapped.Pos_Hinge1

    @property
    def Pos_Hinge2(self) -> c_double:
        return self._wrapped.Pos_Hinge2

    @property
    def MinRebarDiameter(self) -> c_double:
        return self._wrapped.MinRebarDiameter

    @property
    def GammaRd(self) -> c_double:
        return self._wrapped.GammaRd


class RRCBeamPlasticHingeParams(Wrapper):

    @property
    def Active(self) -> c_long:
        return self._wrapped.Active

    @property
    def AppliedReinforcement(self) -> c_long:
        return self._wrapped.AppliedReinforcement

    @property
    def As_Bottom(self) -> c_double:
        return self._wrapped.As_Bottom

    @property
    def As_Top(self) -> c_double:
        return self._wrapped.As_Top

    @property
    def Depth_Bottom(self) -> c_double:
        return self._wrapped.Depth_Bottom

    @property
    def Depth_Top(self) -> c_double:
        return self._wrapped.Depth_Top


class RSpectrumData_ITA(Wrapper):

    @property
    def SubsoilClass(self) -> c_long:
        return self._wrapped.SubsoilClass

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def F0(self) -> c_double:
        return self._wrapped.F0

    @property
    def Tsc(self) -> c_double:
        return self._wrapped.Tsc

    @property
    def TopographicCategory(self) -> c_long:
        return self._wrapped.TopographicCategory

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy


class RRCBeamDesignParameters_EC(Wrapper):

    @property
    def VariableAngleTrussMethod(self) -> c_long:
        return self._wrapped.VariableAngleTrussMethod

    @property
    def Theta(self) -> c_double:
        return self._wrapped.Theta

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def CrackWidthCheck(self) -> c_long:
        return self._wrapped.CrackWidthCheck

    @property
    def MaxCrackWidth_Top(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Top

    @property
    def MaxCrackWidth_Bottom(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Bottom

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def ShortTerm(self) -> c_long:
        return self._wrapped.ShortTerm

    @property
    def Deflection_Beam_L_div(self) -> c_double:
        return self._wrapped.Deflection_Beam_L_div

    @property
    def Deflection_Cantilever_L_div(self) -> c_double:
        return self._wrapped.Deflection_Cantilever_L_div

    @property
    def TopSurface(self) -> c_long:
        return self._wrapped.TopSurface

    @property
    def BottomSurface(self) -> c_long:
        return self._wrapped.BottomSurface

    @property
    def StructClass(self) -> c_long:
        return self._wrapped.StructClass

    @property
    def SeismicZone(self) -> c_long:
        return self._wrapped.SeismicZone

    @property
    def PlasticHinges(self) -> 'RRCBeamPlasticHinges':
        return self._wrapped.PlasticHinges


class RRCBeamDesignParameters_SIA(Wrapper):

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def TopSurface(self) -> c_long:
        return self._wrapped.TopSurface

    @property
    def BottomSurface(self) -> c_long:
        return self._wrapped.BottomSurface

    @property
    def Deflection_Beam_L_div(self) -> c_double:
        return self._wrapped.Deflection_Beam_L_div

    @property
    def Deflection_Cantilever_L_div(self) -> c_double:
        return self._wrapped.Deflection_Cantilever_L_div

    @property
    def VariableAngleTrussMethod(self) -> c_long:
        return self._wrapped.VariableAngleTrussMethod

    @property
    def Theta(self) -> c_double:
        return self._wrapped.Theta

    @property
    def CrackWidthCheck(self) -> c_long:
        return self._wrapped.CrackWidthCheck

    @property
    def MaxCrackWidth_Top(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Top

    @property
    def MaxCrackWidth_Bottom(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Bottom

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def SeismicZone(self) -> c_long:
        return self._wrapped.SeismicZone

    @property
    def PlasticHinges(self) -> 'RRCBeamPlasticHinges':
        return self._wrapped.PlasticHinges


class RSeismicSensitivityResults(Wrapper):

    @property
    def ResultsValidX(self) -> c_long:
        return self._wrapped.ResultsValidX

    @property
    def ResultsValidY(self) -> c_long:
        return self._wrapped.ResultsValidY

    @property
    def ThetaMax_x(self) -> c_double:
        return self._wrapped.ThetaMax_x

    @property
    def ThetaMax_y(self) -> c_double:
        return self._wrapped.ThetaMax_y

    @property
    def Ptot(self) -> c_double:
        return self._wrapped.Ptot

    @property
    def Vtot_x(self) -> c_double:
        return self._wrapped.Vtot_x

    @property
    def Vtot_y(self) -> c_double:
        return self._wrapped.Vtot_y

    @property
    def d_max_x(self) -> c_double:
        return self._wrapped.d_max_x

    @property
    def d_max_y(self) -> c_double:
        return self._wrapped.d_max_y

    @property
    def S_x(self) -> c_double:
        return self._wrapped.S_x

    @property
    def S_y(self) -> c_double:
        return self._wrapped.S_y

    @property
    def Gm_x(self) -> c_double:
        return self._wrapped.Gm_x

    @property
    def Gm_y(self) -> c_double:
        return self._wrapped.Gm_y

    @property
    def M_x(self) -> c_double:
        return self._wrapped.M_x

    @property
    def M_y(self) -> c_double:
        return self._wrapped.M_y

    @property
    def M_z(self) -> c_double:
        return self._wrapped.M_z

    @property
    def Imz(self) -> c_double:
        return self._wrapped.Imz

    @property
    def Error(self) -> c_long:
        return self._wrapped.Error


class RSpectrumData_STAS(Wrapper):

    @property
    def SubsoilClass(self) -> c_long:
        return self._wrapped.SubsoilClass

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def beta0(self) -> c_double:
        return self._wrapped.beta0

    @property
    def TB(self) -> c_double:
        return self._wrapped.TB

    @property
    def TC(self) -> c_double:
        return self._wrapped.TC

    @property
    def TD(self) -> c_double:
        return self._wrapped.TD

    @property
    def gammaI(self) -> c_double:
        return self._wrapped.gammaI

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy


class RStructuralGridParams(Wrapper):

    @property
    def Plane(self) -> c_long:
        return self._wrapped.Plane

    @property
    def WorkPlaneOrStoreyIndex(self) -> c_long:
        return self._wrapped.WorkPlaneOrStoreyIndex

    @property
    def PlaneOffset(self) -> c_double:
        return self._wrapped.PlaneOffset

    @property
    def Visibility(self) -> c_long:
        return self._wrapped.Visibility


class RSpectrumData_SIA(Wrapper):

    @property
    def SubsoilClass(self) -> c_long:
        return self._wrapped.SubsoilClass

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def S(self) -> c_double:
        return self._wrapped.S

    @property
    def TB(self) -> c_double:
        return self._wrapped.TB

    @property
    def TC(self) -> c_double:
        return self._wrapped.TC

    @property
    def TD(self) -> c_double:
        return self._wrapped.TD

    @property
    def gammaI(self) -> c_double:
        return self._wrapped.gammaI

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy


class RSpectrumData_DIN(Wrapper):

    @property
    def SubsoilClass(self) -> c_long:
        return self._wrapped.SubsoilClass

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def S(self) -> c_double:
        return self._wrapped.S

    @property
    def beta0(self) -> c_double:
        return self._wrapped.beta0

    @property
    def TB(self) -> c_double:
        return self._wrapped.TB

    @property
    def TC(self) -> c_double:
        return self._wrapped.TC

    @property
    def TD(self) -> c_double:
        return self._wrapped.TD

    @property
    def gammaI(self) -> c_double:
        return self._wrapped.gammaI

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy


class RXLAMSurfaceEfficiencies(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def xsevCenterPoint(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevCenterPoint

    @property
    def xsevContourPoint1(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourPoint1

    @property
    def xsevContourPoint2(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourPoint2

    @property
    def xsevContourPoint3(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourPoint3

    @property
    def xsevContourPoint4(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourPoint4

    @property
    def xsevContourLineMidPoint1(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourLineMidPoint1

    @property
    def xsevContourLineMidPoint2(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourLineMidPoint2

    @property
    def xsevContourLineMidPoint3(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourLineMidPoint3

    @property
    def xsevContourLineMidPoint4(self) -> 'RXLAMSurfaceEfficiencyValues':
        return self._wrapped.xsevContourLineMidPoint4


class RXLAMSurfaceEfficiencyValues(Wrapper):

    @property
    def xsev_M_N_0(self) -> c_double:
        return self._wrapped.xsev_M_N_0

    @property
    def xsev_M_N_90(self) -> c_double:
        return self._wrapped.xsev_M_N_90

    @property
    def xsev_V_T(self) -> c_double:
        return self._wrapped.xsev_V_T

    @property
    def xsev_Vr_N(self) -> c_double:
        return self._wrapped.xsev_Vr_N

    @property
    def xsev_Max(self) -> c_double:
        return self._wrapped.xsev_Max


class RStructuralGridGenerationParams(Wrapper):

    @property
    def Offset(self) -> 'RPoint2d':
        return self._wrapped.Offset

    @property
    def RotDeg(self) -> c_double:
        return self._wrapped.RotDeg

    @property
    def Colour(self) -> c_long:
        return self._wrapped.Colour

    @property
    def Extension(self) -> c_double:
        return self._wrapped.Extension

    @property
    def LabelTypeX(self) -> c_long:
        return self._wrapped.LabelTypeX

    @property
    def GenerateInPositiveX(self) -> c_long:
        return self._wrapped.GenerateInPositiveX

    @property
    def LabelTypeY(self) -> c_long:
        return self._wrapped.LabelTypeY

    @property
    def GenerateInPositiveY(self) -> c_long:
        return self._wrapped.GenerateInPositiveY

    @property
    def ShowStructuralGridLineTitle(self) -> c_long:
        return self._wrapped.ShowStructuralGridLineTitle


class RVerticalDisplacementValues(Wrapper):

    @property
    def w1(self) -> c_double:
        return self._wrapped.w1

    @property
    def w2(self) -> c_double:
        return self._wrapped.w2

    @property
    def w3(self) -> c_double:
        return self._wrapped.w3

    @property
    def wtot(self) -> c_double:
        return self._wrapped.wtot

    @property
    def wbij(self) -> c_double:
        return self._wrapped.wbij


class RTimberDesignResult(Wrapper):

    @property
    def PosX(self) -> c_double:
        return self._wrapped.PosX

    @property
    def DesignValue(self) -> c_double:
        return self._wrapped.DesignValue

    @property
    def LimitValue(self) -> c_double:
        return self._wrapped.LimitValue


class RPartItem(Wrapper):

    @property
    def ItemType(self) -> c_long:
        return self._wrapped.ItemType

    @property
    def Id(self) -> c_long:
        return self._wrapped.Id


class REnabledLogicalParts(Wrapper):

    @property
    def By_Material(self) -> c_long:
        return self._wrapped.By_Material

    @property
    def By_CrossSection(self) -> c_long:
        return self._wrapped.By_CrossSection

    @property
    def By_CrossSection_LineType(self) -> c_long:
        return self._wrapped.By_CrossSection_LineType

    @property
    def By_CrossSection_ArchitecturalLineElementType(self) -> c_long:
        return self._wrapped.By_CrossSection_ArchitecturalLineElementType

    @property
    def By_DomainType_Thickness(self) -> c_long:
        return self._wrapped.By_DomainType_Thickness

    @property
    def By_ArchitecturalDomainElementType_Thickness(self) -> c_long:
        return self._wrapped.By_ArchitecturalDomainElementType_Thickness

    @property
    def By_Stories(self) -> c_long:
        return self._wrapped.By_Stories

    @property
    def By_StructuralGridLines(self) -> c_long:
        return self._wrapped.By_StructuralGridLines


class RReinforcementCheck(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def rcvCenterPoint(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvCenterPoint

    @property
    def rcvContourPoint1(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourPoint1

    @property
    def rcvContourPoint2(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourPoint2

    @property
    def rcvContourPoint3(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourPoint3

    @property
    def rcvContourPoint4(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourPoint4

    @property
    def rcvContourLineMidPoint1(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourLineMidPoint1

    @property
    def rcvContourLineMidPoint2(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourLineMidPoint2

    @property
    def rcvContourLineMidPoint3(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourLineMidPoint3

    @property
    def rcvContourLineMidPoint4(self) -> 'RReinforcementCheckValues':
        return self._wrapped.rcvContourLineMidPoint4


class RWindowPosition(Wrapper):

    @property
    def Top(self) -> c_long:
        return self._wrapped.Top

    @property
    def Left(self) -> c_long:
        return self._wrapped.Left

    @property
    def Width(self) -> c_long:
        return self._wrapped.Width

    @property
    def Height(self) -> c_long:
        return self._wrapped.Height


class RCrossSectionUserParams(Wrapper):

    @property
    def lParam(self) -> c_long:
        return self._wrapped.lParam

    @property
    def dParam1(self) -> c_double:
        return self._wrapped.dParam1

    @property
    def dParam2(self) -> c_double:
        return self._wrapped.dParam2

    @property
    def dParam3(self) -> c_double:
        return self._wrapped.dParam3

    @property
    def dParam4(self) -> c_double:
        return self._wrapped.dParam4

    @property
    def dParam5(self) -> c_double:
        return self._wrapped.dParam5

    @property
    def dParam6(self) -> c_double:
        return self._wrapped.dParam6

    @property
    def dParam7(self) -> c_double:
        return self._wrapped.dParam7

    @property
    def dParam8(self) -> c_double:
        return self._wrapped.dParam8

    @property
    def dParam9(self) -> c_double:
        return self._wrapped.dParam9

    @property
    def dParam10(self) -> c_double:
        return self._wrapped.dParam10


class RDoubleWedgedI(Wrapper):

    @property
    def Process(self) -> c_long:
        return self._wrapped.Process

    @property
    def h1(self) -> c_double:
        return self._wrapped.h1

    @property
    def b1(self) -> c_double:
        return self._wrapped.b1

    @property
    def tw1(self) -> c_double:
        return self._wrapped.tw1

    @property
    def tf1(self) -> c_double:
        return self._wrapped.tf1

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def h2(self) -> c_double:
        return self._wrapped.h2

    @property
    def b2(self) -> c_double:
        return self._wrapped.b2

    @property
    def tw2(self) -> c_double:
        return self._wrapped.tw2

    @property
    def tf2(self) -> c_double:
        return self._wrapped.tf2

    @property
    def h3(self) -> c_double:
        return self._wrapped.h3

    @property
    def b3(self) -> c_double:
        return self._wrapped.b3

    @property
    def tw3(self) -> c_double:
        return self._wrapped.tw3

    @property
    def tf3(self) -> c_double:
        return self._wrapped.tf3


class RCrossSectionHSQ(Wrapper):

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def b1(self) -> c_double:
        return self._wrapped.b1

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf1(self) -> c_double:
        return self._wrapped.tf1

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf


class RCrossSectionHSQA(Wrapper):

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def b1(self) -> c_double:
        return self._wrapped.b1

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf1(self) -> c_double:
        return self._wrapped.tf1

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf

    @property
    def C(self) -> c_double:
        return self._wrapped.C


class RCrossSection2IX(Wrapper):

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def Process(self) -> c_long:
        return self._wrapped.Process


class RCrossSectionComposite(Wrapper):

    @property
    def CrossSectionIndex(self) -> c_long:
        return self._wrapped.CrossSectionIndex

    @property
    def OuterMaterialIndex(self) -> c_long:
        return self._wrapped.OuterMaterialIndex

    @property
    def CrossSectionMaterialIndex(self) -> c_long:
        return self._wrapped.CrossSectionMaterialIndex

    @property
    def CrossSectionFillMaterialIndex(self) -> c_long:
        return self._wrapped.CrossSectionFillMaterialIndex

    @property
    def CrossSectionAlign(self) -> c_long:
        return self._wrapped.CrossSectionAlign


class RCrossSectionIFB(Wrapper):

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def b2(self) -> c_double:
        return self._wrapped.b2

    @property
    def v2(self) -> c_double:
        return self._wrapped.v2

    @property
    def Process(self) -> c_long:
        return self._wrapped.Process


class RDoubleLClosed(Wrapper):

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def tw(self) -> c_double:
        return self._wrapped.tw

    @property
    def tf(self) -> c_double:
        return self._wrapped.tf

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def Process(self) -> c_long:
        return self._wrapped.Process


class RLoadSurfaceDistributed(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def SurfaceId(self) -> c_long:
        return self._wrapped.SurfaceId

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy

    @property
    def qz(self) -> c_double:
        return self._wrapped.qz


class RRebarSteelGrade_NEN(Wrapper):

    @property
    def fsrep(self) -> c_double:
        return self._wrapped.fsrep

    @property
    def fs(self) -> c_double:
        return self._wrapped.fs

    @property
    def esu(self) -> c_double:
        return self._wrapped.esu


class RRCBeamDesignBendingResult(Wrapper):

    @property
    def M(self) -> c_double:
        return self._wrapped.M

    @property
    def Ast(self) -> c_double:
        return self._wrapped.Ast

    @property
    def Astmin(self) -> c_double:
        return self._wrapped.Astmin

    @property
    def Asc(self) -> c_double:
        return self._wrapped.Asc

    @property
    def Ascmin(self) -> c_double:
        return self._wrapped.Ascmin

    @property
    def xc(self) -> c_double:
        return self._wrapped.xc

    @property
    def MErrorMessage(self) -> c_long:
        return self._wrapped.MErrorMessage


class RLoadTrussStress(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def P(self) -> c_double:
        return self._wrapped.P


class RSection(Wrapper):

    @property
    def SectionType(self) -> c_long:
        return self._wrapped.SectionType

    @property
    def Name(self) -> BSTR:
        return self._wrapped.Name

    @property
    def Visible(self) -> c_long:
        return self._wrapped.Visible

    @property
    def P(self) -> 'RPoint3d':
        return self._wrapped.P

    @property
    def N(self) -> 'RPoint3d':
        return self._wrapped.N

    @property
    def SegmentEndP(self) -> 'RPoint3d':
        return self._wrapped.SegmentEndP

    @property
    def InAllResultBlocks(self) -> c_long:
        return self._wrapped.InAllResultBlocks

    @property
    def ResultBlock(self) -> 'RResultBlock':
        return self._wrapped.ResultBlock

    @property
    def ForAllResultComponents(self) -> c_long:
        return self._wrapped.ForAllResultComponents

    @property
    def ResultComponent(self) -> c_long:
        return self._wrapped.ResultComponent

    @property
    def DisplayMode(self) -> c_long:
        return self._wrapped.DisplayMode

    @property
    def L(self) -> c_double:
        return self._wrapped.L

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def DiagOnBothSide(self) -> c_long:
        return self._wrapped.DiagOnBothSide

    @property
    def DiagInPlane(self) -> c_long:
        return self._wrapped.DiagInPlane


class RXLAMParams(Wrapper):

    @property
    def XLAMindex(self) -> c_long:
        return self._wrapped.XLAMindex

    @property
    def TopLayerDirection(self) -> c_long:
        return self._wrapped.TopLayerDirection

    @property
    def ServiceClass(self) -> c_long:
        return self._wrapped.ServiceClass

    @property
    def k_def(self) -> c_double:
        return self._wrapped.k_def

    @property
    def k_sys(self) -> c_long:
        return self._wrapped.k_sys

    @property
    def k_fin(self) -> c_long:
        return self._wrapped.k_fin


class RDistributedMovingLoadOnBeam(Wrapper):

    @property
    def SystemGL(self) -> c_long:
        return self._wrapped.SystemGL

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Position1(self) -> c_double:
        return self._wrapped.Position1

    @property
    def Fx1(self) -> c_double:
        return self._wrapped.Fx1

    @property
    def Fy1(self) -> c_double:
        return self._wrapped.Fy1

    @property
    def Fz1(self) -> c_double:
        return self._wrapped.Fz1

    @property
    def Position2(self) -> c_double:
        return self._wrapped.Position2

    @property
    def Fx2(self) -> c_double:
        return self._wrapped.Fx2

    @property
    def Fy2(self) -> c_double:
        return self._wrapped.Fy2

    @property
    def Fz2(self) -> c_double:
        return self._wrapped.Fz2


class RLoadBeamFault(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def DL(self) -> c_double:
        return self._wrapped.DL


class RLoadDomainConstant(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy

    @property
    def qz(self) -> c_double:
        return self._wrapped.qz


class RRCBeamDesignResult(Wrapper):

    @property
    def Top(self) -> 'RRCBeamDesignBendingResult':
        return self._wrapped.Top

    @property
    def Bottom(self) -> 'RRCBeamDesignBendingResult':
        return self._wrapped.Bottom

    @property
    def Vsdred_Min(self) -> c_double:
        return self._wrapped.Vsdred_Min

    @property
    def Vsdred_Max(self) -> c_double:
        return self._wrapped.Vsdred_Max

    @property
    def Ved_Vrd(self) -> c_double:
        return self._wrapped.Ved_Vrd

    @property
    def S(self) -> c_double:
        return self._wrapped.S

    @property
    def sv(self) -> c_double:
        return self._wrapped.sv

    @property
    def smax(self) -> c_double:
        return self._wrapped.smax

    @property
    def VErrorMessage(self) -> c_long:
        return self._wrapped.VErrorMessage

    @property
    def Tsd(self) -> c_double:
        return self._wrapped.Tsd

    @property
    def Ted_Trd(self) -> c_double:
        return self._wrapped.Ted_Trd

    @property
    def st(self) -> c_double:
        return self._wrapped.st

    @property
    def Astor(self) -> c_double:
        return self._wrapped.Astor

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def VRdc(self) -> c_double:
        return self._wrapped.VRdc

    @property
    def VRds(self) -> c_double:
        return self._wrapped.VRds


class RColumnCheckingParameters(Wrapper):

    @property
    def CalcEccIncy(self) -> c_long:
        return self._wrapped.CalcEccIncy

    @property
    def CalcEccIncz(self) -> c_long:
        return self._wrapped.CalcEccIncz

    @property
    def CalcEcc2Y(self) -> c_long:
        return self._wrapped.CalcEcc2Y

    @property
    def CalcEcc2Z(self) -> c_long:
        return self._wrapped.CalcEcc2Z

    @property
    def Ky(self) -> c_double:
        return self._wrapped.Ky

    @property
    def Kz(self) -> c_double:
        return self._wrapped.Kz

    @property
    def IsCustomLength(self) -> c_long:
        return self._wrapped.IsCustomLength

    @property
    def ColumnLength(self) -> c_double:
        return self._wrapped.ColumnLength

    @property
    def fieff_EC_ITA(self) -> c_double:
        return self._wrapped.fieff_EC_ITA

    @property
    def SwayImp(self) -> c_long:
        return self._wrapped.SwayImp

    @property
    def BucklingModeY(self) -> c_long:
        return self._wrapped.BucklingModeY

    @property
    def BucklingModeZ(self) -> c_long:
        return self._wrapped.BucklingModeZ

    @property
    def ShrinkCreepEpsSIA(self) -> c_double:
        return self._wrapped.ShrinkCreepEpsSIA

    @property
    def ApproximateCurvatureSIA(self) -> c_long:
        return self._wrapped.ApproximateCurvatureSIA

    @property
    def Sum2ndEccentricites(self) -> c_long:
        return self._wrapped.Sum2ndEccentricites


class RLoadLineDistributed(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def qx1(self) -> c_double:
        return self._wrapped.qx1

    @property
    def qy1(self) -> c_double:
        return self._wrapped.qy1

    @property
    def qz1(self) -> c_double:
        return self._wrapped.qz1

    @property
    def mx1(self) -> c_double:
        return self._wrapped.mx1

    @property
    def my1(self) -> c_double:
        return self._wrapped.my1

    @property
    def mz1(self) -> c_double:
        return self._wrapped.mz1

    @property
    def qx2(self) -> c_double:
        return self._wrapped.qx2

    @property
    def qy2(self) -> c_double:
        return self._wrapped.qy2

    @property
    def qz2(self) -> c_double:
        return self._wrapped.qz2

    @property
    def mx2(self) -> c_double:
        return self._wrapped.mx2

    @property
    def my2(self) -> c_double:
        return self._wrapped.my2

    @property
    def mz2(self) -> c_double:
        return self._wrapped.mz2

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def Position1(self) -> c_double:
        return self._wrapped.Position1

    @property
    def Position2(self) -> c_double:
        return self._wrapped.Position2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Trapezoid(self) -> c_long:
        return self._wrapped.Trapezoid


class RLoadRibConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Fgx(self) -> c_double:
        return self._wrapped.Fgx

    @property
    def Fgy(self) -> c_double:
        return self._wrapped.Fgy

    @property
    def Fgz(self) -> c_double:
        return self._wrapped.Fgz

    @property
    def Mgx(self) -> c_double:
        return self._wrapped.Mgx

    @property
    def Mgy(self) -> c_double:
        return self._wrapped.Mgy

    @property
    def Mgz(self) -> c_double:
        return self._wrapped.Mgz

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR


class RLoadRibThermal(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Tref(self) -> c_double:
        return self._wrapped.Tref

    @property
    def Ttop(self) -> c_double:
        return self._wrapped.Ttop

    @property
    def Tbot(self) -> c_double:
        return self._wrapped.Tbot

    @property
    def Axis(self) -> c_long:
        return self._wrapped.Axis


class RLoadTrussFault(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def DL(self) -> c_double:
        return self._wrapped.DL


class RLoadTrussThermal(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId

    @property
    def Tref(self) -> c_double:
        return self._wrapped.Tref

    @property
    def T0(self) -> c_double:
        return self._wrapped.T0


class RLoadSurfaceEdge(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def SurfaceId(self) -> c_long:
        return self._wrapped.SurfaceId

    @property
    def qx1(self) -> c_double:
        return self._wrapped.qx1

    @property
    def qx2(self) -> c_double:
        return self._wrapped.qx2

    @property
    def qx3(self) -> c_double:
        return self._wrapped.qx3

    @property
    def qx4(self) -> c_double:
        return self._wrapped.qx4

    @property
    def qy1(self) -> c_double:
        return self._wrapped.qy1

    @property
    def qy2(self) -> c_double:
        return self._wrapped.qy2

    @property
    def qy3(self) -> c_double:
        return self._wrapped.qy3

    @property
    def qy4(self) -> c_double:
        return self._wrapped.qy4

    @property
    def qz1(self) -> c_double:
        return self._wrapped.qz1

    @property
    def qz2(self) -> c_double:
        return self._wrapped.qz2

    @property
    def qz3(self) -> c_double:
        return self._wrapped.qz3

    @property
    def qz4(self) -> c_double:
        return self._wrapped.qz4

    @property
    def System1(self) -> c_long:
        return self._wrapped.System1

    @property
    def System2(self) -> c_long:
        return self._wrapped.System2

    @property
    def System3(self) -> c_long:
        return self._wrapped.System3

    @property
    def System4(self) -> c_long:
        return self._wrapped.System4

    @property
    def EdgeLoaded1(self) -> c_long:
        return self._wrapped.EdgeLoaded1

    @property
    def EdgeLoaded2(self) -> c_long:
        return self._wrapped.EdgeLoaded2

    @property
    def EdgeLoaded3(self) -> c_long:
        return self._wrapped.EdgeLoaded3

    @property
    def EdgeLoaded4(self) -> c_long:
        return self._wrapped.EdgeLoaded4

    @property
    def DistributionType1(self) -> c_long:
        return self._wrapped.DistributionType1

    @property
    def DistributionType2(self) -> c_long:
        return self._wrapped.DistributionType2

    @property
    def DistributionType3(self) -> c_long:
        return self._wrapped.DistributionType3

    @property
    def DistributionType4(self) -> c_long:
        return self._wrapped.DistributionType4


class RLoadDomainConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId


class RLoadSurfaceConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def SurfaceId(self) -> c_long:
        return self._wrapped.SurfaceId

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def x(self) -> c_double:
        return self._wrapped.x

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR


class RLoadDomainPolyLine(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Nx(self) -> c_double:
        return self._wrapped.Nx

    @property
    def Ny(self) -> c_double:
        return self._wrapped.Ny

    @property
    def Nz(self) -> c_double:
        return self._wrapped.Nz


class RLoadDomainPolyAssoc(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Nx(self) -> c_double:
        return self._wrapped.Nx

    @property
    def Ny(self) -> c_double:
        return self._wrapped.Ny

    @property
    def Nz(self) -> c_double:
        return self._wrapped.Nz


class RLoadSurfaceToBeam(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Px(self) -> c_double:
        return self._wrapped.Px

    @property
    def Py(self) -> c_double:
        return self._wrapped.Py

    @property
    def Pz(self) -> c_double:
        return self._wrapped.Pz


class RLoadDomainFluid(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def Coord1(self) -> c_double:
        return self._wrapped.Coord1

    @property
    def Coord2(self) -> c_double:
        return self._wrapped.Coord2

    @property
    def P1(self) -> c_double:
        return self._wrapped.P1

    @property
    def P2(self) -> c_double:
        return self._wrapped.P2

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId


class RLoadSurfaceFluid(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def Coord1(self) -> c_double:
        return self._wrapped.Coord1

    @property
    def Coord2(self) -> c_double:
        return self._wrapped.Coord2

    @property
    def P1(self) -> c_double:
        return self._wrapped.P1

    @property
    def P2(self) -> c_double:
        return self._wrapped.P2

    @property
    def SurfaceId(self) -> c_long:
        return self._wrapped.SurfaceId


class RLoadDomainLinear(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def LoadDistributionType(self) -> c_long:
        return self._wrapped.LoadDistributionType

    @property
    def Component(self) -> c_long:
        return self._wrapped.Component

    @property
    def P1(self) -> c_double:
        return self._wrapped.P1

    @property
    def P2(self) -> c_double:
        return self._wrapped.P2

    @property
    def P3(self) -> c_double:
        return self._wrapped.P3

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def x3(self) -> c_double:
        return self._wrapped.x3

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def y3(self) -> c_double:
        return self._wrapped.y3

    @property
    def z1(self) -> c_double:
        return self._wrapped.z1

    @property
    def z2(self) -> c_double:
        return self._wrapped.z2

    @property
    def z3(self) -> c_double:
        return self._wrapped.z3

    @property
    def WindowLoad(self) -> c_long:
        return self._wrapped.WindowLoad


class RLoadDynamic(Wrapper):

    @property
    def DynamicLoadType(self) -> c_long:
        return self._wrapped.DynamicLoadType

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def NodeId(self) -> c_long:
        return self._wrapped.NodeId

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId

    @property
    def FxFunctionId(self) -> c_long:
        return self._wrapped.FxFunctionId

    @property
    def FyFunctionId(self) -> c_long:
        return self._wrapped.FyFunctionId

    @property
    def FzFunctionId(self) -> c_long:
        return self._wrapped.FzFunctionId

    @property
    def MxFunctionId(self) -> c_long:
        return self._wrapped.MxFunctionId

    @property
    def MyFunctionId(self) -> c_long:
        return self._wrapped.MyFunctionId

    @property
    def MzFunctionId(self) -> c_long:
        return self._wrapped.MzFunctionId


class RLoadBeamMemberConcentrated(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def Fgx(self) -> c_double:
        return self._wrapped.Fgx

    @property
    def Fgy(self) -> c_double:
        return self._wrapped.Fgy

    @property
    def Fgz(self) -> c_double:
        return self._wrapped.Fgz

    @property
    def Mgx(self) -> c_double:
        return self._wrapped.Mgx

    @property
    def Mgy(self) -> c_double:
        return self._wrapped.Mgy

    @property
    def Mgz(self) -> c_double:
        return self._wrapped.Mgz

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR


class RLoadRibMemberDistributed(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def qx1(self) -> c_double:
        return self._wrapped.qx1

    @property
    def qy1(self) -> c_double:
        return self._wrapped.qy1

    @property
    def qz1(self) -> c_double:
        return self._wrapped.qz1

    @property
    def mx1(self) -> c_double:
        return self._wrapped.mx1

    @property
    def my1(self) -> c_double:
        return self._wrapped.my1

    @property
    def mz1(self) -> c_double:
        return self._wrapped.mz1

    @property
    def qx2(self) -> c_double:
        return self._wrapped.qx2

    @property
    def qy2(self) -> c_double:
        return self._wrapped.qy2

    @property
    def qz2(self) -> c_double:
        return self._wrapped.qz2

    @property
    def mx2(self) -> c_double:
        return self._wrapped.mx2

    @property
    def my2(self) -> c_double:
        return self._wrapped.my2

    @property
    def mz2(self) -> c_double:
        return self._wrapped.mz2

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def Position1(self) -> c_double:
        return self._wrapped.Position1

    @property
    def Position2(self) -> c_double:
        return self._wrapped.Position2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Trapezoid(self) -> c_long:
        return self._wrapped.Trapezoid


class RLoadDomainPolyLineItem(Wrapper):

    @property
    def StartPoint(self) -> 'RPoint3d':
        return self._wrapped.StartPoint

    @property
    def EndPoint(self) -> 'RPoint3d':
        return self._wrapped.EndPoint

    @property
    def LineGeomType(self) -> c_long:
        return self._wrapped.LineGeomType

    @property
    def CircleArcGeomData(self) -> 'RCircleArcGeomData':
        return self._wrapped.CircleArcGeomData

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def ItemType(self) -> c_long:
        return self._wrapped.ItemType

    @property
    def ElementId(self) -> c_long:
        return self._wrapped.ElementId


class RLoadPanelLinear(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LoadPanelId(self) -> c_long:
        return self._wrapped.LoadPanelId

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def LoadDistributionType(self) -> c_long:
        return self._wrapped.LoadDistributionType

    @property
    def Component(self) -> c_long:
        return self._wrapped.Component

    @property
    def P1(self) -> c_double:
        return self._wrapped.P1

    @property
    def P2(self) -> c_double:
        return self._wrapped.P2

    @property
    def P3(self) -> c_double:
        return self._wrapped.P3

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def x3(self) -> c_double:
        return self._wrapped.x3

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def y3(self) -> c_double:
        return self._wrapped.y3

    @property
    def z1(self) -> c_double:
        return self._wrapped.z1

    @property
    def z2(self) -> c_double:
        return self._wrapped.z2

    @property
    def z3(self) -> c_double:
        return self._wrapped.z3


class RLoadPanelPolyArea(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def LoadDistributionType(self) -> c_long:
        return self._wrapped.LoadDistributionType

    @property
    def Component(self) -> c_long:
        return self._wrapped.Component

    @property
    def P1(self) -> c_double:
        return self._wrapped.P1

    @property
    def P2(self) -> c_double:
        return self._wrapped.P2

    @property
    def P3(self) -> c_double:
        return self._wrapped.P3

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def x3(self) -> c_double:
        return self._wrapped.x3

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def y3(self) -> c_double:
        return self._wrapped.y3

    @property
    def z1(self) -> c_double:
        return self._wrapped.z1

    @property
    def z2(self) -> c_double:
        return self._wrapped.z2

    @property
    def z3(self) -> c_double:
        return self._wrapped.z3

    @property
    def WindowLoad(self) -> c_long:
        return self._wrapped.WindowLoad


class RLoadPanelPolyLine(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def Nx(self) -> c_double:
        return self._wrapped.Nx

    @property
    def Ny(self) -> c_double:
        return self._wrapped.Ny

    @property
    def Nz(self) -> c_double:
        return self._wrapped.Nz


class RLoadLineSelfWeigth(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def LineId(self) -> c_long:
        return self._wrapped.LineId


class RLoadDomainConstant_V154(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId

    @property
    def SystemGLR(self) -> c_long:
        return self._wrapped.SystemGLR

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy

    @property
    def qz(self) -> c_double:
        return self._wrapped.qz

    @property
    def WindowLoad(self) -> c_long:
        return self._wrapped.WindowLoad


class RLoadSurfaceSelfWeigth(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def SurfaceId(self) -> c_long:
        return self._wrapped.SurfaceId


class RLoadDomainSelfWeigth(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def DomainId(self) -> c_long:
        return self._wrapped.DomainId


class RLoadDomainPolyAssoc_V161(Wrapper):

    @property
    def LoadCaseId(self) -> c_long:
        return self._wrapped.LoadCaseId

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def NormalVector(self) -> 'RPoint3d':
        return self._wrapped.NormalVector


class RShowNumbering(Wrapper):

    @property
    def Node(self) -> c_long:
        return self._wrapped.Node

    @property
    def Truss(self) -> c_long:
        return self._wrapped.Truss

    @property
    def Beam(self) -> c_long:
        return self._wrapped.Beam

    @property
    def Rib(self) -> c_long:
        return self._wrapped.Rib

    @property
    def Surface(self) -> c_long:
        return self._wrapped.Surface

    @property
    def Domain(self) -> c_long:
        return self._wrapped.Domain

    @property
    def Support(self) -> c_long:
        return self._wrapped.Support

    @property
    def Links(self) -> c_long:
        return self._wrapped.Links

    @property
    def Rigid(self) -> c_long:
        return self._wrapped.Rigid

    @property
    def Diaphragm(self) -> c_long:
        return self._wrapped.Diaphragm

    @property
    def Spring(self) -> c_long:
        return self._wrapped.Spring

    @property
    def Gap(self) -> c_long:
        return self._wrapped.Gap

    @property
    def Material(self) -> c_long:
        return self._wrapped.Material

    @property
    def CrossSection(self) -> c_long:
        return self._wrapped.CrossSection

    @property
    def Reference(self) -> c_long:
        return self._wrapped.Reference

    @property
    def ARBO_CRETelems(self) -> c_long:
        return self._wrapped.ARBO_CRETelems

    @property
    def DesignGroup(self) -> c_long:
        return self._wrapped.DesignGroup

    @property
    def OptimisationGroup(self) -> c_long:
        return self._wrapped.OptimisationGroup


class RDisplacementValues(Wrapper):

    @property
    def ex(self) -> c_double:
        return self._wrapped.ex

    @property
    def ey(self) -> c_double:
        return self._wrapped.ey

    @property
    def ez(self) -> c_double:
        return self._wrapped.ez

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def eR(self) -> c_double:
        return self._wrapped.eR

    @property
    def fR(self) -> c_double:
        return self._wrapped.fR


class RCSOptimizationResultsPredefinedShapes(Wrapper):

    @property
    def OptimizationEfficiency(self) -> c_double:
        return self._wrapped.OptimizationEfficiency

    @property
    def Efficiency(self) -> c_double:
        return self._wrapped.Efficiency

    @property
    def M(self) -> c_double:
        return self._wrapped.M

    @property
    def DeltaM(self) -> c_double:
        return self._wrapped.DeltaM

    @property
    def GroupCrossSection(self) -> c_long:
        return self._wrapped.GroupCrossSection


class RRibbedDomainParameters(Wrapper):

    @property
    def AutoExcentricityType(self) -> c_long:
        return self._wrapped.AutoExcentricityType

    @property
    def h(self) -> c_double:
        return self._wrapped.h

    @property
    def w(self) -> c_double:
        return self._wrapped.w

    @property
    def d(self) -> c_double:
        return self._wrapped.d

    @property
    def exc(self) -> c_double:
        return self._wrapped.exc


class RConcentratedMovingLoadOnBeam(Wrapper):

    @property
    def SystemGL(self) -> c_long:
        return self._wrapped.SystemGL

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz

    @property
    def Mx(self) -> c_double:
        return self._wrapped.Mx

    @property
    def My(self) -> c_double:
        return self._wrapped.My

    @property
    def Mz(self) -> c_double:
        return self._wrapped.Mz


class RLinearFootingCalced(Wrapper):

    @property
    def Calculated(self) -> c_long:
        return self._wrapped.Calculated

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def StepMeasureSource(self) -> c_long:
        return self._wrapped.StepMeasureSource

    @property
    def dx1(self) -> c_double:
        return self._wrapped.dx1

    @property
    def dx2(self) -> c_double:
        return self._wrapped.dx2


class RSectionElementData(Wrapper):

    @property
    def SurfaceIndex(self) -> c_long:
        return self._wrapped.SurfaceIndex

    @property
    def ContourLineId1(self) -> c_long:
        return self._wrapped.ContourLineId1

    @property
    def ContourLineRatio1(self) -> c_double:
        return self._wrapped.ContourLineRatio1

    @property
    def ContourLineId2(self) -> c_long:
        return self._wrapped.ContourLineId2

    @property
    def ContourLineRatio2(self) -> c_double:
        return self._wrapped.ContourLineRatio2


class RSurfacePointIndexes(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Index(self) -> c_long:
        return self._wrapped.ContourPoint1Index

    @property
    def ContourPoint2Index(self) -> c_long:
        return self._wrapped.ContourPoint2Index

    @property
    def ContourPoint3Index(self) -> c_long:
        return self._wrapped.ContourPoint3Index

    @property
    def ContourPoint4Index(self) -> c_long:
        return self._wrapped.ContourPoint4Index


class RLinearFootingSpec(Wrapper):

    @property
    def FixedX1(self) -> c_long:
        return self._wrapped.FixedX1

    @property
    def FixedX2(self) -> c_long:
        return self._wrapped.FixedX2

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def StepMeasureSource(self) -> c_long:
        return self._wrapped.StepMeasureSource

    @property
    def dx1(self) -> c_double:
        return self._wrapped.dx1

    @property
    def dx2(self) -> c_double:
        return self._wrapped.dx2


class RImperfectionParams_V153(Wrapper):

    @property
    def SwayDirection(self) -> c_long:
        return self._wrapped.SwayDirection

    @property
    def SwayAngle(self) -> c_double:
        return self._wrapped.SwayAngle

    @property
    def BaseHeightType(self) -> c_long:
        return self._wrapped.BaseHeightType

    @property
    def BaseHeight(self) -> c_double:
        return self._wrapped.BaseHeight

    @property
    def StructureAutoHeight(self) -> c_long:
        return self._wrapped.StructureAutoHeight

    @property
    def StructureHeight(self) -> c_double:
        return self._wrapped.StructureHeight

    @property
    def Def(self) -> c_long:
        return self._wrapped.Def

    @property
    def MaterialType(self) -> c_long:
        return self._wrapped.MaterialType

    @property
    def ColumnsInvolved(self) -> c_long:
        return self._wrapped.ColumnsInvolved

    @property
    def Alpha_h(self) -> c_double:
        return self._wrapped.Alpha_h

    @property
    def Alpha_m(self) -> c_double:
        return self._wrapped.Alpha_m

    @property
    def Phi0(self) -> c_double:
        return self._wrapped.Phi0

    @property
    def phi(self) -> c_double:
        return self._wrapped.phi


class RNodeReinforcementValues(Wrapper):

    @property
    def Asbx(self) -> c_double:
        return self._wrapped.Asbx

    @property
    def Asby(self) -> c_double:
        return self._wrapped.Asby

    @property
    def Astx(self) -> c_double:
        return self._wrapped.Astx

    @property
    def Asty(self) -> c_double:
        return self._wrapped.Asty


class RLayerShapeAttributes(Wrapper):

    @property
    def LayerIndex(self) -> c_long:
        return self._wrapped.LayerIndex

    @property
    def Colour(self) -> c_long:
        return self._wrapped.Colour

    @property
    def PenStyle(self) -> c_long:
        return self._wrapped.PenStyle

    @property
    def PenWidth(self) -> c_double:
        return self._wrapped.PenWidth


class RLayerTextParams(Wrapper):

    @property
    def LayerIndex(self) -> c_long:
        return self._wrapped.LayerIndex

    @property
    def Colour(self) -> c_long:
        return self._wrapped.Colour

    @property
    def PenStyle(self) -> c_long:
        return self._wrapped.PenStyle

    @property
    def PenWidth(self) -> c_double:
        return self._wrapped.PenWidth

    @property
    def FontSize(self) -> c_double:
        return self._wrapped.FontSize

    @property
    def Angle(self) -> c_double:
        return self._wrapped.Angle

    @property
    def AlignmentPoint1(self) -> 'RPoint3d':
        return self._wrapped.AlignmentPoint1

    @property
    def AlignmentPoint2(self) -> 'RPoint3d':
        return self._wrapped.AlignmentPoint2

    @property
    def NormalVector(self) -> 'RPoint3d':
        return self._wrapped.NormalVector

    @property
    def HorizontalAlignment(self) -> c_long:
        return self._wrapped.HorizontalAlignment

    @property
    def VerticalAlignment(self) -> c_long:
        return self._wrapped.VerticalAlignment


class RShowSymbols(Wrapper):

    @property
    def ShowGraphicSymbols(self) -> 'RShowGraphicSymbols':
        return self._wrapped.ShowGraphicSymbols

    @property
    def ShowLocalSystems(self) -> 'RShowLocalSystems':
        return self._wrapped.ShowLocalSystems

    @property
    def ShowLoads(self) -> 'RShowLoads':
        return self._wrapped.ShowLoads

    @property
    def ObjectContours3D(self) -> c_long:
        return self._wrapped.ObjectContours3D


class RRebarPos(Wrapper):

    @property
    def TopX(self) -> c_double:
        return self._wrapped.TopX

    @property
    def BottomX(self) -> c_double:
        return self._wrapped.BottomX

    @property
    def TopY(self) -> c_double:
        return self._wrapped.TopY

    @property
    def BottomY(self) -> c_double:
        return self._wrapped.BottomY


class RShowProperties(Wrapper):

    @property
    def MaterialName(self) -> c_long:
        return self._wrapped.MaterialName

    @property
    def CrossSectName(self) -> c_long:
        return self._wrapped.CrossSectName

    @property
    def BoltedJoint(self) -> c_long:
        return self._wrapped.BoltedJoint

    @property
    def ColumnReinf(self) -> c_long:
        return self._wrapped.ColumnReinf

    @property
    def BeamLength(self) -> c_long:
        return self._wrapped.BeamLength

    @property
    def Thickness(self) -> c_long:
        return self._wrapped.Thickness

    @property
    def DomainArea(self) -> c_long:
        return self._wrapped.DomainArea

    @property
    def COBIAXlabels(self) -> c_long:
        return self._wrapped.COBIAXlabels

    @property
    def LoadValue(self) -> c_long:
        return self._wrapped.LoadValue

    @property
    def MassValue(self) -> c_long:
        return self._wrapped.MassValue

    @property
    def Units(self) -> c_long:
        return self._wrapped.Units

    @property
    def ConcentratedLoadValue(self) -> c_long:
        return self._wrapped.ConcentratedLoadValue

    @property
    def LineLoadValue(self) -> c_long:
        return self._wrapped.LineLoadValue

    @property
    def SurfaceLoadValue(self) -> c_long:
        return self._wrapped.SurfaceLoadValue

    @property
    def TemperatureLoadValue(self) -> c_long:
        return self._wrapped.TemperatureLoadValue

    @property
    def SelfWeightValue(self) -> c_long:
        return self._wrapped.SelfWeightValue

    @property
    def OtherLoadValue(self) -> c_long:
        return self._wrapped.OtherLoadValue


class RXLAMSurfaceStressValues(Wrapper):

    @property
    def xssvSxx_m_T(self) -> c_double:
        return self._wrapped.xssvSxx_m_T

    @property
    def xssvSyy_m_T(self) -> c_double:
        return self._wrapped.xssvSyy_m_T

    @property
    def xssvSxy_m_T(self) -> c_double:
        return self._wrapped.xssvSxy_m_T

    @property
    def xssvSxx_m_B(self) -> c_double:
        return self._wrapped.xssvSxx_m_B

    @property
    def xssvSyy_m_B(self) -> c_double:
        return self._wrapped.xssvSyy_m_B

    @property
    def xssvSxy_m_B(self) -> c_double:
        return self._wrapped.xssvSxy_m_B

    @property
    def xssvSxx_n(self) -> c_double:
        return self._wrapped.xssvSxx_n

    @property
    def xssvSyy_n(self) -> c_double:
        return self._wrapped.xssvSyy_n

    @property
    def xssvSxy_n(self) -> c_double:
        return self._wrapped.xssvSxy_n

    @property
    def xssvSxz_max(self) -> c_double:
        return self._wrapped.xssvSxz_max

    @property
    def xssvSyz_max(self) -> c_double:
        return self._wrapped.xssvSyz_max

    @property
    def xssvSrx_max(self) -> c_double:
        return self._wrapped.xssvSrx_max

    @property
    def xssvSry_max(self) -> c_double:
        return self._wrapped.xssvSry_max


class RExtendedDisplayParameters(Wrapper):

    @property
    def BasicDispParams(self) -> 'RBasicDisplayParameters':
        return self._wrapped.BasicDispParams

    @property
    def DisplayAnalysisType(self) -> c_long:
        return self._wrapped.DisplayAnalysisType

    @property
    def ResultsType(self) -> c_long:
        return self._wrapped.ResultsType

    @property
    def MinMaxType(self) -> c_long:
        return self._wrapped.MinMaxType

    @property
    def CriticalResCombinationType(self) -> c_long:
        return self._wrapped.CriticalResCombinationType

    @property
    def SectPlaneContour(self) -> c_long:
        return self._wrapped.SectPlaneContour

    @property
    def DisplayedEnvelopes(self) -> c_long:
        return self._wrapped.DisplayedEnvelopes


class RShowLabels(Wrapper):

    @property
    def ShowNumbering(self) -> 'RShowNumbering':
        return self._wrapped.ShowNumbering

    @property
    def ShowProperties(self) -> 'RShowProperties':
        return self._wrapped.ShowProperties

    @property
    def ShowActualReinf(self) -> 'RShowActualReinforcement':
        return self._wrapped.ShowActualReinf

    @property
    def UseFiniteElements(self) -> c_long:
        return self._wrapped.UseFiniteElements

    @property
    def LabelsOnLines(self) -> c_long:
        return self._wrapped.LabelsOnLines


class RWorldRectangle(Wrapper):

    @property
    def Left(self) -> c_double:
        return self._wrapped.Left

    @property
    def Right(self) -> c_double:
        return self._wrapped.Right

    @property
    def Top(self) -> c_double:
        return self._wrapped.Top

    @property
    def Bottom(self) -> c_double:
        return self._wrapped.Bottom


class RExtendedDisplayParameters_V153(Wrapper):

    @property
    def BasicDispParams(self) -> 'RBasicDisplayParameters_V153':
        return self._wrapped.BasicDispParams

    @property
    def DisplayAnalysisType(self) -> c_long:
        return self._wrapped.DisplayAnalysisType

    @property
    def ResultsType(self) -> c_long:
        return self._wrapped.ResultsType

    @property
    def MinMaxType(self) -> c_long:
        return self._wrapped.MinMaxType

    @property
    def CriticalResCombinationType(self) -> c_long:
        return self._wrapped.CriticalResCombinationType

    @property
    def SectPlaneContour(self) -> c_long:
        return self._wrapped.SectPlaneContour

    @property
    def DisplayedEnvelopes(self) -> c_long:
        return self._wrapped.DisplayedEnvelopes


class RCommonDisplayParameters_V161(Wrapper):

    @property
    def CriticalResSettings(self) -> 'RCommonCriticalResultsSettings_V161':
        return self._wrapped.CriticalResSettings

    @property
    def CutMomentPeaks(self) -> c_long:
        return self._wrapped.CutMomentPeaks

    @property
    def DrawInPlane(self) -> c_long:
        return self._wrapped.DrawInPlane

    @property
    def MiscelSettings(self) -> 'RMiscellaneousSettings':
        return self._wrapped.MiscelSettings


class RPushOverParams(Wrapper):

    @property
    def x(self) -> 'RPushOverDirectionParams':
        return self._wrapped.x

    @property
    def y(self) -> 'RPushOverDirectionParams':
        return self._wrapped.y


class RWindLoadParams(Wrapper):

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def v_b0(self) -> c_double:
        return self._wrapped.v_b0

    @property
    def c_season(self) -> c_double:
        return self._wrapped.c_season

    @property
    def c_o(self) -> c_double:
        return self._wrapped.c_o

    @property
    def TerrainCategoryDifferent(self) -> c_long:
        return self._wrapped.TerrainCategoryDifferent

    @property
    def TerrainCat_Xp(self) -> c_long:
        return self._wrapped.TerrainCat_Xp

    @property
    def TerrainCat_Xm(self) -> c_long:
        return self._wrapped.TerrainCat_Xm

    @property
    def TerrainCat_Yp(self) -> c_long:
        return self._wrapped.TerrainCat_Yp

    @property
    def TerrainCat_Ym(self) -> c_long:
        return self._wrapped.TerrainCat_Ym

    @property
    def CustomDirectionalFactors(self) -> c_long:
        return self._wrapped.CustomDirectionalFactors

    @property
    def c_dir_xp(self) -> c_double:
        return self._wrapped.c_dir_xp

    @property
    def c_dir_xm(self) -> c_double:
        return self._wrapped.c_dir_xm

    @property
    def c_dir_yp(self) -> c_double:
        return self._wrapped.c_dir_yp

    @property
    def c_dir_ym(self) -> c_double:
        return self._wrapped.c_dir_ym

    @property
    def RoofType(self) -> c_long:
        return self._wrapped.RoofType

    @property
    def FlatRoofEdgeType(self) -> c_long:
        return self._wrapped.FlatRoofEdgeType

    @property
    def FlatRoofEdgeParam(self) -> c_double:
        return self._wrapped.FlatRoofEdgeParam

    @property
    def TorsionalEffect(self) -> c_long:
        return self._wrapped.TorsionalEffect

    @property
    def u_xp(self) -> c_double:
        return self._wrapped.u_xp

    @property
    def u_xm(self) -> c_double:
        return self._wrapped.u_xm

    @property
    def u_yp(self) -> c_double:
        return self._wrapped.u_yp

    @property
    def u_ym(self) -> c_double:
        return self._wrapped.u_ym

    @property
    def Iw(self) -> c_double:
        return self._wrapped.Iw

    @property
    def Zone(self) -> c_long:
        return self._wrapped.Zone


class RSeismicParams_V153(Wrapper):

    @property
    def VibrType(self) -> c_long:
        return self._wrapped.VibrType

    @property
    def kg(self) -> c_double:
        return self._wrapped.kg

    @property
    def ks(self) -> c_double:
        return self._wrapped.ks

    @property
    def kt(self) -> c_double:
        return self._wrapped.kt

    @property
    def psi(self) -> c_double:
        return self._wrapped.psi

    @property
    def SeismicCombType(self) -> c_long:
        return self._wrapped.SeismicCombType

    @property
    def qd(self) -> c_double:
        return self._wrapped.qd

    @property
    def ksiV(self) -> c_double:
        return self._wrapped.ksiV

    @property
    def ModalCombType(self) -> c_long:
        return self._wrapped.ModalCombType

    @property
    def Torsion(self) -> c_long:
        return self._wrapped.Torsion

    @property
    def ExcCoeff(self) -> c_double:
        return self._wrapped.ExcCoeff

    @property
    def C(self) -> c_double:
        return self._wrapped.C

    @property
    def nu(self) -> c_double:
        return self._wrapped.nu

    @property
    def LoadCaseLoadCombination(self) -> c_long:
        return self._wrapped.LoadCaseLoadCombination

    @property
    def Eta(self) -> c_double:
        return self._wrapped.Eta

    @property
    def GroupID(self) -> c_long:
        return self._wrapped.GroupID

    @property
    def qdy(self) -> c_double:
        return self._wrapped.qdy

    @property
    def SeismicLimitState(self) -> c_long:
        return self._wrapped.SeismicLimitState


class RNonLinearAnalysis(Wrapper):

    @property
    def LoadCase(self) -> c_long:
        return self._wrapped.LoadCase

    @property
    def SolutionControl(self) -> c_long:
        return self._wrapped.SolutionControl

    @property
    def NodeId(self) -> c_long:
        return self._wrapped.NodeId

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def MaxDisplacement(self) -> c_double:
        return self._wrapped.MaxDisplacement

    @property
    def Increments(self) -> c_long:
        return self._wrapped.Increments

    @property
    def Iterations(self) -> c_long:
        return self._wrapped.Iterations

    @property
    def DisplacementConvergenceValue(self) -> c_double:
        return self._wrapped.DisplacementConvergenceValue

    @property
    def ForceConvergenceValue(self) -> c_double:
        return self._wrapped.ForceConvergenceValue

    @property
    def WorkConvergenceValue(self) -> c_double:
        return self._wrapped.WorkConvergenceValue

    @property
    def EnableDisplacementConvergence(self) -> c_long:
        return self._wrapped.EnableDisplacementConvergence

    @property
    def EnableForceConvergence(self) -> c_long:
        return self._wrapped.EnableForceConvergence

    @property
    def EnableWorkConvergence(self) -> c_long:
        return self._wrapped.EnableWorkConvergence

    @property
    def GeometricNonLinearity(self) -> c_long:
        return self._wrapped.GeometricNonLinearity

    @property
    def ReinforcementCalculation(self) -> c_long:
        return self._wrapped.ReinforcementCalculation

    @property
    def StoreLastIncrementOnly(self) -> c_long:
        return self._wrapped.StoreLastIncrementOnly

    @property
    def ReinforcementCalculationType(self) -> c_long:
        return self._wrapped.ReinforcementCalculationType

    @property
    def ContinueWithoutConvergence(self) -> c_long:
        return self._wrapped.ContinueWithoutConvergence

    @property
    def IncrementFunctionId(self) -> c_long:
        return self._wrapped.IncrementFunctionId

    @property
    def MaterialNonLinearity(self) -> c_long:
        return self._wrapped.MaterialNonLinearity

    @property
    def ConsiderCreep(self) -> c_long:
        return self._wrapped.ConsiderCreep

    @property
    def ConsiderShrinkage(self) -> c_long:
        return self._wrapped.ConsiderShrinkage


class RVibration(Wrapper):

    @property
    def LoadCase(self) -> c_long:
        return self._wrapped.LoadCase

    @property
    def Iterations(self) -> c_long:
        return self._wrapped.Iterations

    @property
    def ModeShapes(self) -> c_long:
        return self._wrapped.ModeShapes

    @property
    def EigenValueConvergence(self) -> c_double:
        return self._wrapped.EigenValueConvergence

    @property
    def EigenVectorConvergence(self) -> c_double:
        return self._wrapped.EigenVectorConvergence

    @property
    def ConvertLoadsToMasses(self) -> c_long:
        return self._wrapped.ConvertLoadsToMasses

    @property
    def ConcentratedMasses(self) -> c_long:
        return self._wrapped.ConcentratedMasses

    @property
    def ConvertConcentratedMassesToLoads(self) -> c_long:
        return self._wrapped.ConvertConcentratedMassesToLoads

    @property
    def MassControl(self) -> c_long:
        return self._wrapped.MassControl

    @property
    def ElementMasses(self) -> c_long:
        return self._wrapped.ElementMasses

    @property
    def MassComponentX(self) -> c_long:
        return self._wrapped.MassComponentX

    @property
    def MassComponentY(self) -> c_long:
        return self._wrapped.MassComponentY

    @property
    def MassComponentZ(self) -> c_long:
        return self._wrapped.MassComponentZ

    @property
    def ConvertSlabsToDiaphragms(self) -> c_long:
        return self._wrapped.ConvertSlabsToDiaphragms

    @property
    def MassMatrixType(self) -> c_long:
        return self._wrapped.MassMatrixType

    @property
    def IncreasedSupportStiffness(self) -> c_long:
        return self._wrapped.IncreasedSupportStiffness

    @property
    def MassesTakenIntoAccount(self) -> c_long:
        return self._wrapped.MassesTakenIntoAccount

    @property
    def HeightZ(self) -> c_double:
        return self._wrapped.HeightZ

    @property
    def StoryID(self) -> c_long:
        return self._wrapped.StoryID


class RBuckling(Wrapper):

    @property
    def LoadCase(self) -> c_long:
        return self._wrapped.LoadCase

    @property
    def Iterations(self) -> c_long:
        return self._wrapped.Iterations

    @property
    def ModeShapes(self) -> c_long:
        return self._wrapped.ModeShapes

    @property
    def EigenValueConvergence(self) -> c_double:
        return self._wrapped.EigenValueConvergence

    @property
    def EigenVectorConvergence(self) -> c_double:
        return self._wrapped.EigenVectorConvergence


class RDynamicAnalysis(Wrapper):

    @property
    def LoadCase(self) -> c_long:
        return self._wrapped.LoadCase

    @property
    def StaticLoadCase(self) -> c_long:
        return self._wrapped.StaticLoadCase

    @property
    def LoadCombination(self) -> c_long:
        return self._wrapped.LoadCombination

    @property
    def TimeIncrementFunctionId(self) -> c_long:
        return self._wrapped.TimeIncrementFunctionId

    @property
    def TimeIncrement(self) -> c_double:
        return self._wrapped.TimeIncrement

    @property
    def NumberOfIncrements(self) -> c_long:
        return self._wrapped.NumberOfIncrements

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def MassMatrixType(self) -> c_long:
        return self._wrapped.MassMatrixType

    @property
    def ConvertLoadsToMasses(self) -> c_long:
        return self._wrapped.ConvertLoadsToMasses

    @property
    def ConcentratedMasses(self) -> c_long:
        return self._wrapped.ConcentratedMasses

    @property
    def ConvertConcentratedMassesToLoads(self) -> c_long:
        return self._wrapped.ConvertConcentratedMassesToLoads

    @property
    def MassControl(self) -> c_long:
        return self._wrapped.MassControl

    @property
    def ElementMasses(self) -> c_long:
        return self._wrapped.ElementMasses

    @property
    def MaterialNonLinearity(self) -> c_long:
        return self._wrapped.MaterialNonLinearity

    @property
    def GeometricNonLinearity(self) -> c_long:
        return self._wrapped.GeometricNonLinearity

    @property
    def PerformIterations(self) -> c_long:
        return self._wrapped.PerformIterations

    @property
    def Iterations(self) -> c_long:
        return self._wrapped.Iterations

    @property
    def DisplacementConvergenceValue(self) -> c_double:
        return self._wrapped.DisplacementConvergenceValue

    @property
    def ForceConvergenceValue(self) -> c_double:
        return self._wrapped.ForceConvergenceValue

    @property
    def WorkConvergenceValue(self) -> c_double:
        return self._wrapped.WorkConvergenceValue

    @property
    def EnableDisplacementConvergence(self) -> c_long:
        return self._wrapped.EnableDisplacementConvergence

    @property
    def EnableForceConvergence(self) -> c_long:
        return self._wrapped.EnableForceConvergence

    @property
    def EnableWorkConvergence(self) -> c_long:
        return self._wrapped.EnableWorkConvergence

    @property
    def ContinueWithoutConvergence(self) -> c_long:
        return self._wrapped.ContinueWithoutConvergence

    @property
    def SavingInterval(self) -> c_double:
        return self._wrapped.SavingInterval

    @property
    def LoadsAndNodalMassesForDamping(self) -> c_long:
        return self._wrapped.LoadsAndNodalMassesForDamping


class RPushOverAnalysis(Wrapper):

    @property
    def LoadCase(self) -> c_long:
        return self._wrapped.LoadCase

    @property
    def ConstantLoadCase(self) -> c_long:
        return self._wrapped.ConstantLoadCase

    @property
    def NodeId(self) -> c_long:
        return self._wrapped.NodeId

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def MaxDisplacement(self) -> c_double:
        return self._wrapped.MaxDisplacement

    @property
    def Increments(self) -> c_long:
        return self._wrapped.Increments

    @property
    def Iterations(self) -> c_long:
        return self._wrapped.Iterations

    @property
    def DisplacementConvergenceValue(self) -> c_double:
        return self._wrapped.DisplacementConvergenceValue

    @property
    def ForceConvergenceValue(self) -> c_double:
        return self._wrapped.ForceConvergenceValue

    @property
    def WorkConvergenceValue(self) -> c_double:
        return self._wrapped.WorkConvergenceValue

    @property
    def EnableDisplacementConvergence(self) -> c_long:
        return self._wrapped.EnableDisplacementConvergence

    @property
    def EnableForceConvergence(self) -> c_long:
        return self._wrapped.EnableForceConvergence

    @property
    def EnableWorkConvergence(self) -> c_long:
        return self._wrapped.EnableWorkConvergence

    @property
    def GeometricNonLinearity(self) -> c_long:
        return self._wrapped.GeometricNonLinearity

    @property
    def ContinueWithoutConvergence(self) -> c_long:
        return self._wrapped.ContinueWithoutConvergence

    @property
    def MaterialNonLinearity(self) -> c_long:
        return self._wrapped.MaterialNonLinearity


class RNonLinearAnalysisResultInfo(Wrapper):

    @property
    def Increments(self) -> c_long:
        return self._wrapped.Increments

    @property
    def Iterations(self) -> c_long:
        return self._wrapped.Iterations

    @property
    def Lambda(self) -> c_double:
        return self._wrapped.Lambda

    @property
    def ErrorP(self) -> c_double:
        return self._wrapped.ErrorP

    @property
    def ErrorU(self) -> c_double:
        return self._wrapped.ErrorU

    @property
    def ErrorE(self) -> c_double:
        return self._wrapped.ErrorE

    @property
    def ErrorEq(self) -> c_double:
        return self._wrapped.ErrorEq

    @property
    def ControlVal(self) -> c_double:
        return self._wrapped.ControlVal

    @property
    def Convergence(self) -> c_long:
        return self._wrapped.Convergence


class RSeismicEq(Wrapper):

    @property
    def seEpsX(self) -> c_double:
        return self._wrapped.seEpsX

    @property
    def seEpsY(self) -> c_double:
        return self._wrapped.seEpsY

    @property
    def seEpsZ(self) -> c_double:
        return self._wrapped.seEpsZ


class RSpectrumData(Wrapper):

    @property
    def SpectrumData_EC(self) -> 'RSpectrumData_EC':
        return self._wrapped.SpectrumData_EC

    @property
    def SpectrumData_ITA(self) -> 'RSpectrumData_ITA':
        return self._wrapped.SpectrumData_ITA

    @property
    def SpectrumData_SIA(self) -> 'RSpectrumData_SIA':
        return self._wrapped.SpectrumData_SIA

    @property
    def SpectrumData_STAS(self) -> 'RSpectrumData_STAS':
        return self._wrapped.SpectrumData_STAS

    @property
    def SpectrumData_DIN(self) -> 'RSpectrumData_DIN':
        return self._wrapped.SpectrumData_DIN


class RRCBeamDesignCrackResults(Wrapper):

    @property
    def Top(self) -> 'RRCBeamDesignCrackResult':
        return self._wrapped.Top

    @property
    def Bottom(self) -> 'RRCBeamDesignCrackResult':
        return self._wrapped.Bottom


class RRCBeamDesignCrackResult(Wrapper):

    @property
    def Wk(self) -> c_double:
        return self._wrapped.Wk

    @property
    def I1(self) -> c_double:
        return self._wrapped.I1

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def I2(self) -> c_double:
        return self._wrapped.I2

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def Mcr(self) -> c_double:
        return self._wrapped.Mcr

    @property
    def Sr_max(self) -> c_double:
        return self._wrapped.Sr_max


class RRCBeamDesignReqReinfs(Wrapper):

    @property
    def Top(self) -> 'RRCBeamDesignReqReinf':
        return self._wrapped.Top

    @property
    def Bottom(self) -> 'RRCBeamDesignReqReinf':
        return self._wrapped.Bottom

    @property
    def Top_CC(self) -> 'RRCBeamDesignReqReinf':
        return self._wrapped.Top_CC

    @property
    def Bottom_CC(self) -> 'RRCBeamDesignReqReinf':
        return self._wrapped.Bottom_CC


class RRCBeamDesignReqReinf(Wrapper):

    @property
    def N(self) -> c_long:
        return self._wrapped.N

    @property
    def Nf(self) -> c_long:
        return self._wrapped.Nf

    @property
    def NRow(self) -> c_long:
        return self._wrapped.NRow

    @property
    def u(self) -> c_double:
        return self._wrapped.u


class RWriteValuesTo(Wrapper):

    @property
    def Nodes(self) -> c_long:
        return self._wrapped.Nodes

    @property
    def Lines(self) -> c_long:
        return self._wrapped.Lines

    @property
    def Surfaces(self) -> c_long:
        return self._wrapped.Surfaces

    @property
    def MinMaxOnly(self) -> c_long:
        return self._wrapped.MinMaxOnly


class RBulkNodalSupportSpringParams(Wrapper):

    @property
    def SupportType(self) -> c_long:
        return self._wrapped.SupportType

    @property
    def SpringParamIndexes(self) -> 'RSpringParamIndexes':
        return self._wrapped.SpringParamIndexes

    @property
    def IsolatorParamIndex(self) -> c_long:
        return self._wrapped.IsolatorParamIndex

    @property
    def IsolatorD2(self) -> c_double:
        return self._wrapped.IsolatorD2

    @property
    def NodeId(self) -> c_long:
        return self._wrapped.NodeId

    @property
    def MemberID(self) -> c_long:
        return self._wrapped.MemberID

    @property
    def SurfaceId1(self) -> c_long:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> c_long:
        return self._wrapped.SurfaceId2

    @property
    def DomainId1(self) -> c_long:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> c_long:
        return self._wrapped.DomainId2

    @property
    def ReferenceId(self) -> c_long:
        return self._wrapped.ReferenceId

    @property
    def ReferenceIdx(self) -> c_long:
        return self._wrapped.ReferenceIdx

    @property
    def ReferenceIdz(self) -> c_long:
        return self._wrapped.ReferenceIdz


class RBasicDisplayParameters(Wrapper):

    @property
    def ResultComponent(self) -> c_long:
        return self._wrapped.ResultComponent

    @property
    def Scale(self) -> c_double:
        return self._wrapped.Scale

    @property
    def DisplayMode(self) -> c_long:
        return self._wrapped.DisplayMode

    @property
    def DisplayShape(self) -> c_long:
        return self._wrapped.DisplayShape

    @property
    def WriteValuesTo(self) -> 'RWriteValuesTo':
        return self._wrapped.WriteValuesTo


class RVirtualBeamParams(Wrapper):

    @property
    def Name(self) -> BSTR:
        return self._wrapped.Name

    @property
    def LocXVid(self) -> c_long:
        return self._wrapped.LocXVid

    @property
    def LocZVid(self) -> c_long:
        return self._wrapped.LocZVid

    @property
    def LocXV(self) -> 'RPoint3d':
        return self._wrapped.LocXV

    @property
    def LocZV(self) -> 'RPoint3d':
        return self._wrapped.LocZV

    @property
    def SectionI(self) -> c_long:
        return self._wrapped.SectionI

    @property
    def SectionJ(self) -> c_long:
        return self._wrapped.SectionJ

    @property
    def DefinitionType(self) -> c_long:
        return self._wrapped.DefinitionType

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2

    @property
    def InnerDomains(self) -> c_long:
        return self._wrapped.InnerDomains


class RSpectrumData_V153(Wrapper):

    @property
    def SpectrumData_EC(self) -> 'RSpectrumData_EC':
        return self._wrapped.SpectrumData_EC

    @property
    def SpectrumData_ITA(self) -> 'RSpectrumData_ITA':
        return self._wrapped.SpectrumData_ITA

    @property
    def SpectrumData_SIA(self) -> 'RSpectrumData_SIA':
        return self._wrapped.SpectrumData_SIA

    @property
    def SpectrumData_STAS(self) -> 'RSpectrumData_STAS':
        return self._wrapped.SpectrumData_STAS

    @property
    def SpectrumData_DIN(self) -> 'RSpectrumData_DIN':
        return self._wrapped.SpectrumData_DIN

    @property
    def SpectrumData_ECHU(self) -> 'RSpectrumData_ECHU':
        return self._wrapped.SpectrumData_ECHU

    @property
    def SpectrumData_ECNL(self) -> 'RSpectrumData_ECNL':
        return self._wrapped.SpectrumData_ECNL


class RNodeCrackWidthValues(Wrapper):

    @property
    def covBottom(self) -> 'RCrackWidthValues':
        return self._wrapped.covBottom

    @property
    def covTop(self) -> 'RCrackWidthValues':
        return self._wrapped.covTop


class RBasicDisplayParameters_V153(Wrapper):

    @property
    def ResultComponent(self) -> c_long:
        return self._wrapped.ResultComponent

    @property
    def Scale(self) -> c_double:
        return self._wrapped.Scale

    @property
    def DisplayMode(self) -> c_long:
        return self._wrapped.DisplayMode

    @property
    def DisplayShape(self) -> c_long:
        return self._wrapped.DisplayShape

    @property
    def WriteValuesTo(self) -> 'RWriteValuesTo':
        return self._wrapped.WriteValuesTo

    @property
    def AutoScale(self) -> c_long:
        return self._wrapped.AutoScale


class RPushOverDirectionParams(Wrapper):

    @property
    def Uniform(self) -> c_long:
        return self._wrapped.Uniform

    @property
    def Modal(self) -> c_long:
        return self._wrapped.Modal

    @property
    def VibrationAnalysisType(self) -> c_long:
        return self._wrapped.VibrationAnalysisType

    @property
    def VibrationLoadCase(self) -> c_long:
        return self._wrapped.VibrationLoadCase

    @property
    def VibrationMode(self) -> c_long:
        return self._wrapped.VibrationMode

    @property
    def AutoDominantMode(self) -> c_long:
        return self._wrapped.AutoDominantMode

    @property
    def AccidentalEcc(self) -> c_double:
        return self._wrapped.AccidentalEcc


class RVirtualStripParams(Wrapper):

    @property
    def Name(self) -> BSTR:
        return self._wrapped.Name

    @property
    def StartP(self) -> 'RPoint3d':
        return self._wrapped.StartP

    @property
    def EndP(self) -> 'RPoint3d':
        return self._wrapped.EndP

    @property
    def SectionI(self) -> c_long:
        return self._wrapped.SectionI

    @property
    def SectionJ(self) -> c_long:
        return self._wrapped.SectionJ

    @property
    def NormV(self) -> 'RPoint3d':
        return self._wrapped.NormV

    @property
    def L(self) -> c_double:
        return self._wrapped.L

    @property
    def R(self) -> c_double:
        return self._wrapped.R

    @property
    def DefinitionType(self) -> c_long:
        return self._wrapped.DefinitionType

    @property
    def EccIY(self) -> c_double:
        return self._wrapped.EccIY

    @property
    def EccIZ(self) -> c_double:
        return self._wrapped.EccIZ

    @property
    def EccJY(self) -> c_double:
        return self._wrapped.EccJY

    @property
    def EccJZ(self) -> c_double:
        return self._wrapped.EccJZ


class RXLAMSurfaceStresses(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def xssvCenterPoint(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvCenterPoint

    @property
    def xssvContourPoint1(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourPoint1

    @property
    def xssvContourPoint2(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourPoint2

    @property
    def xssvContourPoint3(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourPoint3

    @property
    def xssvContourPoint4(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourPoint4

    @property
    def xssvContourLineMidPoint1(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourLineMidPoint1

    @property
    def xssvContourLineMidPoint2(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourLineMidPoint2

    @property
    def xssvContourLineMidPoint3(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourLineMidPoint3

    @property
    def xssvContourLineMidPoint4(self) -> 'RXLAMSurfaceStressValues':
        return self._wrapped.xssvContourLineMidPoint4


class RCircularFootingSpec(Wrapper):

    @property
    def FixedDiam(self) -> c_long:
        return self._wrapped.FixedDiam

    @property
    def Diam(self) -> c_double:
        return self._wrapped.Diam

    @property
    def StepMeasureSource(self) -> c_long:
        return self._wrapped.StepMeasureSource

    @property
    def DeltaR(self) -> c_double:
        return self._wrapped.DeltaR


class RSurfaceStresses(Wrapper):

    @property
    def ContourPointCount(self) -> c_long:
        return self._wrapped.ContourPointCount

    @property
    def ContourPoint1Id(self) -> c_long:
        return self._wrapped.ContourPoint1Id

    @property
    def ContourPoint2Id(self) -> c_long:
        return self._wrapped.ContourPoint2Id

    @property
    def ContourPoint3Id(self) -> c_long:
        return self._wrapped.ContourPoint3Id

    @property
    def ContourPoint4Id(self) -> c_long:
        return self._wrapped.ContourPoint4Id

    @property
    def ContourLine1Id(self) -> c_long:
        return self._wrapped.ContourLine1Id

    @property
    def ContourLine2Id(self) -> c_long:
        return self._wrapped.ContourLine2Id

    @property
    def ContourLine3Id(self) -> c_long:
        return self._wrapped.ContourLine3Id

    @property
    def ContourLine4Id(self) -> c_long:
        return self._wrapped.ContourLine4Id

    @property
    def ssvtmbCenterPoint(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbCenterPoint

    @property
    def ssvtmbContourPoint1(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourPoint1

    @property
    def ssvtmbContourPoint2(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourPoint2

    @property
    def ssvtmbContourPoint3(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourPoint3

    @property
    def ssvtmbContourPoint4(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourPoint4

    @property
    def ssvtmbContourLineMidPoint1(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourLineMidPoint1

    @property
    def ssvtmbContourLineMidPoint2(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourLineMidPoint2

    @property
    def ssvtmbContourLineMidPoint3(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourLineMidPoint3

    @property
    def ssvtmbContourLineMidPoint4(self) -> 'RSurfaceStressValuesTMB':
        return self._wrapped.ssvtmbContourLineMidPoint4


class RReinforcementParameters_STAS(Wrapper):

    @property
    def mbc(self) -> c_double:
        return self._wrapped.mbc

    @property
    def mbt(self) -> c_double:
        return self._wrapped.mbt

    @property
    def ksi0(self) -> c_double:
        return self._wrapped.ksi0

    @property
    def UnfavorableEccentricity_Npos(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Npos

    @property
    def UnfavorableEccentricity_Nneg(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Nneg

    @property
    def RebarPos(self) -> 'RRebarPos':
        return self._wrapped.RebarPos

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def phi(self) -> c_double:
        return self._wrapped.phi

    @property
    def nu(self) -> c_double:
        return self._wrapped.nu

    @property
    def tau_a(self) -> c_double:
        return self._wrapped.tau_a


class RStressPoint(Wrapper):

    @property
    def y(self) -> c_double:
        return self._wrapped.y

    @property
    def z(self) -> c_double:
        return self._wrapped.z


class RStressPointParams(Wrapper):

    @property
    def Tx_y(self) -> c_double:
        return self._wrapped.Tx_y

    @property
    def Tx_z(self) -> c_double:
        return self._wrapped.Tx_z

    @property
    def Vy_y(self) -> c_double:
        return self._wrapped.Vy_y

    @property
    def Vy_z(self) -> c_double:
        return self._wrapped.Vy_z

    @property
    def Vz_y(self) -> c_double:
        return self._wrapped.Vz_y

    @property
    def Vz_z(self) -> c_double:
        return self._wrapped.Vz_z

    @property
    def w(self) -> c_double:
        return self._wrapped.w

    @property
    def Tw_y(self) -> c_double:
        return self._wrapped.Tw_y

    @property
    def Tw_z(self) -> c_double:
        return self._wrapped.Tw_z


class RRectangularFootingCalced(Wrapper):

    @property
    def Calculated(self) -> c_long:
        return self._wrapped.Calculated

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def dx1(self) -> c_double:
        return self._wrapped.dx1

    @property
    def dx2(self) -> c_double:
        return self._wrapped.dx2

    @property
    def dy1(self) -> c_double:
        return self._wrapped.dy1

    @property
    def dy2(self) -> c_double:
        return self._wrapped.dy2


class RDimensionLineParameters(Wrapper):

    @property
    def Orthogonal(self) -> c_long:
        return self._wrapped.Orthogonal

    @property
    def Plane(self) -> c_long:
        return self._wrapped.Plane

    @property
    def OrthoDirection(self) -> c_long:
        return self._wrapped.OrthoDirection

    @property
    def NodeId1(self) -> c_long:
        return self._wrapped.NodeId1

    @property
    def NodeId2(self) -> c_long:
        return self._wrapped.NodeId2

    @property
    def LayerID(self) -> c_long:
        return self._wrapped.LayerID

    @property
    def LabelDistance(self) -> c_double:
        return self._wrapped.LabelDistance

    @property
    def LabelInside(self) -> c_long:
        return self._wrapped.LabelInside

    @property
    def LabelOrientation(self) -> c_long:
        return self._wrapped.LabelOrientation

    @property
    def TickMarkStyle(self) -> c_long:
        return self._wrapped.TickMarkStyle

    @property
    def DisplayUnit(self) -> c_long:
        return self._wrapped.DisplayUnit


class RRectangularFootingSpec(Wrapper):

    @property
    def FixedX1(self) -> c_long:
        return self._wrapped.FixedX1

    @property
    def FixedX2(self) -> c_long:
        return self._wrapped.FixedX2

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def FixedY1(self) -> c_long:
        return self._wrapped.FixedY1

    @property
    def FixedY2(self) -> c_long:
        return self._wrapped.FixedY2

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def StepMeasureSource(self) -> c_long:
        return self._wrapped.StepMeasureSource

    @property
    def dx1(self) -> c_double:
        return self._wrapped.dx1

    @property
    def dx2(self) -> c_double:
        return self._wrapped.dx2

    @property
    def dy1(self) -> c_double:
        return self._wrapped.dy1

    @property
    def dy2(self) -> c_double:
        return self._wrapped.dy2


class RRCBeamDesignParameters_MSZ(Wrapper):

    @property
    def CrackWidthCheck(self) -> c_long:
        return self._wrapped.CrackWidthCheck

    @property
    def MaxCrackWidth_Top(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Top

    @property
    def MaxCrackWidth_Bottom(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Bottom

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def AutoPsi(self) -> c_long:
        return self._wrapped.AutoPsi

    @property
    def Deflection_Beam_L_div(self) -> c_double:
        return self._wrapped.Deflection_Beam_L_div

    @property
    def Deflection_Cantilever_L_div(self) -> c_double:
        return self._wrapped.Deflection_Cantilever_L_div


class RSpectrumData_EC(Wrapper):

    @property
    def SubsoilClass(self) -> c_long:
        return self._wrapped.SubsoilClass

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def S(self) -> c_double:
        return self._wrapped.S

    @property
    def beta0(self) -> c_double:
        return self._wrapped.beta0

    @property
    def TB(self) -> c_double:
        return self._wrapped.TB

    @property
    def TC(self) -> c_double:
        return self._wrapped.TC

    @property
    def TD(self) -> c_double:
        return self._wrapped.TD

    @property
    def gammaI(self) -> c_double:
        return self._wrapped.gammaI

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy


class RRelease(Wrapper):

    @property
    def ReleaseType(self) -> c_long:
        return self._wrapped.ReleaseType

    @property
    def Init(self) -> c_double:
        return self._wrapped.Init

    @property
    def Limit(self) -> c_double:
        return self._wrapped.Limit

    @property
    def FunctionId(self) -> c_long:
        return self._wrapped.FunctionId


class RPlaneTolerance(Wrapper):

    @property
    def ptType(self) -> c_long:
        return self._wrapped.ptType

    @property
    def Value(self) -> c_double:
        return self._wrapped.Value


class RUnitParameters(Wrapper):

    @property
    def ConversionBaseID(self) -> c_long:
        return self._wrapped.ConversionBaseID

    @property
    def UsedID(self) -> c_long:
        return self._wrapped.UsedID

    @property
    def DecimalPlaces(self) -> c_long:
        return self._wrapped.DecimalPlaces

    @property
    def Multiplier(self) -> c_double:
        return self._wrapped.Multiplier


class RMovingLoadOnDomainItem(Wrapper):

    @property
    def SystemGL(self) -> c_long:
        return self._wrapped.SystemGL

    @property
    def Position(self) -> c_double:
        return self._wrapped.Position

    @property
    def a(self) -> c_double:
        return self._wrapped.a

    @property
    def b(self) -> c_double:
        return self._wrapped.b

    @property
    def u(self) -> c_double:
        return self._wrapped.u

    @property
    def Fx(self) -> c_double:
        return self._wrapped.Fx

    @property
    def Fy(self) -> c_double:
        return self._wrapped.Fy

    @property
    def Fz(self) -> c_double:
        return self._wrapped.Fz


class RLoadDomainLine(Wrapper):

    @property
    def px1(self) -> c_double:
        return self._wrapped.px1

    @property
    def px2(self) -> c_double:
        return self._wrapped.px2

    @property
    def py1(self) -> c_double:
        return self._wrapped.py1

    @property
    def py2(self) -> c_double:
        return self._wrapped.py2

    @property
    def pz1(self) -> c_double:
        return self._wrapped.pz1

    @property
    def pz2(self) -> c_double:
        return self._wrapped.pz2

    @property
    def pm1(self) -> c_double:
        return self._wrapped.pm1

    @property
    def pm2(self) -> c_double:
        return self._wrapped.pm2

    @property
    def DistributionType(self) -> c_long:
        return self._wrapped.DistributionType

    @property
    def SegmentId(self) -> c_long:
        return self._wrapped.SegmentId

    @property
    def GlbStartx(self) -> c_double:
        return self._wrapped.GlbStartx

    @property
    def GlbStarty(self) -> c_double:
        return self._wrapped.GlbStarty

    @property
    def GlbStartz(self) -> c_double:
        return self._wrapped.GlbStartz

    @property
    def GlbEndx(self) -> c_double:
        return self._wrapped.GlbEndx

    @property
    def GlbEndy(self) -> c_double:
        return self._wrapped.GlbEndy

    @property
    def GlbEndz(self) -> c_double:
        return self._wrapped.GlbEndz


class RRCBeamDesignParameters_STAS(Wrapper):

    @property
    def mbc(self) -> c_double:
        return self._wrapped.mbc

    @property
    def mbt(self) -> c_double:
        return self._wrapped.mbt

    @property
    def ksi0(self) -> c_double:
        return self._wrapped.ksi0

    @property
    def SeismicZone(self) -> c_long:
        return self._wrapped.SeismicZone

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def PlasticHinges(self) -> 'RRCBeamPlasticHinges':
        return self._wrapped.PlasticHinges


class RRectanularFootingCalced(Wrapper):

    @property
    def Calculated(self) -> c_long:
        return self._wrapped.Calculated

    @property
    def x1(self) -> c_double:
        return self._wrapped.x1

    @property
    def x2(self) -> c_double:
        return self._wrapped.x2

    @property
    def y1(self) -> c_double:
        return self._wrapped.y1

    @property
    def y2(self) -> c_double:
        return self._wrapped.y2

    @property
    def StepMeasureSource(self) -> c_long:
        return self._wrapped.StepMeasureSource

    @property
    def dx1(self) -> c_double:
        return self._wrapped.dx1

    @property
    def dx2(self) -> c_double:
        return self._wrapped.dx2

    @property
    def dy1(self) -> c_double:
        return self._wrapped.dy1

    @property
    def dy2(self) -> c_double:
        return self._wrapped.dy2


class RReleases(Wrapper):

    @property
    def x(self) -> 'RRelease':
        return self._wrapped.x

    @property
    def y(self) -> 'RRelease':
        return self._wrapped.y

    @property
    def z(self) -> 'RRelease':
        return self._wrapped.z

    @property
    def xx(self) -> 'RRelease':
        return self._wrapped.xx

    @property
    def yy(self) -> 'RRelease':
        return self._wrapped.yy

    @property
    def zz(self) -> 'RRelease':
        return self._wrapped.zz


class RSpectrumData_ECHU(Wrapper):

    @property
    def SubsoilClass(self) -> c_long:
        return self._wrapped.SubsoilClass

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def S(self) -> c_double:
        return self._wrapped.S

    @property
    def beta0(self) -> c_double:
        return self._wrapped.beta0

    @property
    def TB(self) -> c_double:
        return self._wrapped.TB

    @property
    def TC(self) -> c_double:
        return self._wrapped.TC

    @property
    def TD(self) -> c_double:
        return self._wrapped.TD

    @property
    def gammaI(self) -> c_double:
        return self._wrapped.gammaI

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy

    @property
    def LocalSpectrum(self) -> c_long:
        return self._wrapped.LocalSpectrum

    @property
    def F0(self) -> c_double:
        return self._wrapped.F0


class RSpectrumData_ECNL(Wrapper):

    @property
    def agr(self) -> c_double:
        return self._wrapped.agr

    @property
    def P(self) -> c_double:
        return self._wrapped.P

    @property
    def TB(self) -> c_double:
        return self._wrapped.TB

    @property
    def TC(self) -> c_double:
        return self._wrapped.TC

    @property
    def TD(self) -> c_double:
        return self._wrapped.TD

    @property
    def gammaI(self) -> c_double:
        return self._wrapped.gammaI

    @property
    def qx(self) -> c_double:
        return self._wrapped.qx

    @property
    def qy(self) -> c_double:
        return self._wrapped.qy


class RDomainVariableThickness(Wrapper):

    @property
    def VariableThicknessType(self) -> c_long:
        return self._wrapped.VariableThicknessType

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2

    @property
    def P3(self) -> 'RPoint3d':
        return self._wrapped.P3

    @property
    def t1(self) -> c_double:
        return self._wrapped.t1

    @property
    def t2(self) -> c_double:
        return self._wrapped.t2

    @property
    def t3(self) -> c_double:
        return self._wrapped.t3


class RDomainExcentricity(Wrapper):

    @property
    def ExcentricityType(self) -> c_long:
        return self._wrapped.ExcentricityType

    @property
    def P1(self) -> 'RPoint3d':
        return self._wrapped.P1

    @property
    def P2(self) -> 'RPoint3d':
        return self._wrapped.P2

    @property
    def P3(self) -> 'RPoint3d':
        return self._wrapped.P3

    @property
    def exc1(self) -> c_double:
        return self._wrapped.exc1

    @property
    def exc2(self) -> c_double:
        return self._wrapped.exc2

    @property
    def exc3(self) -> c_double:
        return self._wrapped.exc3

    @property
    def GroupID(self) -> c_long:
        return self._wrapped.GroupID


class RDomainCompositeRib(Wrapper):

    @property
    def RibMaterial(self) -> c_long:
        return self._wrapped.RibMaterial

    @property
    def CrossSection(self) -> c_long:
        return self._wrapped.CrossSection

    @property
    def Direction(self) -> c_long:
        return self._wrapped.Direction

    @property
    def Origin(self) -> 'RPoint3d':
        return self._wrapped.Origin

    @property
    def d(self) -> c_double:
        return self._wrapped.d

    @property
    def EccType(self) -> c_long:
        return self._wrapped.EccType

    @property
    def Eccentricity(self) -> c_double:
        return self._wrapped.Eccentricity

    @property
    def HasCustomShear(self) -> c_long:
        return self._wrapped.HasCustomShear

    @property
    def CustomShear(self) -> c_double:
        return self._wrapped.CustomShear

    @property
    def ActualRibs(self) -> c_long:
        return self._wrapped.ActualRibs


class RShowActualReinforcement(Wrapper):

    @property
    def Symbol_axb(self) -> c_long:
        return self._wrapped.Symbol_axb

    @property
    def Symbol_ayb(self) -> c_long:
        return self._wrapped.Symbol_ayb

    @property
    def Symbol_axt(self) -> c_long:
        return self._wrapped.Symbol_axt

    @property
    def Symbol_ayt(self) -> c_long:
        return self._wrapped.Symbol_ayt

    @property
    def Label_axb(self) -> c_long:
        return self._wrapped.Label_axb

    @property
    def Label_ayb(self) -> c_long:
        return self._wrapped.Label_ayb

    @property
    def Label_axt(self) -> c_long:
        return self._wrapped.Label_axt

    @property
    def Label_ayt(self) -> c_long:
        return self._wrapped.Label_ayt

    @property
    def ActReinfLabelType(self) -> c_long:
        return self._wrapped.ActReinfLabelType

    @property
    def AccordResComponent(self) -> c_long:
        return self._wrapped.AccordResComponent


class RReinforcementParameters_DIN(Wrapper):

    @property
    def dxt(self) -> c_double:
        return self._wrapped.dxt

    @property
    def dxb(self) -> c_double:
        return self._wrapped.dxb

    @property
    def dyt(self) -> c_double:
        return self._wrapped.dyt

    @property
    def dyb(self) -> c_double:
        return self._wrapped.dyb

    @property
    def SlabLoadTransfer(self) -> c_long:
        return self._wrapped.SlabLoadTransfer

    @property
    def SlabLoadTransferDirection(self) -> c_long:
        return self._wrapped.SlabLoadTransferDirection

    @property
    def MainDirectionTop(self) -> c_long:
        return self._wrapped.MainDirectionTop

    @property
    def MainDirectionBottom(self) -> c_long:
        return self._wrapped.MainDirectionBottom

    @property
    def ct(self) -> c_double:
        return self._wrapped.ct

    @property
    def cb(self) -> c_double:
        return self._wrapped.cb

    @property
    def AggregateSize(self) -> c_double:
        return self._wrapped.AggregateSize

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def EnvClass_T(self) -> c_long:
        return self._wrapped.EnvClass_T

    @property
    def EnvClass_B(self) -> c_long:
        return self._wrapped.EnvClass_B

    @property
    def ShearReinforcementAngle(self) -> c_double:
        return self._wrapped.ShearReinforcementAngle

    @property
    def ShearCrackAngle(self) -> c_double:
        return self._wrapped.ShearCrackAngle


class RColumnStirrupSpacing(Wrapper):

    @property
    def ss_bottom(self) -> c_double:
        return self._wrapped.ss_bottom

    @property
    def ss_middle(self) -> c_double:
        return self._wrapped.ss_middle

    @property
    def ss_top(self) -> c_double:
        return self._wrapped.ss_top


class RReinforcementParameters_MSZ(Wrapper):

    @property
    def UnfavorableEccentricity_Npos(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Npos

    @property
    def UnfavorableEccentricity_Nneg(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Nneg

    @property
    def AutoPsi(self) -> c_long:
        return self._wrapped.AutoPsi

    @property
    def RebarPos(self) -> 'RRebarPos':
        return self._wrapped.RebarPos


class RRCBeamDesignParameters_DIN(Wrapper):

    @property
    def EnvironmentClass(self) -> c_long:
        return self._wrapped.EnvironmentClass

    @property
    def Deflection_Beam_L_div(self) -> c_double:
        return self._wrapped.Deflection_Beam_L_div

    @property
    def Deflection_Cantilever_L_div(self) -> c_double:
        return self._wrapped.Deflection_Cantilever_L_div

    @property
    def VariableAngleTrussMethod(self) -> c_long:
        return self._wrapped.VariableAngleTrussMethod

    @property
    def Theta(self) -> c_double:
        return self._wrapped.Theta

    @property
    def CrackWidthCheck(self) -> c_long:
        return self._wrapped.CrackWidthCheck

    @property
    def MaxCrackWidth_Top(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Top

    @property
    def MaxCrackWidth_Bottom(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Bottom

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength


class RColumnStirrupDiameters(Wrapper):

    @property
    def sd_bottom(self) -> c_double:
        return self._wrapped.sd_bottom

    @property
    def sd_middle(self) -> c_double:
        return self._wrapped.sd_middle

    @property
    def sd_top(self) -> c_double:
        return self._wrapped.sd_top


class RReinforcementParameters_EC(Wrapper):

    @property
    def dxt(self) -> c_double:
        return self._wrapped.dxt

    @property
    def dxb(self) -> c_double:
        return self._wrapped.dxb

    @property
    def dyt(self) -> c_double:
        return self._wrapped.dyt

    @property
    def dyb(self) -> c_double:
        return self._wrapped.dyb

    @property
    def SlabLoadTransfer(self) -> c_long:
        return self._wrapped.SlabLoadTransfer

    @property
    def SlabLoadTransferDirection(self) -> c_long:
        return self._wrapped.SlabLoadTransferDirection

    @property
    def MainDirectionTop(self) -> c_long:
        return self._wrapped.MainDirectionTop

    @property
    def MainDirectionBottom(self) -> c_long:
        return self._wrapped.MainDirectionBottom

    @property
    def ct(self) -> c_double:
        return self._wrapped.ct

    @property
    def cb(self) -> c_double:
        return self._wrapped.cb

    @property
    def AggregateSize(self) -> c_double:
        return self._wrapped.AggregateSize

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def StructClass(self) -> c_long:
        return self._wrapped.StructClass

    @property
    def EnvClass_T(self) -> c_long:
        return self._wrapped.EnvClass_T

    @property
    def EnvClass_B(self) -> c_long:
        return self._wrapped.EnvClass_B

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def UnfavorableEccentricity_Npos(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Npos

    @property
    def UnfavorableEccentricity_Nneg(self) -> c_double:
        return self._wrapped.UnfavorableEccentricity_Nneg

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def ShortTerm(self) -> c_long:
        return self._wrapped.ShortTerm

    @property
    def ShearReinforcementAngle(self) -> c_double:
        return self._wrapped.ShearReinforcementAngle

    @property
    def ShearCrackAngle(self) -> c_double:
        return self._wrapped.ShearCrackAngle

    @property
    def TakeConcTensileStrengthNL(self) -> c_long:
        return self._wrapped.TakeConcTensileStrengthNL

    @property
    def UseFctmfl(self) -> c_long:
        return self._wrapped.UseFctmfl

    @property
    def ShrinkageEps(self) -> c_double:
        return self._wrapped.ShrinkageEps

    @property
    def RCNonlinearSurfType(self) -> c_long:
        return self._wrapped.RCNonlinearSurfType

    @property
    def ReinforcementType(self) -> c_long:
        return self._wrapped.ReinforcementType

    @property
    def AlphaAngle(self) -> c_double:
        return self._wrapped.AlphaAngle

    @property
    def BetaAngle(self) -> c_double:
        return self._wrapped.BetaAngle

    @property
    def CalcFromLimitingCrackWidth(self) -> c_long:
        return self._wrapped.CalcFromLimitingCrackWidth

    @property
    def wk_b(self) -> c_double:
        return self._wrapped.wk_b

    @property
    def wk2_b(self) -> c_double:
        return self._wrapped.wk2_b

    @property
    def wk_t(self) -> c_double:
        return self._wrapped.wk_t

    @property
    def wk2_t(self) -> c_double:
        return self._wrapped.wk2_t

    @property
    def ApproximateLevelArm(self) -> c_long:
        return self._wrapped.ApproximateLevelArm

    @property
    def SeelhoferMartiEquation(self) -> c_long:
        return self._wrapped.SeelhoferMartiEquation

    @property
    def TrapSheetOnlyFormWork(self) -> c_long:
        return self._wrapped.TrapSheetOnlyFormWork

    @property
    def TrapSheetOneLayerReinf(self) -> c_long:
        return self._wrapped.TrapSheetOneLayerReinf

    @property
    def TrapSheetConsidered(self) -> c_long:
        return self._wrapped.TrapSheetConsidered


class RReinforcementParameters_NEN(Wrapper):

    @property
    def AggregateSize(self) -> c_double:
        return self._wrapped.AggregateSize

    @property
    def EnvClass_T(self) -> c_long:
        return self._wrapped.EnvClass_T

    @property
    def SurfaceCheck_T(self) -> c_long:
        return self._wrapped.SurfaceCheck_T

    @property
    def ReductionOf5mm_T(self) -> c_long:
        return self._wrapped.ReductionOf5mm_T

    @property
    def CrackControl_T(self) -> c_long:
        return self._wrapped.CrackControl_T

    @property
    def EnvClass_B(self) -> c_long:
        return self._wrapped.EnvClass_B

    @property
    def SurfaceCheck_B(self) -> c_long:
        return self._wrapped.SurfaceCheck_B

    @property
    def ReductionOf5mm_B(self) -> c_long:
        return self._wrapped.ReductionOf5mm_B

    @property
    def CrackControl_B(self) -> c_long:
        return self._wrapped.CrackControl_B

    @property
    def MainDirectionTop(self) -> c_long:
        return self._wrapped.MainDirectionTop

    @property
    def MainDirectionBottom(self) -> c_long:
        return self._wrapped.MainDirectionBottom

    @property
    def ct(self) -> c_double:
        return self._wrapped.ct

    @property
    def cb(self) -> c_double:
        return self._wrapped.cb

    @property
    def ApplyMinimumCover(self) -> c_long:
        return self._wrapped.ApplyMinimumCover

    @property
    def dxt(self) -> c_double:
        return self._wrapped.dxt

    @property
    def dxb(self) -> c_double:
        return self._wrapped.dxb

    @property
    def dyt(self) -> c_double:
        return self._wrapped.dyt

    @property
    def dyb(self) -> c_double:
        return self._wrapped.dyb


class RRCBeamDesignParameters_EC_RO(Wrapper):

    @property
    def Ksi0_RO(self) -> c_double:
        return self._wrapped.Ksi0_RO

    @property
    def SeismicZone(self) -> c_long:
        return self._wrapped.SeismicZone

    @property
    def fse(self) -> c_double:
        return self._wrapped.fse

    @property
    def VariableAngleTrussMethod(self) -> c_long:
        return self._wrapped.VariableAngleTrussMethod

    @property
    def Theta(self) -> c_double:
        return self._wrapped.Theta

    @property
    def Deflection_Beam_L_div(self) -> c_double:
        return self._wrapped.Deflection_Beam_L_div

    @property
    def Deflection_Cantilever_L_div(self) -> c_double:
        return self._wrapped.Deflection_Cantilever_L_div

    @property
    def CrackWidthCheck(self) -> c_long:
        return self._wrapped.CrackWidthCheck

    @property
    def MaxCrackWidth_Top(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Top

    @property
    def MaxCrackWidth_Bottom(self) -> c_double:
        return self._wrapped.MaxCrackWidth_Bottom

    @property
    def TakeConcTensileStrength(self) -> c_long:
        return self._wrapped.TakeConcTensileStrength

    @property
    def ShortTerm(self) -> c_long:
        return self._wrapped.ShortTerm

    @property
    def PlasticHinges(self) -> 'RRCBeamPlasticHinges':
        return self._wrapped.PlasticHinges


class RRCColumnCapacityDesignParams(Wrapper):

    @property
    def PlasticHinges(self) -> c_long:
        return self._wrapped.PlasticHinges

    @property
    def DuctilityClass(self) -> c_long:
        return self._wrapped.DuctilityClass

    @property
    def PlasticHingeYY_Top(self) -> c_long:
        return self._wrapped.PlasticHingeYY_Top

    @property
    def PlasticHingeYY_Bottom(self) -> c_long:
        return self._wrapped.PlasticHingeYY_Bottom

    @property
    def PlasticHingeZZ_Top(self) -> c_long:
        return self._wrapped.PlasticHingeZZ_Top

    @property
    def PlasticHingeZZ_Bottom(self) -> c_long:
        return self._wrapped.PlasticHingeZZ_Bottom

    @property
    def MRdB_MRdC_RatioYY_Top(self) -> c_double:
        return self._wrapped.MRdB_MRdC_RatioYY_Top

    @property
    def MRdB_MRdC_RatioYY_Bottom(self) -> c_double:
        return self._wrapped.MRdB_MRdC_RatioYY_Bottom

    @property
    def MRdB_MRdC_RatioZZ_Top(self) -> c_double:
        return self._wrapped.MRdB_MRdC_RatioZZ_Top

    @property
    def MRdB_MRdC_RatioZZ_Bottom(self) -> c_double:
        return self._wrapped.MRdB_MRdC_RatioZZ_Bottom

    @property
    def RelativeClearLengthYY(self) -> c_double:
        return self._wrapped.RelativeClearLengthYY

    @property
    def RelativeClearLengthZZ(self) -> c_double:
        return self._wrapped.RelativeClearLengthZZ

    @property
    def GammaRd(self) -> c_double:
        return self._wrapped.GammaRd


class RColumnStirrupZones(Wrapper):

    @property
    def sz_bottom(self) -> c_double:
        return self._wrapped.sz_bottom

    @property
    def sz_middle(self) -> c_double:
        return self._wrapped.sz_middle
