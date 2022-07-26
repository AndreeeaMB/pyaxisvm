# -*- coding: utf-8 -*-
from axisvm.com.core.wrap import AxWrapper
from ctypes import *
from .enum_16_1 import *
from .rec_16_1 import *


class AxisVMModel(AxWrapper):

    @property
    def Settings(self) -> 'AxisVMSettings':
        return self._wrapped.Settings

    @property
    def Materials(self) -> 'AxisVMMaterials':
        return self._wrapped.Materials

    @property
    def CrossSections(self) -> 'AxisVMCrossSections':
        return self._wrapped.CrossSections

    @property
    def References(self) -> 'AxisVMReferences':
        return self._wrapped.References

    @property
    def Nodes(self) -> 'AxisVMNodes':
        return self._wrapped.Nodes

    @property
    def Lines(self) -> 'AxisVMLines':
        return self._wrapped.Lines

    @property
    def NodalSupports(self) -> 'AxisVMNodalSupports':
        return self._wrapped.NodalSupports

    @property
    def LineSupports(self) -> 'AxisVMLineSupports':
        return self._wrapped.LineSupports

    @property
    def SurfaceSupports(self) -> 'AxisVMSurfaceSupports':
        return self._wrapped.SurfaceSupports

    @property
    def LoadCases(self) -> 'AxisVMLoadCases':
        return self._wrapped.LoadCases

    def SaveToFile(self, *args, **kwargs):
        return self._wrapped.SaveToFile(*args, **kwargs)

    @property
    def LoadGroups(self) -> 'AxisVMLoadGroups':
        return self._wrapped.LoadGroups

    @property
    def LoadCombinations(self) -> 'AxisVMLoadCombinations':
        return self._wrapped.LoadCombinations

    @property
    def Loads(self) -> 'AxisVMLoads':
        return self._wrapped.Loads

    def LoadFromFile(self, *args, **kwargs):
        return self._wrapped.LoadFromFile(*args, **kwargs)

    @property
    def Domains(self) -> 'AxisVMDomains':
        return self._wrapped.Domains

    @property
    def Surfaces(self) -> 'AxisVMSurfaces':
        return self._wrapped.Surfaces

    @property
    def View(self) -> int:
        return self._wrapped.View

    @View.setter
    def View(self, Value: int):
        self._wrapped.View = Value

    @property
    def Display(self) -> int:
        return self._wrapped.Display

    @Display.setter
    def Display(self, Value: int):
        self._wrapped.Display = Value

    def FitInView(self, *args, **kwargs):
        return self._wrapped.FitInView(*args, **kwargs)

    @property
    def Calculation(self) -> 'AxisVMCalculation':
        return self._wrapped.Calculation

    @property
    def NeedsSaving(self) -> int:
        return self._wrapped.NeedsSaving

    @property
    def Results(self) -> 'AxisVMResults':
        return self._wrapped.Results

    def BeginUpdate(self, *args, **kwargs):
        return self._wrapped.BeginUpdate(*args, **kwargs)

    def EndUpdate(self, *args, **kwargs):
        return self._wrapped.EndUpdate(*args, **kwargs)

    @property
    def SelectionProcessing(self) -> int:
        return self._wrapped.SelectionProcessing

    @property
    def SelectionResult(self) -> int:
        return self._wrapped.SelectionResult

    def StartSelection(self, *args, **kwargs):
        return self._wrapped.StartSelection(*args, **kwargs)

    def ExportToIFC(self, *args, **kwargs):
        return self._wrapped.ExportToIFC(*args, **kwargs)

    def ExportToDXF(self, *args, **kwargs):
        return self._wrapped.ExportToDXF(*args, **kwargs)

    def ExportToPIA(self, *args, **kwargs):
        return self._wrapped.ExportToPIA(*args, **kwargs)

    @property
    def Members(self) -> 'AxisVMMembers':
        return self._wrapped.Members

    @property
    def SpectrumH(self) -> 'AxisVMSpectrum':
        return self._wrapped.SpectrumH

    @property
    def SpectrumV(self) -> 'AxisVMSpectrum':
        return self._wrapped.SpectrumV

    def GetSeismicParams(self, *args, **kwargs):
        return self._wrapped.GetSeismicParams(*args, **kwargs)

    def SetSeismicParams(self, *args, **kwargs):
        return self._wrapped.SetSeismicParams(*args, **kwargs)

    @property
    def SeismicStoreys(self) -> 'AxisVMSeismicStoreys':
        return self._wrapped.SeismicStoreys

    def UpdateFromPianoRev(self, *args, **kwargs):
        return self._wrapped.UpdateFromPianoRev(*args, **kwargs)

    @property
    def Modified(self) -> int:
        return self._wrapped.Modified

    def Refresh(self, *args, **kwargs):
        return self._wrapped.Refresh(*args, **kwargs)

    @property
    def FileName(self) -> str:
        return self._wrapped.FileName

    @property
    def LinkElements(self) -> 'AxisVMLinkElements':
        return self._wrapped.LinkElements

    @property
    def EdgeConnections(self) -> 'AxisVMEdgeConnections':
        return self._wrapped.EdgeConnections

    @property
    def SteelDesignMembers(self) -> 'AxisVMSteelDesignMembers':
        return self._wrapped.SteelDesignMembers

    @property
    def ActualReinforcement(self) -> 'AxisVMActualReinforcement':
        return self._wrapped.ActualReinforcement

    @property
    def Sections(self) -> 'AxisVMSections':
        return self._wrapped.Sections

    @property
    def DomainSupports(self) -> 'AxisVMDomainSupports':
        return self._wrapped.DomainSupports

    @property
    def Storeys(self) -> 'AxisVMStoreys':
        return self._wrapped.Storeys

    @property
    def TimberDesignMembers(self) -> 'AxisVMTimberDesignMembers':
        return self._wrapped.TimberDesignMembers

    @property
    def DynamicLoadFunctions(self) -> 'AxisVMDynamicLoadFunctions':
        return self._wrapped.DynamicLoadFunctions

    @property
    def TimeIncrementFunctions(self) -> 'AxisVMTimeIncrementFunctions':
        return self._wrapped.TimeIncrementFunctions

    @property
    def IncrementFunctions(self) -> 'AxisVMIncrementFunctions':
        return self._wrapped.IncrementFunctions

    @property
    def RigidBodies(self) -> 'AxisVMRigidBodies':
        return self._wrapped.RigidBodies

    @property
    def Diaphragm(self) -> 'AxisVMDiaphragm':
        return self._wrapped.Diaphragm

    @property
    def RebarSteelGrades(self) -> 'AxisVMRebarSteelGrades':
        return self._wrapped.RebarSteelGrades

    @property
    def MovingLoads(self) -> 'AxisVMMovingLoads':
        return self._wrapped.MovingLoads

    @property
    def ColumnRebars(self) -> 'AxisVMColumnRebars':
        return self._wrapped.ColumnRebars

    @property
    def RCBeamDesign(self) -> 'AxisVMRCBeamDesign':
        return self._wrapped.RCBeamDesign

    @property
    def RCColumnChecking(self) -> 'AxisVMRCColumnChecking':
        return self._wrapped.RCColumnChecking

    def SaveUndo(self, *args, **kwargs):
        return self._wrapped.SaveUndo(*args, **kwargs)

    def Undo(self, *args, **kwargs):
        return self._wrapped.Undo(*args, **kwargs)

    def Redo(self, *args, **kwargs):
        return self._wrapped.Redo(*args, **kwargs)

    @property
    def PushoverHingeFunctions(self) -> 'AxisVMPushoverHingeFunctions':
        return self._wrapped.PushoverHingeFunctions

    @property
    def ProjectName(self) -> str:
        return self._wrapped.ProjectName

    @ProjectName.setter
    def ProjectName(self, Value: str):
        self._wrapped.ProjectName = Value

    @property
    def AnalysisBy(self) -> str:
        return self._wrapped.AnalysisBy

    @AnalysisBy.setter
    def AnalysisBy(self, Value: str):
        self._wrapped.AnalysisBy = Value

    @property
    def Comment(self) -> str:
        return self._wrapped.Comment

    @Comment.setter
    def Comment(self, Value: str):
        self._wrapped.Comment = Value

    @property
    def CriticalGroupCombinations(self) -> 'AxisVMCriticalGroupCombinations':
        return self._wrapped.CriticalGroupCombinations

    @property
    def Envelopes(self) -> 'AxisVMEnvelopes':
        return self._wrapped.Envelopes

    @property
    def Windows(self) -> 'AxisVMWindows':
        return self._wrapped.Windows

    @property
    def CustomParts(self) -> 'AxisVMCustomParts':
        return self._wrapped.CustomParts

    @property
    def LogicalParts(self) -> 'AxisVMLogicalParts':
        return self._wrapped.LogicalParts

    @property
    def LoadPanels(self) -> 'AxisVMLoadPanels':
        return self._wrapped.LoadPanels

    @property
    def Workplanes(self) -> 'AxisVMWorkplanes':
        return self._wrapped.Workplanes

    def SetAPIGlobalData(self, *args, **kwargs):
        return self._wrapped.SetAPIGlobalData(*args, **kwargs)

    def GetAPIGlobalData(self, *args, **kwargs):
        return self._wrapped.GetAPIGlobalData(*args, **kwargs)

    def GetAPIGlobalDataSize(self, *args, **kwargs):
        return self._wrapped.GetAPIGlobalDataSize(*args, **kwargs)

    def DeleteAPIGlobalData(self, *args, **kwargs):
        return self._wrapped.DeleteAPIGlobalData(*args, **kwargs)

    def SetAPIGlobalData_vb(self, *args, **kwargs):
        return self._wrapped.SetAPIGlobalData_vb(*args, **kwargs)

    def ImportDXF(self, *args, **kwargs):
        return self._wrapped.ImportDXF(*args, **kwargs)

    def ImportPDF(self, *args, **kwargs):
        return self._wrapped.ImportPDF(*args, **kwargs)

    def GetIFCExportReinfParams(self, *args, **kwargs):
        return self._wrapped.GetIFCExportReinfParams(*args, **kwargs)

    def ImportIFC(self, *args, **kwargs):
        return self._wrapped.ImportIFC(*args, **kwargs)

    @property
    def CallProgress(self) -> int:
        return self._wrapped.CallProgress

    @CallProgress.setter
    def CallProgress(self, Value: int):
        self._wrapped.CallProgress = Value

    @property
    def SteelCrossSectionOptimization(
            self) -> 'AxisVMCrossSectionOptimization':
        return self._wrapped.SteelCrossSectionOptimization

    @property
    def SpectrumPushOver(self) -> 'AxisVMSpectrum':
        return self._wrapped.SpectrumPushOver

    @property
    def MathTexts(self) -> 'AxisVMMathTexts':
        return self._wrapped.MathTexts

    @property
    def TimberCrossSectionOptimization(
            self) -> 'AxisVMCrossSectionOptimization':
        return self._wrapped.TimberCrossSectionOptimization

    @property
    def Layers(self) -> 'AxisVMLayers':
        return self._wrapped.Layers

    @property
    def XLAMpanels(self) -> 'AxisVMXLAMpanels':
        return self._wrapped.XLAMpanels

    @property
    def DrawingsLibrary(self) -> 'AxisVMDrawingsLibrary':
        return self._wrapped.DrawingsLibrary

    @property
    def Reports(self) -> 'AxisVMReports':
        return self._wrapped.Reports

    def SaveModelBeforeClose(self, *args, **kwargs):
        return self._wrapped.SaveModelBeforeClose(*args, **kwargs)

    def GetCompanyLogoParameters(self, *args, **kwargs):
        return self._wrapped.GetCompanyLogoParameters(*args, **kwargs)

    def SetCompanyLogoParameters(self, *args, **kwargs):
        return self._wrapped.SetCompanyLogoParameters(*args, **kwargs)

    @property
    def StructuralGrids(self) -> 'AxisVMStructuralGrids':
        return self._wrapped.StructuralGrids

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    @property
    def Dimensions(self) -> 'AxisVMDimensions':
        return self._wrapped.Dimensions

    def StartModalSelection(self, *args, **kwargs):
        return self._wrapped.StartModalSelection(*args, **kwargs)

    def ImportRAE(self, *args, **kwargs):
        return self._wrapped.ImportRAE(*args, **kwargs)

    @property
    def VirtualBeams(self) -> 'AxisVMVirtualBeams':
        return self._wrapped.VirtualBeams

    @property
    def Task(self) -> 'AxisVMTask':
        return self._wrapped.Task

    def ImportAXS(self, *args, **kwargs):
        return self._wrapped.ImportAXS(*args, **kwargs)

    @property
    def NodesSupports(self) -> 'AxisVMNodesSupports':
        return self._wrapped.NodesSupports

    @property
    def MembersSupports(self) -> 'AxisVMMembersSupports':
        return self._wrapped.MembersSupports

    @property
    def DomainsSupports(self) -> 'AxisVMDomainsSupports':
        return self._wrapped.DomainsSupports

    @property
    def SpringParams(self) -> 'AxisVMSpringParams':
        return self._wrapped.SpringParams

    @property
    def WindLoad(self) -> 'AxisVMWindLoad':
        return self._wrapped.WindLoad


class AxisVMRigidBodies(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DefineSelectedLinesAsRigidBody(self, *args, **kwargs):
        return self._wrapped.DefineSelectedLinesAsRigidBody(*args, **kwargs)

    def AddSelectedLines(self, *args, **kwargs):
        return self._wrapped.AddSelectedLines(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def GetLines(self, *args, **kwargs):
        return self._wrapped.GetLines(*args, **kwargs)

    def RemoveLinesFromRigidBodies(self, *args, **kwargs):
        return self._wrapped.RemoveLinesFromRigidBodies(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def RemoveLinesFromRigidBodies_vb(self, *args, **kwargs):
        return self._wrapped.RemoveLinesFromRigidBodies_vb(*args, **kwargs)


class AxisVMNodalSupport(AxWrapper):

    @property
    def SupportType(self) -> int:
        return self._wrapped.SupportType

    @property
    def NodeId(self) -> int:
        return self._wrapped.NodeId

    @property
    def BeamId(self) -> int:
        return self._wrapped.BeamId

    @property
    def LineId(self) -> int:
        return self._wrapped.LineId

    @property
    def ReferenceId(self) -> int:
        return self._wrapped.ReferenceId

    def DefineAsNodalGlobal(self, *args, **kwargs):
        return self._wrapped.DefineAsNodalGlobal(*args, **kwargs)

    def DefineAsNodalBeamRelative(self, *args, **kwargs):
        return self._wrapped.DefineAsNodalBeamRelative(*args, **kwargs)

    def DefineAsNodalEdgeRelative(self, *args, **kwargs):
        return self._wrapped.DefineAsNodalEdgeRelative(*args, **kwargs)

    def DefineAsNodalReference(self, *args, **kwargs):
        return self._wrapped.DefineAsNodalReference(*args, **kwargs)

    @property
    def DomainId1(self) -> int:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> int:
        return self._wrapped.DomainId2

    @property
    def SurfaceId1(self) -> int:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> int:
        return self._wrapped.SurfaceId2

    def GetStiffnesses(self, *args, **kwargs):
        return self._wrapped.GetStiffnesses(*args, **kwargs)

    def SetStiffnesses(self, *args, **kwargs):
        return self._wrapped.SetStiffnesses(*args, **kwargs)

    def GetNonLinearity(self, *args, **kwargs):
        return self._wrapped.GetNonLinearity(*args, **kwargs)

    def SetNonLinearity(self, *args, **kwargs):
        return self._wrapped.SetNonLinearity(*args, **kwargs)

    def GetResistances(self, *args, **kwargs):
        return self._wrapped.GetResistances(*args, **kwargs)

    def SetResistances(self, *args, **kwargs):
        return self._wrapped.SetResistances(*args, **kwargs)

    def GetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.GetStiffnessCalcParams(*args, **kwargs)

    def SetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.SetStiffnessCalcParams(*args, **kwargs)

    @property
    def HasFooting(self) -> int:
        return self._wrapped.HasFooting

    @property
    def FootingType(self) -> int:
        return self._wrapped.FootingType

    def GetFootingDimensions(self, *args, **kwargs):
        return self._wrapped.GetFootingDimensions(*args, **kwargs)

    def GetFootingParams(self, *args, **kwargs):
        return self._wrapped.GetFootingParams(*args, **kwargs)

    def GetFootingParams_V153(self, *args, **kwargs):
        return self._wrapped.GetFootingParams_V153(*args, **kwargs)

    @property
    def SpringParams(self) -> 'RNodalSupportSpringParams':
        return self._wrapped.SpringParams

    @SpringParams.setter
    def SpringParams(self, Value: 'RNodalSupportSpringParams'):
        self._wrapped.SpringParams = Value


class AxisVMMember(AxWrapper):

    def GetLines(self, *args, **kwargs):
        return self._wrapped.GetLines(*args, **kwargs)

    @property
    def MemberType(self) -> int:
        return self._wrapped.MemberType

    def DefineAsBeam(self, *args, **kwargs):
        return self._wrapped.DefineAsBeam(*args, **kwargs)

    def DefineAsRib(self, *args, **kwargs):
        return self._wrapped.DefineAsRib(*args, **kwargs)

    @property
    def Length(self) -> float:
        return self._wrapped.Length

    def GetStartReleases(self, *args, **kwargs):
        return self._wrapped.GetStartReleases(*args, **kwargs)

    def SetStartReleases(self, *args, **kwargs):
        return self._wrapped.SetStartReleases(*args, **kwargs)

    def GetEndReleases(self, *args, **kwargs):
        return self._wrapped.GetEndReleases(*args, **kwargs)

    def SetEndReleases(self, *args, **kwargs):
        return self._wrapped.SetEndReleases(*args, **kwargs)

    def GetGeomData(self, *args, **kwargs):
        return self._wrapped.GetGeomData(*args, **kwargs)

    def GetBeamData(self, *args, **kwargs):
        return self._wrapped.GetBeamData(*args, **kwargs)

    def GetRibData(self, *args, **kwargs):
        return self._wrapped.GetRibData(*args, **kwargs)

    def ChangeLocalDirection(self, *args, **kwargs):
        return self._wrapped.ChangeLocalDirection(*args, **kwargs)

    @property
    def Timber_kdef(self) -> float:
        return self._wrapped.Timber_kdef

    @Timber_kdef.setter
    def Timber_kdef(self, Value: float):
        self._wrapped.Timber_kdef = Value

    @property
    def Timber_ServiceClass(self) -> int:
        return self._wrapped.Timber_ServiceClass

    @Timber_ServiceClass.setter
    def Timber_ServiceClass(self, Value: int):
        self._wrapped.Timber_ServiceClass = Value

    def DefineAsTimberBeam(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberBeam(*args, **kwargs)

    def DefineAsTimberRib(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberRib(*args, **kwargs)

    def GetTimberBeamData(self, *args, **kwargs):
        return self._wrapped.GetTimberBeamData(*args, **kwargs)

    def GetTimberRibData(self, *args, **kwargs):
        return self._wrapped.GetTimberRibData(*args, **kwargs)

    def DefineAsRibWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.DefineAsRibWithAutoExcentricity(*args, **kwargs)

    def DefineAsTimberRibWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberRibWithAutoExcentricity(
            *args, **kwargs)

    def GetRibDataWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.GetRibDataWithAutoExcentricity(*args, **kwargs)

    def GetTimberRibDataWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.GetTimberRibDataWithAutoExcentricity(
            *args, **kwargs)

    def GetMeshParameters(self, *args, **kwargs):
        return self._wrapped.GetMeshParameters(*args, **kwargs)

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    @property
    def Weight(self) -> float:
        return self._wrapped.Weight

    @property
    def Volume(self) -> float:
        return self._wrapped.Volume

    @property
    def MeshExists(self) -> int:
        return self._wrapped.MeshExists

    @property
    def IsBeam(self) -> int:
        return self._wrapped.IsBeam

    @property
    def IsColumn(self) -> int:
        return self._wrapped.IsColumn

    @property
    def IsOtherType(self) -> int:
        return self._wrapped.IsOtherType

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @property
    def StoreyId(self) -> int:
        return self._wrapped.StoreyId

    def DeleteMesh(self, *args, **kwargs):
        return self._wrapped.DeleteMesh(*args, **kwargs)

    def GenerateMeshWithParams(self, *args, **kwargs):
        return self._wrapped.GenerateMeshWithParams(*args, **kwargs)

    def CreateMeshWithCoordinates(self, *args, **kwargs):
        return self._wrapped.CreateMeshWithCoordinates(*args, **kwargs)

    @property
    def StartNode(self) -> int:
        return self._wrapped.StartNode

    @property
    def EndNode(self) -> int:
        return self._wrapped.EndNode

    @property
    def ColumnReinforcementParametersExists(self) -> int:
        return self._wrapped.ColumnReinforcementParametersExists

    def DeleteColumnReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.DeleteColumnReinforcementParameters(
            *args, **kwargs)

    def GetColumnReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.GetColumnReinforcementParameters(*args, **kwargs)

    def SetColumnReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.SetColumnReinforcementParameters(*args, **kwargs)

    @property
    def MaterialColour(self) -> c_ulong:
        return self._wrapped.MaterialColour

    @MaterialColour.setter
    def MaterialColour(self, Value: c_ulong):
        self._wrapped.MaterialColour = Value

    @property
    def ContourColour(self) -> c_ulong:
        return self._wrapped.ContourColour

    @ContourColour.setter
    def ContourColour(self, Value: c_ulong):
        self._wrapped.ContourColour = Value

    @property
    def ArchitectElemType(self) -> int:
        return self._wrapped.ArchitectElemType

    @ArchitectElemType.setter
    def ArchitectElemType(self, Value: int):
        self._wrapped.ArchitectElemType = Value

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def CreateMeshWithCoordinates_vb(self, *args, **kwargs):
        return self._wrapped.CreateMeshWithCoordinates_vb(*args, **kwargs)

    @property
    def MaterialColour_vb(self) -> int:
        return self._wrapped.MaterialColour_vb

    @MaterialColour_vb.setter
    def MaterialColour_vb(self, Value: int):
        self._wrapped.MaterialColour_vb = Value

    @property
    def ContourColour_vb(self) -> int:
        return self._wrapped.ContourColour_vb

    @ContourColour_vb.setter
    def ContourColour_vb(self, Value: int):
        self._wrapped.ContourColour_vb = Value

    def DefineAsTruss(self, *args, **kwargs):
        return self._wrapped.DefineAsTruss(*args, **kwargs)

    def GetTrussData(self, *args, **kwargs):
        return self._wrapped.GetTrussData(*args, **kwargs)

    def DefineAsTimberTruss(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberTruss(*args, **kwargs)

    def GetTimberTrussData(self, *args, **kwargs):
        return self._wrapped.GetTimberTrussData(*args, **kwargs)

    @property
    def StiffnessReduction_A(self) -> float:
        return self._wrapped.StiffnessReduction_A

    @StiffnessReduction_A.setter
    def StiffnessReduction_A(self, Value: float):
        self._wrapped.StiffnessReduction_A = Value

    @property
    def StiffnessReduction_I(self) -> float:
        return self._wrapped.StiffnessReduction_I

    @StiffnessReduction_I.setter
    def StiffnessReduction_I(self, Value: float):
        self._wrapped.StiffnessReduction_I = Value

    def DeleteLineElement(self, *args, **kwargs):
        return self._wrapped.DeleteLineElement(*args, **kwargs)

    def GetLinesLocX(self, *args, **kwargs):
        return self._wrapped.GetLinesLocX(*args, **kwargs)

    @property
    def SectionsCount(self) -> int:
        return self._wrapped.SectionsCount

    def GetXofMemberSectionID(self, *args, **kwargs):
        return self._wrapped.GetXofMemberSectionID(*args, **kwargs)

    def GetLineIDAndLineSectionID(self, *args, **kwargs):
        return self._wrapped.GetLineIDAndLineSectionID(*args, **kwargs)

    @property
    def StiffnessReduction(self) -> int:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: int):
        self._wrapped.StiffnessReduction = Value

    def ClearEccentricity(self, *args, **kwargs):
        return self._wrapped.ClearEccentricity(*args, **kwargs)


class AxisVMAttributes(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def AddDefault(self, *args, **kwargs):
        return self._wrapped.AddDefault(*args, **kwargs)

    def GetSizeByName(self, *args, **kwargs):
        return self._wrapped.GetSizeByName(*args, **kwargs)

    def GetSizeByIndex(self, *args, **kwargs):
        return self._wrapped.GetSizeByIndex(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def GetItemByName(self, *args, **kwargs):
        return self._wrapped.GetItemByName(*args, **kwargs)

    def GetItemByIndex(self, *args, **kwargs):
        return self._wrapped.GetItemByIndex(*args, **kwargs)

    def GetName(self, *args, **kwargs):
        return self._wrapped.GetName(*args, **kwargs)

    def DeleteByName(self, *args, **kwargs):
        return self._wrapped.DeleteByName(*args, **kwargs)

    def DeleteByIndex(self, *args, **kwargs):
        return self._wrapped.DeleteByIndex(*args, **kwargs)

    def FillItemByName(self, *args, **kwargs):
        return self._wrapped.FillItemByName(*args, **kwargs)

    def FillItemByIndex(self, *args, **kwargs):
        return self._wrapped.FillItemByIndex(*args, **kwargs)

    def FillAllItemsByName(self, *args, **kwargs):
        return self._wrapped.FillAllItemsByName(*args, **kwargs)

    def FillAllItemsByIndex(self, *args, **kwargs):
        return self._wrapped.FillAllItemsByIndex(*args, **kwargs)

    def FillItemsByName(self, *args, **kwargs):
        return self._wrapped.FillItemsByName(*args, **kwargs)

    def FillItemsByIndex(self, *args, **kwargs):
        return self._wrapped.FillItemsByIndex(*args, **kwargs)

    def SetAllItemsByName(self, *args, **kwargs):
        return self._wrapped.SetAllItemsByName(*args, **kwargs)

    def SetAllItemsByIndex(self, *args, **kwargs):
        return self._wrapped.SetAllItemsByIndex(*args, **kwargs)

    def IsDefaultItemByIndex(self, *args, **kwargs):
        return self._wrapped.IsDefaultItemByIndex(*args, **kwargs)

    def IsDefaultItemByName(self, *args, **kwargs):
        return self._wrapped.IsDefaultItemByName(*args, **kwargs)

    def GetDefault(self, *args, **kwargs):
        return self._wrapped.GetDefault(*args, **kwargs)

    @property
    def InheritCopiedElements(self) -> int:
        return self._wrapped.InheritCopiedElements

    @InheritCopiedElements.setter
    def InheritCopiedElements(self, Value: int):
        self._wrapped.InheritCopiedElements = Value

    @property
    def InheritDividedElements(self) -> int:
        return self._wrapped.InheritDividedElements

    @InheritDividedElements.setter
    def InheritDividedElements(self, Value: int):
        self._wrapped.InheritDividedElements = Value

    def AddDefault_vb(self, *args, **kwargs):
        return self._wrapped.AddDefault_vb(*args, **kwargs)

    def FillItemByName_vb(self, *args, **kwargs):
        return self._wrapped.FillItemByName_vb(*args, **kwargs)

    def FillItemByIndex_vb(self, *args, **kwargs):
        return self._wrapped.FillItemByIndex_vb(*args, **kwargs)

    def FillAllItemsByName_vb(self, *args, **kwargs):
        return self._wrapped.FillAllItemsByName_vb(*args, **kwargs)

    def FillAllItemsByIndex_vb(self, *args, **kwargs):
        return self._wrapped.FillAllItemsByIndex_vb(*args, **kwargs)

    def FillItemsByName_vb(self, *args, **kwargs):
        return self._wrapped.FillItemsByName_vb(*args, **kwargs)

    def FillItemsByIndex_vb(self, *args, **kwargs):
        return self._wrapped.FillItemsByIndex_vb(*args, **kwargs)

    def SetAllItemsByName_vb(self, *args, **kwargs):
        return self._wrapped.SetAllItemsByName_vb(*args, **kwargs)

    def SetAllItemsByIndex_vb(self, *args, **kwargs):
        return self._wrapped.SetAllItemsByIndex_vb(*args, **kwargs)


class AxisVMAttachments(AxWrapper):

    def AddData(self, *args, **kwargs):
        return self._wrapped.AddData(*args, **kwargs)

    def AddData_vb(self, *args, **kwargs):
        return self._wrapped.AddData_vb(*args, **kwargs)

    def GetData(self, *args, **kwargs):
        return self._wrapped.GetData(*args, **kwargs)

    def GetSize(self, *args, **kwargs):
        return self._wrapped.GetSize(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def ItemCount(self) -> int:
        return self._wrapped.ItemCount

    def GetIndexesByName(self, *args, **kwargs):
        return self._wrapped.GetIndexesByName(*args, **kwargs)


class AxisVMLines(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def AddWithXYZ(self, *args, **kwargs):
        return self._wrapped.AddWithXYZ(*args, **kwargs)

    def AddWithXYZDOF(self, *args, **kwargs):
        return self._wrapped.AddWithXYZDOF(*args, **kwargs)

    def DefineSelectedLinesAsRigidBody(self, *args, **kwargs):
        return self._wrapped.DefineSelectedLinesAsRigidBody(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    @property
    def RigidBodyCount(self) -> int:
        return self._wrapped.RigidBodyCount

    def IndexOf2(self, *args, **kwargs):
        return self._wrapped.IndexOf2(*args, **kwargs)

    @property
    def MidPointId(self) -> int:
        return self._wrapped.MidPointId

    @property
    def SectionCount(self) -> int:
        return self._wrapped.SectionCount

    @property
    def MidPointDOF(self) -> int:
        return self._wrapped.MidPointDOF

    @MidPointDOF.setter
    def MidPointDOF(self, Value: int):
        self._wrapped.MidPointDOF = Value

    def GetMidPoint(self, *args, **kwargs):
        return self._wrapped.GetMidPoint(*args, **kwargs)

    def CrossLines(self, *args, **kwargs):
        return self._wrapped.CrossLines(*args, **kwargs)

    def ChangeLocalDirection(self, *args, **kwargs):
        return self._wrapped.ChangeLocalDirection(*args, **kwargs)

    @property
    def MidPointCount(self) -> int:
        return self._wrapped.MidPointCount

    @property
    def LineByMidPoint(self) -> int:
        return self._wrapped.LineByMidPoint

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def SelectAllColumns(self, *args, **kwargs):
        return self._wrapped.SelectAllColumns(*args, **kwargs)

    def SelectAllBeams(self, *args, **kwargs):
        return self._wrapped.SelectAllBeams(*args, **kwargs)

    def SelectAllOthers(self, *args, **kwargs):
        return self._wrapped.SelectAllOthers(*args, **kwargs)

    def SelectAllColumnsAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllColumnsAtStorey(*args, **kwargs)

    def SelectAllBeamsAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllBeamsAtStorey(*args, **kwargs)

    def SelectAllOthersAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllOthersAtStorey(*args, **kwargs)

    def GetSelectedColumnIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedColumnIds(*args, **kwargs)

    def GetSelectedBeamIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedBeamIds(*args, **kwargs)

    def GetSelectedOtherIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedOtherIds(*args, **kwargs)

    def RenameSelectedTrusses(self, *args, **kwargs):
        return self._wrapped.RenameSelectedTrusses(*args, **kwargs)

    def DeleteNameOfAllTrusses(self, *args, **kwargs):
        return self._wrapped.DeleteNameOfAllTrusses(*args, **kwargs)

    def CrossLines_vb(self, *args, **kwargs):
        return self._wrapped.CrossLines_vb(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def StiffnessReduction_A(self) -> int:
        return self._wrapped.StiffnessReduction_A

    @StiffnessReduction_A.setter
    def StiffnessReduction_A(self, Value: int):
        self._wrapped.StiffnessReduction_A = Value

    @property
    def StiffnessReduction_I(self) -> int:
        return self._wrapped.StiffnessReduction_I

    @StiffnessReduction_I.setter
    def StiffnessReduction_I(self, Value: int):
        self._wrapped.StiffnessReduction_I = Value

    @property
    def Attributes(self) -> 'AxisVMAttributes':
        return self._wrapped.Attributes

    @property
    def Attachments(self) -> 'AxisVMAttachments':
        return self._wrapped.Attachments

    @property
    def LocalX_is_ij(self) -> int:
        return self._wrapped.LocalX_is_ij

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    def IndexOfFiniteElementNumber(self, *args, **kwargs):
        return self._wrapped.IndexOfFiniteElementNumber(*args, **kwargs)

    def GetFiniteElementCount(self, *args, **kwargs):
        return self._wrapped.GetFiniteElementCount(*args, **kwargs)

    def GetContinuousLineIDs(self, *args, **kwargs):
        return self._wrapped.GetContinuousLineIDs(*args, **kwargs)

    def BulkGetLineData(self, *args, **kwargs):
        return self._wrapped.BulkGetLineData(*args, **kwargs)

    def BulkSetLineData(self, *args, **kwargs):
        return self._wrapped.BulkSetLineData(*args, **kwargs)

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)

    def BulkGetAttr(self, *args, **kwargs):
        return self._wrapped.BulkGetAttr(*args, **kwargs)

    def BulkSetAttr(self, *args, **kwargs):
        return self._wrapped.BulkSetAttr(*args, **kwargs)

    def BulkGetMemberIds(self, *args, **kwargs):
        return self._wrapped.BulkGetMemberIds(*args, **kwargs)

    def GetSurfaces(self, *args, **kwargs):
        return self._wrapped.GetSurfaces(*args, **kwargs)

    @property
    def StiffnessReduction(self) -> int:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: int):
        self._wrapped.StiffnessReduction = Value

    def BulkGetAttr_V161(self, *args, **kwargs):
        return self._wrapped.BulkGetAttr_V161(*args, **kwargs)

    def BulkSetAttr_V161(self, *args, **kwargs):
        return self._wrapped.BulkSetAttr_V161(*args, **kwargs)


class AxisVMDrawingsLibrary(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    def AddWindow(self, *args, **kwargs):
        return self._wrapped.AddWindow(*args, **kwargs)

    def AddWindows(self, *args, **kwargs):
        return self._wrapped.AddWindows(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DisplayDrawing(self, *args, **kwargs):
        return self._wrapped.DisplayDrawing(*args, **kwargs)


class AxisVMSurface(AxWrapper):

    @property
    def ContourLines(self) -> int:
        return self._wrapped.ContourLines

    @property
    def Weight(self) -> float:
        return self._wrapped.Weight

    @property
    def Volume(self) -> float:
        return self._wrapped.Volume

    @property
    def Area(self) -> float:
        return self._wrapped.Area

    def Modify(self, *args, **kwargs):
        return self._wrapped.Modify(*args, **kwargs)

    @property
    def DomainId(self) -> int:
        return self._wrapped.DomainId

    @DomainId.setter
    def DomainId(self, Value: int):
        self._wrapped.DomainId = Value

    @property
    def PointCount(self) -> int:
        return self._wrapped.PointCount

    def GetContourPoints(self, *args, **kwargs):
        return self._wrapped.GetContourPoints(*args, **kwargs)

    def GetMidPoints(self, *args, **kwargs):
        return self._wrapped.GetMidPoints(*args, **kwargs)

    def GetSurfaceAttr(self, *args, **kwargs):
        return self._wrapped.GetSurfaceAttr(*args, **kwargs)

    def SetSurfaceAttr(self, *args, **kwargs):
        return self._wrapped.SetSurfaceAttr(*args, **kwargs)

    def GetNormalVector(self, *args, **kwargs):
        return self._wrapped.GetNormalVector(*args, **kwargs)

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    def SetContourLines(self, *args, **kwargs):
        return self._wrapped.SetContourLines(*args, **kwargs)

    @property
    def ReinforcementParametersExists(self) -> int:
        return self._wrapped.ReinforcementParametersExists

    def DeleteReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.DeleteReinforcementParameters(*args, **kwargs)

    def GetReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.GetReinforcementParameters(*args, **kwargs)

    def SetReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.SetReinforcementParameters(*args, **kwargs)

    @property
    def MaterialColour(self) -> c_ulong:
        return self._wrapped.MaterialColour

    @MaterialColour.setter
    def MaterialColour(self, Value: c_ulong):
        self._wrapped.MaterialColour = Value

    @property
    def ContourColour(self) -> c_ulong:
        return self._wrapped.ContourColour

    @ContourColour.setter
    def ContourColour(self, Value: c_ulong):
        self._wrapped.ContourColour = Value

    @property
    def ArchitectElemType(self) -> int:
        return self._wrapped.ArchitectElemType

    @ArchitectElemType.setter
    def ArchitectElemType(self, Value: int):
        self._wrapped.ArchitectElemType = Value

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def Modify_vb(self, *args, **kwargs):
        return self._wrapped.Modify_vb(*args, **kwargs)

    def SetContourLines_vb(self, *args, **kwargs):
        return self._wrapped.SetContourLines_vb(*args, **kwargs)

    @property
    def MaterialColour_vb(self) -> int:
        return self._wrapped.MaterialColour_vb

    @MaterialColour_vb.setter
    def MaterialColour_vb(self, Value: int):
        self._wrapped.MaterialColour_vb = Value

    @property
    def ContourColour_vb(self) -> int:
        return self._wrapped.ContourColour_vb

    @ContourColour_vb.setter
    def ContourColour_vb(self, Value: int):
        self._wrapped.ContourColour_vb = Value

    @property
    def StiffnessReduction(self) -> float:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: float):
        self._wrapped.StiffnessReduction = Value

    def SetReinforcementParameters_vb(self, *args, **kwargs):
        return self._wrapped.SetReinforcementParameters_vb(*args, **kwargs)

    def GetVariableThickness(self, *args, **kwargs):
        return self._wrapped.GetVariableThickness(*args, **kwargs)

    def GetSurfaceStiffnessFactors(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStiffnessFactors(*args, **kwargs)

    def SetSurfaceStiffnessFactors(self, *args, **kwargs):
        return self._wrapped.SetSurfaceStiffnessFactors(*args, **kwargs)

    @property
    def StiffnessReduction_V153(self) -> int:
        return self._wrapped.StiffnessReduction_V153

    @StiffnessReduction_V153.setter
    def StiffnessReduction_V153(self, Value: int):
        self._wrapped.StiffnessReduction_V153 = Value


class AxisVMSpringParams(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def IndexOfName(self, *args, **kwargs):
        return self._wrapped.IndexOfName(*args, **kwargs)

    def IndexOfUID(self, *args, **kwargs):
        return self._wrapped.IndexOfUID(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def MaxNameLength(self) -> int:
        return self._wrapped.MaxNameLength

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def Add_V161(self, *args, **kwargs):
        return self._wrapped.Add_V161(*args, **kwargs)


class AxisVMSections(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)

    def GetSegmentChainCount(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainCount(*args, **kwargs)

    def GetSegmentChainCoords(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainCoords(*args, **kwargs)

    def GetSegmentChainData(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainData(*args, **kwargs)

    def GetSegmentChainDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainDisplacementsByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainDisplacements(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainDisplacements(
            *args, **kwargs)

    def GetCriticalSegmentChainDisplacements(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainDisplacements(
            *args, **kwargs)

    def GetSegmentChainVelocitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainVelocitiesByLoadCaseId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainVelocities(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainVelocities(*args, **kwargs)

    def GetSegmentChainAccelerationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainAccelerationsByLoadCaseId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainAccelerations(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainAccelerations(
            *args, **kwargs)

    def GetSegmentChainSurfaceForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainSurfaceForcesByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainSurfaceForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainSurfaceForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainSurfaceForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainSurfaceForces(
            *args, **kwargs)

    def GetCriticalSegmentChainSurfaceForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainSurfaceForces(
            *args, **kwargs)

    def GetSegmentChainCalculatedReinforcementsByLoadCaseId(
            self, *args, **kwargs):
        return self._wrapped.GetSegmentChainCalculatedReinforcementsByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainCalculatedReinforcementsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetSegmentChainCalculatedReinforcementsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainCalculatedReinforcements(
            *args, **kwargs)

    def GetCriticalSegmentChainCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainCalculatedReinforcements(
            *args, **kwargs)

    def GetSegmentChainSurfaceSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainSurfaceSupportForcesByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainSurfaceSupportForcesByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetSegmentChainSurfaceSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainSurfaceSupportForces(
            *args, **kwargs)

    def GetCriticalSegmentChainSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainSurfaceSupportForces(
            *args, **kwargs)

    def GetSegmentChainCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainCrackWidthsByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainCrackWidthsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainCrackWidths(
            *args, **kwargs)

    def GetCriticalSegmentChainCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainCrackWidths(
            *args, **kwargs)

    def GetSegmentChainShearCapacitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainShearCapacitiesByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainShearCapacitiesByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetSegmentChainShearCapacitiesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainShearCapacities(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainShearCapacities(
            *args, **kwargs)

    def GetCriticalSegmentChainShearCapacities(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainShearCapacities(
            *args, **kwargs)

    def GetSegmentChainSurfaceStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainSurfaceStressesByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainSurfaceStressesByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetSegmentChainSurfaceStressesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainSurfaceStresses(
            *args, **kwargs)

    def GetCriticalSegmentChainSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainSurfaceStresses(
            *args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetSegmentChainIntegratedResultantByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSegmentChainIntegratedResultantByLoadCaseId(
            *args, **kwargs)

    def GetSegmentChainIntegratedResultantByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetSegmentChainIntegratedResultantByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSegmentChainIntegratedResultant(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSegmentChainIntegratedResultant(
            *args, **kwargs)

    def GetCriticalSegmentChainIntegratedResultant(self, *args, **kwargs):
        return self._wrapped.GetCriticalSegmentChainIntegratedResultant(
            *args, **kwargs)

    def GetSegmentIntegratedResultantChainCount(self, *args, **kwargs):
        return self._wrapped.GetSegmentIntegratedResultantChainCount(
            *args, **kwargs)

    def GetSegmentIntegratedResultantChainCoords(self, *args, **kwargs):
        return self._wrapped.GetSegmentIntegratedResultantChainCoords(
            *args, **kwargs)

    def GetSegmentIntegratedResultantChainData(self, *args, **kwargs):
        return self._wrapped.GetSegmentIntegratedResultantChainData(
            *args, **kwargs)

    def GetSegmentIntegratedResultantParams(self, *args, **kwargs):
        return self._wrapped.GetSegmentIntegratedResultantParams(
            *args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep


class AxisVMLines3d(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)


class AxisVMRCBeamDesign(AxWrapper):

    def GetLines(self, *args, **kwargs):
        return self._wrapped.GetLines(*args, **kwargs)

    def Calculate(self, *args, **kwargs):
        return self._wrapped.Calculate(*args, **kwargs)

    @property
    def BeamDesignPlane(self) -> int:
        return self._wrapped.BeamDesignPlane

    @BeamDesignPlane.setter
    def BeamDesignPlane(self, Value: int):
        self._wrapped.BeamDesignPlane = Value

    def GetDesignParameters(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters(*args, **kwargs)

    def SetDesignParameters(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters(*args, **kwargs)

    def SetDesignParameters_vb(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters_vb(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def AddMembers(self, *args, **kwargs):
        return self._wrapped.AddMembers(*args, **kwargs)

    def AddMembers_vb(self, *args, **kwargs):
        return self._wrapped.AddMembers_vb(*args, **kwargs)

    def AddLines(self, *args, **kwargs):
        return self._wrapped.AddLines(*args, **kwargs)

    def AddLines_vb(self, *args, **kwargs):
        return self._wrapped.AddLines_vb(*args, **kwargs)

    def GetPartialRCBeamDesignParameters(self, *args, **kwargs):
        return self._wrapped.GetPartialRCBeamDesignParameters(*args, **kwargs)


class AxisVMModels(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def New(self, *args, **kwargs):
        return self._wrapped.New(*args, **kwargs)


class AxisVMCrackWidth(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetCrackWidthsByLoadCaseId(*args, **kwargs)

    def GetCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetCrackWidthsByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeCrackWidths(*args, **kwargs)

    def GetCriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetCriticalCrackWidths(*args, **kwargs)

    def GetAllCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllCrackWidthsByLoadCaseId(*args, **kwargs)

    def GetAllCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllCrackWidthsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeCrackWidths(*args, **kwargs)

    def GetAllCriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalCrackWidths(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def CrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.CrackWidthsByLoadCaseId(*args, **kwargs)

    def CrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.CrackWidthsByLoadCombinationId(*args, **kwargs)

    def EnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.EnvelopeCrackWidths(*args, **kwargs)

    def CriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.CriticalCrackWidths(*args, **kwargs)

    def AllCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllCrackWidthsByLoadCaseId(*args, **kwargs)

    def AllCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllCrackWidthsByLoadCombinationId(*args, **kwargs)

    def AllEnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeCrackWidths(*args, **kwargs)

    def AllCriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.AllCriticalCrackWidths(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeCrackWidths2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeCrackWidths2(*args, **kwargs)

    def GetCriticalCrackWidths2(self, *args, **kwargs):
        return self._wrapped.GetCriticalCrackWidths2(*args, **kwargs)

    def EnvelopeCrackWidths2(self, *args, **kwargs):
        return self._wrapped.EnvelopeCrackWidths2(*args, **kwargs)

    def CriticalCrackWidths2(self, *args, **kwargs):
        return self._wrapped.CriticalCrackWidths2(*args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep


class AxisVMCalculatedReinforcement(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetCalculatedReinforcementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetCalculatedReinforcementsByLoadCaseId(
            *args, **kwargs)

    def GetCalculatedReinforcementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetCalculatedReinforcementsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeCalculatedReinforcements(
            *args, **kwargs)

    def GetCriticalCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.GetCriticalCalculatedReinforcements(
            *args, **kwargs)

    def GetAllCalculatedReinforcementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllCalculatedReinforcementsByLoadCaseId(
            *args, **kwargs)

    def GetAllCalculatedReinforcementsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetAllCalculatedReinforcementsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeCalculatedReinforcements(
            *args, **kwargs)

    def GetAllCriticalCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalCalculatedReinforcements(
            *args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def CalculatedReinforcementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.CalculatedReinforcementsByLoadCaseId(
            *args, **kwargs)

    def CalculatedReinforcementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.CalculatedReinforcementsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.EnvelopeCalculatedReinforcements(*args, **kwargs)

    def CriticalCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.CriticalCalculatedReinforcements(*args, **kwargs)

    def AllCalculatedReinforcementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllCalculatedReinforcementsByLoadCaseId(
            *args, **kwargs)

    def AllCalculatedReinforcementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllCalculatedReinforcementsByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeCalculatedReinforcements(
            *args, **kwargs)

    def AllCriticalCalculatedReinforcements(self, *args, **kwargs):
        return self._wrapped.AllCriticalCalculatedReinforcements(
            *args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeCalculatedReinforcements2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeCalculatedReinforcements2(
            *args, **kwargs)

    def GetCriticalCalculatedReinforcements2(self, *args, **kwargs):
        return self._wrapped.GetCriticalCalculatedReinforcements2(
            *args, **kwargs)

    def EnvelopeCalculatedReinforcements2(self, *args, **kwargs):
        return self._wrapped.EnvelopeCalculatedReinforcements2(*args, **kwargs)

    def CriticalCalculatedReinforcements2(self, *args, **kwargs):
        return self._wrapped.CriticalCalculatedReinforcements2(*args, **kwargs)


class AxisVMTask(AxWrapper):

    def DrawObjectsDirectlyModal(self, *args, **kwargs):
        return self._wrapped.DrawObjectsDirectlyModal(*args, **kwargs)

    def AddSupportModal(self, *args, **kwargs):
        return self._wrapped.AddSupportModal(*args, **kwargs)

    def ShowLoadCasesAndGroupsFormModal(self, *args, **kwargs):
        return self._wrapped.ShowLoadCasesAndGroupsFormModal(*args, **kwargs)

    def AddLoadModal(self, *args, **kwargs):
        return self._wrapped.AddLoadModal(*args, **kwargs)

    def ShowDomainMeshingFormModal(self, *args, **kwargs):
        return self._wrapped.ShowDomainMeshingFormModal(*args, **kwargs)


class AxisVMSettings(AxWrapper):

    @property
    def EditingTolerance(self) -> float:
        return self._wrapped.EditingTolerance

    @EditingTolerance.setter
    def EditingTolerance(self, Value: float):
        self._wrapped.EditingTolerance = Value

    @property
    def CrossSectionEditingTolerance(self) -> float:
        return self._wrapped.CrossSectionEditingTolerance

    @CrossSectionEditingTolerance.setter
    def CrossSectionEditingTolerance(self, Value: float):
        self._wrapped.CrossSectionEditingTolerance = Value

    @property
    def NationalDesignCode(self) -> int:
        return self._wrapped.NationalDesignCode

    @NationalDesignCode.setter
    def NationalDesignCode(self, Value: int):
        self._wrapped.NationalDesignCode = Value

    def GetPlaneTolerance(self, *args, **kwargs):
        return self._wrapped.GetPlaneTolerance(*args, **kwargs)

    def SetPlaneTolerance(self, *args, **kwargs):
        return self._wrapped.SetPlaneTolerance(*args, **kwargs)

    @property
    def ProgramLanguage(self) -> int:
        return self._wrapped.ProgramLanguage

    @ProgramLanguage.setter
    def ProgramLanguage(self, Value: int):
        self._wrapped.ProgramLanguage = Value

    @property
    def FixedMesh(self) -> int:
        return self._wrapped.FixedMesh

    @FixedMesh.setter
    def FixedMesh(self, Value: int):
        self._wrapped.FixedMesh = Value

    @property
    def ReportLanguage(self) -> int:
        return self._wrapped.ReportLanguage

    @ReportLanguage.setter
    def ReportLanguage(self, Value: int):
        self._wrapped.ReportLanguage = Value

    def GetGridOptions(self, *args, **kwargs):
        return self._wrapped.GetGridOptions(*args, **kwargs)

    def SetGridOptions(self, *args, **kwargs):
        return self._wrapped.SetGridOptions(*args, **kwargs)

    def GetCursorSnap(self, *args, **kwargs):
        return self._wrapped.GetCursorSnap(*args, **kwargs)

    def SetCursorSnap(self, *args, **kwargs):
        return self._wrapped.SetCursorSnap(*args, **kwargs)

    def GetEditingOptions(self, *args, **kwargs):
        return self._wrapped.GetEditingOptions(*args, **kwargs)

    def SetEditingOptions(self, *args, **kwargs):
        return self._wrapped.SetEditingOptions(*args, **kwargs)

    def GetTempFolderType(self, *args, **kwargs):
        return self._wrapped.GetTempFolderType(*args, **kwargs)

    def SetTempFolderType(self, *args, **kwargs):
        return self._wrapped.SetTempFolderType(*args, **kwargs)

    @property
    def MomentDiagramType(self) -> int:
        return self._wrapped.MomentDiagramType

    @MomentDiagramType.setter
    def MomentDiagramType(self, Value: int):
        self._wrapped.MomentDiagramType = Value

    @property
    def BackgroundColour(self) -> int:
        return self._wrapped.BackgroundColour

    @BackgroundColour.setter
    def BackgroundColour(self, Value: int):
        self._wrapped.BackgroundColour = Value

    def SetGravity(self, *args, **kwargs):
        return self._wrapped.SetGravity(*args, **kwargs)

    def GetGravity(self, *args, **kwargs):
        return self._wrapped.GetGravity(*args, **kwargs)

    def EnvironmentClassIsValid(self, *args, **kwargs):
        return self._wrapped.EnvironmentClassIsValid(*args, **kwargs)

    def GetUnitParams_Geometry(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Geometry(*args, **kwargs)

    def GetUnitParams_CrossSection(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_CrossSection(*args, **kwargs)

    def GetUnitParams_Material(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Material(*args, **kwargs)

    def GetUnitParams_Properties(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Properties(*args, **kwargs)

    def GetUnitParams_Stiffness(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Stiffness(*args, **kwargs)

    def GetUnitParams_Loads(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Loads(*args, **kwargs)

    def GetUnitParams_Static(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Static(*args, **kwargs)

    def GetUnitParams_RC_design(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_RC_design(*args, **kwargs)

    def GetUnitParams_Steel_design(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Steel_design(*args, **kwargs)

    def GetUnitParams_Timber_design(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Timber_design(*args, **kwargs)

    def GetUnitParams_Dimensioning(self, *args, **kwargs):
        return self._wrapped.GetUnitParams_Dimensioning(*args, **kwargs)

    @property
    def StiffnessReductionColumns_A(self) -> float:
        return self._wrapped.StiffnessReductionColumns_A

    @StiffnessReductionColumns_A.setter
    def StiffnessReductionColumns_A(self, Value: float):
        self._wrapped.StiffnessReductionColumns_A = Value

    @property
    def StiffnessReductionColumns_I(self) -> float:
        return self._wrapped.StiffnessReductionColumns_I

    @StiffnessReductionColumns_I.setter
    def StiffnessReductionColumns_I(self, Value: float):
        self._wrapped.StiffnessReductionColumns_I = Value

    @property
    def StiffnessReductionBeams_A(self) -> float:
        return self._wrapped.StiffnessReductionBeams_A

    @StiffnessReductionBeams_A.setter
    def StiffnessReductionBeams_A(self, Value: float):
        self._wrapped.StiffnessReductionBeams_A = Value

    @property
    def StiffnessReductionBeams_I(self) -> float:
        return self._wrapped.StiffnessReductionBeams_I

    @StiffnessReductionBeams_I.setter
    def StiffnessReductionBeams_I(self, Value: float):
        self._wrapped.StiffnessReductionBeams_I = Value

    @property
    def StiffnessReductionOtherMembers_A(self) -> float:
        return self._wrapped.StiffnessReductionOtherMembers_A

    @StiffnessReductionOtherMembers_A.setter
    def StiffnessReductionOtherMembers_A(self, Value: float):
        self._wrapped.StiffnessReductionOtherMembers_A = Value

    @property
    def StiffnessReductionOtherMembers_I(self) -> float:
        return self._wrapped.StiffnessReductionOtherMembers_I

    @StiffnessReductionOtherMembers_I.setter
    def StiffnessReductionOtherMembers_I(self, Value: float):
        self._wrapped.StiffnessReductionOtherMembers_I = Value

    @property
    def StiffnessReductionWalls(self) -> float:
        return self._wrapped.StiffnessReductionWalls

    @StiffnessReductionWalls.setter
    def StiffnessReductionWalls(self, Value: float):
        self._wrapped.StiffnessReductionWalls = Value

    @property
    def StiffnessReductionSlabs(self) -> float:
        return self._wrapped.StiffnessReductionSlabs

    @StiffnessReductionSlabs.setter
    def StiffnessReductionSlabs(self, Value: float):
        self._wrapped.StiffnessReductionSlabs = Value

    @property
    def StiffnessReductionOtherDomains(self) -> float:
        return self._wrapped.StiffnessReductionOtherDomains

    @StiffnessReductionOtherDomains.setter
    def StiffnessReductionOtherDomains(self, Value: float):
        self._wrapped.StiffnessReductionOtherDomains = Value

    @property
    def NL_ConsequenceClass(self) -> int:
        return self._wrapped.NL_ConsequenceClass

    @NL_ConsequenceClass.setter
    def NL_ConsequenceClass(self, Value: int):
        self._wrapped.NL_ConsequenceClass = Value


class AxisVMMaterials(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def AddDialog(self, *args, **kwargs):
        return self._wrapped.AddDialog(*args, **kwargs)

    def AddSteel_Hungarian_MSZ(self, *args, **kwargs):
        return self._wrapped.AddSteel_Hungarian_MSZ(*args, **kwargs)

    def AddSteel_EuroCode(self, *args, **kwargs):
        return self._wrapped.AddSteel_EuroCode(*args, **kwargs)

    def AddSteel_Romanian_STAS(self, *args, **kwargs):
        return self._wrapped.AddSteel_Romanian_STAS(*args, **kwargs)

    def AddSteel_Dutch_NEN(self, *args, **kwargs):
        return self._wrapped.AddSteel_Dutch_NEN(*args, **kwargs)

    def AddSteel_German_DIN1045_1(self, *args, **kwargs):
        return self._wrapped.AddSteel_German_DIN1045_1(*args, **kwargs)

    def AddSteel_Swiss_SIA26x(self, *args, **kwargs):
        return self._wrapped.AddSteel_Swiss_SIA26x(*args, **kwargs)

    def AddSteel_Italian(self, *args, **kwargs):
        return self._wrapped.AddSteel_Italian(*args, **kwargs)

    def AddConcrete_Hungarian_MSZ(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Hungarian_MSZ(*args, **kwargs)

    def AddConcrete_EuroCode(self, *args, **kwargs):
        return self._wrapped.AddConcrete_EuroCode(*args, **kwargs)

    def AddConcrete_Romanian_STAS(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Romanian_STAS(*args, **kwargs)

    def AddConcrete_Dutch_NEN(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Dutch_NEN(*args, **kwargs)

    def AddConcrete_German_DIN1045_1(self, *args, **kwargs):
        return self._wrapped.AddConcrete_German_DIN1045_1(*args, **kwargs)

    def AddConcrete_Swiss_SIA26x(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Swiss_SIA26x(*args, **kwargs)

    def AddConcrete_Italian(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Italian(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddTimber(self, *args, **kwargs):
        return self._wrapped.AddTimber(*args, **kwargs)

    def AddAluminium(self, *args, **kwargs):
        return self._wrapped.AddAluminium(*args, **kwargs)

    def AddBrick(self, *args, **kwargs):
        return self._wrapped.AddBrick(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def AddFromCatalog(self, *args, **kwargs):
        return self._wrapped.AddFromCatalog(*args, **kwargs)

    def AddFromCatalogFile(self, *args, **kwargs):
        return self._wrapped.AddFromCatalogFile(*args, **kwargs)

    def AddFromDialog(self, *args, **kwargs):
        return self._wrapped.AddFromDialog(*args, **kwargs)

    def AddFromDialog_vb(self, *args, **kwargs):
        return self._wrapped.AddFromDialog_vb(*args, **kwargs)

    def AddSteel_Hungarian_MSZ_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_Hungarian_MSZ_vb(*args, **kwargs)

    def AddSteel_EuroCode_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_EuroCode_vb(*args, **kwargs)

    def AddSteel_Romanian_STAS_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_Romanian_STAS_vb(*args, **kwargs)

    def AddSteel_Dutch_NEN_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_Dutch_NEN_vb(*args, **kwargs)

    def AddSteel_German_DIN1045_1_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_German_DIN1045_1_vb(*args, **kwargs)

    def AddSteel_Swiss_SIA26x_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_Swiss_SIA26x_vb(*args, **kwargs)

    def AddSteel_Italian_vb(self, *args, **kwargs):
        return self._wrapped.AddSteel_Italian_vb(*args, **kwargs)

    def AddConcrete_Hungarian_MSZ_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Hungarian_MSZ_vb(*args, **kwargs)

    def AddConcrete_EuroCode_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_EuroCode_vb(*args, **kwargs)

    def AddConcrete_Romanian_STAS_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Romanian_STAS_vb(*args, **kwargs)

    def AddConcrete_Dutch_NEN_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Dutch_NEN_vb(*args, **kwargs)

    def AddConcrete_German_DIN1045_1_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_German_DIN1045_1_vb(*args, **kwargs)

    def AddConcrete_Swiss_SIA26x_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Swiss_SIA26x_vb(*args, **kwargs)

    def AddConcrete_Italian_vb(self, *args, **kwargs):
        return self._wrapped.AddConcrete_Italian_vb(*args, **kwargs)

    def AddTimber_vb(self, *args, **kwargs):
        return self._wrapped.AddTimber_vb(*args, **kwargs)

    def AddAluminium_vb(self, *args, **kwargs):
        return self._wrapped.AddAluminium_vb(*args, **kwargs)

    def AddBrick_vb(self, *args, **kwargs):
        return self._wrapped.AddBrick_vb(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID


class AxisVMCrossSections(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddCustom(self, *args, **kwargs):
        return self._wrapped.AddCustom(*args, **kwargs)

    def ReplaceWithCustom(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCustom(*args, **kwargs)

    def AddRectangular(self, *args, **kwargs):
        return self._wrapped.AddRectangular(*args, **kwargs)

    def ReplaceWithRectangular(self, *args, **kwargs):
        return self._wrapped.ReplaceWithRectangular(*args, **kwargs)

    def AddI(self, *args, **kwargs):
        return self._wrapped.AddI(*args, **kwargs)

    def ReplaceWithI(self, *args, **kwargs):
        return self._wrapped.ReplaceWithI(*args, **kwargs)

    def AddDoubleI(self, *args, **kwargs):
        return self._wrapped.AddDoubleI(*args, **kwargs)

    def ReplaceWithDoubleI(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleI(*args, **kwargs)

    def AddWedgedI(self, *args, **kwargs):
        return self._wrapped.AddWedgedI(*args, **kwargs)

    def ReplaceWithWedgedI(self, *args, **kwargs):
        return self._wrapped.ReplaceWithWedgedI(*args, **kwargs)

    def AddAsymmetricI(self, *args, **kwargs):
        return self._wrapped.AddAsymmetricI(*args, **kwargs)

    def ReplaceWithAsymmetricI(self, *args, **kwargs):
        return self._wrapped.ReplaceWithAsymmetricI(*args, **kwargs)

    def AddPipe(self, *args, **kwargs):
        return self._wrapped.AddPipe(*args, **kwargs)

    def ReplaceWithPipe(self, *args, **kwargs):
        return self._wrapped.ReplaceWithPipe(*args, **kwargs)

    def AddRegularPolygon(self, *args, **kwargs):
        return self._wrapped.AddRegularPolygon(*args, **kwargs)

    def ReplaceWithRegularPolygon(self, *args, **kwargs):
        return self._wrapped.ReplaceWithRegularPolygon(*args, **kwargs)

    def AddBox(self, *args, **kwargs):
        return self._wrapped.AddBox(*args, **kwargs)

    def ReplaceWithBox(self, *args, **kwargs):
        return self._wrapped.ReplaceWithBox(*args, **kwargs)

    def AddDoubleIBox(self, *args, **kwargs):
        return self._wrapped.AddDoubleIBox(*args, **kwargs)

    def ReplaceWithDoubleIBox(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleIBox(*args, **kwargs)

    def AddU(self, *args, **kwargs):
        return self._wrapped.AddU(*args, **kwargs)

    def ReplaceWithU(self, *args, **kwargs):
        return self._wrapped.ReplaceWithU(*args, **kwargs)

    def AddDoubleU(self, *args, **kwargs):
        return self._wrapped.AddDoubleU(*args, **kwargs)

    def ReplaceWithDoubleU(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleU(*args, **kwargs)

    def AddL(self, *args, **kwargs):
        return self._wrapped.AddL(*args, **kwargs)

    def ReplaceWithL(self, *args, **kwargs):
        return self._wrapped.ReplaceWithL(*args, **kwargs)

    def AddDoubleL(self, *args, **kwargs):
        return self._wrapped.AddDoubleL(*args, **kwargs)

    def ReplaceWithDoubleL(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleL(*args, **kwargs)

    def AddDoubleLFlange(self, *args, **kwargs):
        return self._wrapped.AddDoubleLFlange(*args, **kwargs)

    def ReplaceWithDoubleLFlange(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleLFlange(*args, **kwargs)

    def AddT(self, *args, **kwargs):
        return self._wrapped.AddT(*args, **kwargs)

    def ReplaceWithT(self, *args, **kwargs):
        return self._wrapped.ReplaceWithT(*args, **kwargs)

    def AddReverseT(self, *args, **kwargs):
        return self._wrapped.AddReverseT(*args, **kwargs)

    def ReplaceWithReverseT(self, *args, **kwargs):
        return self._wrapped.ReplaceWithReverseT(*args, **kwargs)

    def AddZ(self, *args, **kwargs):
        return self._wrapped.AddZ(*args, **kwargs)

    def ReplaceWithZ(self, *args, **kwargs):
        return self._wrapped.ReplaceWithZ(*args, **kwargs)

    def AddC(self, *args, **kwargs):
        return self._wrapped.AddC(*args, **kwargs)

    def ReplaceWithC(self, *args, **kwargs):
        return self._wrapped.ReplaceWithC(*args, **kwargs)

    def AddCircle(self, *args, **kwargs):
        return self._wrapped.AddCircle(*args, **kwargs)

    def ReplaceWithCircle(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCircle(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Merge(self, *args, **kwargs):
        return self._wrapped.Merge(*args, **kwargs)

    def AddFromCatalog(self, *args, **kwargs):
        return self._wrapped.AddFromCatalog(*args, **kwargs)

    def AddFromCatalogFile(self, *args, **kwargs):
        return self._wrapped.AddFromCatalogFile(*args, **kwargs)

    def AddFromDialog(self, *args, **kwargs):
        return self._wrapped.AddFromDialog(*args, **kwargs)

    def AddFromEditor(self, *args, **kwargs):
        return self._wrapped.AddFromEditor(*args, **kwargs)

    def Edit(self, *args, **kwargs):
        return self._wrapped.Edit(*args, **kwargs)

    def AddCustomWithUserParams(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParams(*args, **kwargs)

    def ReplaceWithCustomAndUserParams(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCustomAndUserParams(*args, **kwargs)

    def AddCustomWithUserParamsAsArray(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsArray(*args, **kwargs)

    def ReplaceWithCustomAndUserParamsAsArray(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCustomAndUserParamsAsArray(
            *args, **kwargs)

    def AddCustomWithUserParamsAsByteArray(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsByteArray(
            *args, **kwargs)

    def ReplaceWithCustomAndUserParamsAsByteArray(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCustomAndUserParamsAsByteArray(
            *args, **kwargs)

    def ReplaceFromCatalog(self, *args, **kwargs):
        return self._wrapped.ReplaceFromCatalog(*args, **kwargs)

    def ReplaceFromCatalogFile(self, *args, **kwargs):
        return self._wrapped.ReplaceFromCatalogFile(*args, **kwargs)

    def AddFromDialog_vb(self, *args, **kwargs):
        return self._wrapped.AddFromDialog_vb(*args, **kwargs)

    def AddCustomWithUserParamsAsArray_vb(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsArray_vb(*args, **kwargs)

    def ReplaceWithCustomAndUserParamsAsArray_vb(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCustomAndUserParamsAsArray_vb(
            *args, **kwargs)

    def AddCustomWithUserParamsAsByteArray_vb(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsByteArray_vb(
            *args, **kwargs)

    def ReplaceWithCustomAndUserParamsAsByteArray_vb(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCustomAndUserParamsAsByteArray_vb(
            *args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    def AddRectangularRounded(self, *args, **kwargs):
        return self._wrapped.AddRectangularRounded(*args, **kwargs)

    def ReplaceWithRectangularRounded(self, *args, **kwargs):
        return self._wrapped.ReplaceWithRectangularRounded(*args, **kwargs)

    def AddRectangularHollow(self, *args, **kwargs):
        return self._wrapped.AddRectangularHollow(*args, **kwargs)

    def ReplaceWithRectangularHollow(self, *args, **kwargs):
        return self._wrapped.ReplaceWithRectangularHollow(*args, **kwargs)

    def AddIHaunched(self, *args, **kwargs):
        return self._wrapped.AddIHaunched(*args, **kwargs)

    def ReplaceWithIHaunched(self, *args, **kwargs):
        return self._wrapped.ReplaceWithIHaunched(*args, **kwargs)

    def AddTWallHaunched(self, *args, **kwargs):
        return self._wrapped.AddTWallHaunched(*args, **kwargs)

    def ReplaceWithTWallHaunched(self, *args, **kwargs):
        return self._wrapped.ReplaceWithTWallHaunched(*args, **kwargs)

    def AddTTopHaunched(self, *args, **kwargs):
        return self._wrapped.AddTTopHaunched(*args, **kwargs)

    def ReplaceWithTTopHaunched(self, *args, **kwargs):
        return self._wrapped.ReplaceWithTTopHaunched(*args, **kwargs)

    def AddCircleHollow(self, *args, **kwargs):
        return self._wrapped.AddCircleHollow(*args, **kwargs)

    def ReplaceWithCircleHollow(self, *args, **kwargs):
        return self._wrapped.ReplaceWithCircleHollow(*args, **kwargs)

    def AddTrapezoid(self, *args, **kwargs):
        return self._wrapped.AddTrapezoid(*args, **kwargs)

    def ReplaceWithTrapezoid(self, *args, **kwargs):
        return self._wrapped.ReplaceWithTrapezoid(*args, **kwargs)

    def GetDimensionsOfC(self, *args, **kwargs):
        return self._wrapped.GetDimensionsOfC(*args, **kwargs)

    def GetDimensionsOfIHaunched(self, *args, **kwargs):
        return self._wrapped.GetDimensionsOfIHaunched(*args, **kwargs)

    def GetDimensionsOfTWallHaunched(self, *args, **kwargs):
        return self._wrapped.GetDimensionsOfTWallHaunched(*args, **kwargs)

    def GetDimensionsOfTTopHaunched(self, *args, **kwargs):
        return self._wrapped.GetDimensionsOfTTopHaunched(*args, **kwargs)

    def SaveToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveToMetaFile(*args, **kwargs)

    def SaveToBitmapFile(self, *args, **kwargs):
        return self._wrapped.SaveToBitmapFile(*args, **kwargs)

    def AddCompositePipe(self, *args, **kwargs):
        return self._wrapped.AddCompositePipe(*args, **kwargs)

    def AddCompositeBox(self, *args, **kwargs):
        return self._wrapped.AddCompositeBox(*args, **kwargs)

    def AddCompositeRound(self, *args, **kwargs):
        return self._wrapped.AddCompositeRound(*args, **kwargs)

    def AddCompositeRectangle(self, *args, **kwargs):
        return self._wrapped.AddCompositeRectangle(*args, **kwargs)

    def AddFromDialogEx(self, *args, **kwargs):
        return self._wrapped.AddFromDialogEx(*args, **kwargs)

    def EditEx(self, *args, **kwargs):
        return self._wrapped.EditEx(*args, **kwargs)

    def ReplaceFromCatalogEx(self, *args, **kwargs):
        return self._wrapped.ReplaceFromCatalogEx(*args, **kwargs)

    def AddDoubleWedgedI(self, *args, **kwargs):
        return self._wrapped.AddDoubleWedgedI(*args, **kwargs)

    def ReplaceWithDoubleWedgedI(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleWedgedI(*args, **kwargs)

    def AddHSQ(self, *args, **kwargs):
        return self._wrapped.AddHSQ(*args, **kwargs)

    def ReplaceWithHSQ(self, *args, **kwargs):
        return self._wrapped.ReplaceWithHSQ(*args, **kwargs)

    def AddHSQA(self, *args, **kwargs):
        return self._wrapped.AddHSQA(*args, **kwargs)

    def ReplaceWithHSQA(self, *args, **kwargs):
        return self._wrapped.ReplaceWithHSQA(*args, **kwargs)

    def AddFromCatalog_V161(self, *args, **kwargs):
        return self._wrapped.AddFromCatalog_V161(*args, **kwargs)

    def Add2IX(self, *args, **kwargs):
        return self._wrapped.Add2IX(*args, **kwargs)

    def ReplaceWith2IX(self, *args, **kwargs):
        return self._wrapped.ReplaceWith2IX(*args, **kwargs)

    def AddComposite2IX(self, *args, **kwargs):
        return self._wrapped.AddComposite2IX(*args, **kwargs)

    def ReplaceWithComposite2IX(self, *args, **kwargs):
        return self._wrapped.ReplaceWithComposite2IX(*args, **kwargs)

    def AddIFB(self, *args, **kwargs):
        return self._wrapped.AddIFB(*args, **kwargs)

    def ReplaceWithIFB(self, *args, **kwargs):
        return self._wrapped.ReplaceWithIFB(*args, **kwargs)

    def AddSFB(self, *args, **kwargs):
        return self._wrapped.AddSFB(*args, **kwargs)

    def ReplaceWithSFB(self, *args, **kwargs):
        return self._wrapped.ReplaceWithSFB(*args, **kwargs)

    def AddDoubleLClosed(self, *args, **kwargs):
        return self._wrapped.AddDoubleLClosed(*args, **kwargs)

    def ReplaceWithDoubleLClosed(self, *args, **kwargs):
        return self._wrapped.ReplaceWithDoubleLClosed(*args, **kwargs)

    def AddFromCatalogTable(self, *args, **kwargs):
        return self._wrapped.AddFromCatalogTable(*args, **kwargs)


class AxisVMReferences(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)


class AxisVMNodes(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def AddWithDOF(self, *args, **kwargs):
        return self._wrapped.AddWithDOF(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def GetConnectedLines(self, *args, **kwargs):
        return self._wrapped.GetConnectedLines(*args, **kwargs)

    def GetConnectedSurfaces(self, *args, **kwargs):
        return self._wrapped.GetConnectedSurfaces(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def GetNode(self, *args, **kwargs):
        return self._wrapped.GetNode(*args, **kwargs)

    def SetNode(self, *args, **kwargs):
        return self._wrapped.SetNode(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    def GetNodeCoord(self, *args, **kwargs):
        return self._wrapped.GetNodeCoord(*args, **kwargs)

    def SetNodeCoord(self, *args, **kwargs):
        return self._wrapped.SetNodeCoord(*args, **kwargs)

    def GetSelectedNodes(self, *args, **kwargs):
        return self._wrapped.GetSelectedNodes(*args, **kwargs)

    def RenameSelectedNodes(self, *args, **kwargs):
        return self._wrapped.RenameSelectedNodes(*args, **kwargs)

    def Check(self, *args, **kwargs):
        return self._wrapped.Check(*args, **kwargs)

    def DeleteNameOfAllNodes(self, *args, **kwargs):
        return self._wrapped.DeleteNameOfAllNodes(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def Attributes(self) -> 'AxisVMAttributes':
        return self._wrapped.Attributes

    @property
    def Attachments(self) -> 'AxisVMAttachments':
        return self._wrapped.Attachments

    def RemoveSelectedIntermedNodes(self, *args, **kwargs):
        return self._wrapped.RemoveSelectedIntermedNodes(*args, **kwargs)

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)

    def BulkGetCoord(self, *args, **kwargs):
        return self._wrapped.BulkGetCoord(*args, **kwargs)

    def BulkGetDOF(self, *args, **kwargs):
        return self._wrapped.BulkGetDOF(*args, **kwargs)

    def BulkSetDOF(self, *args, **kwargs):
        return self._wrapped.BulkSetDOF(*args, **kwargs)

    def BulkSetNodeCoord(self, *args, **kwargs):
        return self._wrapped.BulkSetNodeCoord(*args, **kwargs)

    def GetNodeLines(self, *args, **kwargs):
        return self._wrapped.GetNodeLines(*args, **kwargs)

    def BulkSelect(self, *args, **kwargs):
        return self._wrapped.BulkSelect(*args, **kwargs)

    def BulkDelete(self, *args, **kwargs):
        return self._wrapped.BulkDelete(*args, **kwargs)


class AxisVMNodalSupports(AxWrapper):

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def AddNodalGlobal(self, *args, **kwargs):
        return self._wrapped.AddNodalGlobal(*args, **kwargs)

    def AddNodalBeamRelative(self, *args, **kwargs):
        return self._wrapped.AddNodalBeamRelative(*args, **kwargs)

    def AddNodalEdgeRelative(self, *args, **kwargs):
        return self._wrapped.AddNodalEdgeRelative(*args, **kwargs)

    def AddNodalReference(self, *args, **kwargs):
        return self._wrapped.AddNodalReference(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    @property
    def HaveStiffnessCalcParams(self) -> int:
        return self._wrapped.HaveStiffnessCalcParams

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    def AddNodalLocal(self, *args, **kwargs):
        return self._wrapped.AddNodalLocal(*args, **kwargs)

    def AddNodalGlobal_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalGlobal_V153(*args, **kwargs)

    def AddNodalBeamRelative_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalBeamRelative_V153(*args, **kwargs)

    def AddNodalEdgeRelative_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalEdgeRelative_V153(*args, **kwargs)

    def AddNodalReference_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalReference_V153(*args, **kwargs)

    def AddNodalLocal_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalLocal_V153(*args, **kwargs)

    def AddIsolator(self, *args, **kwargs):
        return self._wrapped.AddIsolator(*args, **kwargs)


class AxisVMLineSupports(AxWrapper):

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def AddEdgeGlobal(self, *args, **kwargs):
        return self._wrapped.AddEdgeGlobal(*args, **kwargs)

    def AddEdgeRelative(self, *args, **kwargs):
        return self._wrapped.AddEdgeRelative(*args, **kwargs)

    def AddBeamElasticFoundation(self, *args, **kwargs):
        return self._wrapped.AddBeamElasticFoundation(*args, **kwargs)

    def AddRibElasticFoundation(self, *args, **kwargs):
        return self._wrapped.AddRibElasticFoundation(*args, **kwargs)

    @property
    def SectionCount(self) -> int:
        return self._wrapped.SectionCount

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    @property
    def LineId(self) -> int:
        return self._wrapped.LineId

    @property
    def HaveStiffnessCalcParams(self) -> int:
        return self._wrapped.HaveStiffnessCalcParams

    def GetNodeIds(self, *args, **kwargs):
        return self._wrapped.GetNodeIds(*args, **kwargs)

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)

    def AddEdgeGlobalPasternak(self, *args, **kwargs):
        return self._wrapped.AddEdgeGlobalPasternak(*args, **kwargs)

    def AddEdgeRelativePasternak(self, *args, **kwargs):
        return self._wrapped.AddEdgeRelativePasternak(*args, **kwargs)

    def AddBeamPasternakFoundation(self, *args, **kwargs):
        return self._wrapped.AddBeamPasternakFoundation(*args, **kwargs)

    def AddRibPasternakFoundation(self, *args, **kwargs):
        return self._wrapped.AddRibPasternakFoundation(*args, **kwargs)

    def BulkAddPasternak(self, *args, **kwargs):
        return self._wrapped.BulkAddPasternak(*args, **kwargs)


class AxisVMSurfaceSupports(AxWrapper):

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def AddSurfaceElasticFoundation(self, *args, **kwargs):
        return self._wrapped.AddSurfaceElasticFoundation(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    @property
    def SurfaceId(self) -> int:
        return self._wrapped.SurfaceId

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def AddSurfacePasternakFoundation(self, *args, **kwargs):
        return self._wrapped.AddSurfacePasternakFoundation(*args, **kwargs)


class AxisVMLoadCases(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def LoadCaseType(self) -> int:
        return self._wrapped.LoadCaseType

    @property
    def GroupID(self) -> int:
        return self._wrapped.GroupID

    @GroupID.setter
    def GroupID(self, Value: int):
        self._wrapped.GroupID = Value

    @property
    def LoadCount(self) -> int:
        return self._wrapped.LoadCount

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def CreateStandardSeismicCases(self, *args, **kwargs):
        return self._wrapped.CreateStandardSeismicCases(*args, **kwargs)

    def AddWithGroup(self, *args, **kwargs):
        return self._wrapped.AddWithGroup(*args, **kwargs)

    def CreatePushOverCases(self, *args, **kwargs):
        return self._wrapped.CreatePushOverCases(*args, **kwargs)

    @property
    def LoadDurationClass(self) -> int:
        return self._wrapped.LoadDurationClass

    @LoadDurationClass.setter
    def LoadDurationClass(self, Value: int):
        self._wrapped.LoadDurationClass = Value

    def CreatePreStressCases(self, *args, **kwargs):
        return self._wrapped.CreatePreStressCases(*args, **kwargs)

    def CreateImperfectionCase(self, *args, **kwargs):
        return self._wrapped.CreateImperfectionCase(*args, **kwargs)

    def GetPushOverParams(self, *args, **kwargs):
        return self._wrapped.GetPushOverParams(*args, **kwargs)

    def SetPushOverParams(self, *args, **kwargs):
        return self._wrapped.SetPushOverParams(*args, **kwargs)

    def GetImperfectionParams(self, *args, **kwargs):
        return self._wrapped.GetImperfectionParams(*args, **kwargs)

    def SetImperfectionParams(self, *args, **kwargs):
        return self._wrapped.SetImperfectionParams(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    def DeleteAllLoadsFromLoadCase(self, *args, **kwargs):
        return self._wrapped.DeleteAllLoadsFromLoadCase(*args, **kwargs)

    def CreateSnowCases(self, *args, **kwargs):
        return self._wrapped.CreateSnowCases(*args, **kwargs)

    def GetSnowLoadParams(self, *args, **kwargs):
        return self._wrapped.GetSnowLoadParams(*args, **kwargs)

    def SetSnowLoadParams(self, *args, **kwargs):
        return self._wrapped.SetSnowLoadParams(*args, **kwargs)

    def CreateWindCases(self, *args, **kwargs):
        return self._wrapped.CreateWindCases(*args, **kwargs)

    def GetWindLoadParams(self, *args, **kwargs):
        return self._wrapped.GetWindLoadParams(*args, **kwargs)

    def SetWindLoadParams(self, *args, **kwargs):
        return self._wrapped.SetWindLoadParams(*args, **kwargs)

    def GetSeismicParams(self, *args, **kwargs):
        return self._wrapped.GetSeismicParams(*args, **kwargs)

    def SetSeismicParams(self, *args, **kwargs):
        return self._wrapped.SetSeismicParams(*args, **kwargs)

    def GetSeismicParams_V153(self, *args, **kwargs):
        return self._wrapped.GetSeismicParams_V153(*args, **kwargs)

    def SetSeismicParams_V153(self, *args, **kwargs):
        return self._wrapped.SetSeismicParams_V153(*args, **kwargs)

    def SeismicGroupIds(self, *args, **kwargs):
        return self._wrapped.SeismicGroupIds(*args, **kwargs)

    def SeismicSpectrumH(self, *args, **kwargs):
        return self._wrapped.SeismicSpectrumH(*args, **kwargs)

    def SeismicSpectrumV(self, *args, **kwargs):
        return self._wrapped.SeismicSpectrumV(*args, **kwargs)

    @property
    def SeismicGroupID(self) -> int:
        return self._wrapped.SeismicGroupID

    def Delete_V153(self, *args, **kwargs):
        return self._wrapped.Delete_V153(*args, **kwargs)

    def CreateImperfectionCase_V153(self, *args, **kwargs):
        return self._wrapped.CreateImperfectionCase_V153(*args, **kwargs)


class AxisVMLoadGroups(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)


class AxisVMLoadCombinations(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def GetCombination(self, *args, **kwargs):
        return self._wrapped.GetCombination(*args, **kwargs)

    def SetCombination(self, *args, **kwargs):
        return self._wrapped.SetCombination(*args, **kwargs)

    @property
    def Comment(self) -> int:
        return self._wrapped.Comment

    @Comment.setter
    def Comment(self, Value: int):
        self._wrapped.Comment = Value

    def GenerateAutoCombinations(self, *args, **kwargs):
        return self._wrapped.GenerateAutoCombinations(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def SetCombination_vb(self, *args, **kwargs):
        return self._wrapped.SetCombination_vb(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    def GetValidCombinationTypes(self, *args, **kwargs):
        return self._wrapped.GetValidCombinationTypes(*args, **kwargs)


class AxisVMLoads(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def LoadType(self) -> int:
        return self._wrapped.LoadType

    @property
    def ElementId(self) -> int:
        return self._wrapped.ElementId

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    def GetLoad(self, *args, **kwargs):
        return self._wrapped.GetLoad(*args, **kwargs)

    def SetLoad(self, *args, **kwargs):
        return self._wrapped.SetLoad(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def AddNodalForce(self, *args, **kwargs):
        return self._wrapped.AddNodalForce(*args, **kwargs)

    def AddSupportDisplacement(self, *args, **kwargs):
        return self._wrapped.AddSupportDisplacement(*args, **kwargs)

    def AddRibConcentrated(self, *args, **kwargs):
        return self._wrapped.AddRibConcentrated(*args, **kwargs)

    def AddBeamConcentrated(self, *args, **kwargs):
        return self._wrapped.AddBeamConcentrated(*args, **kwargs)

    def AddBeamInfluence(self, *args, **kwargs):
        return self._wrapped.AddBeamInfluence(*args, **kwargs)

    def AddRibDistributed(self, *args, **kwargs):
        return self._wrapped.AddRibDistributed(*args, **kwargs)

    def AddBeamDistributed(self, *args, **kwargs):
        return self._wrapped.AddBeamDistributed(*args, **kwargs)

    def AddRibThermal(self, *args, **kwargs):
        return self._wrapped.AddRibThermal(*args, **kwargs)

    def AddSurfaceThermal(self, *args, **kwargs):
        return self._wrapped.AddSurfaceThermal(*args, **kwargs)

    def AddDomainThermal(self, *args, **kwargs):
        return self._wrapped.AddDomainThermal(*args, **kwargs)

    def AddBeamThermal(self, *args, **kwargs):
        return self._wrapped.AddBeamThermal(*args, **kwargs)

    def AddBeamStress(self, *args, **kwargs):
        return self._wrapped.AddBeamStress(*args, **kwargs)

    def AddTrussStress(self, *args, **kwargs):
        return self._wrapped.AddTrussStress(*args, **kwargs)

    def AddBeamFault(self, *args, **kwargs):
        return self._wrapped.AddBeamFault(*args, **kwargs)

    def AddTrussFault(self, *args, **kwargs):
        return self._wrapped.AddTrussFault(*args, **kwargs)

    def AddTrussThermal(self, *args, **kwargs):
        return self._wrapped.AddTrussThermal(*args, **kwargs)

    def AddRibSelfWeight(self, *args, **kwargs):
        return self._wrapped.AddRibSelfWeight(*args, **kwargs)

    def AddBeamSelfWeight(self, *args, **kwargs):
        return self._wrapped.AddBeamSelfWeight(*args, **kwargs)

    def AddTrussSelfWeight(self, *args, **kwargs):
        return self._wrapped.AddTrussSelfWeight(*args, **kwargs)

    def AddDomainSelfWeight(self, *args, **kwargs):
        return self._wrapped.AddDomainSelfWeight(*args, **kwargs)

    def AddSurfaceSelfWeight(self, *args, **kwargs):
        return self._wrapped.AddSurfaceSelfWeight(*args, **kwargs)

    def AddSurfaceDistributed(self, *args, **kwargs):
        return self._wrapped.AddSurfaceDistributed(*args, **kwargs)

    def AddDomainConstant(self, *args, **kwargs):
        return self._wrapped.AddDomainConstant(*args, **kwargs)

    def AddSurfaceEdge(self, *args, **kwargs):
        return self._wrapped.AddSurfaceEdge(*args, **kwargs)

    def AddDomainConcentrated(self, *args, **kwargs):
        return self._wrapped.AddDomainConcentrated(*args, **kwargs)

    def AddSurfaceConcentrated(self, *args, **kwargs):
        return self._wrapped.AddSurfaceConcentrated(*args, **kwargs)

    def AddDomainPolyArea(self, *args, **kwargs):
        return self._wrapped.AddDomainPolyArea(*args, **kwargs)

    def GetPoly(self, *args, **kwargs):
        return self._wrapped.GetPoly(*args, **kwargs)

    def AddDomainPolyLine(self, *args, **kwargs):
        return self._wrapped.AddDomainPolyLine(*args, **kwargs)

    def AddDomainPolyAssoc(self, *args, **kwargs):
        return self._wrapped.AddDomainPolyAssoc(*args, **kwargs)

    def AddSurfaceToBeam(self, *args, **kwargs):
        return self._wrapped.AddSurfaceToBeam(*args, **kwargs)

    def AddSurfaceToBeamAssoc(self, *args, **kwargs):
        return self._wrapped.AddSurfaceToBeamAssoc(*args, **kwargs)

    def AddDomainFluid(self, *args, **kwargs):
        return self._wrapped.AddDomainFluid(*args, **kwargs)

    def AddSurfaceFluid(self, *args, **kwargs):
        return self._wrapped.AddSurfaceFluid(*args, **kwargs)

    def GetLines(self, *args, **kwargs):
        return self._wrapped.GetLines(*args, **kwargs)

    def SetLines(self, *args, **kwargs):
        return self._wrapped.SetLines(*args, **kwargs)

    def SetPoly(self, *args, **kwargs):
        return self._wrapped.SetPoly(*args, **kwargs)

    def AddDomainLinear(self, *args, **kwargs):
        return self._wrapped.AddDomainLinear(*args, **kwargs)

    def CreateStandardSeismicLoads(self, *args, **kwargs):
        return self._wrapped.CreateStandardSeismicLoads(*args, **kwargs)

    def AddDynamic(self, *args, **kwargs):
        return self._wrapped.AddDynamic(*args, **kwargs)

    def CreateStandardPushOverLoads(self, *args, **kwargs):
        return self._wrapped.CreateStandardPushOverLoads(*args, **kwargs)

    def AddRibMemberConcentrated(self, *args, **kwargs):
        return self._wrapped.AddRibMemberConcentrated(*args, **kwargs)

    def AddBeamMemberConcentrated(self, *args, **kwargs):
        return self._wrapped.AddBeamMemberConcentrated(*args, **kwargs)

    def AddRibMemberDistributed(self, *args, **kwargs):
        return self._wrapped.AddRibMemberDistributed(*args, **kwargs)

    def AddBeamMemberDistributed(self, *args, **kwargs):
        return self._wrapped.AddBeamMemberDistributed(*args, **kwargs)

    def SetLoad_vb(self, *args, **kwargs):
        return self._wrapped.SetLoad_vb(*args, **kwargs)

    def AddSurfaceToBeam_vb(self, *args, **kwargs):
        return self._wrapped.AddSurfaceToBeam_vb(*args, **kwargs)

    def AddSurfaceToBeamAssoc_vb(self, *args, **kwargs):
        return self._wrapped.AddSurfaceToBeamAssoc_vb(*args, **kwargs)

    def SetLines_vb(self, *args, **kwargs):
        return self._wrapped.SetLines_vb(*args, **kwargs)

    def GetDomainPolyLineItems(self, *args, **kwargs):
        return self._wrapped.GetDomainPolyLineItems(*args, **kwargs)

    def CreateSnowLoadOnLoadPanels(self, *args, **kwargs):
        return self._wrapped.CreateSnowLoadOnLoadPanels(*args, **kwargs)

    def DeleteSnowLoadFromAllLoadPanels(self, *args, **kwargs):
        return self._wrapped.DeleteSnowLoadFromAllLoadPanels(*args, **kwargs)

    def DeleteSnowLoadFromLoadPanels(self, *args, **kwargs):
        return self._wrapped.DeleteSnowLoadFromLoadPanels(*args, **kwargs)

    def GetLoadPanelsOfSnowLoad(self, *args, **kwargs):
        return self._wrapped.GetLoadPanelsOfSnowLoad(*args, **kwargs)

    def CreateWindLoadOnLoadPanels(self, *args, **kwargs):
        return self._wrapped.CreateWindLoadOnLoadPanels(*args, **kwargs)

    def DeleteWindLoadFromAllLoadPanels(self, *args, **kwargs):
        return self._wrapped.DeleteWindLoadFromAllLoadPanels(*args, **kwargs)

    def DeleteWindLoadFromLoadPanels(self, *args, **kwargs):
        return self._wrapped.DeleteWindLoadFromLoadPanels(*args, **kwargs)

    def GetLoadPanelsOfWindLoad(self, *args, **kwargs):
        return self._wrapped.GetLoadPanelsOfWindLoad(*args, **kwargs)

    def GetDomains_Surfaces_LoadPanels(self, *args, **kwargs):
        return self._wrapped.GetDomains_Surfaces_LoadPanels(*args, **kwargs)

    def AddLoadPanelConcentrated(self, *args, **kwargs):
        return self._wrapped.AddLoadPanelConcentrated(*args, **kwargs)

    def AddLoadPanelLinear(self, *args, **kwargs):
        return self._wrapped.AddLoadPanelLinear(*args, **kwargs)

    def AddLoadPanelPolyArea(self, *args, **kwargs):
        return self._wrapped.AddLoadPanelPolyArea(*args, **kwargs)

    def AddLoadPanelPolyLine(self, *args, **kwargs):
        return self._wrapped.AddLoadPanelPolyLine(*args, **kwargs)

    def ConvertDerivedSurfaceLoad(self, *args, **kwargs):
        return self._wrapped.ConvertDerivedSurfaceLoad(*args, **kwargs)

    def ConvertSelectedDerivedSurfaceLoad(self, *args, **kwargs):
        return self._wrapped.ConvertSelectedDerivedSurfaceLoad(*args, **kwargs)

    def CreateStandardSeismicLoads_V153(self, *args, **kwargs):
        return self._wrapped.CreateStandardSeismicLoads_V153(*args, **kwargs)

    def AddNodalForces(self, *args, **kwargs):
        return self._wrapped.AddNodalForces(*args, **kwargs)

    def AddLineSelfWeights(self, *args, **kwargs):
        return self._wrapped.AddLineSelfWeights(*args, **kwargs)

    def AddLineDistributeds(self, *args, **kwargs):
        return self._wrapped.AddLineDistributeds(*args, **kwargs)

    def AddSurfaceDistributeds(self, *args, **kwargs):
        return self._wrapped.AddSurfaceDistributeds(*args, **kwargs)

    def AddDomainConstants(self, *args, **kwargs):
        return self._wrapped.AddDomainConstants(*args, **kwargs)

    def AddDomainLinears(self, *args, **kwargs):
        return self._wrapped.AddDomainLinears(*args, **kwargs)

    def AddDomainConstant_V154(self, *args, **kwargs):
        return self._wrapped.AddDomainConstant_V154(*args, **kwargs)

    def AddSurfaceSelfWeights(self, *args, **kwargs):
        return self._wrapped.AddSurfaceSelfWeights(*args, **kwargs)

    def AddDomainSelfWeights(self, *args, **kwargs):
        return self._wrapped.AddDomainSelfWeights(*args, **kwargs)

    def AddNodalMass(self, *args, **kwargs):
        return self._wrapped.AddNodalMass(*args, **kwargs)

    def ModifyNodalMass(self, *args, **kwargs):
        return self._wrapped.ModifyNodalMass(*args, **kwargs)

    def DeleteNodalMass(self, *args, **kwargs):
        return self._wrapped.DeleteNodalMass(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def AddDomainPolyAssoc_V161(self, *args, **kwargs):
        return self._wrapped.AddDomainPolyAssoc_V161(*args, **kwargs)


class AxisVMDomains(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def GenerateMeshOnSelectedDomains(self, *args, **kwargs):
        return self._wrapped.GenerateMeshOnSelectedDomains(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def SelectAllWalls(self, *args, **kwargs):
        return self._wrapped.SelectAllWalls(*args, **kwargs)

    def SelectAllSlabs(self, *args, **kwargs):
        return self._wrapped.SelectAllSlabs(*args, **kwargs)

    def SelectAllOthers(self, *args, **kwargs):
        return self._wrapped.SelectAllOthers(*args, **kwargs)

    def SelectAllWallsAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllWallsAtStorey(*args, **kwargs)

    def SelectAllSlabsAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllSlabsAtStorey(*args, **kwargs)

    def SelectAllOthersAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllOthersAtStorey(*args, **kwargs)

    def GetSelectedWallIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedWallIds(*args, **kwargs)

    def GetSelectedSlabIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedSlabIds(*args, **kwargs)

    def GetSelectedOtherIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedOtherIds(*args, **kwargs)

    def RenameSelectedDomains(self, *args, **kwargs):
        return self._wrapped.RenameSelectedDomains(*args, **kwargs)

    def DeleteReinforcementParametersFromSelectedDomains(
            self, *args, **kwargs):
        return self._wrapped.DeleteReinforcementParametersFromSelectedDomains(
            *args, **kwargs)

    def GenerateMeshOnSelectedDomainsWithOriginalParams(self, *args, **kwargs):
        return self._wrapped.GenerateMeshOnSelectedDomainsWithOriginalParams(
            *args, **kwargs)

    def DeleteNameOfAllDomains(self, *args, **kwargs):
        return self._wrapped.DeleteNameOfAllDomains(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def StiffnessReduction(self) -> int:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: int):
        self._wrapped.StiffnessReduction = Value

    @property
    def Attributes(self) -> 'AxisVMAttributes':
        return self._wrapped.Attributes

    @property
    def Attachments(self) -> 'AxisVMAttachments':
        return self._wrapped.Attachments

    def GetVariableThickness(self, *args, **kwargs):
        return self._wrapped.GetVariableThickness(*args, **kwargs)

    def SetVariableThickness(self, *args, **kwargs):
        return self._wrapped.SetVariableThickness(*args, **kwargs)

    def GetExcentricity(self, *args, **kwargs):
        return self._wrapped.GetExcentricity(*args, **kwargs)

    def SetExcentricity(self, *args, **kwargs):
        return self._wrapped.SetExcentricity(*args, **kwargs)

    def CreateNewExcentricityGroup(self, *args, **kwargs):
        return self._wrapped.CreateNewExcentricityGroup(*args, **kwargs)

    def GetRibbedDomainParameters(self, *args, **kwargs):
        return self._wrapped.GetRibbedDomainParameters(*args, **kwargs)

    def SetRibbedDomainParameters(self, *args, **kwargs):
        return self._wrapped.SetRibbedDomainParameters(*args, **kwargs)

    def GetXLAMParameters(self, *args, **kwargs):
        return self._wrapped.GetXLAMParameters(*args, **kwargs)

    def SetXLAMParameters(self, *args, **kwargs):
        return self._wrapped.SetXLAMParameters(*args, **kwargs)

    @property
    def IsRibbed(self) -> int:
        return self._wrapped.IsRibbed

    @property
    def IsXLAM(self) -> int:
        return self._wrapped.IsXLAM

    @property
    def IsExcentic(self) -> int:
        return self._wrapped.IsExcentic

    @property
    def HasVariableThickness(self) -> int:
        return self._wrapped.HasVariableThickness

    def DeleteMeshes(self, *args, **kwargs):
        return self._wrapped.DeleteMeshes(*args, **kwargs)

    def DeleteAllMeshes(self, *args, **kwargs):
        return self._wrapped.DeleteAllMeshes(*args, **kwargs)

    def GetCustomStiffnessMatrix(self, *args, **kwargs):
        return self._wrapped.GetCustomStiffnessMatrix(*args, **kwargs)

    def SetCustomStiffnessMatrix(self, *args, **kwargs):
        return self._wrapped.SetCustomStiffnessMatrix(*args, **kwargs)

    def CutSelected(self, *args, **kwargs):
        return self._wrapped.CutSelected(*args, **kwargs)

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)

    def BulkGetDomains(self, *args, **kwargs):
        return self._wrapped.BulkGetDomains(*args, **kwargs)

    def BulkSetDomains(self, *args, **kwargs):
        return self._wrapped.BulkSetDomains(*args, **kwargs)

    @property
    def StiffnessReduction_V153(self) -> int:
        return self._wrapped.StiffnessReduction_V153

    @StiffnessReduction_V153.setter
    def StiffnessReduction_V153(self, Value: int):
        self._wrapped.StiffnessReduction_V153 = Value

    def AddHollowCore(self, *args, **kwargs):
        return self._wrapped.AddHollowCore(*args, **kwargs)

    def GetXLAMParameters_V161(self, *args, **kwargs):
        return self._wrapped.GetXLAMParameters_V161(*args, **kwargs)

    def SetXLAMParameters_V161(self, *args, **kwargs):
        return self._wrapped.SetXLAMParameters_V161(*args, **kwargs)

    def AddXLAM(self, *args, **kwargs):
        return self._wrapped.AddXLAM(*args, **kwargs)

    def GetTrapezoidalParameters(self, *args, **kwargs):
        return self._wrapped.GetTrapezoidalParameters(*args, **kwargs)

    def SetTrapezoidalParameters(self, *args, **kwargs):
        return self._wrapped.SetTrapezoidalParameters(*args, **kwargs)

    def AddTrapezoidal(self, *args, **kwargs):
        return self._wrapped.AddTrapezoidal(*args, **kwargs)

    @property
    def IsTrapezoidal(self) -> int:
        return self._wrapped.IsTrapezoidal

    def GetCompositeRibParameters(self, *args, **kwargs):
        return self._wrapped.GetCompositeRibParameters(*args, **kwargs)

    def SetCompositeRibParameters(self, *args, **kwargs):
        return self._wrapped.SetCompositeRibParameters(*args, **kwargs)

    def AddCompositeRib(self, *args, **kwargs):
        return self._wrapped.AddCompositeRib(*args, **kwargs)

    @property
    def IsCompositeRib(self) -> int:
        return self._wrapped.IsCompositeRib

    def SetRibbedDomainActual(self, *args, **kwargs):
        return self._wrapped.SetRibbedDomainActual(*args, **kwargs)

    def GetHollowCoreParameters(self, *args, **kwargs):
        return self._wrapped.GetHollowCoreParameters(*args, **kwargs)

    def SetHollowCoreParameters(self, *args, **kwargs):
        return self._wrapped.SetHollowCoreParameters(*args, **kwargs)

    @property
    def IsHollowCore(self) -> int:
        return self._wrapped.IsHollowCore


class AxisVMSurfaces(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def GetAllCoordinatesOfSurfaces(self, *args, **kwargs):
        return self._wrapped.GetAllCoordinatesOfSurfaces(*args, **kwargs)

    def DeleteReinforcementParametersFromSelectedSurfaces(
            self, *args, **kwargs):
        return self._wrapped.DeleteReinforcementParametersFromSelectedSurfaces(
            *args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def GetAllCoordinatesOfSurfaces_vb(self, *args, **kwargs):
        return self._wrapped.GetAllCoordinatesOfSurfaces_vb(*args, **kwargs)

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def StiffnessReduction(self) -> int:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: int):
        self._wrapped.StiffnessReduction = Value

    @property
    def Attributes(self) -> 'AxisVMAttributes':
        return self._wrapped.Attributes

    @property
    def Attachments(self) -> 'AxisVMAttachments':
        return self._wrapped.Attachments

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)

    def BulkGetSurfaces(self, *args, **kwargs):
        return self._wrapped.BulkGetSurfaces(*args, **kwargs)

    def BulkSetSurfaces(self, *args, **kwargs):
        return self._wrapped.BulkSetSurfaces(*args, **kwargs)

    @property
    def StiffnessReduction_V153(self) -> int:
        return self._wrapped.StiffnessReduction_V153

    @StiffnessReduction_V153.setter
    def StiffnessReduction_V153(self, Value: int):
        self._wrapped.StiffnessReduction_V153 = Value


class AxisVMCalculation(AxWrapper):

    def LinearAnalysis(self, *args, **kwargs):
        return self._wrapped.LinearAnalysis(*args, **kwargs)

    def NonLinearAnalysis(self, *args, **kwargs):
        return self._wrapped.NonLinearAnalysis(*args, **kwargs)

    def Vibration(self, *args, **kwargs):
        return self._wrapped.Vibration(*args, **kwargs)

    def Buckling(self, *args, **kwargs):
        return self._wrapped.Buckling(*args, **kwargs)

    def NonLinearVibration(self, *args, **kwargs):
        return self._wrapped.NonLinearVibration(*args, **kwargs)

    @property
    def CallMainProgress(self) -> int:
        return self._wrapped.CallMainProgress

    @CallMainProgress.setter
    def CallMainProgress(self, Value: int):
        self._wrapped.CallMainProgress = Value

    def LinearAnalysis2(self, *args, **kwargs):
        return self._wrapped.LinearAnalysis2(*args, **kwargs)

    def NonLinearAnalysis2(self, *args, **kwargs):
        return self._wrapped.NonLinearAnalysis2(*args, **kwargs)

    def Vibration2(self, *args, **kwargs):
        return self._wrapped.Vibration2(*args, **kwargs)

    def Buckling2(self, *args, **kwargs):
        return self._wrapped.Buckling2(*args, **kwargs)

    def NonLinearVibration2(self, *args, **kwargs):
        return self._wrapped.NonLinearVibration2(*args, **kwargs)

    def DynamicAnalysis(self, *args, **kwargs):
        return self._wrapped.DynamicAnalysis(*args, **kwargs)

    def PushOverAnalysis(self, *args, **kwargs):
        return self._wrapped.PushOverAnalysis(*args, **kwargs)


class AxisVMResults(AxWrapper):

    @property
    def Displacements(self) -> 'AxisVMDisplacements':
        return self._wrapped.Displacements

    @property
    def Forces(self) -> 'AxisVMForces':
        return self._wrapped.Forces

    @property
    def Stresses(self) -> 'AxisVMStresses':
        return self._wrapped.Stresses

    @property
    def ResultCaseCount(self) -> int:
        return self._wrapped.ResultCaseCount

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @property
    def LoadLevelCount(self) -> int:
        return self._wrapped.LoadLevelCount

    @property
    def ModeShapeCount(self) -> int:
        return self._wrapped.ModeShapeCount

    @property
    def ResultCaseOfLoadCase(self) -> int:
        return self._wrapped.ResultCaseOfLoadCase

    @property
    def ResultCaseOfLoadCombination(self) -> int:
        return self._wrapped.ResultCaseOfLoadCombination

    @property
    def Frequency(self) -> int:
        return self._wrapped.Frequency

    def GetAllFrequencies(self, *args, **kwargs):
        return self._wrapped.GetAllFrequencies(*args, **kwargs)

    def GetFrequencyParameters(self, *args, **kwargs):
        return self._wrapped.GetFrequencyParameters(*args, **kwargs)

    @property
    def Ncr(self) -> int:
        return self._wrapped.Ncr

    def GetAllNcr(self, *args, **kwargs):
        return self._wrapped.GetAllNcr(*args, **kwargs)

    def GetNcrParameters(self, *args, **kwargs):
        return self._wrapped.GetNcrParameters(*args, **kwargs)

    def GetNonLinearAnalysisResultInfo(self, *args, **kwargs):
        return self._wrapped.GetNonLinearAnalysisResultInfo(*args, **kwargs)

    def GetNonLinearAnalysisParameters(self, *args, **kwargs):
        return self._wrapped.GetNonLinearAnalysisParameters(*args, **kwargs)

    def GetVibrationParameters(self, *args, **kwargs):
        return self._wrapped.GetVibrationParameters(*args, **kwargs)

    def GetNonLinearVibrationParameters(self, *args, **kwargs):
        return self._wrapped.GetNonLinearVibrationParameters(*args, **kwargs)

    def GetBucklingParameters(self, *args, **kwargs):
        return self._wrapped.GetBucklingParameters(*args, **kwargs)

    @property
    def SteelDesignResults(self) -> 'AxisVMSteelDesignResults':
        return self._wrapped.SteelDesignResults

    @property
    def CalculatedReinforcement(self) -> 'AxisVMCalculatedReinforcement':
        return self._wrapped.CalculatedReinforcement

    @property
    def ReinforcementCheck(self) -> 'AxisVMReinforcementCheck':
        return self._wrapped.ReinforcementCheck

    @property
    def ShearCapacity(self) -> 'AxisVMShearCapacity':
        return self._wrapped.ShearCapacity

    @property
    def CrackWidth(self) -> 'AxisVMCrackWidth':
        return self._wrapped.CrackWidth

    @property
    def Velocity(self) -> 'AxisVMVelocity':
        return self._wrapped.Velocity

    @property
    def Acceleration(self) -> 'AxisVMAcceleration':
        return self._wrapped.Acceleration

    def GetModeActive(self, *args, **kwargs):
        return self._wrapped.GetModeActive(*args, **kwargs)

    def SetModeActive(self, *args, **kwargs):
        return self._wrapped.SetModeActive(*args, **kwargs)

    def GetSeismicEqCoeff(self, *args, **kwargs):
        return self._wrapped.GetSeismicEqCoeff(*args, **kwargs)

    def GetCapacityCurve(self, *args, **kwargs):
        return self._wrapped.GetCapacityCurve(*args, **kwargs)

    @property
    def TimeStepCount(self) -> int:
        return self._wrapped.TimeStepCount

    @property
    def TimberDesignResults(self) -> 'AxisVMTimberDesignResults':
        return self._wrapped.TimberDesignResults

    def GetCapacityCurvePushOver(self, *args, **kwargs):
        return self._wrapped.GetCapacityCurvePushOver(*args, **kwargs)

    def GetAllModalMassfactors(self, *args, **kwargs):
        return self._wrapped.GetAllModalMassfactors(*args, **kwargs)

    def GetAllActivatedMasses(self, *args, **kwargs):
        return self._wrapped.GetAllActivatedMasses(*args, **kwargs)

    def GetUsedMassOfNodes(self, *args, **kwargs):
        return self._wrapped.GetUsedMassOfNodes(*args, **kwargs)

    def GetResultsValid(self, *args, **kwargs):
        return self._wrapped.GetResultsValid(*args, **kwargs)

    def GetSectionCoordinates(self, *args, **kwargs):
        return self._wrapped.GetSectionCoordinates(*args, **kwargs)

    def SaveXYchartToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveXYchartToMetaFile(*args, **kwargs)

    def GetXYchartOptionsJSON(self, *args, **kwargs):
        return self._wrapped.GetXYchartOptionsJSON(*args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep

    def UpdateResults(self, *args, **kwargs):
        return self._wrapped.UpdateResults(*args, **kwargs)

    def GetTotalLoadsByLoadCaseID(self, *args, **kwargs):
        return self._wrapped.GetTotalLoadsByLoadCaseID(*args, **kwargs)

    @property
    def Strains(self) -> 'AxisVMStrains':
        return self._wrapped.Strains

    @property
    def VerticalDisplacements(self) -> 'AxisVMVerticalDisplacements':
        return self._wrapped.VerticalDisplacements

    @property
    def CalcCrackWidth(self) -> 'AxisVMCalcCrackWidth':
        return self._wrapped.CalcCrackWidth


class AxisVMMembers(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def ChangeLocalDirection(self, *args, **kwargs):
        return self._wrapped.ChangeLocalDirection(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def DeleteMesh(self, *args, **kwargs):
        return self._wrapped.DeleteMesh(*args, **kwargs)

    def DeleteMeshFromSelectedItems(self, *args, **kwargs):
        return self._wrapped.DeleteMeshFromSelectedItems(*args, **kwargs)

    def SelectAllColumns(self, *args, **kwargs):
        return self._wrapped.SelectAllColumns(*args, **kwargs)

    def SelectAllBeams(self, *args, **kwargs):
        return self._wrapped.SelectAllBeams(*args, **kwargs)

    def SelectAllOthers(self, *args, **kwargs):
        return self._wrapped.SelectAllOthers(*args, **kwargs)

    def SelectAllColumnsAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllColumnsAtStorey(*args, **kwargs)

    def SelectAllBeamsAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllBeamsAtStorey(*args, **kwargs)

    def SelectAllOthersAtStorey(self, *args, **kwargs):
        return self._wrapped.SelectAllOthersAtStorey(*args, **kwargs)

    def GetSelectedColumnIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedColumnIds(*args, **kwargs)

    def GetSelectedBeamIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedBeamIds(*args, **kwargs)

    def GetSelectedOtherIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedOtherIds(*args, **kwargs)

    def RenameSelectedBeams(self, *args, **kwargs):
        return self._wrapped.RenameSelectedBeams(*args, **kwargs)

    def RenameSelectedRibs(self, *args, **kwargs):
        return self._wrapped.RenameSelectedRibs(*args, **kwargs)

    def GenerateMeshWithParamsOnSelectedItems(self, *args, **kwargs):
        return self._wrapped.GenerateMeshWithParamsOnSelectedItems(
            *args, **kwargs)

    def DeleteNameOfAllBeams(self, *args, **kwargs):
        return self._wrapped.DeleteNameOfAllBeams(*args, **kwargs)

    def DeleteNameOfAllRibs(self, *args, **kwargs):
        return self._wrapped.DeleteNameOfAllRibs(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def IndexOf_vb(self, *args, **kwargs):
        return self._wrapped.IndexOf_vb(*args, **kwargs)

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    def RenameSelectedTrusses(self, *args, **kwargs):
        return self._wrapped.RenameSelectedTrusses(*args, **kwargs)

    def DeleteNameOfAllTrussses(self, *args, **kwargs):
        return self._wrapped.DeleteNameOfAllTrussses(*args, **kwargs)

    @property
    def StiffnessReduction_A(self) -> int:
        return self._wrapped.StiffnessReduction_A

    @StiffnessReduction_A.setter
    def StiffnessReduction_A(self, Value: int):
        self._wrapped.StiffnessReduction_A = Value

    @property
    def StiffnessReduction_I(self) -> int:
        return self._wrapped.StiffnessReduction_I

    @StiffnessReduction_I.setter
    def StiffnessReduction_I(self, Value: int):
        self._wrapped.StiffnessReduction_I = Value

    @property
    def Attributes(self) -> 'AxisVMAttributes':
        return self._wrapped.Attributes

    @property
    def Attachments(self) -> 'AxisVMAttachments':
        return self._wrapped.Attachments

    @property
    def LocalX_is_ij(self) -> int:
        return self._wrapped.LocalX_is_ij

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    def GetContinuousMemberIDs(self, *args, **kwargs):
        return self._wrapped.GetContinuousMemberIDs(*args, **kwargs)

    def AssembleSelectedMembers(self, *args, **kwargs):
        return self._wrapped.AssembleSelectedMembers(*args, **kwargs)

    def BulkGetMembers(self, *args, **kwargs):
        return self._wrapped.BulkGetMembers(*args, **kwargs)

    def BulkSetMembers(self, *args, **kwargs):
        return self._wrapped.BulkSetMembers(*args, **kwargs)

    @property
    def StiffnessReduction(self) -> int:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: int):
        self._wrapped.StiffnessReduction = Value

    def BulkGetMembers_V161(self, *args, **kwargs):
        return self._wrapped.BulkGetMembers_V161(*args, **kwargs)

    def BulkSetMembers_V161(self, *args, **kwargs):
        return self._wrapped.BulkSetMembers_V161(*args, **kwargs)

    def ClearEccentricities(self, *args, **kwargs):
        return self._wrapped.ClearEccentricities(*args, **kwargs)


class AxisVMSpectrum(AxWrapper):

    def LoadFromFile(self, *args, **kwargs):
        return self._wrapped.LoadFromFile(*args, **kwargs)

    def SaveToFile(self, *args, **kwargs):
        return self._wrapped.SaveToFile(*args, **kwargs)

    @property
    def Parametric(self) -> int:
        return self._wrapped.Parametric

    def GetSpectrumData(self, *args, **kwargs):
        return self._wrapped.GetSpectrumData(*args, **kwargs)

    def SetSpectrumData(self, *args, **kwargs):
        return self._wrapped.SetSpectrumData(*args, **kwargs)

    def SetPoints(self, *args, **kwargs):
        return self._wrapped.SetPoints(*args, **kwargs)

    def SetPoints_vb(self, *args, **kwargs):
        return self._wrapped.SetPoints_vb(*args, **kwargs)

    def GetPoints(self, *args, **kwargs):
        return self._wrapped.GetPoints(*args, **kwargs)

    def Disable(self, *args, **kwargs):
        return self._wrapped.Disable(*args, **kwargs)

    def GetSpectrumData_V153(self, *args, **kwargs):
        return self._wrapped.GetSpectrumData_V153(*args, **kwargs)

    def SetSpectrumData_V153(self, *args, **kwargs):
        return self._wrapped.SetSpectrumData_V153(*args, **kwargs)

    @property
    def Disabled(self) -> int:
        return self._wrapped.Disabled


class AxisVMSeismicStoreys(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def IndexOfZ(self, *args, **kwargs):
        return self._wrapped.IndexOfZ(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def HasEmptyStorey(self) -> int:
        return self._wrapped.HasEmptyStorey

    def DeleteEmptyStoreys(self, *args, **kwargs):
        return self._wrapped.DeleteEmptyStoreys(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def LevelId(self) -> int:
        return self._wrapped.LevelId

    @property
    def LevelZ(self) -> int:
        return self._wrapped.LevelZ

    @LevelZ.setter
    def LevelZ(self, Value: int):
        self._wrapped.LevelZ = Value

    @property
    def Height(self) -> int:
        return self._wrapped.Height

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)

    def GetSeismicSensitivityResults(self, *args, **kwargs):
        return self._wrapped.GetSeismicSensitivityResults(*args, **kwargs)


class AxisVMLinkElements(AxWrapper):

    def AddNN(self, *args, **kwargs):
        return self._wrapped.AddNN(*args, **kwargs)

    def AddLL(self, *args, **kwargs):
        return self._wrapped.AddLL(*args, **kwargs)

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def LinkElementType(self) -> int:
        return self._wrapped.LinkElementType

    def GetRec(self, *args, **kwargs):
        return self._wrapped.GetRec(*args, **kwargs)

    def SetRec(self, *args, **kwargs):
        return self._wrapped.SetRec(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)


class AxisVMEdgeConnections(AxWrapper):

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetRec(self, *args, **kwargs):
        return self._wrapped.GetRec(*args, **kwargs)

    def SetRec(self, *args, **kwargs):
        return self._wrapped.SetRec(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)


class AxisVMSteelDesignMembers(AxWrapper):

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetDesignParameters(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters(*args, **kwargs)

    def SetDesignParameters(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def GetLineIds(self, *args, **kwargs):
        return self._wrapped.GetLineIds(*args, **kwargs)

    @property
    def Length(self) -> int:
        return self._wrapped.Length

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def Add2(self, *args, **kwargs):
        return self._wrapped.Add2(*args, **kwargs)

    def GetDesignParameters2(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters2(*args, **kwargs)

    def SetDesignParameters2(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters2(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def Add2_vb(self, *args, **kwargs):
        return self._wrapped.Add2_vb(*args, **kwargs)

    def Add3(self, *args, **kwargs):
        return self._wrapped.Add3(*args, **kwargs)

    def GetDesignParameters3(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters3(*args, **kwargs)

    def SetDesignParameters3(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters3(*args, **kwargs)

    def GetLateralSupports(self, *args, **kwargs):
        return self._wrapped.GetLateralSupports(*args, **kwargs)

    def SetLateralSupports(self, *args, **kwargs):
        return self._wrapped.SetLateralSupports(*args, **kwargs)

    @property
    def CrossSetionID(self) -> int:
        return self._wrapped.CrossSetionID

    @CrossSetionID.setter
    def CrossSetionID(self, Value: int):
        self._wrapped.CrossSetionID = Value

    def Add_V153(self, *args, **kwargs):
        return self._wrapped.Add_V153(*args, **kwargs)

    def GetDesignParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters_V153(*args, **kwargs)

    def SetDesignParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters_V153(*args, **kwargs)


class AxisVMActualReinforcement(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def AddDomainReinforcement(self, *args, **kwargs):
        return self._wrapped.AddDomainReinforcement(*args, **kwargs)

    def AddPolygonReinforcement(self, *args, **kwargs):
        return self._wrapped.AddPolygonReinforcement(*args, **kwargs)

    @property
    def ActualReinforcementType(self) -> int:
        return self._wrapped.ActualReinforcementType

    def IndexOfDomainReinforcement(self, *args, **kwargs):
        return self._wrapped.IndexOfDomainReinforcement(*args, **kwargs)

    def GetReinforcement(self, *args, **kwargs):
        return self._wrapped.GetReinforcement(*args, **kwargs)

    def GetSurfaceReinforcement(self, *args, **kwargs):
        return self._wrapped.GetSurfaceReinforcement(*args, **kwargs)

    def GetSurfaceReinforcements(self, *args, **kwargs):
        return self._wrapped.GetSurfaceReinforcements(*args, **kwargs)

    def AddDomainReinforcement_vb(self, *args, **kwargs):
        return self._wrapped.AddDomainReinforcement_vb(*args, **kwargs)

    def AddPolygonReinforcement_vb(self, *args, **kwargs):
        return self._wrapped.AddPolygonReinforcement_vb(*args, **kwargs)


class AxisVMDomainSupports(AxWrapper):

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def AddDomainElasticFoundation(self, *args, **kwargs):
        return self._wrapped.AddDomainElasticFoundation(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    @property
    def DomainId(self) -> int:
        return self._wrapped.DomainId

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def AddDomainPasternakSupport(self, *args, **kwargs):
        return self._wrapped.AddDomainPasternakSupport(*args, **kwargs)


class AxisVMStoreys(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def IndexOfZ(self, *args, **kwargs):
        return self._wrapped.IndexOfZ(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def HasEmptyStorey(self) -> int:
        return self._wrapped.HasEmptyStorey

    def DeleteEmptyStoreys(self, *args, **kwargs):
        return self._wrapped.DeleteEmptyStoreys(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def LevelId(self) -> int:
        return self._wrapped.LevelId

    @property
    def LevelZ(self) -> int:
        return self._wrapped.LevelZ

    @LevelZ.setter
    def LevelZ(self, Value: int):
        self._wrapped.LevelZ = Value

    @property
    def Height(self) -> int:
        return self._wrapped.Height

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)

    @property
    def AutoSearchStyle(self) -> int:
        return self._wrapped.AutoSearchStyle

    @AutoSearchStyle.setter
    def AutoSearchStyle(self, Value: int):
        self._wrapped.AutoSearchStyle = Value

    def AutoSearch(self, *args, **kwargs):
        return self._wrapped.AutoSearch(*args, **kwargs)


class AxisVMTimberDesignMembers(AxWrapper):

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetDesignParameters(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters(*args, **kwargs)

    def SetDesignParameters(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def GetLineIds(self, *args, **kwargs):
        return self._wrapped.GetLineIds(*args, **kwargs)

    @property
    def Length(self) -> int:
        return self._wrapped.Length

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def Add_V153(self, *args, **kwargs):
        return self._wrapped.Add_V153(*args, **kwargs)

    def GetDesignParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetDesignParameters_V153(*args, **kwargs)

    def SetDesignParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetDesignParameters_V153(*args, **kwargs)


class AxisVMDynamicLoadFunctions(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def PointCount(self) -> int:
        return self._wrapped.PointCount

    def DeletePoint(self, *args, **kwargs):
        return self._wrapped.DeletePoint(*args, **kwargs)

    def DeletePoints(self, *args, **kwargs):
        return self._wrapped.DeletePoints(*args, **kwargs)

    def AddPoint(self, *args, **kwargs):
        return self._wrapped.AddPoint(*args, **kwargs)

    def GetPoints(self, *args, **kwargs):
        return self._wrapped.GetPoints(*args, **kwargs)

    def Modify(self, *args, **kwargs):
        return self._wrapped.Modify(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddFromFile(self, *args, **kwargs):
        return self._wrapped.AddFromFile(*args, **kwargs)

    def SaveToFile(self, *args, **kwargs):
        return self._wrapped.SaveToFile(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def Modify_vb(self, *args, **kwargs):
        return self._wrapped.Modify_vb(*args, **kwargs)


class AxisVMTimeIncrementFunctions(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def PointCount(self) -> int:
        return self._wrapped.PointCount

    def DeletePoint(self, *args, **kwargs):
        return self._wrapped.DeletePoint(*args, **kwargs)

    def DeletePoints(self, *args, **kwargs):
        return self._wrapped.DeletePoints(*args, **kwargs)

    def AddPoint(self, *args, **kwargs):
        return self._wrapped.AddPoint(*args, **kwargs)

    def GetPoints(self, *args, **kwargs):
        return self._wrapped.GetPoints(*args, **kwargs)

    def Modify(self, *args, **kwargs):
        return self._wrapped.Modify(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddFromFile(self, *args, **kwargs):
        return self._wrapped.AddFromFile(*args, **kwargs)

    def SaveToFile(self, *args, **kwargs):
        return self._wrapped.SaveToFile(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def Modify_vb(self, *args, **kwargs):
        return self._wrapped.Modify_vb(*args, **kwargs)


class AxisVMIncrementFunctions(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def PointCount(self) -> int:
        return self._wrapped.PointCount

    def DeletePoint(self, *args, **kwargs):
        return self._wrapped.DeletePoint(*args, **kwargs)

    def DeletePoints(self, *args, **kwargs):
        return self._wrapped.DeletePoints(*args, **kwargs)

    def AddPoint(self, *args, **kwargs):
        return self._wrapped.AddPoint(*args, **kwargs)

    def GetPoints(self, *args, **kwargs):
        return self._wrapped.GetPoints(*args, **kwargs)

    def Modify(self, *args, **kwargs):
        return self._wrapped.Modify(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddFromFile(self, *args, **kwargs):
        return self._wrapped.AddFromFile(*args, **kwargs)

    def SaveToFile(self, *args, **kwargs):
        return self._wrapped.SaveToFile(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def Modify_vb(self, *args, **kwargs):
        return self._wrapped.Modify_vb(*args, **kwargs)


class AxisVMDiaphragm(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def AddSelectedLines(self, *args, **kwargs):
        return self._wrapped.AddSelectedLines(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def GetLines(self, *args, **kwargs):
        return self._wrapped.GetLines(*args, **kwargs)

    def GetDOF(self, *args, **kwargs):
        return self._wrapped.GetDOF(*args, **kwargs)

    def RemoveLinesFromDiaphragm(self, *args, **kwargs):
        return self._wrapped.RemoveLinesFromDiaphragm(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def RemoveLinesFromDiaphragm_vb(self, *args, **kwargs):
        return self._wrapped.RemoveLinesFromDiaphragm_vb(*args, **kwargs)


class AxisVMRebarSteelGrades(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def AddFromCatalog(self, *args, **kwargs):
        return self._wrapped.AddFromCatalog(*args, **kwargs)

    def AddFromCatalogFile(self, *args, **kwargs):
        return self._wrapped.AddFromCatalogFile(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    @property
    def NationalDesignCode(self) -> int:
        return self._wrapped.NationalDesignCode

    def GetData(self, *args, **kwargs):
        return self._wrapped.GetData(*args, **kwargs)

    def SetData(self, *args, **kwargs):
        return self._wrapped.SetData(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID


class AxisVMMovingLoads(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetMovingLoadType(self, *args, **kwargs):
        return self._wrapped.GetMovingLoadType(*args, **kwargs)

    def GetMovingLoadOnBeam(self, *args, **kwargs):
        return self._wrapped.GetMovingLoadOnBeam(*args, **kwargs)

    def GetMovingLoadOnDomain(self, *args, **kwargs):
        return self._wrapped.GetMovingLoadOnDomain(*args, **kwargs)

    def SetAsMovingLoadOnBeam(self, *args, **kwargs):
        return self._wrapped.SetAsMovingLoadOnBeam(*args, **kwargs)

    def SetAsMovingLoadOnDomain(self, *args, **kwargs):
        return self._wrapped.SetAsMovingLoadOnDomain(*args, **kwargs)

    def AddMovingLoadOnBeam(self, *args, **kwargs):
        return self._wrapped.AddMovingLoadOnBeam(*args, **kwargs)

    def AddMovingLoadOnDomain(self, *args, **kwargs):
        return self._wrapped.AddMovingLoadOnDomain(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)


class AxisVMColumnRebars(AxWrapper):

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteRebarsFrom(self, *args, **kwargs):
        return self._wrapped.DeleteRebarsFrom(*args, **kwargs)

    def GetRebars(self, *args, **kwargs):
        return self._wrapped.GetRebars(*args, **kwargs)

    def SetRebars(self, *args, **kwargs):
        return self._wrapped.SetRebars(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def CrossSectionID(self) -> int:
        return self._wrapped.CrossSectionID

    @CrossSectionID.setter
    def CrossSectionID(self, Value: int):
        self._wrapped.CrossSectionID = Value

    @property
    def RebarCount(self) -> int:
        return self._wrapped.RebarCount

    @property
    def RebarsArea(self) -> int:
        return self._wrapped.RebarsArea

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def SetRebars_vb(self, *args, **kwargs):
        return self._wrapped.SetRebars_vb(*args, **kwargs)


class AxisVMRCColumnChecking(AxWrapper):

    def GenererateNMInteractionDiagByLine(self, *args, **kwargs):
        return self._wrapped.GenererateNMInteractionDiagByLine(*args, **kwargs)

    def GenererateNMInteractionDiagByMember(self, *args, **kwargs):
        return self._wrapped.GenererateNMInteractionDiagByMember(
            *args, **kwargs)

    def GenererateNMInteractionDiagByParameters(self, *args, **kwargs):
        return self._wrapped.GenererateNMInteractionDiagByParameters(
            *args, **kwargs)

    def GetMyMzPolyByNx(self, *args, **kwargs):
        return self._wrapped.GetMyMzPolyByNx(*args, **kwargs)

    def GetNMInteractionDiagMinMax(self, *args, **kwargs):
        return self._wrapped.GetNMInteractionDiagMinMax(*args, **kwargs)

    def CheckMembers(self, *args, **kwargs):
        return self._wrapped.CheckMembers(*args, **kwargs)

    def CheckByParameters(self, *args, **kwargs):
        return self._wrapped.CheckByParameters(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def CheckMembers_vb(self, *args, **kwargs):
        return self._wrapped.CheckMembers_vb(*args, **kwargs)

    def CheckByParameters_vb(self, *args, **kwargs):
        return self._wrapped.CheckByParameters_vb(*args, **kwargs)

    def CheckVTMembers(self, *args, **kwargs):
        return self._wrapped.CheckVTMembers(*args, **kwargs)

    def CheckVTByParameters(self, *args, **kwargs):
        return self._wrapped.CheckVTByParameters(*args, **kwargs)

    def CheckVTMembers_vb(self, *args, **kwargs):
        return self._wrapped.CheckVTMembers_vb(*args, **kwargs)

    def CheckVTByParameters_vb(self, *args, **kwargs):
        return self._wrapped.CheckVTByParameters_vb(*args, **kwargs)

    def CheckVTByParameters_EQCapacityDesign(self, *args, **kwargs):
        return self._wrapped.CheckVTByParameters_EQCapacityDesign(
            *args, **kwargs)

    def CheckVTByParameters_EQCapacityDesign_vb(self, *args, **kwargs):
        return self._wrapped.CheckVTByParameters_EQCapacityDesign_vb(
            *args, **kwargs)


class AxisVMPushoverHingeFunctions(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def PointCount(self) -> int:
        return self._wrapped.PointCount

    def GetPoints(self, *args, **kwargs):
        return self._wrapped.GetPoints(*args, **kwargs)

    def Modify(self, *args, **kwargs):
        return self._wrapped.Modify(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddFromFile(self, *args, **kwargs):
        return self._wrapped.AddFromFile(*args, **kwargs)

    def SaveToFile(self, *args, **kwargs):
        return self._wrapped.SaveToFile(*args, **kwargs)

    def Add_vb(self, *args, **kwargs):
        return self._wrapped.Add_vb(*args, **kwargs)

    def Modify_vb(self, *args, **kwargs):
        return self._wrapped.Modify_vb(*args, **kwargs)


class AxisVMCriticalGroupCombinations(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Used(self) -> int:
        return self._wrapped.Used

    @Used.setter
    def Used(self, Value: int):
        self._wrapped.Used = Value

    @property
    def Editable(self) -> int:
        return self._wrapped.Editable

    def AddDefaultCombinations(self, *args, **kwargs):
        return self._wrapped.AddDefaultCombinations(*args, **kwargs)

    @property
    def Linking(self) -> int:
        return self._wrapped.Linking

    @Linking.setter
    def Linking(self, Value: int):
        self._wrapped.Linking = Value

    @property
    def LinkingEditable(self) -> int:
        return self._wrapped.LinkingEditable

    def Validate(self, *args, **kwargs):
        return self._wrapped.Validate(*args, **kwargs)


class AxisVMEnvelopes(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def ClearUserEnvelopes(self, *args, **kwargs):
        return self._wrapped.ClearUserEnvelopes(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @property
    def UserEnevelopeCount(self) -> int:
        return self._wrapped.UserEnevelopeCount

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def IndexOfName(self, *args, **kwargs):
        return self._wrapped.IndexOfName(*args, **kwargs)

    def IndexOfStandard(self, *args, **kwargs):
        return self._wrapped.IndexOfStandard(*args, **kwargs)

    def IndexOfUID(self, *args, **kwargs):
        return self._wrapped.IndexOfUID(*args, **kwargs)

    def IndexOfDefault(self, *args, **kwargs):
        return self._wrapped.IndexOfDefault(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    def GetEnvelope(self, *args, **kwargs):
        return self._wrapped.GetEnvelope(*args, **kwargs)

    def SetEnvelope(self, *args, **kwargs):
        return self._wrapped.SetEnvelope(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @property
    def Group(self) -> int:
        return self._wrapped.Group

    def Update(self, *args, **kwargs):
        return self._wrapped.Update(*args, **kwargs)


class AxisVMWindows(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def ActiveWindowIndex(self) -> int:
        return self._wrapped.ActiveWindowIndex

    @ActiveWindowIndex.setter
    def ActiveWindowIndex(self, Value: int):
        self._wrapped.ActiveWindowIndex = Value

    @property
    def ActiveWindow(self) -> 'AxisVMWindow':
        return self._wrapped.ActiveWindow

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Duplicate(self, *args, **kwargs):
        return self._wrapped.Duplicate(*args, **kwargs)

    def Remove(self, *args, **kwargs):
        return self._wrapped.Remove(*args, **kwargs)

    def GetCommonDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetCommonDisplayParameters(*args, **kwargs)

    def SetCommonDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetCommonDisplayParameters(*args, **kwargs)

    def GetStaticDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetStaticDisplayParameters(*args, **kwargs)

    def GetBucklingDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetBucklingDisplayParameters(*args, **kwargs)

    def GetVibrationDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetVibrationDisplayParameters(*args, **kwargs)

    def GetDynamicDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetDynamicDisplayParameters(*args, **kwargs)

    def GetRCDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetRCDesignDisplayParameters(*args, **kwargs)

    def GetSteelDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignDisplayParameters(*args, **kwargs)

    def GetTimberDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignDisplayParameters(*args, **kwargs)

    def GetDisplayOptions(self, *args, **kwargs):
        return self._wrapped.GetDisplayOptions(*args, **kwargs)

    def SetStaticDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetStaticDisplayParameters(*args, **kwargs)

    def SetBucklingDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetBucklingDisplayParameters(*args, **kwargs)

    def SetVibrationDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetVibrationDisplayParameters(*args, **kwargs)

    def SetDynamicDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetDynamicDisplayParameters(*args, **kwargs)

    def SetRCDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetRCDesignDisplayParameters(*args, **kwargs)

    def SetSteelDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetSteelDesignDisplayParameters(*args, **kwargs)

    def SetTimberDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetTimberDesignDisplayParameters(*args, **kwargs)

    def SetDisplayOptions(self, *args, **kwargs):
        return self._wrapped.SetDisplayOptions(*args, **kwargs)

    def GetDefaultDisplayOptions(self, *args, **kwargs):
        return self._wrapped.GetDefaultDisplayOptions(*args, **kwargs)

    def SetDefaultDisplayOptions(self, *args, **kwargs):
        return self._wrapped.SetDefaultDisplayOptions(*args, **kwargs)

    @property
    def Display(self) -> int:
        return self._wrapped.Display

    @Display.setter
    def Display(self, Value: int):
        self._wrapped.Display = Value

    def GetWindowDisplayPartUIDs(self, *args, **kwargs):
        return self._wrapped.GetWindowDisplayPartUIDs(*args, **kwargs)

    def SetWindowDisplayPartUIDs(self, *args, **kwargs):
        return self._wrapped.SetWindowDisplayPartUIDs(*args, **kwargs)

    def SaveWindowToBitmap(self, *args, **kwargs):
        return self._wrapped.SaveWindowToBitmap(*args, **kwargs)

    def SaveWindowsToBitmap(self, *args, **kwargs):
        return self._wrapped.SaveWindowsToBitmap(*args, **kwargs)

    def SaveWindowToClipboard(self, *args, **kwargs):
        return self._wrapped.SaveWindowToClipboard(*args, **kwargs)

    def SaveWindowsToClipboard(self, *args, **kwargs):
        return self._wrapped.SaveWindowsToClipboard(*args, **kwargs)

    def SaveWindowToMetafile(self, *args, **kwargs):
        return self._wrapped.SaveWindowToMetafile(*args, **kwargs)

    def SaveWindowsToMetafile(self, *args, **kwargs):
        return self._wrapped.SaveWindowsToMetafile(*args, **kwargs)

    @property
    def LoadCaseIndex(self) -> int:
        return self._wrapped.LoadCaseIndex

    @LoadCaseIndex.setter
    def LoadCaseIndex(self, Value: int):
        self._wrapped.LoadCaseIndex = Value

    @property
    def View(self) -> int:
        return self._wrapped.View

    @View.setter
    def View(self, Value: int):
        self._wrapped.View = Value

    @property
    def WorkPlaneIndex(self) -> int:
        return self._wrapped.WorkPlaneIndex

    @WorkPlaneIndex.setter
    def WorkPlaneIndex(self, Value: int):
        self._wrapped.WorkPlaneIndex = Value

    @property
    def StoryIndex(self) -> int:
        return self._wrapped.StoryIndex

    @StoryIndex.setter
    def StoryIndex(self, Value: int):
        self._wrapped.StoryIndex = Value

    @property
    def ActiveStoryIndex(self) -> int:
        return self._wrapped.ActiveStoryIndex

    @ActiveStoryIndex.setter
    def ActiveStoryIndex(self, Value: int):
        self._wrapped.ActiveStoryIndex = Value

    def GetVisibleLayerIDs(self, *args, **kwargs):
        return self._wrapped.GetVisibleLayerIDs(*args, **kwargs)

    def SetVisibleLayerIDs(self, *args, **kwargs):
        return self._wrapped.SetVisibleLayerIDs(*args, **kwargs)

    def GetDetectedLayerIDs(self, *args, **kwargs):
        return self._wrapped.GetDetectedLayerIDs(*args, **kwargs)

    def SetDetectedLayerIDs(self, *args, **kwargs):
        return self._wrapped.SetDetectedLayerIDs(*args, **kwargs)

    def GetLockedLayerIDs(self, *args, **kwargs):
        return self._wrapped.GetLockedLayerIDs(*args, **kwargs)

    def SetLockedLayerIDs(self, *args, **kwargs):
        return self._wrapped.SetLockedLayerIDs(*args, **kwargs)

    def GetVisibleStructuralGridIDs(self, *args, **kwargs):
        return self._wrapped.GetVisibleStructuralGridIDs(*args, **kwargs)

    def SetVisibleStructuralGridIDs(self, *args, **kwargs):
        return self._wrapped.SetVisibleStructuralGridIDs(*args, **kwargs)

    def GetWorldRectangle(self, *args, **kwargs):
        return self._wrapped.GetWorldRectangle(*args, **kwargs)

    def SetWorldRectangle(self, *args, **kwargs):
        return self._wrapped.SetWorldRectangle(*args, **kwargs)

    def ReDraw(self, *args, **kwargs):
        return self._wrapped.ReDraw(*args, **kwargs)

    def GetVisibleSectionIDs(self, *args, **kwargs):
        return self._wrapped.GetVisibleSectionIDs(*args, **kwargs)

    def SetVisibleSectionIDs(self, *args, **kwargs):
        return self._wrapped.SetVisibleSectionIDs(*args, **kwargs)

    def GetStaticDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetStaticDisplayParameters_V153(*args, **kwargs)

    def GetBucklingDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetBucklingDisplayParameters_V153(*args, **kwargs)

    def GetVibrationDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetVibrationDisplayParameters_V153(
            *args, **kwargs)

    def GetDynamicDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetDynamicDisplayParameters_V153(*args, **kwargs)

    def GetRCDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetRCDesignDisplayParameters_V153(*args, **kwargs)

    def GetSteelDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignDisplayParameters_V153(
            *args, **kwargs)

    def GetTimberDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignDisplayParameters_V153(
            *args, **kwargs)

    def SetStaticDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetStaticDisplayParameters_V153(*args, **kwargs)

    def SetBucklingDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetBucklingDisplayParameters_V153(*args, **kwargs)

    def SetVibrationDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetVibrationDisplayParameters_V153(
            *args, **kwargs)

    def SetDynamicDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetDynamicDisplayParameters_V153(*args, **kwargs)

    def SetRCDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetRCDesignDisplayParameters_V153(*args, **kwargs)

    def SetSteelDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetSteelDesignDisplayParameters_V153(
            *args, **kwargs)

    def SetTimberDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetTimberDesignDisplayParameters_V153(
            *args, **kwargs)

    @property
    def Switch(self) -> int:
        return self._wrapped.Switch

    @Switch.setter
    def Switch(self, Value: int):
        self._wrapped.Switch = Value

    def GetCommonDisplayParameters_V161(self, *args, **kwargs):
        return self._wrapped.GetCommonDisplayParameters_V161(*args, **kwargs)

    def SetCommonDisplayParameters_V161(self, *args, **kwargs):
        return self._wrapped.SetCommonDisplayParameters_V161(*args, **kwargs)


class AxisVMCustomParts(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetPart(self, *args, **kwargs):
        return self._wrapped.GetPart(*args, **kwargs)

    def DeletePart(self, *args, **kwargs):
        return self._wrapped.DeletePart(*args, **kwargs)

    def ModifyPartFromSelectedItems(self, *args, **kwargs):
        return self._wrapped.ModifyPartFromSelectedItems(*args, **kwargs)

    def ModifyPart(self, *args, **kwargs):
        return self._wrapped.ModifyPart(*args, **kwargs)

    def SelectPartItems(self, *args, **kwargs):
        return self._wrapped.SelectPartItems(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def PartUID(self) -> int:
        return self._wrapped.PartUID

    def AddPartItemsFromSelectedItemsToPart(self, *args, **kwargs):
        return self._wrapped.AddPartItemsFromSelectedItemsToPart(
            *args, **kwargs)

    def AddPartItemsToPart(self, *args, **kwargs):
        return self._wrapped.AddPartItemsToPart(*args, **kwargs)

    @property
    def RootFolder(self) -> 'AxisVMCustomPartFolder':
        return self._wrapped.RootFolder

    def GetCustomPartFolderByPath(self, *args, **kwargs):
        return self._wrapped.GetCustomPartFolderByPath(*args, **kwargs)

    @property
    def IsCustomPart(self) -> int:
        return self._wrapped.IsCustomPart

    @property
    def Attachments(self) -> 'AxisVMAttachments':
        return self._wrapped.Attachments

    def GetPartItemsByUID(self, *args, **kwargs):
        return self._wrapped.GetPartItemsByUID(*args, **kwargs)

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def FullName(self) -> int:
        return self._wrapped.FullName


class AxisVMLogicalParts(AxWrapper):

    def GetBy_Material(self, *args, **kwargs):
        return self._wrapped.GetBy_Material(*args, **kwargs)

    def GetBy_CrossSection(self, *args, **kwargs):
        return self._wrapped.GetBy_CrossSection(*args, **kwargs)

    def GetBy_CrossSection_LineType(self, *args, **kwargs):
        return self._wrapped.GetBy_CrossSection_LineType(*args, **kwargs)

    def GetBy_CrossSection_ArchitecturalLineElementType(self, *args, **kwargs):
        return self._wrapped.GetBy_CrossSection_ArchitecturalLineElementType(
            *args, **kwargs)

    def GetBy_CrossSection_LineType_Storey(self, *args, **kwargs):
        return self._wrapped.GetBy_CrossSection_LineType_Storey(
            *args, **kwargs)

    def GetBy_CrossSection_ArchitecturalLineElementType_Storey(
            self, *args, **kwargs):
        return self._wrapped.GetBy_CrossSection_ArchitecturalLineElementType_Storey(
            *args, **kwargs)

    def GetBy_DomainElementType_Thickness(self, *args, **kwargs):
        return self._wrapped.GetBy_DomainElementType_Thickness(*args, **kwargs)

    def GetBy_ArchitecturalDomainElementType_Thickness(self, *args, **kwargs):
        return self._wrapped.GetBy_ArchitecturalDomainElementType_Thickness(
            *args, **kwargs)

    def GetBy_DomainElementType_Thickness_Storey(self, *args, **kwargs):
        return self._wrapped.GetBy_DomainElementType_Thickness_Storey(
            *args, **kwargs)

    def GetBy_ArchitecturalDomainElementType_Thickness_Storey(
            self, *args, **kwargs):
        return self._wrapped.GetBy_ArchitecturalDomainElementType_Thickness_Storey(
            *args, **kwargs)

    def GetEnabledLogicalParts(self, *args, **kwargs):
        return self._wrapped.GetEnabledLogicalParts(*args, **kwargs)

    def SetEnabledLogicalParts(self, *args, **kwargs):
        return self._wrapped.SetEnabledLogicalParts(*args, **kwargs)

    def SaveDefaultEnabledLogicalParts(self, *args, **kwargs):
        return self._wrapped.SaveDefaultEnabledLogicalParts(*args, **kwargs)

    @property
    def IsLogicalPart(self) -> int:
        return self._wrapped.IsLogicalPart

    def GetBy_StructuralGridLineUID(self, *args, **kwargs):
        return self._wrapped.GetBy_StructuralGridLineUID(*args, **kwargs)

    def GetPartItemsByUID(self, *args, **kwargs):
        return self._wrapped.GetPartItemsByUID(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @property
    def FullName(self) -> int:
        return self._wrapped.FullName


class AxisVMLoadPanels(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def AddFromDomain(self, *args, **kwargs):
        return self._wrapped.AddFromDomain(*args, **kwargs)

    def AddFromMemberIDs(self, *args, **kwargs):
        return self._wrapped.AddFromMemberIDs(*args, **kwargs)

    def AddFromPolygon(self, *args, **kwargs):
        return self._wrapped.AddFromPolygon(*args, **kwargs)

    def AddFromLineIDs(self, *args, **kwargs):
        return self._wrapped.AddFromLineIDs(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID


class AxisVMWorkplanes(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def AddGlobal(self, *args, **kwargs):
        return self._wrapped.AddGlobal(*args, **kwargs)

    def AddGeneral(self, *args, **kwargs):
        return self._wrapped.AddGeneral(*args, **kwargs)

    def AddSmart(self, *args, **kwargs):
        return self._wrapped.AddSmart(*args, **kwargs)

    def GetGlobalParameters(self, *args, **kwargs):
        return self._wrapped.GetGlobalParameters(*args, **kwargs)

    def GetGeneralParameters(self, *args, **kwargs):
        return self._wrapped.GetGeneralParameters(*args, **kwargs)

    def GetSmartParameters(self, *args, **kwargs):
        return self._wrapped.GetSmartParameters(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @property
    def WorkplaneType(self) -> int:
        return self._wrapped.WorkplaneType

    @property
    def HideNotInPlane(self) -> int:
        return self._wrapped.HideNotInPlane

    @HideNotInPlane.setter
    def HideNotInPlane(self, Value: int):
        self._wrapped.HideNotInPlane = Value

    @property
    def ShowGrayedNotInPlane(self) -> int:
        return self._wrapped.ShowGrayedNotInPlane

    @ShowGrayedNotInPlane.setter
    def ShowGrayedNotInPlane(self, Value: int):
        self._wrapped.ShowGrayedNotInPlane = Value

    def SetGlobalParameters(self, *args, **kwargs):
        return self._wrapped.SetGlobalParameters(*args, **kwargs)

    def SetGeneralParameters(self, *args, **kwargs):
        return self._wrapped.SetGeneralParameters(*args, **kwargs)

    def SetSmartParameters(self, *args, **kwargs):
        return self._wrapped.SetSmartParameters(*args, **kwargs)


class AxisVMCrossSectionOptimization(AxWrapper):

    @property
    def GroupCount(self) -> int:
        return self._wrapped.GroupCount

    @property
    def GroupCrossSectionCount(self) -> int:
        return self._wrapped.GroupCrossSectionCount

    @property
    def OptimizationType(self) -> int:
        return self._wrapped.OptimizationType

    def AddGroup(self, *args, **kwargs):
        return self._wrapped.AddGroup(*args, **kwargs)

    def AddGroup_vb(self, *args, **kwargs):
        return self._wrapped.AddGroup_vb(*args, **kwargs)

    def AddCrossSectionFromModel(self, *args, **kwargs):
        return self._wrapped.AddCrossSectionFromModel(*args, **kwargs)

    def AddCrossSectionFromCatalog(self, *args, **kwargs):
        return self._wrapped.AddCrossSectionFromCatalog(*args, **kwargs)

    def AddCrossSectionFromDialog(self, *args, **kwargs):
        return self._wrapped.AddCrossSectionFromDialog(*args, **kwargs)

    def DeleteGroupCrossSection(self, *args, **kwargs):
        return self._wrapped.DeleteGroupCrossSection(*args, **kwargs)

    def GetOptimizationChecks(self, *args, **kwargs):
        return self._wrapped.GetOptimizationChecks(*args, **kwargs)

    def GetParametersForPredefinedShapes(self, *args, **kwargs):
        return self._wrapped.GetParametersForPredefinedShapes(*args, **kwargs)

    def GetParametersForParametricOptimization(self, *args, **kwargs):
        return self._wrapped.GetParametersForParametricOptimization(
            *args, **kwargs)

    def SetOptimizationChecks(self, *args, **kwargs):
        return self._wrapped.SetOptimizationChecks(*args, **kwargs)

    def SetParametersForPredefinedShapes(self, *args, **kwargs):
        return self._wrapped.SetParametersForPredefinedShapes(*args, **kwargs)

    def SetParametersForParametricOptimization(self, *args, **kwargs):
        return self._wrapped.SetParametersForParametricOptimization(
            *args, **kwargs)

    def GetGroupCrossSections(self, *args, **kwargs):
        return self._wrapped.GetGroupCrossSections(*args, **kwargs)

    def GetMemberDesignIDs(self, *args, **kwargs):
        return self._wrapped.GetMemberDesignIDs(*args, **kwargs)

    def SetMemberDesignIDs(self, *args, **kwargs):
        return self._wrapped.SetMemberDesignIDs(*args, **kwargs)

    def SetMemberDesignIDs_vb(self, *args, **kwargs):
        return self._wrapped.SetMemberDesignIDs_vb(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def CallMainProgress(self) -> int:
        return self._wrapped.CallMainProgress

    @CallMainProgress.setter
    def CallMainProgress(self, Value: int):
        self._wrapped.CallMainProgress = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    def GetParametricShapeOptimizationResultsByLoadCaseId(
            self, *args, **kwargs):
        return self._wrapped.GetParametricShapeOptimizationResultsByLoadCaseId(
            *args, **kwargs)

    def GetParametricShapeOptimizationResultsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetParametricShapeOptimizationResultsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeParametricShapeOptimizationResults(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeParametricShapeOptimizationResults(
            *args, **kwargs)

    def GetCriticalParametricShapeOptimizationResults(self, *args, **kwargs):
        return self._wrapped.GetCriticalParametricShapeOptimizationResults(
            *args, **kwargs)

    def ParametricShapeOptimizationResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.ParametricShapeOptimizationResultsByLoadCaseId(
            *args, **kwargs)

    def ParametricShapeOptimizationResultsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.ParametricShapeOptimizationResultsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeParametricShapeOptimizationResults(self, *args, **kwargs):
        return self._wrapped.EnvelopeParametricShapeOptimizationResults(
            *args, **kwargs)

    def CriticalParametricShapeOptimizationResults(self, *args, **kwargs):
        return self._wrapped.CriticalParametricShapeOptimizationResults(
            *args, **kwargs)

    def GetPredefinedShapesOptimizationResultsByLoadCaseId(
            self, *args, **kwargs):
        return self._wrapped.GetPredefinedShapesOptimizationResultsByLoadCaseId(
            *args, **kwargs)

    def GetPredefinedShapesOptimizationResultsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetPredefinedShapesOptimizationResultsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopePredefinedShapesOptimizationResults(self, *args, **kwargs):
        return self._wrapped.GetEnvelopePredefinedShapesOptimizationResults(
            *args, **kwargs)

    def GetCriticalPredefinedShapesOptimizationResults(self, *args, **kwargs):
        return self._wrapped.GetCriticalPredefinedShapesOptimizationResults(
            *args, **kwargs)

    def PredefinedShapesOptimizationResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.PredefinedShapesOptimizationResultsByLoadCaseId(
            *args, **kwargs)

    def PredefinedShapesOptimizationResultsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.PredefinedShapesOptimizationResultsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopePredefinedShapesOptimizationResults(self, *args, **kwargs):
        return self._wrapped.EnvelopePredefinedShapesOptimizationResults(
            *args, **kwargs)

    def CriticalPredefinedShapesOptimizationResults(self, *args, **kwargs):
        return self._wrapped.CriticalPredefinedShapesOptimizationResults(
            *args, **kwargs)

    def ReplaceCrossSectionToGroupCrossSection(self, *args, **kwargs):
        return self._wrapped.ReplaceCrossSectionToGroupCrossSection(
            *args, **kwargs)

    def ReplaceCrossSectionToModelCrossSection(self, *args, **kwargs):
        return self._wrapped.ReplaceCrossSectionToModelCrossSection(
            *args, **kwargs)

    @property
    def GroupName(self) -> int:
        return self._wrapped.GroupName

    @property
    def GroupCrossSectionShape(self) -> int:
        return self._wrapped.GroupCrossSectionShape

    def DeleteGroup(self, *args, **kwargs):
        return self._wrapped.DeleteGroup(*args, **kwargs)

    @property
    def GroupCrossSectionShapeEx(self) -> int:
        return self._wrapped.GroupCrossSectionShapeEx


class AxisVMMathTexts(AxWrapper):

    def New(self, *args, **kwargs):
        return self._wrapped.New(*args, **kwargs)

    def AddToReport(self, *args, **kwargs):
        return self._wrapped.AddToReport(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def GetUIDs(self, *args, **kwargs):
        return self._wrapped.GetUIDs(*args, **kwargs)

    def GetMathText(self, *args, **kwargs):
        return self._wrapped.GetMathText(*args, **kwargs)

    def SetMathText(self, *args, **kwargs):
        return self._wrapped.SetMathText(*args, **kwargs)

    def ShowInWindow(self, *args, **kwargs):
        return self._wrapped.ShowInWindow(*args, **kwargs)


class AxisVMLayers(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Colour(self) -> int:
        return self._wrapped.Colour

    @Colour.setter
    def Colour(self, Value: int):
        self._wrapped.Colour = Value

    @property
    def PenStyle(self) -> int:
        return self._wrapped.PenStyle

    @PenStyle.setter
    def PenStyle(self, Value: int):
        self._wrapped.PenStyle = Value

    @property
    def PenWidth(self) -> int:
        return self._wrapped.PenWidth

    @PenWidth.setter
    def PenWidth(self, Value: int):
        self._wrapped.PenWidth = Value

    @property
    def IsEmpty(self) -> int:
        return self._wrapped.IsEmpty

    @property
    def TextsCount(self) -> int:
        return self._wrapped.TextsCount

    @property
    def ShapesCount(self) -> int:
        return self._wrapped.ShapesCount

    @property
    def ShapeType(self) -> int:
        return self._wrapped.ShapeType

    @property
    def FontName(self) -> int:
        return self._wrapped.FontName

    @FontName.setter
    def FontName(self, Value: int):
        self._wrapped.FontName = Value

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def LayerType(self) -> int:
        return self._wrapped.LayerType

    @property
    def Text(self) -> int:
        return self._wrapped.Text

    @Text.setter
    def Text(self, Value: int):
        self._wrapped.Text = Value

    def AddLayer(self, *args, **kwargs):
        return self._wrapped.AddLayer(*args, **kwargs)

    def AddShape(self, *args, **kwargs):
        return self._wrapped.AddShape(*args, **kwargs)

    def AddText(self, *args, **kwargs):
        return self._wrapped.AddText(*args, **kwargs)

    def DeleteLayer(self, *args, **kwargs):
        return self._wrapped.DeleteLayer(*args, **kwargs)

    def DeleteShape(self, *args, **kwargs):
        return self._wrapped.DeleteShape(*args, **kwargs)

    def DeleteText(self, *args, **kwargs):
        return self._wrapped.DeleteText(*args, **kwargs)

    def GetShapeAttributes(self, *args, **kwargs):
        return self._wrapped.GetShapeAttributes(*args, **kwargs)

    def GetShapeIDs(self, *args, **kwargs):
        return self._wrapped.GetShapeIDs(*args, **kwargs)

    def GetShapePolygon(self, *args, **kwargs):
        return self._wrapped.GetShapePolygon(*args, **kwargs)

    def GetTextParams(self, *args, **kwargs):
        return self._wrapped.GetTextParams(*args, **kwargs)

    def GetTextIDs(self, *args, **kwargs):
        return self._wrapped.GetTextIDs(*args, **kwargs)

    def SetShapeAttributes(self, *args, **kwargs):
        return self._wrapped.SetShapeAttributes(*args, **kwargs)

    def SetTextParams(self, *args, **kwargs):
        return self._wrapped.SetTextParams(*args, **kwargs)


class AxisVMXLAMpanels(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def AddFromCatalog(self, *args, **kwargs):
        return self._wrapped.AddFromCatalog(*args, **kwargs)

    def GetLayerThicknesses(self, *args, **kwargs):
        return self._wrapped.GetLayerThicknesses(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def ReplaceFromCatalog(self, *args, **kwargs):
        return self._wrapped.ReplaceFromCatalog(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name


class AxisVMReports(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    def NewFromTemplateFile(self, *args, **kwargs):
        return self._wrapped.NewFromTemplateFile(*args, **kwargs)

    def AddDrawingFromLibrary(self, *args, **kwargs):
        return self._wrapped.AddDrawingFromLibrary(*args, **kwargs)

    def AddImageFromFile(self, *args, **kwargs):
        return self._wrapped.AddImageFromFile(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def GenerateFromTemplateFile(self, *args, **kwargs):
        return self._wrapped.GenerateFromTemplateFile(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    @property
    def TemplateDescription(self) -> int:
        return self._wrapped.TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, Value: int):
        self._wrapped.TemplateDescription = Value

    def AddRootFolder(self, *args, **kwargs):
        return self._wrapped.AddRootFolder(*args, **kwargs)

    @property
    def ImageCount(self) -> int:
        return self._wrapped.ImageCount

    @property
    def ImagePath(self) -> int:
        return self._wrapped.ImagePath

    @property
    def ImageCaption(self) -> int:
        return self._wrapped.ImageCaption

    def DeleteImage(self, *args, **kwargs):
        return self._wrapped.DeleteImage(*args, **kwargs)

    def ImagesInFolder(self, *args, **kwargs):
        return self._wrapped.ImagesInFolder(*args, **kwargs)


class AxisVMStructuralGrids(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def GenerateStructuralGrid(self, *args, **kwargs):
        return self._wrapped.GenerateStructuralGrid(*args, **kwargs)

    def GetStructuralGridParams(self, *args, **kwargs):
        return self._wrapped.GetStructuralGridParams(*args, **kwargs)

    def SetStructuralGridParams(self, *args, **kwargs):
        return self._wrapped.SetStructuralGridParams(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value


class AxisVMDimensions(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def AddDimensionLine(self, *args, **kwargs):
        return self._wrapped.AddDimensionLine(*args, **kwargs)

    def AddTextBox(self, *args, **kwargs):
        return self._wrapped.AddTextBox(*args, **kwargs)

    def GetParams(self, *args, **kwargs):
        return self._wrapped.GetParams(*args, **kwargs)

    def SetParams(self, *args, **kwargs):
        return self._wrapped.SetParams(*args, **kwargs)

    def GetText(self, *args, **kwargs):
        return self._wrapped.GetText(*args, **kwargs)

    def SetText(self, *args, **kwargs):
        return self._wrapped.SetText(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def DimensionType(self) -> int:
        return self._wrapped.DimensionType

    @property
    def MeasurementCharacter(self) -> str:
        return self._wrapped.MeasurementCharacter


class AxisVMVirtualBeams(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: int):
        self._wrapped.Name = Value

    @property
    def Length(self) -> int:
        return self._wrapped.Length

    @property
    def VirtualBeamType(self) -> int:
        return self._wrapped.VirtualBeamType

    def GetDomains(self, *args, **kwargs):
        return self._wrapped.GetDomains(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def IndexOf(self, *args, **kwargs):
        return self._wrapped.IndexOf(*args, **kwargs)

    def AddNewVirtualBeam(self, *args, **kwargs):
        return self._wrapped.AddNewVirtualBeam(*args, **kwargs)

    def AddNewDomainToVirtualBeam(self, *args, **kwargs):
        return self._wrapped.AddNewDomainToVirtualBeam(*args, **kwargs)

    def ModifyDomains(self, *args, **kwargs):
        return self._wrapped.ModifyDomains(*args, **kwargs)

    def GetVirtualBeamParams(self, *args, **kwargs):
        return self._wrapped.GetVirtualBeamParams(*args, **kwargs)

    def GetVirtualStripParams(self, *args, **kwargs):
        return self._wrapped.GetVirtualStripParams(*args, **kwargs)

    def SetVirtualBeamParams(self, *args, **kwargs):
        return self._wrapped.SetVirtualBeamParams(*args, **kwargs)

    def SetVirtualStripParams(self, *args, **kwargs):
        return self._wrapped.SetVirtualStripParams(*args, **kwargs)

    def GetCenterCoordinates(self, *args, **kwargs):
        return self._wrapped.GetCenterCoordinates(*args, **kwargs)

    @property
    def ChainCount(self) -> int:
        return self._wrapped.ChainCount

    @property
    def SectionCount(self) -> int:
        return self._wrapped.SectionCount

    def AddNewVirtualStrip(self, *args, **kwargs):
        return self._wrapped.AddNewVirtualStrip(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    def GetReductionPointCoordinates(self, *args, **kwargs):
        return self._wrapped.GetReductionPointCoordinates(*args, **kwargs)

    def GetExtendedDomainList(self, *args, **kwargs):
        return self._wrapped.GetExtendedDomainList(*args, **kwargs)


class AxisVMNodesSupports(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def DomainId1(self) -> int:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> int:
        return self._wrapped.DomainId2

    @property
    def HasStiffnessCalcParams(self) -> int:
        return self._wrapped.HasStiffnessCalcParams

    @property
    def HasFooting(self) -> int:
        return self._wrapped.HasFooting

    @property
    def FootingType(self) -> int:
        return self._wrapped.FootingType

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def LineId(self) -> int:
        return self._wrapped.LineId

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @property
    def NodeId(self) -> int:
        return self._wrapped.NodeId

    @property
    def ReferenceId(self) -> int:
        return self._wrapped.ReferenceId

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SupportType(self) -> int:
        return self._wrapped.SupportType

    @property
    def SurfaceId1(self) -> int:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> int:
        return self._wrapped.SurfaceId2

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def GetStiffnesses(self, *args, **kwargs):
        return self._wrapped.GetStiffnesses(*args, **kwargs)

    def GetNonLinearity(self, *args, **kwargs):
        return self._wrapped.GetNonLinearity(*args, **kwargs)

    def GetResistances(self, *args, **kwargs):
        return self._wrapped.GetResistances(*args, **kwargs)

    def GetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.GetStiffnessCalcParams(*args, **kwargs)

    def SetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.SetStiffnessCalcParams(*args, **kwargs)

    def AddNodalGlobal(self, *args, **kwargs):
        return self._wrapped.AddNodalGlobal(*args, **kwargs)

    def AddNodalMemberRelative(self, *args, **kwargs):
        return self._wrapped.AddNodalMemberRelative(*args, **kwargs)

    def AddNodalDomainRelative(self, *args, **kwargs):
        return self._wrapped.AddNodalDomainRelative(*args, **kwargs)

    def AddNodalReferenceRelative(self, *args, **kwargs):
        return self._wrapped.AddNodalReferenceRelative(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def RenameSelected(self, *args, **kwargs):
        return self._wrapped.RenameSelected(*args, **kwargs)

    def GetNodalSupportID(self, *args, **kwargs):
        return self._wrapped.GetNodalSupportID(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def SetStiffnesses(self, *args, **kwargs):
        return self._wrapped.SetStiffnesses(*args, **kwargs)

    def SetNonLinearity(self, *args, **kwargs):
        return self._wrapped.SetNonLinearity(*args, **kwargs)

    def SetResistances(self, *args, **kwargs):
        return self._wrapped.SetResistances(*args, **kwargs)

    def GetFootingParams(self, *args, **kwargs):
        return self._wrapped.GetFootingParams(*args, **kwargs)

    def GetFootingParams_V153(self, *args, **kwargs):
        return self._wrapped.GetFootingParams_V153(*args, **kwargs)

    def AddNodalGlobal_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalGlobal_V153(*args, **kwargs)

    def AddNodalMemberRelative_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalMemberRelative_V153(*args, **kwargs)

    def AddNodalDomainRelative_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalDomainRelative_V153(*args, **kwargs)

    def AddNodalReference_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalReference_V153(*args, **kwargs)

    def AddNodalLocal_V153(self, *args, **kwargs):
        return self._wrapped.AddNodalLocal_V153(*args, **kwargs)

    @property
    def SpringParams(self) -> int:
        return self._wrapped.SpringParams

    @SpringParams.setter
    def SpringParams(self, Value: int):
        self._wrapped.SpringParams = Value

    def AddIsolator(self, *args, **kwargs):
        return self._wrapped.AddIsolator(*args, **kwargs)

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)


class AxisVMMembersSupports(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def HasStiffnessCalcParams(self) -> int:
        return self._wrapped.HasStiffnessCalcParams

    @property
    def HasFooting(self) -> int:
        return self._wrapped.HasFooting

    @property
    def FootingType(self) -> int:
        return self._wrapped.FootingType

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @property
    def MemberID(self) -> int:
        return self._wrapped.MemberID

    @property
    def SectionCount(self) -> int:
        return self._wrapped.SectionCount

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def SupportType(self) -> int:
        return self._wrapped.SupportType

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def GetLineSupportIds(self, *args, **kwargs):
        return self._wrapped.GetLineSupportIds(*args, **kwargs)

    def GetStiffnesses(self, *args, **kwargs):
        return self._wrapped.GetStiffnesses(*args, **kwargs)

    def GetNonLinearity(self, *args, **kwargs):
        return self._wrapped.GetNonLinearity(*args, **kwargs)

    def GetResistances(self, *args, **kwargs):
        return self._wrapped.GetResistances(*args, **kwargs)

    def GetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.GetStiffnessCalcParams(*args, **kwargs)

    def SetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.SetStiffnessCalcParams(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    def GetFootingDimensions(self, *args, **kwargs):
        return self._wrapped.GetFootingDimensions(*args, **kwargs)

    def GetFootingParams(self, *args, **kwargs):
        return self._wrapped.GetFootingParams(*args, **kwargs)

    def AddMembersSupport(self, *args, **kwargs):
        return self._wrapped.AddMembersSupport(*args, **kwargs)

    def AddDomainEdgeSupport(self, *args, **kwargs):
        return self._wrapped.AddDomainEdgeSupport(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def RenameSelected(self, *args, **kwargs):
        return self._wrapped.RenameSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def SetStiffnesses(self, *args, **kwargs):
        return self._wrapped.SetStiffnesses(*args, **kwargs)

    def SetNonLinearity(self, *args, **kwargs):
        return self._wrapped.SetNonLinearity(*args, **kwargs)

    def SetResistances(self, *args, **kwargs):
        return self._wrapped.SetResistances(*args, **kwargs)

    def AddDomainEdgeRefSupport(self, *args, **kwargs):
        return self._wrapped.AddDomainEdgeRefSupport(*args, **kwargs)

    @property
    def ReferenceId(self) -> int:
        return self._wrapped.ReferenceId

    def GetFootingParams_V153(self, *args, **kwargs):
        return self._wrapped.GetFootingParams_V153(*args, **kwargs)

    def BulkAdd(self, *args, **kwargs):
        return self._wrapped.BulkAdd(*args, **kwargs)

    def AddPasternakSupport(self, *args, **kwargs):
        return self._wrapped.AddPasternakSupport(*args, **kwargs)

    def AddDomainEdgePasternakSupport(self, *args, **kwargs):
        return self._wrapped.AddDomainEdgePasternakSupport(*args, **kwargs)

    def GetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.GetPasternakStiffness(*args, **kwargs)

    def SetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.SetPasternakStiffness(*args, **kwargs)

    def BulkAddPasternak(self, *args, **kwargs):
        return self._wrapped.BulkAddPasternak(*args, **kwargs)


class AxisVMDomainsSupports(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def IndexOfUID(self) -> int:
        return self._wrapped.IndexOfUID

    @property
    def Name(self) -> int:
        return self._wrapped.Name

    @property
    def DomainId(self) -> int:
        return self._wrapped.DomainId

    @property
    def SelCount(self) -> int:
        return self._wrapped.SelCount

    @property
    def Selected(self) -> int:
        return self._wrapped.Selected

    @Selected.setter
    def Selected(self, Value: int):
        self._wrapped.Selected = Value

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def GetStiffnesses(self, *args, **kwargs):
        return self._wrapped.GetStiffnesses(*args, **kwargs)

    def GetNonLinearity(self, *args, **kwargs):
        return self._wrapped.GetNonLinearity(*args, **kwargs)

    def GetResistances(self, *args, **kwargs):
        return self._wrapped.GetResistances(*args, **kwargs)

    def GetSelectedItemIds(self, *args, **kwargs):
        return self._wrapped.GetSelectedItemIds(*args, **kwargs)

    def AddDomainsSupport(self, *args, **kwargs):
        return self._wrapped.AddDomainsSupport(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def DeleteSelected(self, *args, **kwargs):
        return self._wrapped.DeleteSelected(*args, **kwargs)

    def RenameSelected(self, *args, **kwargs):
        return self._wrapped.RenameSelected(*args, **kwargs)

    def SelectAll(self, *args, **kwargs):
        return self._wrapped.SelectAll(*args, **kwargs)

    def SetStiffnesses(self, *args, **kwargs):
        return self._wrapped.SetStiffnesses(*args, **kwargs)

    def SetNonLinearity(self, *args, **kwargs):
        return self._wrapped.SetNonLinearity(*args, **kwargs)

    def SetResistances(self, *args, **kwargs):
        return self._wrapped.SetResistances(*args, **kwargs)

    def AddDomainPasternakSupport(self, *args, **kwargs):
        return self._wrapped.AddDomainPasternakSupport(*args, **kwargs)

    def GetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.GetPasternakStiffness(*args, **kwargs)

    def SetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.SetPasternakStiffness(*args, **kwargs)

    @property
    def Item(self) -> int:
        return self._wrapped.Item


class AxisVMWindLoad(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Params(self) -> 'RWindLoadParams_V161':
        return self._wrapped.Params

    @Params.setter
    def Params(self, Value: 'RWindLoadParams_V161'):
        self._wrapped.Params = Value

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    @property
    def CodeAllowed(self) -> int:
        return self._wrapped.CodeAllowed

    @property
    def Defined(self) -> int:
        return self._wrapped.Defined

    def CreateWindCases(self, *args, **kwargs):
        return self._wrapped.CreateWindCases(*args, **kwargs)

    def DeleteWindCases(self, *args, **kwargs):
        return self._wrapped.DeleteWindCases(*args, **kwargs)


class AxisVMWindSubStructure(AxWrapper):

    @property
    def Params(self) -> 'RWindSubStructParams':
        return self._wrapped.Params

    @Params.setter
    def Params(self, Value: 'RWindSubStructParams'):
        self._wrapped.Params = Value

    def SetPanels(self, *args, **kwargs):
        return self._wrapped.SetPanels(*args, **kwargs)

    def GetPanels(self, *args, **kwargs):
        return self._wrapped.GetPanels(*args, **kwargs)


class AxisVMMaterial(AxWrapper):

    @property
    def NationalDesignCode(self) -> int:
        return self._wrapped.NationalDesignCode

    @NationalDesignCode.setter
    def NationalDesignCode(self, Value: int):
        self._wrapped.NationalDesignCode = Value

    @property
    def NationalDesignName(self) -> str:
        return self._wrapped.NationalDesignName

    @NationalDesignName.setter
    def NationalDesignName(self, Value: str):
        self._wrapped.NationalDesignName = Value

    @property
    def MaterialDesignName(self) -> str:
        return self._wrapped.MaterialDesignName

    @MaterialDesignName.setter
    def MaterialDesignName(self, Value: str):
        self._wrapped.MaterialDesignName = Value

    @property
    def MaterialType(self) -> int:
        return self._wrapped.MaterialType

    @MaterialType.setter
    def MaterialType(self, Value: int):
        self._wrapped.MaterialType = Value

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: str):
        self._wrapped.Name = Value

    @property
    def FillColour(self) -> c_ulong:
        return self._wrapped.FillColour

    @FillColour.setter
    def FillColour(self, Value: c_ulong):
        self._wrapped.FillColour = Value

    @property
    def ContourColour(self) -> c_ulong:
        return self._wrapped.ContourColour

    @ContourColour.setter
    def ContourColour(self, Value: c_ulong):
        self._wrapped.ContourColour = Value

    @property
    def ex(self) -> float:
        return self._wrapped.ex

    @ex.setter
    def ex(self, Value: float):
        self._wrapped.ex = Value

    @property
    def ey(self) -> float:
        return self._wrapped.ey

    @ey.setter
    def ey(self, Value: float):
        self._wrapped.ey = Value

    @property
    def ez(self) -> float:
        return self._wrapped.ez

    @ez.setter
    def ez(self, Value: float):
        self._wrapped.ez = Value

    @property
    def Nux(self) -> float:
        return self._wrapped.Nux

    @Nux.setter
    def Nux(self, Value: float):
        self._wrapped.Nux = Value

    @property
    def nuy(self) -> float:
        return self._wrapped.nuy

    @nuy.setter
    def nuy(self, Value: float):
        self._wrapped.nuy = Value

    @property
    def nuz(self) -> float:
        return self._wrapped.nuz

    @nuz.setter
    def nuz(self, Value: float):
        self._wrapped.nuz = Value

    @property
    def Alfax(self) -> float:
        return self._wrapped.Alfax

    @Alfax.setter
    def Alfax(self, Value: float):
        self._wrapped.Alfax = Value

    @property
    def Alfay(self) -> float:
        return self._wrapped.Alfay

    @Alfay.setter
    def Alfay(self, Value: float):
        self._wrapped.Alfay = Value

    @property
    def Alfaz(self) -> float:
        return self._wrapped.Alfaz

    @Alfaz.setter
    def Alfaz(self, Value: float):
        self._wrapped.Alfaz = Value

    @property
    def Rho(self) -> float:
        return self._wrapped.Rho

    @Rho.setter
    def Rho(self, Value: float):
        self._wrapped.Rho = Value

    @property
    def Fy(self) -> float:
        return self._wrapped.Fy

    @Fy.setter
    def Fy(self, Value: float):
        self._wrapped.Fy = Value

    @property
    def Fu(self) -> float:
        return self._wrapped.Fu

    @Fu.setter
    def Fu(self, Value: float):
        self._wrapped.Fu = Value

    @property
    def Fy40(self) -> float:
        return self._wrapped.Fy40

    @Fy40.setter
    def Fy40(self, Value: float):
        self._wrapped.Fy40 = Value

    @property
    def Fu40(self) -> float:
        return self._wrapped.Fu40

    @Fu40.setter
    def Fu40(self, Value: float):
        self._wrapped.Fu40 = Value

    @property
    def SigmaH(self) -> float:
        return self._wrapped.SigmaH

    @SigmaH.setter
    def SigmaH(self, Value: float):
        self._wrapped.SigmaH = Value

    @property
    def SigmapH(self) -> float:
        return self._wrapped.SigmapH

    @SigmapH.setter
    def SigmapH(self, Value: float):
        self._wrapped.SigmapH = Value

    @property
    def Ry(self) -> float:
        return self._wrapped.Ry

    @Ry.setter
    def Ry(self, Value: float):
        self._wrapped.Ry = Value

    @property
    def R(self) -> float:
        return self._wrapped.R

    @R.setter
    def R(self, Value: float):
        self._wrapped.R = Value

    @property
    def Rc(self) -> float:
        return self._wrapped.Rc

    @Rc.setter
    def Rc(self, Value: float):
        self._wrapped.Rc = Value

    @property
    def SigmabH(self) -> float:
        return self._wrapped.SigmabH

    @SigmabH.setter
    def SigmabH(self, Value: float):
        self._wrapped.SigmabH = Value

    @property
    def SigmahH(self) -> float:
        return self._wrapped.SigmahH

    @SigmahH.setter
    def SigmahH(self, Value: float):
        self._wrapped.SigmahH = Value

    @property
    def Fit(self) -> float:
        return self._wrapped.Fit

    @Fit.setter
    def Fit(self, Value: float):
        self._wrapped.Fit = Value

    @property
    def GammaC(self) -> float:
        return self._wrapped.GammaC

    @GammaC.setter
    def GammaC(self, Value: float):
        self._wrapped.GammaC = Value

    @property
    def Alfacc(self) -> float:
        return self._wrapped.Alfacc

    @Alfacc.setter
    def Alfacc(self, Value: float):
        self._wrapped.Alfacc = Value

    @property
    def Fck(self) -> float:
        return self._wrapped.Fck

    @Fck.setter
    def Fck(self, Value: float):
        self._wrapped.Fck = Value

    @property
    def Fck_cube(self) -> float:
        return self._wrapped.Fck_cube

    @Fck_cube.setter
    def Fck_cube(self, Value: float):
        self._wrapped.Fck_cube = Value

    @property
    def EpsT(self) -> float:
        return self._wrapped.EpsT

    @property
    def EpsL(self) -> float:
        return self._wrapped.EpsL

    @property
    def EpsP(self) -> float:
        return self._wrapped.EpsP

    @property
    def EpsBH(self) -> float:
        return self._wrapped.EpsBH

    @property
    def EpsC1(self) -> float:
        return self._wrapped.EpsC1

    @property
    def EpsC1u(self) -> float:
        return self._wrapped.EpsC1u

    @property
    def EpsC2(self) -> float:
        return self._wrapped.EpsC2

    @property
    def EpsC2u(self) -> float:
        return self._wrapped.EpsC2u

    @property
    def EpsC3(self) -> float:
        return self._wrapped.EpsC3

    @property
    def EpsC3u(self) -> float:
        return self._wrapped.EpsC3u

    @property
    def EpsC1d(self) -> float:
        return self._wrapped.EpsC1d

    @property
    def EpsC2d(self) -> float:
        return self._wrapped.EpsC2d

    @property
    def E005(self) -> float:
        return self._wrapped.E005

    @E005.setter
    def E005(self, Value: float):
        self._wrapped.E005 = Value

    @property
    def Gmean(self) -> float:
        return self._wrapped.Gmean

    @Gmean.setter
    def Gmean(self, Value: float):
        self._wrapped.Gmean = Value

    @property
    def fmk(self) -> float:
        return self._wrapped.fmk

    @fmk.setter
    def fmk(self, Value: float):
        self._wrapped.fmk = Value

    @property
    def ft0k(self) -> float:
        return self._wrapped.ft0k

    @ft0k.setter
    def ft0k(self, Value: float):
        self._wrapped.ft0k = Value

    @property
    def ft90k(self) -> float:
        return self._wrapped.ft90k

    @ft90k.setter
    def ft90k(self, Value: float):
        self._wrapped.ft90k = Value

    @property
    def fc0k(self) -> float:
        return self._wrapped.fc0k

    @fc0k.setter
    def fc0k(self, Value: float):
        self._wrapped.fc0k = Value

    @property
    def fc90kz(self) -> float:
        return self._wrapped.fc90kz

    @fc90kz.setter
    def fc90kz(self, Value: float):
        self._wrapped.fc90kz = Value

    @property
    def fvkz(self) -> float:
        return self._wrapped.fvkz

    @fvkz.setter
    def fvkz(self, Value: float):
        self._wrapped.fvkz = Value

    @property
    def GammaM(self) -> float:
        return self._wrapped.GammaM

    @GammaM.setter
    def GammaM(self, Value: float):
        self._wrapped.GammaM = Value

    @property
    def fc90ky(self) -> float:
        return self._wrapped.fc90ky

    @fc90ky.setter
    def fc90ky(self, Value: float):
        self._wrapped.fc90ky = Value

    @property
    def fvky(self) -> float:
        return self._wrapped.fvky

    @fvky.setter
    def fvky(self, Value: float):
        self._wrapped.fvky = Value

    @property
    def S(self) -> float:
        return self._wrapped.S

    @S.setter
    def S(self, Value: float):
        self._wrapped.S = Value

    @property
    def TimberType(self) -> int:
        return self._wrapped.TimberType

    @TimberType.setter
    def TimberType(self, Value: int):
        self._wrapped.TimberType = Value

    @property
    def FillColour_vb(self) -> int:
        return self._wrapped.FillColour_vb

    @FillColour_vb.setter
    def FillColour_vb(self, Value: int):
        self._wrapped.FillColour_vb = Value

    @property
    def ContourColour_vb(self) -> int:
        return self._wrapped.ContourColour_vb

    @ContourColour_vb.setter
    def ContourColour_vb(self, Value: int):
        self._wrapped.ContourColour_vb = Value

    @property
    def UID(self) -> int:
        return self._wrapped.UID


class AxisVMMovingLoadOnDomain(AxWrapper):

    @property
    def ItemCount(self) -> int:
        return self._wrapped.ItemCount

    def AddItem(self, *args, **kwargs):
        return self._wrapped.AddItem(*args, **kwargs)

    def DeleteItem(self, *args, **kwargs):
        return self._wrapped.DeleteItem(*args, **kwargs)

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)

    def GetPath(self, *args, **kwargs):
        return self._wrapped.GetPath(*args, **kwargs)

    def SetPath(self, *args, **kwargs):
        return self._wrapped.SetPath(*args, **kwargs)

    @property
    def Steps(self) -> int:
        return self._wrapped.Steps

    @Steps.setter
    def Steps(self, Value: int):
        self._wrapped.Steps = Value

    @property
    def RunningMode(self) -> int:
        return self._wrapped.RunningMode

    @RunningMode.setter
    def RunningMode(self, Value: int):
        self._wrapped.RunningMode = Value

    @property
    def StructureMode(self) -> int:
        return self._wrapped.StructureMode

    @StructureMode.setter
    def StructureMode(self, Value: int):
        self._wrapped.StructureMode = Value

    @property
    def ConcentratedLoad(self) -> int:
        return self._wrapped.ConcentratedLoad

    @ConcentratedLoad.setter
    def ConcentratedLoad(self, Value: int):
        self._wrapped.ConcentratedLoad = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def SetPath_vb(self, *args, **kwargs):
        return self._wrapped.SetPath_vb(*args, **kwargs)


class AxisVMCrossSection(AxWrapper):

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: str):
        self._wrapped.Name = Value

    @property
    def CrossSectionShape(self) -> int:
        return self._wrapped.CrossSectionShape

    @CrossSectionShape.setter
    def CrossSectionShape(self, Value: int):
        self._wrapped.CrossSectionShape = Value

    @property
    def Process(self) -> int:
        return self._wrapped.Process

    @Process.setter
    def Process(self, Value: int):
        self._wrapped.Process = Value

    @property
    def StressPointCount(self) -> int:
        return self._wrapped.StressPointCount

    @property
    def aX(self) -> float:
        return self._wrapped.aX

    @aX.setter
    def aX(self, Value: float):
        self._wrapped.aX = Value

    @property
    def aY(self) -> float:
        return self._wrapped.aY

    @aY.setter
    def aY(self, Value: float):
        self._wrapped.aY = Value

    @property
    def aZ(self) -> float:
        return self._wrapped.aZ

    @aZ.setter
    def aZ(self, Value: float):
        self._wrapped.aZ = Value

    @property
    def Ix(self) -> float:
        return self._wrapped.Ix

    @Ix.setter
    def Ix(self, Value: float):
        self._wrapped.Ix = Value

    @property
    def Iy(self) -> float:
        return self._wrapped.Iy

    @Iy.setter
    def Iy(self, Value: float):
        self._wrapped.Iy = Value

    @property
    def Iz(self) -> float:
        return self._wrapped.Iz

    @Iz.setter
    def Iz(self, Value: float):
        self._wrapped.Iz = Value

    @property
    def Hy(self) -> float:
        return self._wrapped.Hy

    @Hy.setter
    def Hy(self, Value: float):
        self._wrapped.Hy = Value

    @property
    def Hz(self) -> float:
        return self._wrapped.Hz

    @Hz.setter
    def Hz(self, Value: float):
        self._wrapped.Hz = Value

    @property
    def tw(self) -> float:
        return self._wrapped.tw

    @tw.setter
    def tw(self, Value: float):
        self._wrapped.tw = Value

    @property
    def tf(self) -> float:
        return self._wrapped.tf

    @tf.setter
    def tf(self, Value: float):
        self._wrapped.tf = Value

    @property
    def Iw(self) -> float:
        return self._wrapped.Iw

    @Iw.setter
    def Iw(self, Value: float):
        self._wrapped.Iw = Value

    @property
    def Iyz(self) -> float:
        return self._wrapped.Iyz

    @Iyz.setter
    def Iyz(self, Value: float):
        self._wrapped.Iyz = Value

    @property
    def Ys(self) -> float:
        return self._wrapped.Ys

    @Ys.setter
    def Ys(self, Value: float):
        self._wrapped.Ys = Value

    @property
    def Zs(self) -> float:
        return self._wrapped.Zs

    @Zs.setter
    def Zs(self, Value: float):
        self._wrapped.Zs = Value

    @property
    def W1t(self) -> float:
        return self._wrapped.W1t

    @W1t.setter
    def W1t(self, Value: float):
        self._wrapped.W1t = Value

    @property
    def W1b(self) -> float:
        return self._wrapped.W1b

    @W1b.setter
    def W1b(self, Value: float):
        self._wrapped.W1b = Value

    @property
    def W2t(self) -> float:
        return self._wrapped.W2t

    @W2t.setter
    def W2t(self, Value: float):
        self._wrapped.W2t = Value

    @property
    def W2b(self) -> float:
        return self._wrapped.W2b

    @W2b.setter
    def W2b(self, Value: float):
        self._wrapped.W2b = Value

    @property
    def W1pl(self) -> float:
        return self._wrapped.W1pl

    @W1pl.setter
    def W1pl(self, Value: float):
        self._wrapped.W1pl = Value

    @property
    def W2pl(self) -> float:
        return self._wrapped.W2pl

    @W2pl.setter
    def W2pl(self, Value: float):
        self._wrapped.W2pl = Value

    @property
    def r1(self) -> float:
        return self._wrapped.r1

    @r1.setter
    def r1(self, Value: float):
        self._wrapped.r1 = Value

    @property
    def r2(self) -> float:
        return self._wrapped.r2

    @r2.setter
    def r2(self, Value: float):
        self._wrapped.r2 = Value

    @property
    def r3(self) -> float:
        return self._wrapped.r3

    @r3.setter
    def r3(self, Value: float):
        self._wrapped.r3 = Value

    @property
    def b2(self) -> float:
        return self._wrapped.b2

    @b2.setter
    def b2(self, Value: float):
        self._wrapped.b2 = Value

    @property
    def h2(self) -> float:
        return self._wrapped.h2

    @h2.setter
    def h2(self, Value: float):
        self._wrapped.h2 = Value

    @property
    def tw2(self) -> float:
        return self._wrapped.tw2

    @tw2.setter
    def tw2(self, Value: float):
        self._wrapped.tw2 = Value

    @property
    def tf2(self) -> float:
        return self._wrapped.tf2

    @tf2.setter
    def tf2(self, Value: float):
        self._wrapped.tf2 = Value

    @property
    def a(self) -> float:
        return self._wrapped.a

    @a.setter
    def a(self, Value: float):
        self._wrapped.a = Value

    @property
    def b1(self) -> float:
        return self._wrapped.b1

    @b1.setter
    def b1(self, Value: float):
        self._wrapped.b1 = Value

    @property
    def N(self) -> int:
        return self._wrapped.N

    @N.setter
    def N(self, Value: int):
        self._wrapped.N = Value

    @property
    def Yg(self) -> float:
        return self._wrapped.Yg

    @Yg.setter
    def Yg(self, Value: float):
        self._wrapped.Yg = Value

    @property
    def Zg(self) -> float:
        return self._wrapped.Zg

    @Zg.setter
    def Zg(self, Value: float):
        self._wrapped.Zg = Value

    @property
    def Alpha(self) -> float:
        return self._wrapped.Alpha

    @property
    def Mirrored(self) -> int:
        return self._wrapped.Mirrored

    @property
    def OuterPerimeter(self) -> float:
        return self._wrapped.OuterPerimeter

    @property
    def InnerPerimeter(self) -> float:
        return self._wrapped.InnerPerimeter

    @property
    def I1(self) -> float:
        return self._wrapped.I1

    @property
    def I2(self) -> float:
        return self._wrapped.I2

    @property
    def Ialpha(self) -> float:
        return self._wrapped.Ialpha

    @property
    def ShapePolygonList(self) -> 'AxisVMPolygon2dList':
        return self._wrapped.ShapePolygonList

    def AddStressPoint(self, *args, **kwargs):
        return self._wrapped.AddStressPoint(*args, **kwargs)

    def DeleteStressPoint(self, *args, **kwargs):
        return self._wrapped.DeleteStressPoint(*args, **kwargs)

    def Move(self, *args, **kwargs):
        return self._wrapped.Move(*args, **kwargs)

    def Rotate(self, *args, **kwargs):
        return self._wrapped.Rotate(*args, **kwargs)

    def Mirror(self, *args, **kwargs):
        return self._wrapped.Mirror(*args, **kwargs)

    @property
    def b(self) -> float:
        return self._wrapped.b

    @b.setter
    def b(self, Value: float):
        self._wrapped.b = Value

    @property
    def h(self) -> float:
        return self._wrapped.h

    @h.setter
    def h(self, Value: float):
        self._wrapped.h = Value

    def VerifyProperties(self, *args, **kwargs):
        return self._wrapped.VerifyProperties(*args, **kwargs)

    def GetStressPoint(self, *args, **kwargs):
        return self._wrapped.GetStressPoint(*args, **kwargs)

    def SetStressPoint(self, *args, **kwargs):
        return self._wrapped.SetStressPoint(*args, **kwargs)

    def GetStressPointParams(self, *args, **kwargs):
        return self._wrapped.GetStressPointParams(*args, **kwargs)

    def SetStressPointParams(self, *args, **kwargs):
        return self._wrapped.SetStressPointParams(*args, **kwargs)

    def GetUserParams(self, *args, **kwargs):
        return self._wrapped.GetUserParams(*args, **kwargs)

    def SetUserParams(self, *args, **kwargs):
        return self._wrapped.SetUserParams(*args, **kwargs)

    def GetUserParamsAsArray(self, *args, **kwargs):
        return self._wrapped.GetUserParamsAsArray(*args, **kwargs)

    def SetUserParamsAsArray(self, *args, **kwargs):
        return self._wrapped.SetUserParamsAsArray(*args, **kwargs)

    def GetUserParamsAsByteArray(self, *args, **kwargs):
        return self._wrapped.GetUserParamsAsByteArray(*args, **kwargs)

    def SetUserParamsAsByteArray(self, *args, **kwargs):
        return self._wrapped.SetUserParamsAsByteArray(*args, **kwargs)

    @property
    def Yg_Tekla(self) -> float:
        return self._wrapped.Yg_Tekla

    @Yg_Tekla.setter
    def Yg_Tekla(self, Value: float):
        self._wrapped.Yg_Tekla = Value

    @property
    def Zg_Tekla(self) -> float:
        return self._wrapped.Zg_Tekla

    @Zg_Tekla.setter
    def Zg_Tekla(self, Value: float):
        self._wrapped.Zg_Tekla = Value

    def SetUserParamsAsArray_vb(self, *args, **kwargs):
        return self._wrapped.SetUserParamsAsArray_vb(*args, **kwargs)

    def SetUserParamsAsByteArray_vb(self, *args, **kwargs):
        return self._wrapped.SetUserParamsAsByteArray_vb(*args, **kwargs)

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def CrossSectionShapeEx(self) -> int:
        return self._wrapped.CrossSectionShapeEx

    @CrossSectionShapeEx.setter
    def CrossSectionShapeEx(self, Value: int):
        self._wrapped.CrossSectionShapeEx = Value

    @property
    def DoubleWedgedI(self) -> 'RDoubleWedgedI':
        return self._wrapped.DoubleWedgedI

    @DoubleWedgedI.setter
    def DoubleWedgedI(self, Value: 'RDoubleWedgedI'):
        self._wrapped.DoubleWedgedI = Value

    @property
    def CrossSection2IX(self) -> 'RCrossSection2IX':
        return self._wrapped.CrossSection2IX

    @CrossSection2IX.setter
    def CrossSection2IX(self, Value: 'RCrossSection2IX'):
        self._wrapped.CrossSection2IX = Value

    @property
    def CrossSectionHSQ(self) -> 'RCrossSectionHSQ':
        return self._wrapped.CrossSectionHSQ

    @CrossSectionHSQ.setter
    def CrossSectionHSQ(self, Value: 'RCrossSectionHSQ'):
        self._wrapped.CrossSectionHSQ = Value

    @property
    def CrossSectionHSQA(self) -> 'RCrossSectionHSQA':
        return self._wrapped.CrossSectionHSQA

    @CrossSectionHSQA.setter
    def CrossSectionHSQA(self, Value: 'RCrossSectionHSQA'):
        self._wrapped.CrossSectionHSQA = Value

    @property
    def CrossSectionIFB(self) -> 'RCrossSectionIFB':
        return self._wrapped.CrossSectionIFB

    @CrossSectionIFB.setter
    def CrossSectionIFB(self, Value: 'RCrossSectionIFB'):
        self._wrapped.CrossSectionIFB = Value

    @property
    def CrossSectionSFB(self) -> 'RCrossSectionSFB':
        return self._wrapped.CrossSectionSFB

    @CrossSectionSFB.setter
    def CrossSectionSFB(self, Value: 'RCrossSectionSFB'):
        self._wrapped.CrossSectionSFB = Value

    @property
    def DoubleLClosed(self) -> 'RDoubleLClosed':
        return self._wrapped.DoubleLClosed

    @DoubleLClosed.setter
    def DoubleLClosed(self, Value: 'RDoubleLClosed'):
        self._wrapped.DoubleLClosed = Value


class AxisVMCrossSectionTables(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def PrgTableName(self) -> int:
        return self._wrapped.PrgTableName

    @property
    def DocTableName(self) -> int:
        return self._wrapped.DocTableName

    @property
    def FileName(self) -> int:
        return self._wrapped.FileName

    @property
    def Manufacturer(self) -> int:
        return self._wrapped.Manufacturer


class AxisVMCrossSectionTable(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @property
    def CrossSectionName(self) -> int:
        return self._wrapped.CrossSectionName

    @property
    def DocTableName(self) -> str:
        return self._wrapped.DocTableName

    @property
    def TableID(self) -> int:
        return self._wrapped.TableID


class AxisVMSpringParam(AxWrapper):

    @property
    def FullRec(self) -> 'RSpringParam':
        return self._wrapped.FullRec

    @FullRec.setter
    def FullRec(self, Value: 'RSpringParam'):
        self._wrapped.FullRec = Value

    @property
    def FunctionPoints(self) -> 'RPoint2d':
        return self._wrapped.FunctionPoints

    @FunctionPoints.setter
    def FunctionPoints(self, Value: 'RPoint2d'):
        self._wrapped.FunctionPoints = Value

    @property
    def FullRec_V161(self) -> 'RSpringParam_V161':
        return self._wrapped.FullRec_V161

    @FullRec_V161.setter
    def FullRec_V161(self, Value: 'RSpringParam_V161'):
        self._wrapped.FullRec_V161 = Value


class AxisVMSupports(AxWrapper):

    ...


class AxisVMSteelDesignResults(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetSteelDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignResultsByLoadCaseId(*args, **kwargs)

    def GetSteelDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSteelDesignResults(*args, **kwargs)

    def GetCriticalSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.GetCriticalSteelDesignResults(*args, **kwargs)

    def GetAllSteelDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllSteelDesignResultsByLoadCaseId(
            *args, **kwargs)

    def GetAllSteelDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllSteelDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeSteelDesignResults(*args, **kwargs)

    def GetAllCriticalSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalSteelDesignResults(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    def SteelDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SteelDesignResultsByLoadCaseId(*args, **kwargs)

    def SteelDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SteelDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.EnvelopeSteelDesignResults(*args, **kwargs)

    def CriticalSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.CriticalSteelDesignResults(*args, **kwargs)

    def AllSteelDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllSteelDesignResultsByLoadCaseId(*args, **kwargs)

    def AllSteelDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllSteelDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeSteelDesignResults(*args, **kwargs)

    def AllCriticalSteelDesignResults(self, *args, **kwargs):
        return self._wrapped.AllCriticalSteelDesignResults(*args, **kwargs)

    def GetEfficiencyAndCombination(self, *args, **kwargs):
        return self._wrapped.GetEfficiencyAndCombination(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEfficiencyAndCombinationByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetEfficiencyAndCombinationByLoadCaseId(
            *args, **kwargs)

    def GetEfficiencyAndCombinationByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetEfficiencyAndCombinationByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeEfficiencyAndCombination(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeEfficiencyAndCombination(
            *args, **kwargs)

    def GetCriticalEfficiencyAndCombination(self, *args, **kwargs):
        return self._wrapped.GetCriticalEfficiencyAndCombination(
            *args, **kwargs)

    def GetEnvelopeSteelDesignResults2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSteelDesignResults2(*args, **kwargs)

    def GetSteelDesignResultsByLoadCaseId_Abs(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignResultsByLoadCaseId_Abs(
            *args, **kwargs)

    def GetSteelDesignResultsByLoadCombinationId_Abs(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignResultsByLoadCombinationId_Abs(
            *args, **kwargs)

    def GetEnvelopeSteelDesignResults_Abs(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSteelDesignResults_Abs(*args, **kwargs)

    def GetCriticalSteelDesignResults_Abs(self, *args, **kwargs):
        return self._wrapped.GetCriticalSteelDesignResults_Abs(*args, **kwargs)


class AxisVMCalcCrackWidth(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetCrackWidthsByLoadCaseId(*args, **kwargs)

    def GetCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetCrackWidthsByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeCrackWidths(*args, **kwargs)

    def GetCriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetCriticalCrackWidths(*args, **kwargs)

    def GetAllCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllCrackWidthsByLoadCaseId(*args, **kwargs)

    def GetAllCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllCrackWidthsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeCrackWidths(*args, **kwargs)

    def GetAllCriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalCrackWidths(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def CrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.CrackWidthsByLoadCaseId(*args, **kwargs)

    def CrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.CrackWidthsByLoadCombinationId(*args, **kwargs)

    def EnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.EnvelopeCrackWidths(*args, **kwargs)

    def CriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.CriticalCrackWidths(*args, **kwargs)

    def AllCrackWidthsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllCrackWidthsByLoadCaseId(*args, **kwargs)

    def AllCrackWidthsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllCrackWidthsByLoadCombinationId(*args, **kwargs)

    def AllEnvelopeCrackWidths(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeCrackWidths(*args, **kwargs)

    def AllCriticalCrackWidths(self, *args, **kwargs):
        return self._wrapped.AllCriticalCrackWidths(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeCrackWidths2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeCrackWidths2(*args, **kwargs)

    def GetCriticalCrackWidths2(self, *args, **kwargs):
        return self._wrapped.GetCriticalCrackWidths2(*args, **kwargs)

    def EnvelopeCrackWidths2(self, *args, **kwargs):
        return self._wrapped.EnvelopeCrackWidths2(*args, **kwargs)

    def CriticalCrackWidths2(self, *args, **kwargs):
        return self._wrapped.CriticalCrackWidths2(*args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep


class AxisVMVelocity(AxWrapper):

    def GetNodalVelocityByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetNodalVelocityByLoadCaseId(*args, **kwargs)

    def GetEnvelopeNodalVelocity(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalVelocity(*args, **kwargs)

    def GetAllNodalVelocitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllNodalVelocitiesByLoadCaseId(*args, **kwargs)

    def GetAllEnvelopeNodalVelocities(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeNodalVelocities(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def TimeStep(self) -> int:
        return self._wrapped.TimeStep

    @TimeStep.setter
    def TimeStep(self, Value: int):
        self._wrapped.TimeStep = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def NodalVelocityByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.NodalVelocityByLoadCaseId(*args, **kwargs)

    def EnvelopeNodalVelocity(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalVelocity(*args, **kwargs)

    def AllNodalVelocitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllNodalVelocitiesByLoadCaseId(*args, **kwargs)

    def AllEnvelopeNodalVelocities(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeNodalVelocities(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value


class AxisVMCrossSectionEditor(AxWrapper):

    def AddCustomWithUserParams(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParams(*args, **kwargs)

    def AddCustomWithUserParamsAsArray(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsArray(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def AddCustomWithUserParamsAsByteArray(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsByteArray(
            *args, **kwargs)

    def AddCustomWithUserParamsAsArray_vb(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsArray_vb(*args, **kwargs)

    def AddCustomWithUserParamsAsByteArray_vb(self, *args, **kwargs):
        return self._wrapped.AddCustomWithUserParamsAsByteArray_vb(
            *args, **kwargs)


class AxisVMPolygon2d(AxWrapper):

    @property
    def Hole(self) -> int:
        return self._wrapped.Hole

    @Hole.setter
    def Hole(self, Value: int):
        self._wrapped.Hole = Value

    @property
    def LineCount(self) -> int:
        return self._wrapped.LineCount

    @property
    def Line(self) -> int:
        return self._wrapped.Line

    @Line.setter
    def Line(self, Value: int):
        self._wrapped.Line = Value

    def AddLine(self, *args, **kwargs):
        return self._wrapped.AddLine(*args, **kwargs)

    def DeleteLine(self, *args, **kwargs):
        return self._wrapped.DeleteLine(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)


class AxisVMLine2d(AxWrapper):

    @property
    def LineType(self) -> int:
        return self._wrapped.LineType

    @LineType.setter
    def LineType(self, Value: int):
        self._wrapped.LineType = Value

    @property
    def CircleArcOrientation(self) -> int:
        return self._wrapped.CircleArcOrientation

    @CircleArcOrientation.setter
    def CircleArcOrientation(self, Value: int):
        self._wrapped.CircleArcOrientation = Value

    def SetLinePoints(self, *args, **kwargs):
        return self._wrapped.SetLinePoints(*args, **kwargs)

    def GetLinePoints(self, *args, **kwargs):
        return self._wrapped.GetLinePoints(*args, **kwargs)

    def SetPoint(self, *args, **kwargs):
        return self._wrapped.SetPoint(*args, **kwargs)

    def GetPoint(self, *args, **kwargs):
        return self._wrapped.GetPoint(*args, **kwargs)

    def SetCircleArcCenter(self, *args, **kwargs):
        return self._wrapped.SetCircleArcCenter(*args, **kwargs)

    def GetCircleArcCenter(self, *args, **kwargs):
        return self._wrapped.GetCircleArcCenter(*args, **kwargs)


class AxisVMLineSupport(AxWrapper):

    @property
    def SupportType(self) -> int:
        return self._wrapped.SupportType

    @property
    def EdgeId(self) -> int:
        return self._wrapped.EdgeId

    @property
    def SurfaceId1(self) -> int:
        return self._wrapped.SurfaceId1

    @property
    def SurfaceId2(self) -> int:
        return self._wrapped.SurfaceId2

    @property
    def DomainId1(self) -> int:
        return self._wrapped.DomainId1

    @property
    def DomainId2(self) -> int:
        return self._wrapped.DomainId2

    @property
    def LineId(self) -> int:
        return self._wrapped.LineId

    def GetStiffnesses(self, *args, **kwargs):
        return self._wrapped.GetStiffnesses(*args, **kwargs)

    def SetStiffnesses(self, *args, **kwargs):
        return self._wrapped.SetStiffnesses(*args, **kwargs)

    def GetNonLinearity(self, *args, **kwargs):
        return self._wrapped.GetNonLinearity(*args, **kwargs)

    def SetNonLinearity(self, *args, **kwargs):
        return self._wrapped.SetNonLinearity(*args, **kwargs)

    def GetResistances(self, *args, **kwargs):
        return self._wrapped.GetResistances(*args, **kwargs)

    def SetResistances(self, *args, **kwargs):
        return self._wrapped.SetResistances(*args, **kwargs)

    def GetStiffnessesXYZ(self, *args, **kwargs):
        return self._wrapped.GetStiffnessesXYZ(*args, **kwargs)

    def SetStiffnessesXYZ(self, *args, **kwargs):
        return self._wrapped.SetStiffnessesXYZ(*args, **kwargs)

    def GetNonLinearityXYZ(self, *args, **kwargs):
        return self._wrapped.GetNonLinearityXYZ(*args, **kwargs)

    def SetNonLinearityXYZ(self, *args, **kwargs):
        return self._wrapped.SetNonLinearityXYZ(*args, **kwargs)

    def GetResistancesXYZ(self, *args, **kwargs):
        return self._wrapped.GetResistancesXYZ(*args, **kwargs)

    def SetResistancesXYZ(self, *args, **kwargs):
        return self._wrapped.SetResistancesXYZ(*args, **kwargs)

    @property
    def SectionCount(self) -> int:
        return self._wrapped.SectionCount

    @property
    def SectionPos(self) -> int:
        return self._wrapped.SectionPos

    def GetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.GetStiffnessCalcParams(*args, **kwargs)

    def SetStiffnessCalcParams(self, *args, **kwargs):
        return self._wrapped.SetStiffnessCalcParams(*args, **kwargs)

    @property
    def HasFooting(self) -> int:
        return self._wrapped.HasFooting

    @property
    def FootingType(self) -> int:
        return self._wrapped.FootingType

    def GetFootingDimensions(self, *args, **kwargs):
        return self._wrapped.GetFootingDimensions(*args, **kwargs)

    def GetFootingParams(self, *args, **kwargs):
        return self._wrapped.GetFootingParams(*args, **kwargs)

    def GetFootingParams_V153(self, *args, **kwargs):
        return self._wrapped.GetFootingParams_V153(*args, **kwargs)

    def GetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.GetPasternakStiffness(*args, **kwargs)

    def SetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.SetPasternakStiffness(*args, **kwargs)


class AxisVMMovingLoadOnBeam(AxWrapper):

    @property
    def ItemCount(self) -> int:
        return self._wrapped.ItemCount

    def AddItem(self, *args, **kwargs):
        return self._wrapped.AddItem(*args, **kwargs)

    def DeleteItem(self, *args, **kwargs):
        return self._wrapped.DeleteItem(*args, **kwargs)

    @property
    def ItemType(self) -> int:
        return self._wrapped.ItemType

    def GetItem(self, *args, **kwargs):
        return self._wrapped.GetItem(*args, **kwargs)

    def SetItem(self, *args, **kwargs):
        return self._wrapped.SetItem(*args, **kwargs)

    def GetPath(self, *args, **kwargs):
        return self._wrapped.GetPath(*args, **kwargs)

    def SetPath(self, *args, **kwargs):
        return self._wrapped.SetPath(*args, **kwargs)

    @property
    def Steps(self) -> int:
        return self._wrapped.Steps

    @Steps.setter
    def Steps(self, Value: int):
        self._wrapped.Steps = Value

    @property
    def RunningMode(self) -> int:
        return self._wrapped.RunningMode

    @RunningMode.setter
    def RunningMode(self, Value: int):
        self._wrapped.RunningMode = Value

    @property
    def StructureMode(self) -> int:
        return self._wrapped.StructureMode

    @StructureMode.setter
    def StructureMode(self, Value: int):
        self._wrapped.StructureMode = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)

    def SetPath_vb(self, *args, **kwargs):
        return self._wrapped.SetPath_vb(*args, **kwargs)


class AxisVMLine(AxWrapper):

    @property
    def StartNode(self) -> int:
        return self._wrapped.StartNode

    @StartNode.setter
    def StartNode(self, Value: int):
        self._wrapped.StartNode = Value

    @property
    def EndNode(self) -> int:
        return self._wrapped.EndNode

    @EndNode.setter
    def EndNode(self, Value: int):
        self._wrapped.EndNode = Value

    @property
    def GeomType(self) -> int:
        return self._wrapped.GeomType

    @property
    def LineType(self) -> int:
        return self._wrapped.LineType

    @property
    def Reference(self) -> int:
        return self._wrapped.Reference

    @Reference.setter
    def Reference(self, Value: int):
        self._wrapped.Reference = Value

    @property
    def NonLinearity(self) -> int:
        return self._wrapped.NonLinearity

    @NonLinearity.setter
    def NonLinearity(self, Value: int):
        self._wrapped.NonLinearity = Value

    @property
    def TrussResistance(self) -> float:
        return self._wrapped.TrussResistance

    @TrussResistance.setter
    def TrussResistance(self, Value: float):
        self._wrapped.TrussResistance = Value

    def DefineAsTruss(self, *args, **kwargs):
        return self._wrapped.DefineAsTruss(*args, **kwargs)

    def DefineAsBeam(self, *args, **kwargs):
        return self._wrapped.DefineAsBeam(*args, **kwargs)

    def DefineAsRib(self, *args, **kwargs):
        return self._wrapped.DefineAsRib(*args, **kwargs)

    def DefineAsSpring(self, *args, **kwargs):
        return self._wrapped.DefineAsSpring(*args, **kwargs)

    def DefineAsGap(self, *args, **kwargs):
        return self._wrapped.DefineAsGap(*args, **kwargs)

    @property
    def Length(self) -> float:
        return self._wrapped.Length

    @property
    def MidPointId(self) -> int:
        return self._wrapped.MidPointId

    @property
    def SectionCount(self) -> int:
        return self._wrapped.SectionCount

    @property
    def MidPointDOF(self) -> int:
        return self._wrapped.MidPointDOF

    @MidPointDOF.setter
    def MidPointDOF(self, Value: int):
        self._wrapped.MidPointDOF = Value

    def GetGeomData(self, *args, **kwargs):
        return self._wrapped.GetGeomData(*args, **kwargs)

    def SetGeomData(self, *args, **kwargs):
        return self._wrapped.SetGeomData(*args, **kwargs)

    def GetStartReleases(self, *args, **kwargs):
        return self._wrapped.GetStartReleases(*args, **kwargs)

    def SetStartReleases(self, *args, **kwargs):
        return self._wrapped.SetStartReleases(*args, **kwargs)

    def GetEndReleases(self, *args, **kwargs):
        return self._wrapped.GetEndReleases(*args, **kwargs)

    def SetEndReleases(self, *args, **kwargs):
        return self._wrapped.SetEndReleases(*args, **kwargs)

    def GetMidPoint(self, *args, **kwargs):
        return self._wrapped.GetMidPoint(*args, **kwargs)

    def SetGeomType(self, *args, **kwargs):
        return self._wrapped.SetGeomType(*args, **kwargs)

    @property
    def SectionPos(self) -> int:
        return self._wrapped.SectionPos

    def GetTrussData(self, *args, **kwargs):
        return self._wrapped.GetTrussData(*args, **kwargs)

    def GetBeamData(self, *args, **kwargs):
        return self._wrapped.GetBeamData(*args, **kwargs)

    def GetRibData(self, *args, **kwargs):
        return self._wrapped.GetRibData(*args, **kwargs)

    def GetSpringData(self, *args, **kwargs):
        return self._wrapped.GetSpringData(*args, **kwargs)

    def GetGapData(self, *args, **kwargs):
        return self._wrapped.GetGapData(*args, **kwargs)

    def ChangeLocalDirection(self, *args, **kwargs):
        return self._wrapped.ChangeLocalDirection(*args, **kwargs)

    def SplitByNode(self, *args, **kwargs):
        return self._wrapped.SplitByNode(*args, **kwargs)

    def SplitByN(self, *args, **kwargs):
        return self._wrapped.SplitByN(*args, **kwargs)

    @property
    def Timber_kdef(self) -> float:
        return self._wrapped.Timber_kdef

    @Timber_kdef.setter
    def Timber_kdef(self, Value: float):
        self._wrapped.Timber_kdef = Value

    @property
    def Timber_ServiceClass(self) -> int:
        return self._wrapped.Timber_ServiceClass

    @Timber_ServiceClass.setter
    def Timber_ServiceClass(self, Value: int):
        self._wrapped.Timber_ServiceClass = Value

    def DefineAsTimberTruss(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberTruss(*args, **kwargs)

    def DefineAsTimberBeam(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberBeam(*args, **kwargs)

    def DefineAsTimberRib(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberRib(*args, **kwargs)

    def GetTimberTrussData(self, *args, **kwargs):
        return self._wrapped.GetTimberTrussData(*args, **kwargs)

    def GetTimberBeamData(self, *args, **kwargs):
        return self._wrapped.GetTimberBeamData(*args, **kwargs)

    def GetTimberRibData(self, *args, **kwargs):
        return self._wrapped.GetTimberRibData(*args, **kwargs)

    def DefineAsRibWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.DefineAsRibWithAutoExcentricity(*args, **kwargs)

    def DefineAsTimberRibWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.DefineAsTimberRibWithAutoExcentricity(
            *args, **kwargs)

    def GetRibDataWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.GetRibDataWithAutoExcentricity(*args, **kwargs)

    def GetTimberRibDataWithAutoExcentricity(self, *args, **kwargs):
        return self._wrapped.GetTimberRibDataWithAutoExcentricity(
            *args, **kwargs)

    @property
    def Weight(self) -> float:
        return self._wrapped.Weight

    @property
    def Volume(self) -> float:
        return self._wrapped.Volume

    @property
    def IsBeam(self) -> int:
        return self._wrapped.IsBeam

    @property
    def IsColumn(self) -> int:
        return self._wrapped.IsColumn

    @property
    def IsOtherType(self) -> int:
        return self._wrapped.IsOtherType

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @property
    def StoreyId(self) -> int:
        return self._wrapped.StoreyId

    @property
    def MemberID(self) -> int:
        return self._wrapped.MemberID

    @property
    def ColumnReinforcementParametersExists(self) -> int:
        return self._wrapped.ColumnReinforcementParametersExists

    def DeleteColumnReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.DeleteColumnReinforcementParameters(
            *args, **kwargs)

    def GetColumnReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.GetColumnReinforcementParameters(*args, **kwargs)

    def SetColumnReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.SetColumnReinforcementParameters(*args, **kwargs)

    @property
    def RigidBodyId(self) -> int:
        return self._wrapped.RigidBodyId

    @property
    def MaterialColour(self) -> c_ulong:
        return self._wrapped.MaterialColour

    @MaterialColour.setter
    def MaterialColour(self, Value: c_ulong):
        self._wrapped.MaterialColour = Value

    @property
    def ContourColour(self) -> c_ulong:
        return self._wrapped.ContourColour

    @ContourColour.setter
    def ContourColour(self, Value: c_ulong):
        self._wrapped.ContourColour = Value

    @property
    def ArchitectElemType(self) -> int:
        return self._wrapped.ArchitectElemType

    @ArchitectElemType.setter
    def ArchitectElemType(self, Value: int):
        self._wrapped.ArchitectElemType = Value

    @property
    def MaterialColour_vb(self) -> int:
        return self._wrapped.MaterialColour_vb

    @MaterialColour_vb.setter
    def MaterialColour_vb(self, Value: int):
        self._wrapped.MaterialColour_vb = Value

    @property
    def ContourColour_vb(self) -> int:
        return self._wrapped.ContourColour_vb

    @ContourColour_vb.setter
    def ContourColour_vb(self, Value: int):
        self._wrapped.ContourColour_vb = Value

    @property
    def StiffnessReduction_A(self) -> float:
        return self._wrapped.StiffnessReduction_A

    @StiffnessReduction_A.setter
    def StiffnessReduction_A(self, Value: float):
        self._wrapped.StiffnessReduction_A = Value

    @property
    def StiffnessReduction_I(self) -> float:
        return self._wrapped.StiffnessReduction_I

    @StiffnessReduction_I.setter
    def StiffnessReduction_I(self, Value: float):
        self._wrapped.StiffnessReduction_I = Value

    def DeleteLineElement(self, *args, **kwargs):
        return self._wrapped.DeleteLineElement(*args, **kwargs)

    @property
    def StiffnessReduction(self) -> int:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: int):
        self._wrapped.StiffnessReduction = Value


class AxisVMResultTreeIterator(AxWrapper):

    def GetFirstNode(self, *args, **kwargs):
        return self._wrapped.GetFirstNode(*args, **kwargs)

    def GetNextSibling(self, *args, **kwargs):
        return self._wrapped.GetNextSibling(*args, **kwargs)

    def GetFirstChild(self, *args, **kwargs):
        return self._wrapped.GetFirstChild(*args, **kwargs)

    def HasChildren(self, *args, **kwargs):
        return self._wrapped.HasChildren(*args, **kwargs)

    @property
    def Text(self) -> int:
        return self._wrapped.Text

    @property
    def ResultRec(self) -> int:
        return self._wrapped.ResultRec


class AxisVMApplication(AxWrapper):

    @property
    def Visible(self) -> int:
        return self._wrapped.Visible

    @Visible.setter
    def Visible(self, Value: int):
        self._wrapped.Visible = Value

    @property
    def Loaded(self) -> int:
        return self._wrapped.Loaded

    @property
    def Models(self) -> 'AxisVMModels':
        return self._wrapped.Models

    @property
    def AskCloseOnLastReleased(self) -> int:
        return self._wrapped.AskCloseOnLastReleased

    @AskCloseOnLastReleased.setter
    def AskCloseOnLastReleased(self, Value: int):
        self._wrapped.AskCloseOnLastReleased = Value

    @property
    def LibraryMajorVersion(self) -> int:
        return self._wrapped.LibraryMajorVersion

    @property
    def Version(self) -> str:
        return self._wrapped.Version

    @property
    def LibraryMinorVersion(self) -> int:
        return self._wrapped.LibraryMinorVersion

    @property
    def CloseOnLastReleased(self) -> int:
        return self._wrapped.CloseOnLastReleased

    @CloseOnLastReleased.setter
    def CloseOnLastReleased(self, Value: int):
        self._wrapped.CloseOnLastReleased = Value

    @property
    def MainFormTab(self) -> int:
        return self._wrapped.MainFormTab

    @MainFormTab.setter
    def MainFormTab(self, Value: int):
        self._wrapped.MainFormTab = Value

    def MessageDlg(self, *args, **kwargs):
        return self._wrapped.MessageDlg(*args, **kwargs)

    @property
    def ApplicationClose(self) -> int:
        return self._wrapped.ApplicationClose

    @ApplicationClose.setter
    def ApplicationClose(self, Value: int):
        self._wrapped.ApplicationClose = Value

    @property
    def Catalog(self) -> 'AxisVMCatalog':
        return self._wrapped.Catalog

    @property
    def MainFormWindowState(self) -> int:
        return self._wrapped.MainFormWindowState

    @MainFormWindowState.setter
    def MainFormWindowState(self, Value: int):
        self._wrapped.MainFormWindowState = Value

    @property
    def MainFormWindowPosition(self) -> 'RWindowPosition':
        return self._wrapped.MainFormWindowPosition

    @MainFormWindowPosition.setter
    def MainFormWindowPosition(self, Value: 'RWindowPosition'):
        self._wrapped.MainFormWindowPosition = Value

    @property
    def MainFormWindowLeft(self) -> int:
        return self._wrapped.MainFormWindowLeft

    @MainFormWindowLeft.setter
    def MainFormWindowLeft(self, Value: int):
        self._wrapped.MainFormWindowLeft = Value

    @property
    def MainFormWindowTop(self) -> int:
        return self._wrapped.MainFormWindowTop

    @MainFormWindowTop.setter
    def MainFormWindowTop(self, Value: int):
        self._wrapped.MainFormWindowTop = Value

    @property
    def MainFormWindowWidth(self) -> int:
        return self._wrapped.MainFormWindowWidth

    @MainFormWindowWidth.setter
    def MainFormWindowWidth(self, Value: int):
        self._wrapped.MainFormWindowWidth = Value

    @property
    def MainFormWindowHeight(self) -> int:
        return self._wrapped.MainFormWindowHeight

    @MainFormWindowHeight.setter
    def MainFormWindowHeight(self, Value: int):
        self._wrapped.MainFormWindowHeight = Value

    def BringToFront(self, *args, **kwargs):
        return self._wrapped.BringToFront(*args, **kwargs)

    @property
    def ModalLevel(self) -> int:
        return self._wrapped.ModalLevel

    @property
    def ObjectCreator(self) -> 'AxisVMObjectCreator':
        return self._wrapped.ObjectCreator

    def ChangeUnitSystem(self, *args, **kwargs):
        return self._wrapped.ChangeUnitSystem(*args, **kwargs)

    @property
    def CrossSectionEditor(self) -> 'AxisVMCrossSectionEditor':
        return self._wrapped.CrossSectionEditor

    @property
    def ClientAliveTest(self) -> int:
        return self._wrapped.ClientAliveTest

    @ClientAliveTest.setter
    def ClientAliveTest(self, Value: int):
        self._wrapped.ClientAliveTest = Value

    @property
    def ClientAliveTestIntervalSec(self) -> int:
        return self._wrapped.ClientAliveTestIntervalSec

    @ClientAliveTestIntervalSec.setter
    def ClientAliveTestIntervalSec(self, Value: int):
        self._wrapped.ClientAliveTestIntervalSec = Value

    def MessageDlg_vb(self, *args, **kwargs):
        return self._wrapped.MessageDlg_vb(*args, **kwargs)

    @property
    def FullExePath(self) -> str:
        return self._wrapped.FullExePath

    def EnableMainForm(self, *args, **kwargs):
        return self._wrapped.EnableMainForm(*args, **kwargs)

    def DisableMainForm(self, *args, **kwargs):
        return self._wrapped.DisableMainForm(*args, **kwargs)

    @property
    def AxisVMPlatform(self) -> int:
        return self._wrapped.AxisVMPlatform

    @property
    def AskSaveOnLastReleased(self) -> int:
        return self._wrapped.AskSaveOnLastReleased

    @AskSaveOnLastReleased.setter
    def AskSaveOnLastReleased(self, Value: int):
        self._wrapped.AskSaveOnLastReleased = Value

    def CustomFunction(self, *args, **kwargs):
        return self._wrapped.CustomFunction(*args, **kwargs)

    def Quit(self, *args, **kwargs):
        return self._wrapped.Quit(*args, **kwargs)

    @property
    def COMclientsLoaded(self) -> int:
        return self._wrapped.COMclientsLoaded

    def UnLoadCOMclients(self, *args, **kwargs):
        return self._wrapped.UnLoadCOMclients(*args, **kwargs)

    def HandleMessages(self, *args, **kwargs):
        return self._wrapped.HandleMessages(*args, **kwargs)

    def InitThread(self, *args, **kwargs):
        return self._wrapped.InitThread(*args, **kwargs)


class AxisVMForces(AxWrapper):

    def GetLineForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineForceByLoadCaseId(*args, **kwargs)

    def GetLineForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineForceByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeLineForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineForce(*args, **kwargs)

    def GetCriticalLineForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineForce(*args, **kwargs)

    def GetLineForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineForcesByLoadCaseId(*args, **kwargs)

    def GetLineForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineForcesByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeLineForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineForces(*args, **kwargs)

    def GetCriticalLineForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineForces(*args, **kwargs)

    def GetAllLineForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllLineForcesByLoadCaseId(*args, **kwargs)

    def GetAllLineForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllLineForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeLineForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeLineForces(*args, **kwargs)

    def GetAllCriticalLineForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalLineForces(*args, **kwargs)

    def GetLineForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetLineForcesForResultBlocks(*args, **kwargs)

    def GetSurfaceForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceForceByLoadCaseId(*args, **kwargs)

    def GetSurfaceForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceForceByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSurfaceForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceForce(*args, **kwargs)

    def GetCriticalSurfaceForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceForce(*args, **kwargs)

    def GetSurfaceForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceForcesByLoadCaseId(*args, **kwargs)

    def GetSurfaceForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSurfaceForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceForces(*args, **kwargs)

    def GetCriticalSurfaceForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceForces(*args, **kwargs)

    def GetAllSurfaceForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllSurfaceForcesByLoadCaseId(*args, **kwargs)

    def GetAllSurfaceForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllSurfaceForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeSurfaceForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeSurfaceForces(*args, **kwargs)

    def GetAllCriticalSurfaceForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalSurfaceForces(*args, **kwargs)

    def GetSurfaceForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSurfaceForcesForResultBlocks(*args, **kwargs)

    def GetSurfaceForceValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSurfaceForceValuesForResultBlocks(
            *args, **kwargs)

    def GetNodalSupportForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetNodalSupportForceByLoadCaseId(*args, **kwargs)

    def GetNodalSupportForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetNodalSupportForceByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeNodalSupportForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalSupportForce(*args, **kwargs)

    def GetCriticalNodalSupportForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalNodalSupportForce(*args, **kwargs)

    def GetAllNodalSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllNodalSupportForcesByLoadCaseId(
            *args, **kwargs)

    def GetAllNodalSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllNodalSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeNodalSupportForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeNodalSupportForces(*args, **kwargs)

    def GetAllCriticalNodalSupportForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalNodalSupportForces(*args, **kwargs)

    def GetNodalSupportForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetNodalSupportForcesForResultBlocks(
            *args, **kwargs)

    def GetLineSupportForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineSupportForceByLoadCaseId(*args, **kwargs)

    def GetLineSupportForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineSupportForceByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeLineSupportForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineSupportForce(*args, **kwargs)

    def GetCriticalLineSupportForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineSupportForce(*args, **kwargs)

    def GetLineSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineSupportForcesByLoadCaseId(*args, **kwargs)

    def GetLineSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeLineSupportForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineSupportForces(*args, **kwargs)

    def GetCriticalLineSupportForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineSupportForces(*args, **kwargs)

    def GetAllLineSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllLineSupportForcesByLoadCaseId(
            *args, **kwargs)

    def GetAllLineSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllLineSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeLineSupportForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeLineSupportForces(*args, **kwargs)

    def GetAllCriticalLineSupportForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalLineSupportForces(*args, **kwargs)

    def GetLineSupportForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetLineSupportForcesForResultBlocks(
            *args, **kwargs)

    def GetSurfaceSupportForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceSupportForceByLoadCaseId(
            *args, **kwargs)

    def GetSurfaceSupportForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceSupportForceByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSurfaceSupportForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceSupportForce(*args, **kwargs)

    def GetCriticalSurfaceSupportForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceSupportForce(*args, **kwargs)

    def GetSurfaceSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceSupportForcesByLoadCaseId(
            *args, **kwargs)

    def GetSurfaceSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceSupportForces(*args, **kwargs)

    def GetCriticalSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceSupportForces(*args, **kwargs)

    def GetAllSurfaceSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllSurfaceSupportForcesByLoadCaseId(
            *args, **kwargs)

    def GetAllSurfaceSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllSurfaceSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeSurfaceSupportForces(
            *args, **kwargs)

    def GetAllCriticalSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalSurfaceSupportForces(
            *args, **kwargs)

    def GetSurfaceSupportForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSurfaceSupportForcesForResultBlocks(
            *args, **kwargs)

    def GetSurfaceSupportForceValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSurfaceSupportForceValuesForResultBlocks(
            *args, **kwargs)

    def GetSpringForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSpringForceByLoadCaseId(*args, **kwargs)

    def GetSpringForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSpringForceByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeSpringForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSpringForce(*args, **kwargs)

    def GetCriticalSpringForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalSpringForce(*args, **kwargs)

    def GetAllSpringForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllSpringForcesByLoadCaseId(*args, **kwargs)

    def GetAllSpringForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllSpringForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeSpringForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeSpringForces(*args, **kwargs)

    def GetAllCriticalSpringForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalSpringForces(*args, **kwargs)

    def GetSpringForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSpringForcesForResultBlocks(*args, **kwargs)

    def GetGapForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetGapForceByLoadCaseId(*args, **kwargs)

    def GetGapForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetGapForceByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeGapForce(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeGapForce(*args, **kwargs)

    def GetCriticalGapForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalGapForce(*args, **kwargs)

    def GetAllGapForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllGapForcesByLoadCaseId(*args, **kwargs)

    def GetAllGapForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllGapForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeGapForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeGapForces(*args, **kwargs)

    def GetAllCriticalGapForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalGapForces(*args, **kwargs)

    def GetGapForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetGapForcesForResultBlocks(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevelOrTimeStep(self) -> int:
        return self._wrapped.LoadLevelOrTimeStep

    @LoadLevelOrTimeStep.setter
    def LoadLevelOrTimeStep(self, Value: int):
        self._wrapped.LoadLevelOrTimeStep = Value

    @property
    def LineForceComponent(self) -> int:
        return self._wrapped.LineForceComponent

    @LineForceComponent.setter
    def LineForceComponent(self, Value: int):
        self._wrapped.LineForceComponent = Value

    @property
    def SurfaceForceComponent(self) -> int:
        return self._wrapped.SurfaceForceComponent

    @SurfaceForceComponent.setter
    def SurfaceForceComponent(self, Value: int):
        self._wrapped.SurfaceForceComponent = Value

    @property
    def NodalSupportForceComponent(self) -> int:
        return self._wrapped.NodalSupportForceComponent

    @NodalSupportForceComponent.setter
    def NodalSupportForceComponent(self, Value: int):
        self._wrapped.NodalSupportForceComponent = Value

    @property
    def LineSupportForceComponent(self) -> int:
        return self._wrapped.LineSupportForceComponent

    @LineSupportForceComponent.setter
    def LineSupportForceComponent(self, Value: int):
        self._wrapped.LineSupportForceComponent = Value

    @property
    def SurfaceSupportForceComponent(self) -> int:
        return self._wrapped.SurfaceSupportForceComponent

    @SurfaceSupportForceComponent.setter
    def SurfaceSupportForceComponent(self, Value: int):
        self._wrapped.SurfaceSupportForceComponent = Value

    @property
    def SpringForceComponent(self) -> int:
        return self._wrapped.SpringForceComponent

    @SpringForceComponent.setter
    def SpringForceComponent(self, Value: int):
        self._wrapped.SpringForceComponent = Value

    def LineForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineForceByLoadCaseId(*args, **kwargs)

    def LineForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineForceByLoadCombinationId(*args, **kwargs)

    def EnvelopeLineForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineForce(*args, **kwargs)

    def CriticalLineForce(self, *args, **kwargs):
        return self._wrapped.CriticalLineForce(*args, **kwargs)

    def LineForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineForcesByLoadCaseId(*args, **kwargs)

    def LineForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineForcesByLoadCombinationId(*args, **kwargs)

    def EnvelopeLineForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineForces(*args, **kwargs)

    def CriticalLineForces(self, *args, **kwargs):
        return self._wrapped.CriticalLineForces(*args, **kwargs)

    def AllLineForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllLineForcesByLoadCaseId(*args, **kwargs)

    def AllLineForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllLineForcesByLoadCombinationId(*args, **kwargs)

    def AllEnvelopeLineForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeLineForces(*args, **kwargs)

    def AllCriticalLineForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalLineForces(*args, **kwargs)

    def LineForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.LineForcesForResultBlocks(*args, **kwargs)

    def SurfaceForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SurfaceForceByLoadCaseId(*args, **kwargs)

    def SurfaceForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SurfaceForceByLoadCombinationId(*args, **kwargs)

    def EnvelopeSurfaceForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceForce(*args, **kwargs)

    def CriticalSurfaceForce(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceForce(*args, **kwargs)

    def SurfaceForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SurfaceForcesByLoadCaseId(*args, **kwargs)

    def SurfaceForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SurfaceForcesByLoadCombinationId(*args, **kwargs)

    def EnvelopeSurfaceForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceForces(*args, **kwargs)

    def CriticalSurfaceForces(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceForces(*args, **kwargs)

    def AllSurfaceForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllSurfaceForcesByLoadCaseId(*args, **kwargs)

    def AllSurfaceForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllSurfaceForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeSurfaceForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeSurfaceForces(*args, **kwargs)

    def AllCriticalSurfaceForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalSurfaceForces(*args, **kwargs)

    def SurfaceForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SurfaceForcesForResultBlocks(*args, **kwargs)

    def SurfaceForceValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SurfaceForceValuesForResultBlocks(*args, **kwargs)

    def NodalSupportForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.NodalSupportForceByLoadCaseId(*args, **kwargs)

    def NodalSupportForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.NodalSupportForceByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeNodalSupportForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalSupportForce(*args, **kwargs)

    def CriticalNodalSupportForce(self, *args, **kwargs):
        return self._wrapped.CriticalNodalSupportForce(*args, **kwargs)

    def AllNodalSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllNodalSupportForcesByLoadCaseId(*args, **kwargs)

    def AllNodalSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllNodalSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeNodalSupportForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeNodalSupportForces(*args, **kwargs)

    def AllCriticalNodalSupportForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalNodalSupportForces(*args, **kwargs)

    def NodalSupportForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.NodalSupportForcesForResultBlocks(*args, **kwargs)

    def LineSupportForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineSupportForceByLoadCaseId(*args, **kwargs)

    def LineSupportForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineSupportForceByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeLineSupportForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineSupportForce(*args, **kwargs)

    def CriticalLineSupportForce(self, *args, **kwargs):
        return self._wrapped.CriticalLineSupportForce(*args, **kwargs)

    def LineSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineSupportForcesByLoadCaseId(*args, **kwargs)

    def LineSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeLineSupportForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineSupportForces(*args, **kwargs)

    def CriticalLineSupportForces(self, *args, **kwargs):
        return self._wrapped.CriticalLineSupportForces(*args, **kwargs)

    def AllLineSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllLineSupportForcesByLoadCaseId(*args, **kwargs)

    def AllLineSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllLineSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeLineSupportForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeLineSupportForces(*args, **kwargs)

    def AllCriticalLineSupportForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalLineSupportForces(*args, **kwargs)

    def LineSupportForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.LineSupportForcesForResultBlocks(*args, **kwargs)

    def SurfaceSupportForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SurfaceSupportForceByLoadCaseId(*args, **kwargs)

    def SurfaceSupportForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SurfaceSupportForceByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeSurfaceSupportForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceSupportForce(*args, **kwargs)

    def CriticalSurfaceSupportForce(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceSupportForce(*args, **kwargs)

    def SurfaceSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SurfaceSupportForcesByLoadCaseId(*args, **kwargs)

    def SurfaceSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SurfaceSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceSupportForces(*args, **kwargs)

    def CriticalSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceSupportForces(*args, **kwargs)

    def AllSurfaceSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllSurfaceSupportForcesByLoadCaseId(
            *args, **kwargs)

    def AllSurfaceSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllSurfaceSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeSurfaceSupportForces(*args, **kwargs)

    def AllCriticalSurfaceSupportForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalSurfaceSupportForces(*args, **kwargs)

    def SurfaceSupportForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SurfaceSupportForcesForResultBlocks(
            *args, **kwargs)

    def SurfaceSupportForceValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SurfaceSupportForceValuesForResultBlocks(
            *args, **kwargs)

    def SpringForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SpringForceByLoadCaseId(*args, **kwargs)

    def SpringForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SpringForceByLoadCombinationId(*args, **kwargs)

    def EnvelopeSpringForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeSpringForce(*args, **kwargs)

    def CriticalSpringForce(self, *args, **kwargs):
        return self._wrapped.CriticalSpringForce(*args, **kwargs)

    def AllSpringForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllSpringForcesByLoadCaseId(*args, **kwargs)

    def AllSpringForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllSpringForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeSpringForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeSpringForces(*args, **kwargs)

    def AllCriticalSpringForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalSpringForces(*args, **kwargs)

    def SpringForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SpringForcesForResultBlocks(*args, **kwargs)

    def GapForceByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GapForceByLoadCaseId(*args, **kwargs)

    def GapForceByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GapForceByLoadCombinationId(*args, **kwargs)

    def EnvelopeGapForce(self, *args, **kwargs):
        return self._wrapped.EnvelopeGapForce(*args, **kwargs)

    def CriticalGapForce(self, *args, **kwargs):
        return self._wrapped.CriticalGapForce(*args, **kwargs)

    def AllGapForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllGapForcesByLoadCaseId(*args, **kwargs)

    def AllGapForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllGapForcesByLoadCombinationId(*args, **kwargs)

    def AllEnvelopeGapForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeGapForces(*args, **kwargs)

    def AllCriticalGapForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalGapForces(*args, **kwargs)

    def GapForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GapForcesForResultBlocks(*args, **kwargs)

    def GetEdgeConnectionForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetEdgeConnectionForcesByLoadCaseId(
            *args, **kwargs)

    def GetEdgeConnectionForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetEdgeConnectionForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeEdgeConnectionForces(*args, **kwargs)

    def GetCriticalEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalEdgeConnectionForces(*args, **kwargs)

    def GetAllEdgeConnectionForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllEdgeConnectionForcesByLoadCaseId(
            *args, **kwargs)

    def GetAllEdgeConnectionForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllEdgeConnectionForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeEdgeConnectionForces(
            *args, **kwargs)

    def GetAllCriticalEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalEdgeConnectionForces(
            *args, **kwargs)

    def GetEdgeConnectionForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetEdgeConnectionForcesForResultBlocks(
            *args, **kwargs)

    @property
    def EdgeConnectionForceComponent(self) -> int:
        return self._wrapped.EdgeConnectionForceComponent

    @EdgeConnectionForceComponent.setter
    def EdgeConnectionForceComponent(self, Value: int):
        self._wrapped.EdgeConnectionForceComponent = Value

    def EdgeConnectionForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.EdgeConnectionForcesByLoadCaseId(*args, **kwargs)

    def EdgeConnectionForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.EdgeConnectionForcesByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeEdgeConnectionForces(*args, **kwargs)

    def CriticalEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.CriticalEdgeConnectionForces(*args, **kwargs)

    def AllEdgeConnectionForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllEdgeConnectionForcesByLoadCaseId(
            *args, **kwargs)

    def AllEdgeConnectionForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllEdgeConnectionForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeEdgeConnectionForces(*args, **kwargs)

    def AllCriticalEdgeConnectionForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalEdgeConnectionForces(*args, **kwargs)

    def EdgeConnectionForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.EdgeConnectionForcesForResultBlocks(
            *args, **kwargs)

    def GetLinkElementForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLinkElementForcesByLoadCaseId(*args, **kwargs)

    def GetLinkElementForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLinkElementForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeLinkElementForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLinkElementForces(*args, **kwargs)

    def GetCriticalLinkElementForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalLinkElementForces(*args, **kwargs)

    def GetAllLinkElementForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllLinkElementForcesByLoadCaseId(
            *args, **kwargs)

    def GetAllLinkElementForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllLinkElementForcesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeLinkElementForces(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeLinkElementForces(*args, **kwargs)

    def GetAllCriticalLinkElementForces(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalLinkElementForces(*args, **kwargs)

    def GetLinkElementForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetLinkElementForcesForResultBlocks(
            *args, **kwargs)

    @property
    def LinkElementForceComponent(self) -> int:
        return self._wrapped.LinkElementForceComponent

    @LinkElementForceComponent.setter
    def LinkElementForceComponent(self, Value: int):
        self._wrapped.LinkElementForceComponent = Value

    def LinkElementForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LinkElementForcesByLoadCaseId(*args, **kwargs)

    def LinkElementForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LinkElementForcesByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeLinkElementForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeLinkElementForces(*args, **kwargs)

    def CriticalLinkElementForces(self, *args, **kwargs):
        return self._wrapped.CriticalLinkElementForces(*args, **kwargs)

    def AllLinkElementForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllLinkElementForcesByLoadCaseId(*args, **kwargs)

    def AllLinkElementForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllLinkElementForcesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeLinkElementForces(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeLinkElementForces(*args, **kwargs)

    def AllCriticalLinkElementForces(self, *args, **kwargs):
        return self._wrapped.AllCriticalLinkElementForces(*args, **kwargs)

    def LinkElementForcesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.LinkElementForcesForResultBlocks(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeLineForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineForce2(*args, **kwargs)

    def GetCriticalLineForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineForce2(*args, **kwargs)

    def GetEnvelopeSurfaceForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceForce2(*args, **kwargs)

    def GetCriticalSurfaceForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceForce2(*args, **kwargs)

    def GetEnvelopeNodalSupportForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalSupportForce2(*args, **kwargs)

    def GetCriticalNodalSupportForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalNodalSupportForce2(*args, **kwargs)

    def GetEnvelopeLineSupportForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineSupportForce2(*args, **kwargs)

    def GetCriticalLineSupportForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineSupportForce2(*args, **kwargs)

    def GetEnvelopeSurfaceSupportForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceSupportForce2(*args, **kwargs)

    def GetCriticalSurfaceSupportForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceSupportForce2(*args, **kwargs)

    def GetEnvelopeSpringForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSpringForce2(*args, **kwargs)

    def GetCriticalSpringForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalSpringForce2(*args, **kwargs)

    def GetEnvelopeGapForce2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeGapForce2(*args, **kwargs)

    def GetCriticalGapForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalGapForce2(*args, **kwargs)

    def EnvelopeLineForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineForce2(*args, **kwargs)

    def CriticalLineForce2(self, *args, **kwargs):
        return self._wrapped.CriticalLineForce2(*args, **kwargs)

    def EnvelopeSurfaceForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceForce2(*args, **kwargs)

    def CriticalSurfaceForce2(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceForce2(*args, **kwargs)

    def EnvelopeNodalSupportForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalSupportForce2(*args, **kwargs)

    def CriticalNodalSupportForce2(self, *args, **kwargs):
        return self._wrapped.CriticalNodalSupportForce2(*args, **kwargs)

    def EnvelopeLineSupportForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineSupportForce2(*args, **kwargs)

    def CriticalLineSupportForce2(self, *args, **kwargs):
        return self._wrapped.CriticalLineSupportForce2(*args, **kwargs)

    def EnvelopeSurfaceSupportForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceSupportForce2(*args, **kwargs)

    def CriticalSurfaceSupportForce2(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceSupportForce2(*args, **kwargs)

    def EnvelopeSpringForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeSpringForce2(*args, **kwargs)

    def CriticalSpringForce2(self, *args, **kwargs):
        return self._wrapped.CriticalSpringForce2(*args, **kwargs)

    def EnvelopeGapForce2(self, *args, **kwargs):
        return self._wrapped.EnvelopeGapForce2(*args, **kwargs)

    def CriticalGapForce2(self, *args, **kwargs):
        return self._wrapped.CriticalGapForce2(*args, **kwargs)

    def GetEnvelopeEdgeConnectionForces2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeEdgeConnectionForces2(*args, **kwargs)

    def GetCriticalEdgeConnectionForces2(self, *args, **kwargs):
        return self._wrapped.GetCriticalEdgeConnectionForces2(*args, **kwargs)

    def EnvelopeEdgeConnectionForces2(self, *args, **kwargs):
        return self._wrapped.EnvelopeEdgeConnectionForces2(*args, **kwargs)

    def CriticalEdgeConnectionForces2(self, *args, **kwargs):
        return self._wrapped.CriticalEdgeConnectionForces2(*args, **kwargs)

    def GetEnvelopeLinkElementForces2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLinkElementForces2(*args, **kwargs)

    def GetCriticalLinkElementForces2(self, *args, **kwargs):
        return self._wrapped.GetCriticalLinkElementForces2(*args, **kwargs)

    def EnvelopeLinkElementForces2(self, *args, **kwargs):
        return self._wrapped.EnvelopeLinkElementForces2(*args, **kwargs)

    def CriticalLinkElementForces2(self, *args, **kwargs):
        return self._wrapped.CriticalLinkElementForces2(*args, **kwargs)

    def GetMemberForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetMemberForcesByLoadCaseId(*args, **kwargs)

    def GetMemberForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetMemberForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeMemberForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeMemberForces(*args, **kwargs)

    def GetCriticalMemberForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalMemberForces(*args, **kwargs)

    def SaveMemberForcesToMetaFileByLoadCaseID(self, *args, **kwargs):
        return self._wrapped.SaveMemberForcesToMetaFileByLoadCaseID(
            *args, **kwargs)

    def SaveMemberForcesToMetaFileByLoadCombinationID(self, *args, **kwargs):
        return self._wrapped.SaveMemberForcesToMetaFileByLoadCombinationID(
            *args, **kwargs)

    def SaveEnvelopeMemberForcesToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveEnvelopeMemberForcesToMetaFile(
            *args, **kwargs)

    def SaveCriticalMemberForcesToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveCriticalMemberForcesToMetaFile(
            *args, **kwargs)

    def GetLineForcesByLoadCaseIdConnectedToNode(self, *args, **kwargs):
        return self._wrapped.GetLineForcesByLoadCaseIdConnectedToNode(
            *args, **kwargs)

    def LineForcesByLoadCaseIdConnectedToNode(self, *args, **kwargs):
        return self._wrapped.LineForcesByLoadCaseIdConnectedToNode(
            *args, **kwargs)

    def GetLineForcesByLoadCombinationIdConnectedToNode(self, *args, **kwargs):
        return self._wrapped.GetLineForcesByLoadCombinationIdConnectedToNode(
            *args, **kwargs)

    def LineForcesByLoadCombinationIdConnectedToNode(self, *args, **kwargs):
        return self._wrapped.LineForcesByLoadCombinationIdConnectedToNode(
            *args, **kwargs)

    def GetEnvelopeLineForcesConnectedToNode(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineForcesConnectedToNode(
            *args, **kwargs)

    def EnvelopeLineForcesConnectedToNode(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineForcesConnectedToNode(*args, **kwargs)

    def GetCriticalLineForcesConnectedToNode(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineForcesConnectedToNode(
            *args, **kwargs)

    def CriticalLineForcesConnectedToNode(self, *args, **kwargs):
        return self._wrapped.CriticalLineForcesConnectedToNode(*args, **kwargs)

    def GetVirtualBeamOrStripForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetVirtualBeamOrStripForcesByLoadCaseId(
            *args, **kwargs)

    def VirtualBeamOrStripForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.VirtualBeamOrStripForcesByLoadCaseId(
            *args, **kwargs)

    def GetVirtualBeamOrStripForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetVirtualBeamOrStripForcesByLoadCombinationId(
            *args, **kwargs)

    def VirtualBeamOrStripForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.VirtualBeamOrStripForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeVirtualBeamOrStripForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeVirtualBeamOrStripForces(
            *args, **kwargs)

    def EnvelopeVirtualBeamOrStripForces(self, *args, **kwargs):
        return self._wrapped.EnvelopeVirtualBeamOrStripForces(*args, **kwargs)

    def GetCriticalVirtualBeamOrStripForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalVirtualBeamOrStripForces(
            *args, **kwargs)

    def CriticalVirtualBeamOrStripForces(self, *args, **kwargs):
        return self._wrapped.CriticalVirtualBeamOrStripForces(*args, **kwargs)

    @property
    def VirtualBeamForceComponent(self) -> int:
        return self._wrapped.VirtualBeamForceComponent

    @VirtualBeamForceComponent.setter
    def VirtualBeamForceComponent(self, Value: int):
        self._wrapped.VirtualBeamForceComponent = Value

    def GetEnvelopeVirtualBeamOrStripForces2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeVirtualBeamOrStripForces2(
            *args, **kwargs)

    def EnvelopeVirtualBeamOrStripForces2(self, *args, **kwargs):
        return self._wrapped.EnvelopeVirtualBeamOrStripForces2(*args, **kwargs)

    def GetCriticalVirtualBeamOrStripForce(self, *args, **kwargs):
        return self._wrapped.GetCriticalVirtualBeamOrStripForce(
            *args, **kwargs)

    def CriticalVirtualBeamOrStripForce(self, *args, **kwargs):
        return self._wrapped.CriticalVirtualBeamOrStripForce(*args, **kwargs)

    def GetCriticalVirtualBeamOrStripForce2(self, *args, **kwargs):
        return self._wrapped.GetCriticalVirtualBeamOrStripForce2(
            *args, **kwargs)

    def CriticalVirtualBeamOrStripForce2(self, *args, **kwargs):
        return self._wrapped.CriticalVirtualBeamOrStripForce2(*args, **kwargs)

    @property
    def SeismicComponentSumType(self) -> int:
        return self._wrapped.SeismicComponentSumType

    @SeismicComponentSumType.setter
    def SeismicComponentSumType(self, Value: int):
        self._wrapped.SeismicComponentSumType = Value

    def GetLineForceByLoadCombinationIdEQ(self, *args, **kwargs):
        return self._wrapped.GetLineForceByLoadCombinationIdEQ(*args, **kwargs)

    def GetEnvelopeLineForceEQ(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineForceEQ(*args, **kwargs)

    def GetCriticalLineForceEQ(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineForceEQ(*args, **kwargs)

    def LineForceByLoadCombinationIdEQ(self, *args, **kwargs):
        return self._wrapped.LineForceByLoadCombinationIdEQ(*args, **kwargs)

    def EnvelopeLineForceEQ(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineForceEQ(*args, **kwargs)

    def CriticalLineForceEQ(self, *args, **kwargs):
        return self._wrapped.CriticalLineForceEQ(*args, **kwargs)

    def SaveVirtualBeamOrStripForcesToMetaFileByLoadCaseID(
            self, *args, **kwargs):
        return self._wrapped.SaveVirtualBeamOrStripForcesToMetaFileByLoadCaseID(
            *args, **kwargs)

    def SaveVirtualBeamOrStripForcesToMetaFileByLoadCombinationID(
            self, *args, **kwargs):
        return self._wrapped.SaveVirtualBeamOrStripForcesToMetaFileByLoadCombinationID(
            *args, **kwargs)

    def SaveEnvelopeVirtualBeamOrStripForcesToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveEnvelopeVirtualBeamOrStripForcesToMetaFile(
            *args, **kwargs)

    def SaveCriticalVirtualBeamOrStripForcesToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveCriticalVirtualBeamOrStripForcesToMetaFile(
            *args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep

    def GetMembersSupportForcesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetMembersSupportForcesByLoadCaseId(
            *args, **kwargs)

    def GetMembersSupportForcesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetMembersSupportForcesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeMembersSupportForces(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeMembersSupportForces(*args, **kwargs)

    def GetCriticalMembersSupportForces(self, *args, **kwargs):
        return self._wrapped.GetCriticalMembersSupportForces(*args, **kwargs)

    def NodalSupportForceByLoadCombinationIdEQ(self, *args, **kwargs):
        return self._wrapped.NodalSupportForceByLoadCombinationIdEQ(
            *args, **kwargs)

    def EnvelopeNodalSupportForceEQ(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalSupportForceEQ(*args, **kwargs)

    def CriticalNodalSupportForceEQ(self, *args, **kwargs):
        return self._wrapped.CriticalNodalSupportForceEQ(*args, **kwargs)

    def LineSupportForceByLoadCombinationIdEQ(self, *args, **kwargs):
        return self._wrapped.LineSupportForceByLoadCombinationIdEQ(
            *args, **kwargs)

    def EnvelopeLineSupportForceEQ(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineSupportForceEQ(*args, **kwargs)

    def CriticalLineSupportForceEQ(self, *args, **kwargs):
        return self._wrapped.CriticalLineSupportForceEQ(*args, **kwargs)

    @property
    def SupportSeismicSumType(self) -> int:
        return self._wrapped.SupportSeismicSumType

    @SupportSeismicSumType.setter
    def SupportSeismicSumType(self, Value: int):
        self._wrapped.SupportSeismicSumType = Value

    def SurfaceForceByLoadCombinationIdEQ(self, *args, **kwargs):
        return self._wrapped.SurfaceForceByLoadCombinationIdEQ(*args, **kwargs)

    def EnvelopeSurfaceForceEQ(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceForceEQ(*args, **kwargs)

    def CriticalSurfaceForceEQ(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceForceEQ(*args, **kwargs)

    def CriticalLineForce2EQ(self, *args, **kwargs):
        return self._wrapped.CriticalLineForce2EQ(*args, **kwargs)


class AxisVMVerticalDisplacements(AxWrapper):

    def GetEnvelopeNodalDisplacement(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalDisplacement(*args, **kwargs)

    def GetAllEnvelopeNodalDisplacements(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeNodalDisplacements(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def EnvelopeNodalDisplacement(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalDisplacement(*args, **kwargs)

    def AllEnvelopeNodalDisplacements(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeNodalDisplacements(*args, **kwargs)


class AxisVMObjectCreator(AxWrapper):

    def NewLine2d(self, *args, **kwargs):
        return self._wrapped.NewLine2d(*args, **kwargs)

    def NewPolygon2d(self, *args, **kwargs):
        return self._wrapped.NewPolygon2d(*args, **kwargs)

    def NewPolygon2dList(self, *args, **kwargs):
        return self._wrapped.NewPolygon2dList(*args, **kwargs)

    def NewLines3d(self, *args, **kwargs):
        return self._wrapped.NewLines3d(*args, **kwargs)

    def NewMovingLoadOnBeam(self, *args, **kwargs):
        return self._wrapped.NewMovingLoadOnBeam(*args, **kwargs)

    def NewMovingLoadOnDomain(self, *args, **kwargs):
        return self._wrapped.NewMovingLoadOnDomain(*args, **kwargs)


class AxisVMCatalog(AxWrapper):

    def GetMaterialNames(self, *args, **kwargs):
        return self._wrapped.GetMaterialNames(*args, **kwargs)

    def GetCrossSectionNames(self, *args, **kwargs):
        return self._wrapped.GetCrossSectionNames(*args, **kwargs)

    def GetCrossSectionTableNames(self, *args, **kwargs):
        return self._wrapped.GetCrossSectionTableNames(*args, **kwargs)

    def GetMaterial(self, *args, **kwargs):
        return self._wrapped.GetMaterial(*args, **kwargs)

    def GetCrossSection(self, *args, **kwargs):
        return self._wrapped.GetCrossSection(*args, **kwargs)

    def GetMaterialNamesByType(self, *args, **kwargs):
        return self._wrapped.GetMaterialNamesByType(*args, **kwargs)

    def GetRebarSteelGradeNames(self, *args, **kwargs):
        return self._wrapped.GetRebarSteelGradeNames(*args, **kwargs)

    def GetXLAMmanufacturers(self, *args, **kwargs):
        return self._wrapped.GetXLAMmanufacturers(*args, **kwargs)

    def GetXLAMnamesByManufacturers(self, *args, **kwargs):
        return self._wrapped.GetXLAMnamesByManufacturers(*args, **kwargs)

    def GetCrossSectionNamesEx(self, *args, **kwargs):
        return self._wrapped.GetCrossSectionNamesEx(*args, **kwargs)

    def GetCrossSectionTableNamesEx(self, *args, **kwargs):
        return self._wrapped.GetCrossSectionTableNamesEx(*args, **kwargs)

    def GetCrossSectionEx(self, *args, **kwargs):
        return self._wrapped.GetCrossSectionEx(*args, **kwargs)

    def GetAllTables(self, *args, **kwargs):
        return self._wrapped.GetAllTables(*args, **kwargs)

    def GetTableCrossSections(self, *args, **kwargs):
        return self._wrapped.GetTableCrossSections(*args, **kwargs)

    def GetCrossSection_V154(self, *args, **kwargs):
        return self._wrapped.GetCrossSection_V154(*args, **kwargs)


class AxisVMPolygon2dList(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    @property
    def Item(self) -> int:
        return self._wrapped.Item

    @Item.setter
    def Item(self, Value: int):
        self._wrapped.Item = Value

    def Add(self, *args, **kwargs):
        return self._wrapped.Add(*args, **kwargs)

    def Delete(self, *args, **kwargs):
        return self._wrapped.Delete(*args, **kwargs)

    def Clear(self, *args, **kwargs):
        return self._wrapped.Clear(*args, **kwargs)


class AxisVMDisplacements(AxWrapper):

    def GetNodalDisplacementByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetNodalDisplacementByLoadCaseId(*args, **kwargs)

    def GetNodalDisplacementByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetNodalDisplacementByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeNodalDisplacement(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalDisplacement(*args, **kwargs)

    def GetCriticalNodalDisplacement(self, *args, **kwargs):
        return self._wrapped.GetCriticalNodalDisplacement(*args, **kwargs)

    def GetAllNodalDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllNodalDisplacementsByLoadCaseId(
            *args, **kwargs)

    def GetAllNodalDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllNodalDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeNodalDisplacements(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeNodalDisplacements(*args, **kwargs)

    def GetAllCriticalNodalDisplacements(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalNodalDisplacements(*args, **kwargs)

    def GetNodalDisplacementsForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetNodalDisplacementsForResultBlocks(
            *args, **kwargs)

    def GetLineDisplacementByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineDisplacementByLoadCaseId(*args, **kwargs)

    def GetLineDisplacementByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineDisplacementByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeLineDisplacement(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineDisplacement(*args, **kwargs)

    def GetCriticalLineDisplacement(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineDisplacement(*args, **kwargs)

    def GetLineDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineDisplacementsByLoadCaseId(*args, **kwargs)

    def GetLineDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeLineDisplacements(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineDisplacements(*args, **kwargs)

    def GetCriticalLineDisplacements(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineDisplacements(*args, **kwargs)

    def GetAllLineDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllLineDisplacementsByLoadCaseId(
            *args, **kwargs)

    def GetAllLineDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllLineDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeLineDisplacements(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeLineDisplacements(*args, **kwargs)

    def GetAllCriticalLineDisplacements(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalLineDisplacements(*args, **kwargs)

    def GetLineDisplacementsForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetLineDisplacementsForResultBlocks(
            *args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevelOrModeShapeOrTimeStep(self) -> int:
        return self._wrapped.LoadLevelOrModeShapeOrTimeStep

    @LoadLevelOrModeShapeOrTimeStep.setter
    def LoadLevelOrModeShapeOrTimeStep(self, Value: int):
        self._wrapped.LoadLevelOrModeShapeOrTimeStep = Value

    @property
    def WithReinforcement(self) -> int:
        return self._wrapped.WithReinforcement

    @WithReinforcement.setter
    def WithReinforcement(self, Value: int):
        self._wrapped.WithReinforcement = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def NodalDisplacementByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.NodalDisplacementByLoadCaseId(*args, **kwargs)

    def NodalDisplacementByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.NodalDisplacementByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeNodalDisplacement(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalDisplacement(*args, **kwargs)

    def CriticalNodalDisplacement(self, *args, **kwargs):
        return self._wrapped.CriticalNodalDisplacement(*args, **kwargs)

    def AllNodalDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllNodalDisplacementsByLoadCaseId(*args, **kwargs)

    def AllNodalDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllNodalDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeNodalDisplacements(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeNodalDisplacements(*args, **kwargs)

    def AllCriticalNodalDisplacements(self, *args, **kwargs):
        return self._wrapped.AllCriticalNodalDisplacements(*args, **kwargs)

    def NodalDisplacementsForResultBlocks(self, *args, **kwargs):
        return self._wrapped.NodalDisplacementsForResultBlocks(*args, **kwargs)

    def LineDisplacementByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineDisplacementByLoadCaseId(*args, **kwargs)

    def LineDisplacementByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineDisplacementByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeLineDisplacement(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineDisplacement(*args, **kwargs)

    def CriticalLineDisplacement(self, *args, **kwargs):
        return self._wrapped.CriticalLineDisplacement(*args, **kwargs)

    def LineDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineDisplacementsByLoadCaseId(*args, **kwargs)

    def LineDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeLineDisplacements(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineDisplacements(*args, **kwargs)

    def CriticalLineDisplacements(self, *args, **kwargs):
        return self._wrapped.CriticalLineDisplacements(*args, **kwargs)

    def AllLineDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllLineDisplacementsByLoadCaseId(*args, **kwargs)

    def AllLineDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllLineDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeLineDisplacements(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeLineDisplacements(*args, **kwargs)

    def AllCriticalLineDisplacements(self, *args, **kwargs):
        return self._wrapped.AllCriticalLineDisplacements(*args, **kwargs)

    def LineDisplacementsForResultBlocks(self, *args, **kwargs):
        return self._wrapped.LineDisplacementsForResultBlocks(*args, **kwargs)

    def GetEndReleasesDeformationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetEndReleasesDeformationsByLoadCaseId(
            *args, **kwargs)

    def GetEndReleasesDeformationsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetEndReleasesDeformationsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeEndReleasesDeformations(
            *args, **kwargs)

    def GetCriticalEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.GetCriticalEndReleasesDeformations(
            *args, **kwargs)

    def GetAllEndReleasesDeformationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllEndReleasesDeformationsByLoadCaseId(
            *args, **kwargs)

    def GetAllEndReleasesDeformationsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.GetAllEndReleasesDeformationsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeEndReleasesDeformations(
            *args, **kwargs)

    def GetAllCriticalEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalEndReleasesDeformations(
            *args, **kwargs)

    def EndReleasesDeformationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.EndReleasesDeformationsByLoadCaseId(
            *args, **kwargs)

    def EndReleasesDeformationsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.EndReleasesDeformationsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.EnvelopeEndReleasesDeformations(*args, **kwargs)

    def CriticalEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.CriticalEndReleasesDeformations(*args, **kwargs)

    def AllEndReleasesDeformationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllEndReleasesDeformationsByLoadCaseId(
            *args, **kwargs)

    def AllEndReleasesDeformationsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllEndReleasesDeformationsByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeEndReleasesDeformations(
            *args, **kwargs)

    def AllCriticalEndReleasesDeformations(self, *args, **kwargs):
        return self._wrapped.AllCriticalEndReleasesDeformations(
            *args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeNodalDisplacement2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalDisplacement2(*args, **kwargs)

    def GetCriticalNodalDisplacement2(self, *args, **kwargs):
        return self._wrapped.GetCriticalNodalDisplacement2(*args, **kwargs)

    def GetEnvelopeLineDisplacement2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineDisplacement2(*args, **kwargs)

    def GetCriticalLineDisplacement2(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineDisplacement2(*args, **kwargs)

    def EnvelopeNodalDisplacement2(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalDisplacement2(*args, **kwargs)

    def CriticalNodalDisplacement2(self, *args, **kwargs):
        return self._wrapped.CriticalNodalDisplacement2(*args, **kwargs)

    def EnvelopeLineDisplacement2(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineDisplacement2(*args, **kwargs)

    def CriticalLineDisplacement2(self, *args, **kwargs):
        return self._wrapped.CriticalLineDisplacement2(*args, **kwargs)

    def GetMemberDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetMemberDisplacementsByLoadCaseId(
            *args, **kwargs)

    def GetMemberDisplacementsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetMemberDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeMemberDisplacements(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeMemberDisplacements(*args, **kwargs)

    def GetCriticalMemberDisplacements(self, *args, **kwargs):
        return self._wrapped.GetCriticalMemberDisplacements(*args, **kwargs)

    @property
    def DisplacementSystem(self) -> int:
        return self._wrapped.DisplacementSystem

    @DisplacementSystem.setter
    def DisplacementSystem(self, Value: int):
        self._wrapped.DisplacementSystem = Value

    def SaveMemberDisplacementsToMetaFileByLoadCaseID(self, *args, **kwargs):
        return self._wrapped.SaveMemberDisplacementsToMetaFileByLoadCaseID(
            *args, **kwargs)

    def SaveMemberDisplacementsToMetaFileByLoadCombinationID(
            self, *args, **kwargs):
        return self._wrapped.SaveMemberDisplacementsToMetaFileByLoadCombinationID(
            *args, **kwargs)

    def SaveEnvelopeMemberDisplacementsToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveEnvelopeMemberDisplacementsToMetaFile(
            *args, **kwargs)

    def SaveCriticalMemberDisplacementsToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveCriticalMemberDisplacementsToMetaFile(
            *args, **kwargs)

    def VirtualBeamOrStripDisplacementsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.VirtualBeamOrStripDisplacementsByLoadCaseId(
            *args, **kwargs)

    def VirtualBeamOrStripDisplacementsByLoadCombinationId(
            self, *args, **kwargs):
        return self._wrapped.VirtualBeamOrStripDisplacementsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeVirtualBeamOrStripDisplacements(self, *args, **kwargs):
        return self._wrapped.EnvelopeVirtualBeamOrStripDisplacements(
            *args, **kwargs)

    def CriticalVirtualBeamOrStripDisplacements(self, *args, **kwargs):
        return self._wrapped.CriticalVirtualBeamOrStripDisplacements(
            *args, **kwargs)

    def EnvelopeVirtualBeamOrStripDisplacements2(self, *args, **kwargs):
        return self._wrapped.EnvelopeVirtualBeamOrStripDisplacements2(
            *args, **kwargs)

    def CriticalVirtualBeamOrStripDisplacement(self, *args, **kwargs):
        return self._wrapped.CriticalVirtualBeamOrStripDisplacement(
            *args, **kwargs)

    def CriticalVirtualBeamOrStripDisplacement2(self, *args, **kwargs):
        return self._wrapped.CriticalVirtualBeamOrStripDisplacement2(
            *args, **kwargs)

    def SaveVirtualBeamOrStripDisplacementsToMetaFileByLoadCaseID(
            self, *args, **kwargs):
        return self._wrapped.SaveVirtualBeamOrStripDisplacementsToMetaFileByLoadCaseID(
            *args, **kwargs)

    def SaveVirtualBeamOrStripDisplacementsToMetaFileByLoadCombinationID(
            self, *args, **kwargs):
        return self._wrapped.SaveVirtualBeamOrStripDisplacementsToMetaFileByLoadCombinationID(
            *args, **kwargs)

    def SaveEnvelopeVirtualBeamOrStripDisplacementsToMetaFile(
            self, *args, **kwargs):
        return self._wrapped.SaveEnvelopeVirtualBeamOrStripDisplacementsToMetaFile(
            *args, **kwargs)

    def SaveCriticalVirtualBeamOrStripDisplacementsToMetaFile(
            self, *args, **kwargs):
        return self._wrapped.SaveCriticalVirtualBeamOrStripDisplacementsToMetaFile(
            *args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep


class AxisVMDomain(AxWrapper):

    @property
    def ContourLines(self) -> int:
        return self._wrapped.ContourLines

    @property
    def HoleCount(self) -> int:
        return self._wrapped.HoleCount

    @property
    def HoleLines(self) -> int:
        return self._wrapped.HoleLines

    @property
    def Weight(self) -> float:
        return self._wrapped.Weight

    @property
    def Volume(self) -> float:
        return self._wrapped.Volume

    @property
    def Area(self) -> float:
        return self._wrapped.Area

    @property
    def MeshExists(self) -> int:
        return self._wrapped.MeshExists

    @property
    def MeshSurfaceIds(self) -> int:
        return self._wrapped.MeshSurfaceIds

    def AddHole(self, *args, **kwargs):
        return self._wrapped.AddHole(*args, **kwargs)

    def Modify(self, *args, **kwargs):
        return self._wrapped.Modify(*args, **kwargs)

    def GenerateMesh(self, *args, **kwargs):
        return self._wrapped.GenerateMesh(*args, **kwargs)

    def GetSurfaceAttr(self, *args, **kwargs):
        return self._wrapped.GetSurfaceAttr(*args, **kwargs)

    def SetSurfaceAttr(self, *args, **kwargs):
        return self._wrapped.SetSurfaceAttr(*args, **kwargs)

    def GetNormalVector(self, *args, **kwargs):
        return self._wrapped.GetNormalVector(*args, **kwargs)

    def GetTrMatrix(self, *args, **kwargs):
        return self._wrapped.GetTrMatrix(*args, **kwargs)

    def GetMeshParameters(self, *args, **kwargs):
        return self._wrapped.GetMeshParameters(*args, **kwargs)

    def SetMeshParameters(self, *args, **kwargs):
        return self._wrapped.SetMeshParameters(*args, **kwargs)

    def SetContourLines(self, *args, **kwargs):
        return self._wrapped.SetContourLines(*args, **kwargs)

    def DeleteHole(self, *args, **kwargs):
        return self._wrapped.DeleteHole(*args, **kwargs)

    def GetMeshSurfacesCoordinates(self, *args, **kwargs):
        return self._wrapped.GetMeshSurfacesCoordinates(*args, **kwargs)

    @property
    def HoleArea(self) -> int:
        return self._wrapped.HoleArea

    @property
    def IsWall(self) -> int:
        return self._wrapped.IsWall

    @property
    def IsSlab(self) -> int:
        return self._wrapped.IsSlab

    @property
    def IsOtherType(self) -> int:
        return self._wrapped.IsOtherType

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @property
    def SeismicStoreyId(self) -> int:
        return self._wrapped.SeismicStoreyId

    @property
    def StoreyId(self) -> int:
        return self._wrapped.StoreyId

    def GetInnerDomainIds(self, *args, **kwargs):
        return self._wrapped.GetInnerDomainIds(*args, **kwargs)

    @property
    def OuterDomainId(self) -> int:
        return self._wrapped.OuterDomainId

    def GetReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.GetReinforcementParameters(*args, **kwargs)

    def SetReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.SetReinforcementParameters(*args, **kwargs)

    @property
    def ReinforcementParametersExists(self) -> int:
        return self._wrapped.ReinforcementParametersExists

    def DeleteReinforcementParameters(self, *args, **kwargs):
        return self._wrapped.DeleteReinforcementParameters(*args, **kwargs)

    def ModifyHole(self, *args, **kwargs):
        return self._wrapped.ModifyHole(*args, **kwargs)

    def SetElasticFoundation(self, *args, **kwargs):
        return self._wrapped.SetElasticFoundation(*args, **kwargs)

    def GetElasticFoundation(self, *args, **kwargs):
        return self._wrapped.GetElasticFoundation(*args, **kwargs)

    @property
    def ElasticFoundationExists(self) -> int:
        return self._wrapped.ElasticFoundationExists

    def DeleteElasticFoundation(self, *args, **kwargs):
        return self._wrapped.DeleteElasticFoundation(*args, **kwargs)

    @property
    def MaterialColour(self) -> c_ulong:
        return self._wrapped.MaterialColour

    @MaterialColour.setter
    def MaterialColour(self, Value: c_ulong):
        self._wrapped.MaterialColour = Value

    @property
    def ContourColour(self) -> c_ulong:
        return self._wrapped.ContourColour

    @ContourColour.setter
    def ContourColour(self, Value: c_ulong):
        self._wrapped.ContourColour = Value

    @property
    def ArchitectElemType(self) -> int:
        return self._wrapped.ArchitectElemType

    @ArchitectElemType.setter
    def ArchitectElemType(self, Value: int):
        self._wrapped.ArchitectElemType = Value

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    def AddHole_vb(self, *args, **kwargs):
        return self._wrapped.AddHole_vb(*args, **kwargs)

    def Modify_vb(self, *args, **kwargs):
        return self._wrapped.Modify_vb(*args, **kwargs)

    def SetContourLines_vb(self, *args, **kwargs):
        return self._wrapped.SetContourLines_vb(*args, **kwargs)

    def ModifyHole_vb(self, *args, **kwargs):
        return self._wrapped.ModifyHole_vb(*args, **kwargs)

    @property
    def MaterialColour_vb(self) -> int:
        return self._wrapped.MaterialColour_vb

    @MaterialColour_vb.setter
    def MaterialColour_vb(self, Value: int):
        self._wrapped.MaterialColour_vb = Value

    @property
    def ContourColour_vb(self) -> int:
        return self._wrapped.ContourColour_vb

    @ContourColour_vb.setter
    def ContourColour_vb(self, Value: int):
        self._wrapped.ContourColour_vb = Value

    @property
    def StiffnessReduction(self) -> float:
        return self._wrapped.StiffnessReduction

    @StiffnessReduction.setter
    def StiffnessReduction(self, Value: float):
        self._wrapped.StiffnessReduction = Value

    @property
    def ContourPolygon(self) -> 'AxisVMLines3d':
        return self._wrapped.ContourPolygon

    def SetReinforcementParameters_vb(self, *args, **kwargs):
        return self._wrapped.SetReinforcementParameters_vb(*args, **kwargs)

    @property
    def VariableThickness(self) -> int:
        return self._wrapped.VariableThickness

    def DeleteMesh(self, *args, **kwargs):
        return self._wrapped.DeleteMesh(*args, **kwargs)

    def GetSurfaceStiffnessFactors(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStiffnessFactors(*args, **kwargs)

    def SetSurfaceStiffnessFactors(self, *args, **kwargs):
        return self._wrapped.SetSurfaceStiffnessFactors(*args, **kwargs)

    def GetCustomStiffnessMatrix(self, *args, **kwargs):
        return self._wrapped.GetCustomStiffnessMatrix(*args, **kwargs)

    def SetCustomStiffnessMatrix(self, *args, **kwargs):
        return self._wrapped.SetCustomStiffnessMatrix(*args, **kwargs)

    @property
    def StiffnessReduction_V153(self) -> int:
        return self._wrapped.StiffnessReduction_V153

    @StiffnessReduction_V153.setter
    def StiffnessReduction_V153(self, Value: int):
        self._wrapped.StiffnessReduction_V153 = Value


class AxisVMReinforcementCheck(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetReinforcementChecksByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetReinforcementChecksByLoadCaseId(
            *args, **kwargs)

    def GetReinforcementChecksByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetReinforcementChecksByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeReinforcementChecks(*args, **kwargs)

    def GetCriticalReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.GetCriticalReinforcementChecks(*args, **kwargs)

    def GetAllReinforcementChecksByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllReinforcementChecksByLoadCaseId(
            *args, **kwargs)

    def GetAllReinforcementChecksByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllReinforcementChecksByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeReinforcementChecks(*args, **kwargs)

    def GetAllCriticalReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalReinforcementChecks(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    def ReinforcementChecksByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.ReinforcementChecksByLoadCaseId(*args, **kwargs)

    def ReinforcementChecksByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.ReinforcementChecksByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.EnvelopeReinforcementChecks(*args, **kwargs)

    def CriticalReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.CriticalReinforcementChecks(*args, **kwargs)

    def AllReinforcementChecksByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllReinforcementChecksByLoadCaseId(
            *args, **kwargs)

    def AllReinforcementChecksByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllReinforcementChecksByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeReinforcementChecks(*args, **kwargs)

    def AllCriticalReinforcementChecks(self, *args, **kwargs):
        return self._wrapped.AllCriticalReinforcementChecks(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value


class AxisVMLoadPanel(AxWrapper):

    @property
    def EdgeCount(self) -> int:
        return self._wrapped.EdgeCount

    @property
    def SelectedEdge(self) -> int:
        return self._wrapped.SelectedEdge

    @SelectedEdge.setter
    def SelectedEdge(self, Value: int):
        self._wrapped.SelectedEdge = Value

    def SetAllEdgeParameters(self, *args, **kwargs):
        return self._wrapped.SetAllEdgeParameters(*args, **kwargs)

    def SetEdgeParameters(self, *args, **kwargs):
        return self._wrapped.SetEdgeParameters(*args, **kwargs)

    def GetAllEdgeParameters(self, *args, **kwargs):
        return self._wrapped.GetAllEdgeParameters(*args, **kwargs)

    def GetEdgeParameters(self, *args, **kwargs):
        return self._wrapped.GetEdgeParameters(*args, **kwargs)

    def GetContourPolygon(self, *args, **kwargs):
        return self._wrapped.GetContourPolygon(*args, **kwargs)

    def GetContourLineIDs(self, *args, **kwargs):
        return self._wrapped.GetContourLineIDs(*args, **kwargs)

    @property
    def ContourType(self) -> int:
        return self._wrapped.ContourType

    def GetLines(self, *args, **kwargs):
        return self._wrapped.GetLines(*args, **kwargs)

    def SetLines(self, *args, **kwargs):
        return self._wrapped.SetLines(*args, **kwargs)

    def GetNodes(self, *args, **kwargs):
        return self._wrapped.GetNodes(*args, **kwargs)

    def SetNodes(self, *args, **kwargs):
        return self._wrapped.SetNodes(*args, **kwargs)

    @property
    def Auto(self) -> int:
        return self._wrapped.Auto

    @Auto.setter
    def Auto(self, Value: int):
        self._wrapped.Auto = Value

    def GetDomains(self, *args, **kwargs):
        return self._wrapped.GetDomains(*args, **kwargs)

    def SetDomains(self, *args, **kwargs):
        return self._wrapped.SetDomains(*args, **kwargs)


class AxisVMStresses(AxWrapper):

    def GetLineStressByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineStressByLoadCaseId(*args, **kwargs)

    def GetLineStressByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineStressByLoadCombinationId(*args, **kwargs)

    def GetEnvelopeLineStress(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineStress(*args, **kwargs)

    def GetCriticalLineStress(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineStress(*args, **kwargs)

    def GetLineStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetLineStressesByLoadCaseId(*args, **kwargs)

    def GetLineStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetLineStressesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeLineStresses(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineStresses(*args, **kwargs)

    def GetCriticalLineStresses(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineStresses(*args, **kwargs)

    def GetAllLineStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllLineStressesByLoadCaseId(*args, **kwargs)

    def GetAllLineStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllLineStressesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeLineStresses(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeLineStresses(*args, **kwargs)

    def GetAllCriticalLineStresses(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalLineStresses(*args, **kwargs)

    def GetLineStressesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetLineStressesForResultBlocks(*args, **kwargs)

    def GetSurfaceStressByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStressByLoadCaseId(*args, **kwargs)

    def GetSurfaceStressByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStressByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSurfaceStress(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceStress(*args, **kwargs)

    def GetCriticalSurfaceStress(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceStress(*args, **kwargs)

    def GetSurfaceStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStressesByLoadCaseId(*args, **kwargs)

    def GetSurfaceStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStressesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceStresses(*args, **kwargs)

    def GetCriticalSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceStresses(*args, **kwargs)

    def GetAllSurfaceStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllSurfaceStressesByLoadCaseId(*args, **kwargs)

    def GetAllSurfaceStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllSurfaceStressesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeSurfaceStresses(*args, **kwargs)

    def GetAllCriticalSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalSurfaceStresses(*args, **kwargs)

    def GetSurfaceStressesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStressesForResultBlocks(*args, **kwargs)

    def GetSurfaceStressValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetSurfaceStressValuesForResultBlocks(
            *args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevelOrTimeStep(self) -> int:
        return self._wrapped.LoadLevelOrTimeStep

    @LoadLevelOrTimeStep.setter
    def LoadLevelOrTimeStep(self, Value: int):
        self._wrapped.LoadLevelOrTimeStep = Value

    @property
    def LineStressComponent(self) -> int:
        return self._wrapped.LineStressComponent

    @LineStressComponent.setter
    def LineStressComponent(self, Value: int):
        self._wrapped.LineStressComponent = Value

    @property
    def SurfaceStressComponent(self) -> int:
        return self._wrapped.SurfaceStressComponent

    @SurfaceStressComponent.setter
    def SurfaceStressComponent(self, Value: int):
        self._wrapped.SurfaceStressComponent = Value

    def LineStressByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineStressByLoadCaseId(*args, **kwargs)

    def LineStressByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineStressByLoadCombinationId(*args, **kwargs)

    def EnvelopeLineStress(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineStress(*args, **kwargs)

    def CriticalLineStress(self, *args, **kwargs):
        return self._wrapped.CriticalLineStress(*args, **kwargs)

    def LineStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.LineStressesByLoadCaseId(*args, **kwargs)

    def LineStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.LineStressesByLoadCombinationId(*args, **kwargs)

    def EnvelopeLineStresses(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineStresses(*args, **kwargs)

    def CriticalLineStresses(self, *args, **kwargs):
        return self._wrapped.CriticalLineStresses(*args, **kwargs)

    def AllLineStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllLineStressesByLoadCaseId(*args, **kwargs)

    def AllLineStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllLineStressesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeLineStresses(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeLineStresses(*args, **kwargs)

    def AllCriticalLineStresses(self, *args, **kwargs):
        return self._wrapped.AllCriticalLineStresses(*args, **kwargs)

    def LineStressesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.LineStressesForResultBlocks(*args, **kwargs)

    def SurfaceStressByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SurfaceStressByLoadCaseId(*args, **kwargs)

    def SurfaceStressByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SurfaceStressByLoadCombinationId(*args, **kwargs)

    def EnvelopeSurfaceStress(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceStress(*args, **kwargs)

    def CriticalSurfaceStress(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceStress(*args, **kwargs)

    def SurfaceStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.SurfaceStressesByLoadCaseId(*args, **kwargs)

    def SurfaceStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.SurfaceStressesByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceStresses(*args, **kwargs)

    def CriticalSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceStresses(*args, **kwargs)

    def AllSurfaceStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllSurfaceStressesByLoadCaseId(*args, **kwargs)

    def AllSurfaceStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllSurfaceStressesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeSurfaceStresses(*args, **kwargs)

    def AllCriticalSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.AllCriticalSurfaceStresses(*args, **kwargs)

    def SurfaceStressesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SurfaceStressesForResultBlocks(*args, **kwargs)

    def SurfaceStressValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.SurfaceStressValuesForResultBlocks(
            *args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeLineStress2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeLineStress2(*args, **kwargs)

    def GetCriticalLineStress2(self, *args, **kwargs):
        return self._wrapped.GetCriticalLineStress2(*args, **kwargs)

    def GetEnvelopeSurfaceStress2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeSurfaceStress2(*args, **kwargs)

    def GetCriticalSurfaceStress2(self, *args, **kwargs):
        return self._wrapped.GetCriticalSurfaceStress2(*args, **kwargs)

    def EnvelopeLineStress2(self, *args, **kwargs):
        return self._wrapped.EnvelopeLineStress2(*args, **kwargs)

    def CriticalLineStress2(self, *args, **kwargs):
        return self._wrapped.CriticalLineStress2(*args, **kwargs)

    def EnvelopeSurfaceStress2(self, *args, **kwargs):
        return self._wrapped.EnvelopeSurfaceStress2(*args, **kwargs)

    def CriticalSurfaceStress2(self, *args, **kwargs):
        return self._wrapped.CriticalSurfaceStress2(*args, **kwargs)

    def GetMemberStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetMemberStressesByLoadCaseId(*args, **kwargs)

    def GetMemberStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetMemberStressesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeMemberStresses(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeMemberStresses(*args, **kwargs)

    def GetCriticalMemberStresses(self, *args, **kwargs):
        return self._wrapped.GetCriticalMemberStresses(*args, **kwargs)

    @property
    def XLAMSurfaceStressComponent(self) -> int:
        return self._wrapped.XLAMSurfaceStressComponent

    @XLAMSurfaceStressComponent.setter
    def XLAMSurfaceStressComponent(self, Value: int):
        self._wrapped.XLAMSurfaceStressComponent = Value

    def GetXLAMSurfaceStressByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceStressByLoadCaseId(*args, **kwargs)

    def GetXLAMSurfaceStressByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceStressByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeXLAMSurfaceStress(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeXLAMSurfaceStress(*args, **kwargs)

    def GetCriticalXLAMSurfaceStress(self, *args, **kwargs):
        return self._wrapped.GetCriticalXLAMSurfaceStress(*args, **kwargs)

    def GetXLAMSurfaceStressesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceStressesByLoadCaseId(
            *args, **kwargs)

    def GetXLAMSurfaceStressesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceStressesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeXLAMSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeXLAMSurfaceStresses(*args, **kwargs)

    def GetCriticalXLAMSurfaceStresses(self, *args, **kwargs):
        return self._wrapped.GetCriticalXLAMSurfaceStresses(*args, **kwargs)

    def GetXLAMSurfaceStressesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceStressesForResultBlocks(
            *args, **kwargs)

    def GetXLAMSurfaceStressValuesForResultBlocks(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceStressValuesForResultBlocks(
            *args, **kwargs)

    def GetXLAMSurfaceEfficiencyByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceEfficiencyByLoadCaseId(
            *args, **kwargs)

    def GetXLAMSurfaceEfficiencyByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceEfficiencyByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeXLAMSurfaceEfficiency(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeXLAMSurfaceEfficiency(*args, **kwargs)

    def GetCriticalXLAMSurfaceEfficiency(self, *args, **kwargs):
        return self._wrapped.GetCriticalXLAMSurfaceEfficiency(*args, **kwargs)

    def GetXLAMSurfaceEfficienciesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceEfficienciesByLoadCaseId(
            *args, **kwargs)

    def GetXLAMSurfaceEfficienciesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetXLAMSurfaceEfficienciesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeXLAMSurfaceEfficiencies(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeXLAMSurfaceEfficiencies(
            *args, **kwargs)

    def GetCriticalXLAMSurfaceEfficiencies(self, *args, **kwargs):
        return self._wrapped.GetCriticalXLAMSurfaceEfficiencies(
            *args, **kwargs)

    def SaveMemberStressesToMetaFileByLoadCaseID(self, *args, **kwargs):
        return self._wrapped.SaveMemberStressesToMetaFileByLoadCaseID(
            *args, **kwargs)

    def SaveMemberStressesToMetaFileByLoadCombinationID(self, *args, **kwargs):
        return self._wrapped.SaveMemberStressesToMetaFileByLoadCombinationID(
            *args, **kwargs)

    def SaveEnvelopeMemberStressesToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveEnvelopeMemberStressesToMetaFile(
            *args, **kwargs)

    def SaveCriticalMemberStressesToMetaFile(self, *args, **kwargs):
        return self._wrapped.SaveCriticalMemberStressesToMetaFile(
            *args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep


class AxisVMWindow(AxWrapper):

    def Duplicate(self, *args, **kwargs):
        return self._wrapped.Duplicate(*args, **kwargs)

    def Remove(self, *args, **kwargs):
        return self._wrapped.Remove(*args, **kwargs)

    def GetStaticDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetStaticDisplayParameters(*args, **kwargs)

    def GetBucklingDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetBucklingDisplayParameters(*args, **kwargs)

    def GetVibrationDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetVibrationDisplayParameters(*args, **kwargs)

    def GetDynamicDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetDynamicDisplayParameters(*args, **kwargs)

    def GetRCDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetRCDesignDisplayParameters(*args, **kwargs)

    def GetSteelDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignDisplayParameters(*args, **kwargs)

    def GetTimberDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignDisplayParameters(*args, **kwargs)

    def GetDisplayOptions(self, *args, **kwargs):
        return self._wrapped.GetDisplayOptions(*args, **kwargs)

    def SetStaticDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetStaticDisplayParameters(*args, **kwargs)

    def SetBucklingDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetBucklingDisplayParameters(*args, **kwargs)

    def SetVibrationDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetVibrationDisplayParameters(*args, **kwargs)

    def SetDynamicDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetDynamicDisplayParameters(*args, **kwargs)

    def SetRCDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetRCDesignDisplayParameters(*args, **kwargs)

    def SetSteelDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetSteelDesignDisplayParameters(*args, **kwargs)

    def SetTimberDesignDisplayParameters(self, *args, **kwargs):
        return self._wrapped.SetTimberDesignDisplayParameters(*args, **kwargs)

    def SetDisplayOptions(self, *args, **kwargs):
        return self._wrapped.SetDisplayOptions(*args, **kwargs)

    @property
    def Display(self) -> int:
        return self._wrapped.Display

    @Display.setter
    def Display(self, Value: int):
        self._wrapped.Display = Value

    def GetWindowDisplayPartUIDs(self, *args, **kwargs):
        return self._wrapped.GetWindowDisplayPartUIDs(*args, **kwargs)

    def SetWindowDisplayPartUIDs(self, *args, **kwargs):
        return self._wrapped.SetWindowDisplayPartUIDs(*args, **kwargs)

    def SaveWindowToBitmap(self, *args, **kwargs):
        return self._wrapped.SaveWindowToBitmap(*args, **kwargs)

    @property
    def Width(self) -> int:
        return self._wrapped.Width

    @property
    def Height(self) -> int:
        return self._wrapped.Height

    def GetPixelPosition(self, *args, **kwargs):
        return self._wrapped.GetPixelPosition(*args, **kwargs)

    def SaveWindowToClipboard(self, *args, **kwargs):
        return self._wrapped.SaveWindowToClipboard(*args, **kwargs)

    def SaveWindowToMetafile(self, *args, **kwargs):
        return self._wrapped.SaveWindowToMetafile(*args, **kwargs)

    @property
    def View(self) -> int:
        return self._wrapped.View

    @View.setter
    def View(self, Value: int):
        self._wrapped.View = Value

    @property
    def WorkPlaneIndex(self) -> int:
        return self._wrapped.WorkPlaneIndex

    @WorkPlaneIndex.setter
    def WorkPlaneIndex(self, Value: int):
        self._wrapped.WorkPlaneIndex = Value

    @property
    def StoryIndex(self) -> int:
        return self._wrapped.StoryIndex

    @StoryIndex.setter
    def StoryIndex(self, Value: int):
        self._wrapped.StoryIndex = Value

    @property
    def ActiveStoryIndex(self) -> int:
        return self._wrapped.ActiveStoryIndex

    @ActiveStoryIndex.setter
    def ActiveStoryIndex(self, Value: int):
        self._wrapped.ActiveStoryIndex = Value

    @property
    def ShowOnlySelected(self) -> int:
        return self._wrapped.ShowOnlySelected

    @ShowOnlySelected.setter
    def ShowOnlySelected(self, Value: int):
        self._wrapped.ShowOnlySelected = Value

    def GetVisibleLayerIDs(self, *args, **kwargs):
        return self._wrapped.GetVisibleLayerIDs(*args, **kwargs)

    def SetVisibleLayerIDs(self, *args, **kwargs):
        return self._wrapped.SetVisibleLayerIDs(*args, **kwargs)

    def GetDetectedLayerIDs(self, *args, **kwargs):
        return self._wrapped.GetDetectedLayerIDs(*args, **kwargs)

    def SetDetectedLayerIDs(self, *args, **kwargs):
        return self._wrapped.SetDetectedLayerIDs(*args, **kwargs)

    def GetLockedLayerIDs(self, *args, **kwargs):
        return self._wrapped.GetLockedLayerIDs(*args, **kwargs)

    def SetLockedLayerIDs(self, *args, **kwargs):
        return self._wrapped.SetLockedLayerIDs(*args, **kwargs)

    def GetVisibleStructuralGridIDs(self, *args, **kwargs):
        return self._wrapped.GetVisibleStructuralGridIDs(*args, **kwargs)

    def SetVisibleStructuralGridIDs(self, *args, **kwargs):
        return self._wrapped.SetVisibleStructuralGridIDs(*args, **kwargs)

    def GetWorldRectangle(self, *args, **kwargs):
        return self._wrapped.GetWorldRectangle(*args, **kwargs)

    def SetWorldRectangle(self, *args, **kwargs):
        return self._wrapped.SetWorldRectangle(*args, **kwargs)

    def ReDraw(self, *args, **kwargs):
        return self._wrapped.ReDraw(*args, **kwargs)

    def PanToCoord(self, *args, **kwargs):
        return self._wrapped.PanToCoord(*args, **kwargs)

    def GetStaticDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetStaticDisplayParameters_V153(*args, **kwargs)

    def GetBucklingDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetBucklingDisplayParameters_V153(*args, **kwargs)

    def GetVibrationDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetVibrationDisplayParameters_V153(
            *args, **kwargs)

    def GetDynamicDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetDynamicDisplayParameters_V153(*args, **kwargs)

    def GetRCDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetRCDesignDisplayParameters_V153(*args, **kwargs)

    def GetSteelDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetSteelDesignDisplayParameters_V153(
            *args, **kwargs)

    def GetTimberDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignDisplayParameters_V153(
            *args, **kwargs)

    def SetStaticDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetStaticDisplayParameters_V153(*args, **kwargs)

    def SetBucklingDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetBucklingDisplayParameters_V153(*args, **kwargs)

    def SetVibrationDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetVibrationDisplayParameters_V153(
            *args, **kwargs)

    def SetDynamicDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetDynamicDisplayParameters_V153(*args, **kwargs)

    def SetRCDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetRCDesignDisplayParameters_V153(*args, **kwargs)

    def SetSteelDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetSteelDesignDisplayParameters_V153(
            *args, **kwargs)

    def SetTimberDesignDisplayParameters_V153(self, *args, **kwargs):
        return self._wrapped.SetTimberDesignDisplayParameters_V153(
            *args, **kwargs)

    @property
    def Switch(self) -> int:
        return self._wrapped.Switch

    @Switch.setter
    def Switch(self, Value: int):
        self._wrapped.Switch = Value


class AxisVMAcceleration(AxWrapper):

    def GetNodalAccelerationByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetNodalAccelerationByLoadCaseId(*args, **kwargs)

    def GetEnvelopeNodalAcceleration(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeNodalAcceleration(*args, **kwargs)

    def GetAllNodalAccelerationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllNodalAccelerationsByLoadCaseId(
            *args, **kwargs)

    def GetAllEnvelopeNodalAccelerations(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeNodalAccelerations(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def TimeStep(self) -> int:
        return self._wrapped.TimeStep

    @TimeStep.setter
    def TimeStep(self, Value: int):
        self._wrapped.TimeStep = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def NodalAccelerationByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.NodalAccelerationByLoadCaseId(*args, **kwargs)

    def EnvelopeNodalAcceleration(self, *args, **kwargs):
        return self._wrapped.EnvelopeNodalAcceleration(*args, **kwargs)

    def AllNodalAccelerationsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllNodalAccelerationsByLoadCaseId(*args, **kwargs)

    def AllEnvelopeNodalAccelerations(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeNodalAccelerations(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value


class AxisVMDomainSupport(AxWrapper):

    @property
    def SupportType(self) -> int:
        return self._wrapped.SupportType

    def GetStiffnessesXYZ(self, *args, **kwargs):
        return self._wrapped.GetStiffnessesXYZ(*args, **kwargs)

    def SetStiffnessesXYZ(self, *args, **kwargs):
        return self._wrapped.SetStiffnessesXYZ(*args, **kwargs)

    def GetNonLinearityXYZ(self, *args, **kwargs):
        return self._wrapped.GetNonLinearityXYZ(*args, **kwargs)

    def SetNonLinearityXYZ(self, *args, **kwargs):
        return self._wrapped.SetNonLinearityXYZ(*args, **kwargs)

    def GetResistancesXYZ(self, *args, **kwargs):
        return self._wrapped.GetResistancesXYZ(*args, **kwargs)

    def SetResistancesXYZ(self, *args, **kwargs):
        return self._wrapped.SetResistancesXYZ(*args, **kwargs)

    @property
    def DomainId(self) -> int:
        return self._wrapped.DomainId

    def GetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.GetPasternakStiffness(*args, **kwargs)

    def SetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.SetPasternakStiffness(*args, **kwargs)


class AxisVMShearCapacity(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetShearCapacitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetShearCapacitiesByLoadCaseId(*args, **kwargs)

    def GetShearCapacitiesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetShearCapacitiesByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeShearCapacities(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeShearCapacities(*args, **kwargs)

    def GetCriticalShearCapacities(self, *args, **kwargs):
        return self._wrapped.GetCriticalShearCapacities(*args, **kwargs)

    def GetAllShearCapacitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllShearCapacitiesByLoadCaseId(*args, **kwargs)

    def GetAllShearCapacitiesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllShearCapacitiesByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeShearCapacities(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeShearCapacities(*args, **kwargs)

    def GetAllCriticalShearCapacities(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalShearCapacities(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def MinMaxType(self) -> int:
        return self._wrapped.MinMaxType

    @MinMaxType.setter
    def MinMaxType(self, Value: int):
        self._wrapped.MinMaxType = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    @property
    def Component(self) -> int:
        return self._wrapped.Component

    @Component.setter
    def Component(self, Value: int):
        self._wrapped.Component = Value

    def ShearCapacitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.ShearCapacitiesByLoadCaseId(*args, **kwargs)

    def ShearCapacitiesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.ShearCapacitiesByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeShearCapacities(self, *args, **kwargs):
        return self._wrapped.EnvelopeShearCapacities(*args, **kwargs)

    def CriticalShearCapacities(self, *args, **kwargs):
        return self._wrapped.CriticalShearCapacities(*args, **kwargs)

    def AllShearCapacitiesByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllShearCapacitiesByLoadCaseId(*args, **kwargs)

    def AllShearCapacitiesByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllShearCapacitiesByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeShearCapacities(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeShearCapacities(*args, **kwargs)

    def AllCriticalShearCapacities(self, *args, **kwargs):
        return self._wrapped.AllCriticalShearCapacities(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEnvelopeShearCapacities2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeShearCapacities2(*args, **kwargs)

    def GetCriticalShearCapacities2(self, *args, **kwargs):
        return self._wrapped.GetCriticalShearCapacities2(*args, **kwargs)

    def EnvelopeShearCapacities2(self, *args, **kwargs):
        return self._wrapped.EnvelopeShearCapacities2(*args, **kwargs)

    def CriticalShearCapacities2(self, *args, **kwargs):
        return self._wrapped.CriticalShearCapacities2(*args, **kwargs)

    def SetUserCreep(self, *args, **kwargs):
        return self._wrapped.SetUserCreep(*args, **kwargs)

    @property
    def UserCreep(self) -> int:
        return self._wrapped.UserCreep


class AxisVMTimberDesignResults(AxWrapper):

    @property
    def Count(self) -> int:
        return self._wrapped.Count

    def GetTimberDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignResultsByLoadCaseId(
            *args, **kwargs)

    def GetTimberDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeTimberDesignResults(*args, **kwargs)

    def GetCriticalTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.GetCriticalTimberDesignResults(*args, **kwargs)

    def GetAllTimberDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetAllTimberDesignResultsByLoadCaseId(
            *args, **kwargs)

    def GetAllTimberDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetAllTimberDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def GetAllEnvelopeTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.GetAllEnvelopeTimberDesignResults(*args, **kwargs)

    def GetAllCriticalTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.GetAllCriticalTimberDesignResults(*args, **kwargs)

    @property
    def AnalysisType(self) -> int:
        return self._wrapped.AnalysisType

    @AnalysisType.setter
    def AnalysisType(self, Value: int):
        self._wrapped.AnalysisType = Value

    @property
    def LoadCaseId(self) -> int:
        return self._wrapped.LoadCaseId

    @LoadCaseId.setter
    def LoadCaseId(self, Value: int):
        self._wrapped.LoadCaseId = Value

    @property
    def LoadCombinationId(self) -> int:
        return self._wrapped.LoadCombinationId

    @LoadCombinationId.setter
    def LoadCombinationId(self, Value: int):
        self._wrapped.LoadCombinationId = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def LoadLevel(self) -> int:
        return self._wrapped.LoadLevel

    @LoadLevel.setter
    def LoadLevel(self, Value: int):
        self._wrapped.LoadLevel = Value

    def TimberDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.TimberDesignResultsByLoadCaseId(*args, **kwargs)

    def TimberDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.TimberDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def EnvelopeTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.EnvelopeTimberDesignResults(*args, **kwargs)

    def CriticalTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.CriticalTimberDesignResults(*args, **kwargs)

    def AllTimberDesignResultsByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.AllTimberDesignResultsByLoadCaseId(
            *args, **kwargs)

    def AllTimberDesignResultsByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.AllTimberDesignResultsByLoadCombinationId(
            *args, **kwargs)

    def AllEnvelopeTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.AllEnvelopeTimberDesignResults(*args, **kwargs)

    def AllCriticalTimberDesignResults(self, *args, **kwargs):
        return self._wrapped.AllCriticalTimberDesignResults(*args, **kwargs)

    def GetEfficiencyAndCombination(self, *args, **kwargs):
        return self._wrapped.GetEfficiencyAndCombination(*args, **kwargs)

    @property
    def EnvelopeUID(self) -> int:
        return self._wrapped.EnvelopeUID

    @EnvelopeUID.setter
    def EnvelopeUID(self, Value: int):
        self._wrapped.EnvelopeUID = Value

    def GetEfficiencyAndCombinationByLoadCaseId(self, *args, **kwargs):
        return self._wrapped.GetEfficiencyAndCombinationByLoadCaseId(
            *args, **kwargs)

    def GetEfficiencyAndCombinationByLoadCombinationId(self, *args, **kwargs):
        return self._wrapped.GetEfficiencyAndCombinationByLoadCombinationId(
            *args, **kwargs)

    def GetEnvelopeEfficiencyAndCombination(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeEfficiencyAndCombination(
            *args, **kwargs)

    def GetCriticalEfficiencyAndCombination(self, *args, **kwargs):
        return self._wrapped.GetCriticalEfficiencyAndCombination(
            *args, **kwargs)

    def GetEnvelopeTimberDesignResults2(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeTimberDesignResults2(*args, **kwargs)

    def GetTimberDesignResultsByLoadCaseId_Abs(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignResultsByLoadCaseId_Abs(
            *args, **kwargs)

    def GetTimberDesignResultsByLoadCombinationId_Abs(self, *args, **kwargs):
        return self._wrapped.GetTimberDesignResultsByLoadCombinationId_Abs(
            *args, **kwargs)

    def GetEnvelopeTimberDesignResults_Abs(self, *args, **kwargs):
        return self._wrapped.GetEnvelopeTimberDesignResults_Abs(
            *args, **kwargs)

    def GetCriticalTimberDesignResults_Abs(self, *args, **kwargs):
        return self._wrapped.GetCriticalTimberDesignResults_Abs(
            *args, **kwargs)


class AxisVMStrains(AxWrapper):

    ...


class AxisVMCustomPartFolder(AxWrapper):

    @property
    def Path(self) -> str:
        return self._wrapped.Path

    @property
    def PartCount(self) -> int:
        return self._wrapped.PartCount

    @property
    def PartId(self) -> int:
        return self._wrapped.PartId

    @property
    def PartUID(self) -> int:
        return self._wrapped.PartUID

    @property
    def SubFolderCount(self) -> int:
        return self._wrapped.SubFolderCount

    @property
    def SubFolder(self) -> int:
        return self._wrapped.SubFolder

    @property
    def ParentFolder(self) -> 'AxisVMCustomPartFolder':
        return self._wrapped.ParentFolder

    @property
    def IsRootFolder(self) -> int:
        return self._wrapped.IsRootFolder

    def AddPartFromSelectedItems(self, *args, **kwargs):
        return self._wrapped.AddPartFromSelectedItems(*args, **kwargs)

    def AddPart(self, *args, **kwargs):
        return self._wrapped.AddPart(*args, **kwargs)

    def DeletePart(self, *args, **kwargs):
        return self._wrapped.DeletePart(*args, **kwargs)

    def AddSubFolder(self, *args, **kwargs):
        return self._wrapped.AddSubFolder(*args, **kwargs)

    def DeleteSubFolder(self, *args, **kwargs):
        return self._wrapped.DeleteSubFolder(*args, **kwargs)

    def RenamePart(self, *args, **kwargs):
        return self._wrapped.RenamePart(*args, **kwargs)

    def RenameSubFolder(self, *args, **kwargs):
        return self._wrapped.RenameSubFolder(*args, **kwargs)

    def GetPart(self, *args, **kwargs):
        return self._wrapped.GetPart(*args, **kwargs)

    def ModifyPartFromSelectedItems(self, *args, **kwargs):
        return self._wrapped.ModifyPartFromSelectedItems(*args, **kwargs)

    def ModifyPart(self, *args, **kwargs):
        return self._wrapped.ModifyPart(*args, **kwargs)

    def SelectPartItems(self, *args, **kwargs):
        return self._wrapped.SelectPartItems(*args, **kwargs)

    def AddPartItemsFromSelectedItemsToPart(self, *args, **kwargs):
        return self._wrapped.AddPartItemsFromSelectedItemsToPart(
            *args, **kwargs)

    def AddPartItemsToPart(self, *args, **kwargs):
        return self._wrapped.AddPartItemsToPart(*args, **kwargs)

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: str):
        self._wrapped.Name = Value


class AxisVMLoadGroup(AxWrapper):

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: str):
        self._wrapped.Name = Value

    @property
    def LoadGroupType(self) -> int:
        return self._wrapped.LoadGroupType

    @LoadGroupType.setter
    def LoadGroupType(self, Value: int):
        self._wrapped.LoadGroupType = Value

    @property
    def SimultExc(self) -> int:
        return self._wrapped.SimultExc

    @SimultExc.setter
    def SimultExc(self, Value: int):
        self._wrapped.SimultExc = Value

    @property
    def CombinationType(self) -> int:
        return self._wrapped.CombinationType

    @CombinationType.setter
    def CombinationType(self, Value: int):
        self._wrapped.CombinationType = Value

    @property
    def gammaI(self) -> float:
        return self._wrapped.gammaI

    @gammaI.setter
    def gammaI(self, Value: float):
        self._wrapped.gammaI = Value

    @property
    def GammaSup(self) -> float:
        return self._wrapped.GammaSup

    @GammaSup.setter
    def GammaSup(self, Value: float):
        self._wrapped.GammaSup = Value

    @property
    def GammaInf(self) -> float:
        return self._wrapped.GammaInf

    @GammaInf.setter
    def GammaInf(self, Value: float):
        self._wrapped.GammaInf = Value

    @property
    def Psi0(self) -> float:
        return self._wrapped.Psi0

    @Psi0.setter
    def Psi0(self, Value: float):
        self._wrapped.Psi0 = Value

    @property
    def Psi1(self) -> float:
        return self._wrapped.Psi1

    @Psi1.setter
    def Psi1(self, Value: float):
        self._wrapped.Psi1 = Value

    @property
    def Psi2(self) -> float:
        return self._wrapped.Psi2

    @Psi2.setter
    def Psi2(self, Value: float):
        self._wrapped.Psi2 = Value

    @property
    def SfactUp(self) -> float:
        return self._wrapped.SfactUp

    @SfactUp.setter
    def SfactUp(self, Value: float):
        self._wrapped.SfactUp = Value

    @property
    def SfactInf(self) -> float:
        return self._wrapped.SfactInf

    @SfactInf.setter
    def SfactInf(self, Value: float):
        self._wrapped.SfactInf = Value

    @property
    def SimFact(self) -> float:
        return self._wrapped.SimFact

    @SimFact.setter
    def SimFact(self, Value: float):
        self._wrapped.SimFact = Value

    @property
    def DynFact(self) -> float:
        return self._wrapped.DynFact

    @DynFact.setter
    def DynFact(self, Value: float):
        self._wrapped.DynFact = Value

    @property
    def psi(self) -> float:
        return self._wrapped.psi

    @psi.setter
    def psi(self, Value: float):
        self._wrapped.psi = Value

    @property
    def PsiT(self) -> float:
        return self._wrapped.PsiT

    @PsiT.setter
    def PsiT(self, Value: float):
        self._wrapped.PsiT = Value

    @property
    def GammaFsw(self) -> float:
        return self._wrapped.GammaFsw

    @GammaFsw.setter
    def GammaFsw(self, Value: float):
        self._wrapped.GammaFsw = Value

    @property
    def PermLoadRatio(self) -> float:
        return self._wrapped.PermLoadRatio

    @PermLoadRatio.setter
    def PermLoadRatio(self, Value: float):
        self._wrapped.PermLoadRatio = Value

    @property
    def Ksi(self) -> float:
        return self._wrapped.Ksi

    @Ksi.setter
    def Ksi(self, Value: float):
        self._wrapped.Ksi = Value

    @property
    def SeismicGroupID(self) -> int:
        return self._wrapped.SeismicGroupID


class AxisVMStructuralGrid(AxWrapper):

    @property
    def LinesCount(self) -> int:
        return self._wrapped.LinesCount

    @property
    def UID(self) -> int:
        return self._wrapped.UID

    @property
    def Plane(self) -> int:
        return self._wrapped.Plane

    @property
    def TrMatrix(self) -> 'RMatrix3x3':
        return self._wrapped.TrMatrix

    @property
    def NormalVector(self) -> 'RPoint3d':
        return self._wrapped.NormalVector

    def AddLine(self, *args, **kwargs):
        return self._wrapped.AddLine(*args, **kwargs)

    def GetLine(self, *args, **kwargs):
        return self._wrapped.GetLine(*args, **kwargs)

    def SetLine(self, *args, **kwargs):
        return self._wrapped.SetLine(*args, **kwargs)

    def DeleteLine(self, *args, **kwargs):
        return self._wrapped.DeleteLine(*args, **kwargs)

    @property
    def Name(self) -> str:
        return self._wrapped.Name

    @Name.setter
    def Name(self, Value: str):
        self._wrapped.Name = Value

    @property
    def SpacingDirection(self) -> int:
        return self._wrapped.SpacingDirection


class AxisVMSurfaceSupport(AxWrapper):

    @property
    def SupportType(self) -> int:
        return self._wrapped.SupportType

    def GetStiffnessesXYZ(self, *args, **kwargs):
        return self._wrapped.GetStiffnessesXYZ(*args, **kwargs)

    def SetStiffnessesXYZ(self, *args, **kwargs):
        return self._wrapped.SetStiffnessesXYZ(*args, **kwargs)

    def GetNonLinearityXYZ(self, *args, **kwargs):
        return self._wrapped.GetNonLinearityXYZ(*args, **kwargs)

    def SetNonLinearityXYZ(self, *args, **kwargs):
        return self._wrapped.SetNonLinearityXYZ(*args, **kwargs)

    def GetResistancesXYZ(self, *args, **kwargs):
        return self._wrapped.GetResistancesXYZ(*args, **kwargs)

    def SetResistancesXYZ(self, *args, **kwargs):
        return self._wrapped.SetResistancesXYZ(*args, **kwargs)

    @property
    def SurfaceId(self) -> int:
        return self._wrapped.SurfaceId

    def GetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.GetPasternakStiffness(*args, **kwargs)

    def SetPasternakStiffness(self, *args, **kwargs):
        return self._wrapped.SetPasternakStiffness(*args, **kwargs)
