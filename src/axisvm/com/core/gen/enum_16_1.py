# -*- coding: utf-8 -*-
from enum import Enum


class ECrossSectionProcess(Enum):
    cspOther = 0
    cspRolled = 1
    cspWelded = 2
    cspColdFormed = 3


class EMcrMethod(Enum):
    mcrmAuto = 0
    mcrmC1Lopez = 1
    mcrmC1C2C3User = 2
    mcrmDutch = 3
    mcrmDutchUser = 4
    mcrmAutoLS = 5
    mcrmUser = 6


class ENationalDesignCode(Enum):
    ndcOther = 0
    ndcHungarian_MSZ = 1
    ndcEuroCode = 2
    ndcRomanian_STAS = 4
    ndcDutch_NEN = 5
    ndcGerman_DIN1045_1 = 6
    ndcSwiss_SIA26x = 7
    ndcEuroCode_GER = 8
    ndcItalian = 9
    ndcEuroCode_Austrian = 10
    ndcEuroCode_UK = 11
    ndcEuroCode_NL = 12
    ndcEuroCode_FIN = 13
    ndcEuroCode_RO = 14
    ndcEuroCode_HU = 15
    ndcEuroCode_CZ = 16
    ndcEuroCode_B = 17
    ndcEuroCode_PL = 18
    ndcEuroCode_DK = 19
    ndcEuroCode_S = 20
    ndcUS = 21
    ndcCA_NBCC = 22
    ndcCA_Ontario = 23
    ndcCA_Bridge = 24
    ndcEuroCode_SK = 25
    ndcEuroCode_LV = 26
    ndcEuroCode_NO = 27
    ndcEuroCode_GR = 28


class EReleaseType(Enum):
    rtRigid = 0
    rtHinged = 1
    rtSemiRigid = 2
    rtPlastic = 3
    rtPushover = 4


class ETimberType(Enum):
    ttHardwood = 0
    ttGLULAM = 1
    ttLVL = 2
    ttSoftWood = 3
    ttOther = 4


class EWorkplanesError(Enum):
    wpeInvalidName = -100001
    wpeNameAlreadyExists = -100002
    wpeInvalidWorkPlaneParameters = -100003
    wpeWorkplaneIsNotGlobal = -100004
    wpeWorkplaneIsNotSmart = -100005
    wpeWorkplaneIsNotGeneral = -100006


class ECrossSectionDoubleUType(Enum):
    duOpened = 0
    duClosed = 1


class ELongBoolean(Enum):
    lbFalse = 0
    lbTrue = 1


class ELineType(Enum):
    ltTruss = 0
    ltBeam = 1
    ltRib = 2
    ltSpring = 3
    ltGap = 4
    ltEdge = 5
    ltHole = 6
    ltSimpleLine = 7
    ltNNLink = 8
    ltLLLink = 9


class EAutoExcentricityType(Enum):
    aetCustom = 0
    aetTop = 1
    aetMid = 2
    aetBottom = 3


class ELineNonLinearity(Enum):
    lnlTensionAndCompression = 0
    lnlTensionOnly = 1
    lnlCompressionOnly = 2


class EGapType(Enum):
    agtActiveInTension = 0
    agtActiveInCompression = 1


class ESpringDirection(Enum):
    sdGlobal = 0
    sdGeometry = 1
    sdPointReference = 2
    sdVectorReference = 3
    sdElementRelative = 4
    sdNodeRelative = 5
    sdSeismicIsolator = 6


class ELineStiffnessReduction(Enum):
    lsr_AX = 0
    lsr_AY = 1
    lsr_AZ = 2
    lsr_IX = 3
    lsr_IY = 4
    lsr_IZ = 5


class EMemberLocXOrientation(Enum):
    mlxo_ij = 1
    mlxo_ji = 2


class ELEEccType(Enum):
    leet_None = 0
    leet_CustomOffset = 1
    leet_AlignementPoint = 2
    leet_Group = 3
    leet_Ref = 4
    leet_RibDomain = 5


class ELEEccAlignementPoint(Enum):
    leeap_TopLeft = 1
    leeap_TopCenter = 2
    leeap_TopRight = 3
    leeap_CenterLeft = 4
    leeap_CenterCenter = 5
    leeap_CenterRight = 6
    leeap_BottomLeft = 7
    leeap_BottomCenter = 8
    leeap_BottomRight = 9


class EReleasePosType(Enum):
    rptAuto = 0
    rptRatio = 1
    rptLength = 2


class ECrossSectionError(Enum):
    cseNotAllowedProcessForShape = -100001
    cseNotAllowedProcessForParameters = -100002
    cseNonPositive_b = -100003
    cseNonPositive_h = -100004
    cseNonPositive_tw = -100005
    cseNonPositive_tf = -100006
    cseNonPositive_d = -100007
    cseNonPositive_v = -100008
    cseNonPositive_b1 = -100009
    cseNonPositive_h1 = -100010
    cseNonPositive_b2 = -100011
    cseNonPositive_h2 = -100012
    cseNonPositive_tw1 = -100013
    cseNonPositive_tf1 = -100014
    cseNonPositive_tw2 = -100015
    cseNonPositive_tf2 = -100016
    cseNonPositive_R = -100017
    cseNegative_r1 = -100018
    cseNegative_r2 = -100019
    cseNegative_r3 = -100020
    cseNegative_e = -100021
    cseNegative_a = -100022
    cseTooHigh_h = -100023
    cseTooHigh_tw = -100024
    cseTooHigh_tf = -100025
    cseTooHigh_r1 = -100026
    cseTooHigh_r2 = -100027
    cseTooHigh_r3 = -100028
    cseTooHigh_v = -100029
    cseTooLow_e = -100030
    cseTooHigh_tw1 = -100031
    cseTooHigh_tf1 = -100032
    cseTooHigh_tw2 = -100033
    cseTooHigh_tf2 = -100034
    cseTooLow_h = -100035
    cseTooLow_r1 = -100036
    cseTooLow_N = -100037
    cseDifferentThicknesses = -100038
    cseDifferentWidthAndHeight = -100039
    cseIncompatibleWidthAndHegiht = -100040
    cseNonPositiveAx = -100041
    cseNegativeAy = -100042
    cseAyIsHigherThanAx = -100043
    cseNegativeAz = -100044
    cseAzIsHigherThanAx = -100045
    cseNonPositiveIx = -100046
    cseNonPositiveIy = -100047
    cseNonPositiveIz = -100048
    cseNonPositiveHy = -100049
    cseNonPositiveHz = -100050
    cseNegativeIw = -100051
    cseNegativeW1t = -100052
    cseNegativeW1b = -100053
    cseNegativeW2t = -100054
    cseNegativeW2b = -100055
    cseNegativeW1pl = -100056
    cseNegativeW2pl = -100057
    cseEmptyName = -100058
    cseNameAlreadyExists = -100059
    cseExtParams = -100060
    cseErrorAdding = -100061
    cseErrorEditing = -100062
    cseInvalidCrossSectionType = -100063
    cseDifferentCrossSectionShape = -100064
    cseException = -101000
    cseTooHigh_e = -100065
    cseTooLargeInnerCrossSection = -100066
    cseInvalidMaterials = -100067
    cseNonPositive_b3 = -100068
    cseNonPositive_h3 = -100069
    cseNonPositive_tw3 = -100070
    cseNonPositive_tf3 = -100071
    cseTooHigh_tw3 = -100072
    cseTooHigh_tf3 = -100073
    cseTooLow_b = -100074
    cseNonPositive_c = -100075
    cseTooLow_c = -100076
    cseTooHigh_h2 = -100077
    cseTooLow_b2 = -100078


class ESystem(Enum):
    sysGlobal = 0
    sysLocal = 1
    sysReference = 2


class ETerrainCategory(Enum):
    tc0 = 0
    tcI = 1
    tcII = 2
    tcIII = 3
    tcIV = 4


class EWindStructureRoofType(Enum):
    wsrtUndefined = 0
    wsrtFlat = 1
    wsrtMonopitch = 2
    wsrtDuopitch = 3
    wsrtHip = 4
    wsrtBarrel = 5
    wsrtMonopitchCanopy = 6
    wsrtDuopitchCanopy = 7
    wsrtFreestandingWall = 8
    wsrtSignBoard = 9


class ERoofInternalPressure(Enum):
    ripUndefined = 0
    ripAuto = 1
    ripOpeningAreaBased = 2
    ripInternalCoeff = 3
    ripOff = 4


class ERoofFrictionEffect(Enum):
    rfeSmooth = 1
    rfeRough = 2
    rfeVeryRough = 3
    rfeCustom = 4


class ERoofMultiSpanPos(Enum):
    rmspFirst = 1
    rmspSecond = 2
    rmspInner = 3


class ERoofMultiSpanDir(Enum):
    rmsdX = 1
    rmsdY = 2


class EFlatRoofEdgeType(Enum):
    retNone = 0
    retSharpEaves = 1
    retWithParapetWall = 2
    retRoundEaves = 3
    retMansardEaves = 4


class EWorkplaneType(Enum):
    wptGlobal = 0
    wptSmart = 1
    wptGeneral = 2


class EDesignApproach(Enum):
    daClass = 0
    daElastic = 1


class EMessageDialogType(Enum):
    mdtWarning = 0
    mdtError = 1
    mdtInformation = 2
    mdtConfirmation = 3
    mdtCustom = 4
    mdtErrorConfirmation = 5


class EMessageDialogButton(Enum):
    mdbNone = 0
    mdbHelp = 1
    mdbCancel = 2
    mdbOK = 4
    mdbNo = 8
    mdbYes = 16
    mdbAbort = 32
    mdbIgnore = 64
    mdbRetry = 128
    mdbAll = 256
    mdbNoToAll = 512
    mdbYesToAll = 1024
    mdbClose = 2048


class EArchitectElemType(Enum):
    aetAuto = 0
    aetColumn = 1
    aetBeam = 2
    aetWall = 3
    aetSlab = 4


class ESurfaceStiffnessReduction(Enum):
    ssr_AC = 0
    ssr_ACS = 1
    ssr_IC = 2


class ERunningMode(Enum):
    rmOneWay = 0
    rmRoundTrip = 1


class ESwayDirection(Enum):
    sdPlusX = 0
    sdMinX = 1
    sdPlusY = 2
    sdMinY = 3
    sdCustom = 4


class EEdgeConnectionForce(Enum):
    ecfNx = 0
    ecfVy = 1
    ecfVz = 2
    ecfTx = 3
    ecfMy = 4
    ecfMz = 5


class EGlobalWorkplaneType(Enum):
    gwptXY = 0
    gwptXZ = 1
    gwptYZ = 2


class EStructureMode(Enum):
    smCrainrunway = 0
    smBridge = 1


class ESmartWorkplaneElementType(Enum):
    swetMember = 0
    swetSurface = 1
    swetDomain = 2


class EMovingLoadError(Enum):
    mleInvalidItemType = -100001
    mleInvalidSystemValue = -100002
    mleInvalidMovingLoadType = -100003
    mleInvalidPathOrNodes = -100004
    mleInvalidNValue = -100005
    mleInvalidNormVLength = -100006
    mleInvalidPathOrNormV = -100007
    mleInvalidLoadCase = -100008
    mleInvalidLoadGroup = -100009
    mleInvalidMovingLoad = -100010


class EBaseHeightType(Enum):
    bhtLowest = 0
    bhtCustom = 1


class EAnalysisType(Enum):
    atLinearStatic = 0
    atNonLinearStatic = 1
    atLinearVibration = 2
    atNonLinearVibration = 3
    atBuckling = 4
    atDynamic = 5


class ELinkElementForce(Enum):
    lefNx = 0
    lefVy = 1
    lefVz = 2
    lefTx = 3
    lefMy = 4
    lefMz = 5


class EMinMaxType(Enum):
    mtMin = 0
    mtMax = 1
    mtMinMax = 2


class EVelocity(Enum):
    veX = 0
    veY = 1
    veZ = 2
    veXX = 3
    veYY = 4
    veZZ = 5
    veR = 6
    veRR = 7


class EExpClass_EC(Enum):
    ecX0 = 0
    ecXC1 = 1
    ecXC2 = 2
    ecXC3 = 3
    ecXC4 = 4
    ecXD1 = 5
    ecXD2 = 6
    ecXD3 = 7
    ecXS1 = 8
    ecXS2 = 9
    ecXS3 = 10
    ecXF1 = 11
    ecXF2 = 12
    ecXF3 = 13
    ecXF4 = 14
    ecXD2b = 15


class EReinforcementCheckStatus(Enum):
    scsNotAvailable = 0
    scsOK = 1
    scsFail = 2


class ESpringParType(Enum):
    sptNodal = 0
    sptIsolator = 1
    sptConstraint = 2


class ESpringParNNType(Enum):
    spnntLinear = 0
    spnntNonLinearElastic = 1
    spnntNonLinearPlastic = 2


class ESpringParDOFType(Enum):
    spdoftTranslation = 0
    spdoftRotation = 1
    spdoftWarping = 2


class ESpringParDampingType(Enum):
    spdtKelvin = 0
    spdtMaxwell = 1


class ESpringParNonLinearity(Enum):
    spnlTensionAndCompression = 0
    spnlTensionOnly = 1
    spnlCompressionOnly = 2


class ESpringParNLDefType(Enum):
    spnldtByParam = 0
    spnldtByFunction = 1


class ESpringParHardeningRule(Enum):
    sphrIsotropic = 0
    sphrKinematic = 1


class ESpringParMatrixType(Enum):
    spmtTangentMatrix = 0
    spmtInitialMatrix = 1


class ESpringParIsolatorType(Enum):
    spitRubber = 0
    spitSlider = 1
    spitCustom = 2


class EIFCDomainReinforcementLinkType(Enum):
    idrltUbar = 0
    idrltOverlap = 1
    idrltLbar = 2
    idrltNone = 3


class EIFCQuestionableDomainLink(Enum):
    iqdlNone = 0
    iqdlReinforce = 1


class EIFCDomainOverlap(Enum):
    idoSeparately = 0
    idoAnchored = 1
    idoOverRun = 2


class EShearCapacity(Enum):
    scVRdc = 0
    scVEdMinusVRdc = 1
    scVRdmax = 2
    scVEdDivVRdmax = 3
    scaVEd = 4


class ECombinationType(Enum):
    ctOther = 0
    ctSLS1 = 1
    ctSLSChar = 1
    ctSLS2 = 2
    ctSLSFreq = 2
    ctSLS3 = 3
    ctSLSQuasi = 3
    ctULS1 = 4
    ctULS = 4
    ctULS2 = 5
    ctULSSeismic = 5
    ctULS3 = 6
    ctULSExceptional = 6
    ctULSALL = 7
    ctULSab = 8
    ctULSa = 9
    ctULSb = 10
    ctULSALLab = 11
    ctULSA1 = 12
    ctULSA2 = 13
    ctULSA3 = 14
    ctULSA4 = 15
    ctULSA5 = 16
    ctULSA6 = 17
    ctULSA7 = 18
    ctULSA8 = 19
    ctULSAllSE1 = 20
    ctULSAllSE2 = 21
    ctULSAllSE3 = 22
    ctULSAllSE4 = 23
    ctULSAllSE5 = 24
    ctULSAllSE6 = 25
    ctULSAllSE7 = 26
    ctULSAllSE8 = 27
    ctSemiAutoSLS1 = 28
    ctSemiAutoSLS2 = 29
    ctSemiAutoSLS3 = 30
    ctAuto = 31


class EStructuralGridPlane(Enum):
    sgp_XY = 0
    sgp_XZ = 1
    sgp_YZ = 2
    sgp_WorkPlane = 3
    sgp_Story = 4


class EGridLineSpacingDirection(Enum):
    glsd_X = 0
    glsd_Y = 1
    glsd_Other = 2


class ELineSupportType(Enum):
    lstEdgeGlobal = 0
    lstEdgeRelative = 1
    lstBeamElasticFoundation = 2
    lstRibElasticFoundation = 3
    lstEdgeReference = 4


class ESettingsError(Enum):
    seteInvalidGravityDirection = -100001
    seteInvalidGravityAcceleration = -100002


class EView(Enum):
    vFront = 0
    vTop = 1
    vSide = 2
    vPerspective = 3


class EDisplay(Enum):
    dWireframe = 0
    dHidden = 1
    dRendered = 2
    dTextured = 3
    dSolidResult = 4


class EIFCVersion(Enum):
    ifc20 = 0
    ifc2x = 1
    ifc2x2 = 2
    ifc2x3 = 3


class EDXFVersion(Enum):
    dxfR12 = 0
    dxfR2000 = 1


class ELengthUnit(Enum):
    lu_mm = 0
    lu_cm = 1
    lu_dm = 2
    lu_m = 3
    lu_inch = 4
    lu_foot = 5
    lu_yard = 6


class EXYDirection(Enum):
    xyd_x = 1
    xyd_y = 2


class EHollowHoleType(Enum):
    hht_Circular = 1
    hht_Rectangular = 2


class ESectionType(Enum):
    stPlane = 0
    stSegment = 1


class EFileImportPlane(Enum):
    fipPlaneXY = 0
    fipPlaneXZ = 1
    fipPlaneYZ = 2
    fipWorkPlane = 3


class EFileImportAs(Enum):
    fiaActualNodes = 0
    fiaBackgroundLayer = 1


class EFileImportMode(Enum):
    fimOverwrite = 0
    fimAdd = 1


class EAxis(Enum):
    aX = 0
    aY = 1
    aZ = 2
    aXX = 3
    aYY = 4
    aZZ = 5


class EIFCimportMethod(Enum):
    iimStaticModel = 0
    iimArchitecturalModelObjects = 1


class EIFCopeningsAlignedToDomainEdge(Enum):
    ioatdeImportAsOpenings = 0
    ioatdeAdjustTheDomain = 1


class EAttributesError(Enum):
    atteCannotAddAttribute = -100001
    atteCannotGetAttribute = -100002
    atteInvalidName = -100003
    atteInvalidOrEmptyItemData = -100004
    atteAttributeNotFound = -100005
    atteNameAlreadyExists = -100006
    atteCannotDeleteAttribute = -100007
    atteCannotSetAttribute = -100008
    atteInvalidOrEmptyItemIndexes = -100009
    atteItemIndexOutOfBounds = -100010
    atteAttributeSizeMustMatch = -100011
    atteItemsDataMustContainAllItems = -100012


class EMovingLoadType(Enum):
    mltMovingLoadOnBeam = 0
    mltMovingLoadOnDomain = 1


class ESectionDisplayMode(Enum):
    sdmDiagramOnly = 0
    sdmDiagramAvg = 1
    sdmDiagramRes = 2
    sdmResultant = 3
    sdmDiagramSegWidth = 4


class EMaterialType(Enum):
    mtOther = 0
    mtSteel = 1
    mtConcrete = 2
    mtTimber = 3
    mtAluminium = 4
    mtBrick = 5


class ETimberDesignResultsError(Enum):
    tdreCOMError = -100001
    tdreLoadCaseIdIndexOutOfBounds = -100002
    tdreLoadCombinationIdIndexOutOfBounds = -100003
    tdreInvalidAnalysisType = -100004
    tdreCombinationTypeNotValidForCurrentNationalDesignCode = -100005


class ELineError(Enum):
    lneNodeIndexOutOfBounds = -100001
    lneReferenceIndexOutOfBounds = -100002
    lneReadOnlyPropertyForThisLineType = -100003
    lnePropertyNotValidForThisLineType = -100004
    lneMaterialIndexOutOfBounds = -100005
    lneCrossSectionIndexOutOfBounds = -100006
    lneNoLinesAreSelected = -100007
    lneLineHasNoMidPoint = -100008
    lneEmptyLineList = -100009
    lneSectionIndexOutOfBounds = -100010
    lneNotBeam = -100011
    lneNotGap = -100012
    lneNotRib = -100013
    lneNotSpring = -100014
    lneNotTruss = -100015
    lneNodeNotOnLine = -100016
    lneErrorSplittingLine = -100017
    lneNMustBeGreaterThan1 = -100018
    lneIllegalServiceClassValue = -100019
    lneDomainIndexOutOfBounds = -100020
    lneStoreyIdOutOfBounds = -100021
    lneInvalidLineType = -100022
    lneReinforcementParametersNotExsist = -100023
    lneInvalidColumnRebarsId = -100024
    lneInvalidConcreteMaterialId = -100025
    lneInvalidRebarSteelGradeId = -100026
    lneInvalidRelease = -100027
    lneInvalidLineTypeOrFEnumber = -100028
    lneInvalidFunctionIDofRelease = -100029
    lneReleaseInitAndLimitMustBe0 = -100030
    lneFunctionIdMustBe0 = -100031
    lneLinesNotContinuous = -100032
    lneStartEndCrossSectionTypeIncompatible = -100033
    lneInvalidRCCheckingParameters = -100034
    lneRCShrinkageEpsMustBePositive = -100035
    lneStirrupParametersAreInvalid = -100036
    lneShearCrackAngleIsInvalid = -100037
    lneInvalidSteelMaterialId = -100038
    lneInvalidStiffnessReduction = -100039
    lneStiffnessReductionNotAllowed = -100040
    lneInvalidStiffnessReductionMat = -100041
    lneReleaseFunctionIndexError = -100042
    lneReleaseInvalidType = -100043
    lneInvalidRefZ = -100044
    lneReleaseInvalidMaterial = -100045
    lneReleaseInvalidComponent = -100046


class ECrossSectionShapeEx(Enum):
    csseAll = 0
    csseCustom = 1
    csseRectangular = 2
    csseI = 3
    csseDoubleI = 4
    csseWedgedI = 5
    csseAsymmetricI = 6
    cssePipe = 7
    csseRegularPolygon = 8
    csseBox = 9
    csseDoubleIBox = 10
    csseU = 11
    csseDoubleUOpened = 12
    csseDoubleUClosed = 13
    csseL = 14
    csseDoubleL = 15
    csseDoubleLFlange = 16
    csseT = 17
    csseZ = 18
    csseC = 19
    csseS = 20
    csseJ = 21
    csseCircle = 22
    csseRectangleRounded = 23
    csseRectangleHollow = 24
    csseIHaunched = 25
    csseTWallHaunched = 26
    csseTTopHaunched = 27
    csseCircleHollow = 28
    csseTrapezoid = 29
    csse2LX = 30
    csse4L = 31
    csseCross = 32
    csseCompositePipe = 33
    csseCompositeBox = 34
    csseCompositeRound = 35
    csseCompositeRectangle = 36
    csseDoubleWedgedI = 37
    csseHSQ = 38
    csseHSQA = 39
    csse2IX = 40
    csseComposite2IX = 41
    csseIFB = 42
    csseSFB = 43
    csseDoubleLClosed = 44


class ECrossSectionRegion(Enum):
    cssr_Unknown = 0
    cssr_EU = 1
    cssr_HU = 2
    cssr_RO = 3
    cssr_US = 4
    cssr_NL = 5
    cssr_CN = 6
    cssr_SK = 7
    cssr_CA = 8
    cssr_SE = 9
    cssr_BR = 10
    cssr_PL = 11
    cssr_RU = 12
    cssr_CH = 13
    cssr_CZ = 14
    cssr_DE = 15
    cssr_FR = 16
    cssr_ES = 17
    cssr_IT = 18
    cssr_AR = 19
    cssr_AT = 20
    cssr_BE = 21
    cssr_BG = 22
    cssr_DK = 23
    cssr_EE = 24
    cssr_FI = 25
    cssr_GR = 26
    cssr_IN = 27
    cssr_JP = 28
    cssr_LV = 29
    cssr_LT = 30
    cssr_NO = 31
    cssr_RS = 32
    cssr_SI = 33
    cssr_ZA = 34
    cssr_TR = 35
    cssr_UK = 36
    cssr_AU = 37
    cssr_NZ = 38
    cssr_PT = 39
    cssr_HR = 40
    cssr_KR = 41
    cssr_IL = 42


class ELoadType(Enum):
    ltNodalForce = 0
    ltBeamConcentrated = 1
    ltBeamDistributed = 2
    ltBeamThermal = 3
    ltBeamStress = 4
    ltBeamFault = 5
    ltBeamEnd = 6
    ltBeamSelfWeight = 7
    ltTrussThermal = 8
    ltTrussStress = 9
    ltTrussFault = 10
    ltTrussSelfWeight = 11
    ltSurfaceSelfWeight = 12
    ltSurfaceDistributed = 13
    ltSurfaceEdge = 14
    ltSurfaceThermal = 15
    ltSurfaceStress = 16
    ltBeamInfluence = 17
    ltDomainSelfWeight = 18
    ltDomainDistributed = 19
    ltDomainConstant = 19
    ltDomainEdge = 20
    ltDomainThermal = 21
    ltDomainStress = 22
    ltRibSelfWeight = 23
    ltRibThermal = 24
    ltRibConcentrated = 25
    ltRibDistributed = 26
    ltSupportDisplacement = 27
    ltDomainConcentrated = 28
    ltSurfaceConcentrated = 30
    ltDomainPolyArea = 33
    ltDomainLinear = 34
    ltDomainFluid = 36
    ltSurfaceFluid = 37
    ltLoadDomainPolyLine = 38
    ltSurfaceToBeam = 39
    ltDomainPolyAssoc = 40
    ltSurfaceToBeamAssoc = 41
    ltNone = -1
    ltDynamicNodalForce = 42
    ltDynamicNodalAcceleration = 43
    ltDynamicNodalSupportAcceleration = 44
    ltBeamMemberConcentrated = 45
    ltBeamMemberDistributed = 46
    ltRibMemberConcentrated = 47
    ltRibMemberDistributed = 48


class EResultType(Enum):
    rtLoadCase = 0
    rtLoadCombination = 1
    rtEnvelope = 2
    rtCritical = 3


class EStoreyAutoSearchStyle(Enum):
    sassDomain = 0
    sassBeam = 1
    sassBoth = 2


class ERCBeamShape(Enum):
    rcbsRectangle = 0
    rcbsDownStand = 1
    rcbsUpStand = 2


class EStructClass_EC(Enum):
    scS1 = 0
    scS2 = 1
    scS3 = 2
    scS4 = 3
    scS5 = 4
    scS6 = 5


class ECrossSectionShape(Enum):
    cssAll = 0
    cssCustom = 1
    cssRectangular = 2
    cssI = 4
    cssDoubleI = 8
    cssWedgedI = 16
    cssAsymmetricI = 32
    cssPipe = 64
    cssRegularPolygon = 128
    cssBox = 256
    cssDoubleIBox = 512
    cssU = 1024
    cssDoubleUOpened = 2048
    cssDoubleUClosed = 4096
    cssL = 8192
    cssDoubleL = 16384
    cssDoubleLFlange = 32768
    cssT = 65536
    cssZ = 131072
    cssC = 262144
    cssS = 524288
    cssJ = 1048576
    cssCircle = 2097152
    cssRectangleRounded = 4194304
    cssRectangleHollow = 8388608
    cssIHaunched = 16777216
    cssTWallHaunched = 33554432
    cssTTopHaunched = 67108864
    cssCircleHollow = 134217728
    cssTrapezoid = 268435456
    css2LX = 536870912
    css4L = 1073741824


class EMembersSupportsError(Enum):
    mseSectionIdOutOfBounds = -100001
    msePadFootingNotDefined = -100002
    mseInvalidType = -100003
    mseStiffnessCalcParamsNotDefined = -100004
    mseInvalidRefType = -100005
    mseMaterialIndexOutOfBounds = -100006


class ESurfaceVertexType(Enum):
    svtContourPoint = 0
    svtContourLineMidPoint = 1
    svtCenterPoint = 2


class EVirtualBeamError(Enum):
    vbeDomainIndexOutOfBounds = -100001
    vbeDomainIndexIsInvalid = -100002
    vbeDomainListIsEmpty = -100003
    vbeChainIndexIsInvalid = -100004
    vbeDuplication = -100005
    vbeInvalidParameters = -100006
    vbeInvalidReferenceParams = -100007
    vbeVirtualBeamNoSection = -100008
    vbeInvalidSections = -100009


class EDisplacementSystem(Enum):
    dsLocal = 0
    dsGlobal = 1


class EPlaneToleranceType(Enum):
    ptRelativePerThousand = 0
    ptAbsolute = 1


class ELanguage(Enum):
    lngEnglish = 0
    lngHungarian = 1
    lngGerman = 2
    lngRomanian = 3
    lngSpanish = 4
    lngItalian = 5
    lngRussian = 6
    lngPortuguese = 7
    lngSerbian = 8
    lngDutch = 9
    lngFrench = 10
    lngHebrew = 11
    lngArabic = 12
    lngCzech = 13
    lngSlovakian = 14
    lngBrasilianPortuguese = 15
    lngGreek = 16
    lngCroatian = 17
    lngPolish = 18
    lngBulgarian = 19


class ECompanyLogoPosition(Enum):
    clpNoLogo = 0
    clpLeft = 1
    clpRight = 2
    clpTopLeft = 3
    clpTopCenter = 4
    clpTopRight = 5


class ELine3dType(Enum):
    ltStraightLine3d = 0
    ltCircleArc3d = 1


class EDegreeOfFreedom(Enum):
    dofFree = 0
    dofXfix = 1
    dofYfix = 2
    dofZfix = 4
    dofXXfix = 8
    dofYYfix = 16
    dofZZfix = 32
    dofwfix = 64
    dofTrussAndMembraneXZ = 58
    dofFrameXZ = 42
    dofPlateXY = 35
    dofPlateXZ = 21
    dofPlateYZ = 14
    dofFrameXY = 28
    dofFrameYZ = 49


class ESeismicDuctilityClass(Enum):
    sdc_DCM = 0
    sdc_DCH = 1


class ELoadPanelEdgeType(Enum):
    lpetNone = 0
    lpetParapet = 1
    lpetWall = 2


class ELoadPanelContourType(Enum):
    lpctUserDefined = 0
    lpctAssociated = 1


class ERCBeam_EC_SIA_SeismicZone(Enum):
    rcbsecSeismicH = 0
    rcbsecSeismicM = 1
    rcbsecAntiSeismic = 2


class EVBDomainsDuplicateMode(Enum):
    ddmDuplicationError = 0
    ddmNoDuplication = 1
    ddmDuplication = 2


class ESupportSeismicComponentSumType(Enum):
    sscstCritical = 0
    sscstFxyzWithLinkedMyz = 1


class ECompanyLogoSizeOption(Enum):
    clsoAuto = 0
    clsoWidth = 1
    clsoHeight = 2


class EGeometryUnitType(Enum):
    gut_Geom_Distance = 0
    gut_Geom_Angle = 1
    gut_Geom_Struct_size = 2


class ERCBeam_ECRO_STAS_SeismicZone(Enum):
    rcbssSeismicH = 0
    rcbssSeismicM = 1
    rcbsszAntiSeismic = 2
    rcbsszSeismicH = 3
    rcbsszSeismicM = 4


class EVirtualBeamType(Enum):
    vbtVirtualBeam = 0
    vbtVirtualStrip = 1


class EDistributionType(Enum):
    dtGlobal = 0
    dtLocal = 1
    dtProjected = 2
    dtEdgeLocal = 3


class EReinforcement(Enum):
    rAsbx = 0
    rAsby = 1
    rAstx = 2
    rAsty = 3


class EReinforcementStatus(Enum):
    rsOK = 0
    rsComprReinforcementNeededX = 1
    rsComprReinforcementNeededY = 2
    rsCannotBeReinforcedX = 3
    rsCannotBeReinforcedY = 4


class EGeneralAlignmentHorizontal(Enum):
    gahLeft = 0
    gahRight = 1
    gahCenter = 2


class EVirtualBeamForce(Enum):
    vbfNx = 0
    vbfVy = 1
    vbfVz = 2
    vbfTx = 3
    vbfMy = 4
    vbfMz = 5


class ECrossSectionUnitType(Enum):
    csut_Size = 0
    csut_Area = 1
    csut_Static_moment = 2
    csut_Area_Moment_Inertia = 3
    csut_Warping_constant = 4


class ERebarType(Enum):
    rtRibbed = 0
    rtWelded = 1
    rtSmooth = 2


class EAcceleration(Enum):
    acX = 0
    acY = 1
    acZ = 2
    acXX = 3
    acYY = 4
    acZZ = 5
    acR = 6
    acRR = 7


class ESolutionControl(Enum):
    scForce = 0
    scDisplacement = 1
    scArcLength = 2
    scPushOver = 3


class EGeneralAlignmentVertical(Enum):
    gavTop = 0
    gavBottom = 1
    gavCenter = 2


class ECompositeInnerCSalign(Enum):
    cicsa_CentreGravity = 0
    cicsa_Centre = 1


class EStiffeners(Enum):
    sNo = 0
    sTransversal = 1


class ESteelCantileverFixedEnd(Enum):
    scfeStartNode = 0
    scfeEndNode = 1


class ESteelBucklingLengthMode(Enum):
    sblm_Factor = 0
    sblm_Length = 1
    sblm_Auto = 2
    sblm_None = 3


class ESteelLateralSupports(Enum):
    ammAuto = 0
    ammEstimatedFromKzKw = 1
    ammForkSupports = 2
    ammUserDefined = 3


class ESteelFireParBetaMethod(Enum):
    sfpbm_Auto = 0
    sfpbm_User = 1


class ESteelSLSHMethod(Enum):
    sslshm_Member = 0
    sslshm_Structure = 1
    sslshm_Custom = 2
    sslshm_Level = 3


class ESteelSLSEMethod(Enum):
    sslsem_No = 0
    sslsem_2 = 1
    sslsem_Left = 2
    sslsem_Right = 3


class ESteelSLSLMethod(Enum):
    sslslm_Member = 0
    sslslm_Custom = 1
    sslslm_Conn = 2


class ESteelSLSPreCamberCurve(Enum):
    sslspcc_Quadratic = 0
    sslslm_Linear = 1


class ELinkElementType(Enum):
    letNN = 0
    letLL = 1


class ENodalSupportType(Enum):
    nstNodalGlobal = 0
    nstNodalBeamRelative = 1
    nstNodalEdgeRelative = 2
    nstNodalReference = 3
    nstTrieder = 4
    nstSeismicIsolator = 5


class EPadFootingType(Enum):
    pftPlate = 0
    pftStepped = 1
    pftSloped = 2


class EReferenceType(Enum):
    rtPoint = 0
    rtVector = 1
    rtAxis = 2
    rtPlane = 3
    rtBeta = 4
    rtNone = 5


class EImperfectionParMatType(Enum):
    ipmtConcSteel = 0
    ipmtBrick = 1
    ipmtOther = 2


class EMeshType(Enum):
    mtAdaptive = 0
    mtUniform = 1


class EMeshGeometryType(Enum):
    mgtTriangle = 0
    mgtQuad = 1
    mgtMixedQuadTriangle = 2


class EGeneralError(Enum):
    errDatabaseNotReady = -101
    errNotFound = -102
    errIndexOutOfBounds = -103
    errReadOnly = -104
    errInternalException = -105
    errNotSupportedByNationalDesignCode = -106
    errCOMServerInternalError = -107
    errNotImplemented = -108
    errEnvelopeIdOutOfBounds = -109
    errMinMaxNotAllowed = -110
    errNoLoadCaseInLoadGroups = -111
    errNoResults = -112
    errCriticalCombinationNotAllowed = -113
    errInvalidName = -114
    errCombinationTypeNotAllowed = -115
    errInvalidEnvelopeUID = -116
    errInvalidPosition = -117
    errIndexDuplication = -118
    errJSONpropertyMissing = -119
    errMembersNotAllowed = -120
    errCreepNotSupported = -121
    errOutOfMemory = -122


class EMaterialUnitType(Enum):
    mut_Young_modulus = 0
    mut_Mass = 1
    mut_Limit_stress = 2
    mut_Limit_strain = 3


class ELinkElementError(Enum):
    leeLineIndexOutOfBounds = -100001
    leeInvalidSystemType = -100002
    leeReferenceIndexOutOfBounds = -100003
    leeErrorAddingNN = -100004
    leeErrorAddingLL = -100005
    leeInvalidLinkElementType = -100006
    leeNotConnectingMasterLineAndMasterStartLink = -100007
    leeNotConnectingMasterLineAndMasterEndLink = -100008
    leeNotConnectingSlaveLineAndMasterStartLink = -100009
    leeNotConnectingSlaveLineAndMasterEndLink = -100010


class ECrossSectionImageExportOptions(Enum):
    csieoNone = 0
    csieoFilled = 1
    csieoStressPointsMarks = 2
    csieoStressPointsLabels = 4
    csieoMainAxis = 8
    csieoMainAxisLabels = 16


class EReinforcementCalculation(Enum):
    rcActual = 0
    rcCalculated = 1


class EXYchartFillType(Enum):
    xycftNone = 0
    xycftSolid = 1
    xycftGradient = 2


class EResultsError(Enum):
    reInvalidAnalysisType = -100001
    reResultCaseIndexOutOfBounds = -100002
    reResultCaseIsNotLoadCase = -100003
    reResultCaseIsNotLoadCombination = -100004
    reLoadCaseIsOutOfBounds = -100005
    reLoadCombinationIsOutOfBounds = -100006
    reFrequencyIndexOutOfBounds = -100007
    reModeShapeIndexOutOfBounds = -100008
    reLoadLevelIndexOutOfBounds = -100009
    reInvalidArrayLength = -100010
    reInvalidLoadCaseType = -100011
    reInvalidNationalDesignCode = -100012
    reInvalidResponseSpectraParam = -100013
    reITAReductionCriterionNotSatisfied = -100014
    reSteelDesignResultsDisabled = -100015
    reCalculatedReinforcementDisabled = -100016
    reReinforcementCheckDisabled = -100017
    reMissingAnalysisResults = -100018
    reRC3moduleNotAvailable = -100019
    reRC1moduleNotAvailable = -100020
    reTD1moduleNotAvailable = -100021
    reDYNmoduleNotAvailable = -100022
    reSE2moduleNotAvailable = -100023
    reNLpackageNotAvailable = -100024
    rePushoverSpectrumIsNotValid = -100025
    rePushoverSpectrumIsNotParametric = -100026


class EMassControl(Enum):
    mcConvertLoadToMasses = 0
    mcMassesOnly = 1


class EDirectObjectDrawType(Enum):
    dodt_Column = 0
    dodt_BeamHorizontal = 1
    dodt_Beam = 2
    dodt_Wall = 3
    dodt_Slab = 4
    dodt_SlabVoids = 5
    dodt_Domain = 6
    dodt_Hole = 7


class EPartItemType(Enum):
    pitNode = 0
    pitLine = 1
    pitSurface = 2
    pitDomain = 3


class EXYchartLabelingStyle(Enum):
    xyclsArrange = 0
    xyclsOverlapFilter = 1


class EPropertiesUnitType(Enum):
    put_Beam_length = 0
    put_Thickness = 1
    put_Surface = 2
    put_Volume = 3
    put_Mass = 4
    put_Mass_per_length = 5
    put_Gap_opening = 6


class ELineGeomType(Enum):
    lgtStraightLine = 0
    lgtCircleArc = 1
    lgtEllipseArc = 2


class ECalculationUserInteraction(Enum):
    cuiUserInteraction = 0
    cuiNoUserInteractionWithAutoCorrect = 1
    cuiNoUserInteractionWithoutAutoCorrect = 2
    cuiNoUserInteractionWithAutoCorrectNoShow = 3
    cuiNoUserInteractionWithoutAutoCorrectNoShow = 4


class EShowStructuralGridLineTitle(Enum):
    ssgltStart = 0
    ssgltEnd = 1
    ssgltBoth = 2


class EVBDefinitionType(Enum):
    vbdtCentroid = 0
    vbdtStraight = 1
    vbdt1PAndV = 2
    vbdt2P = 3


class EEnvironmentClass(Enum):
    ecClassX0 = 0
    ecClassXC1 = 1
    ecClassXC2 = 2
    ecClassXC3 = 3
    ecClassXC4 = 4
    ecClassXD1 = 5
    ecClassXD2 = 6
    ecClassXD3 = 7
    ecClassXD4 = 8
    ecClassXS1 = 9
    ecClassXS2 = 10
    ecClassXS3 = 11
    ecClassXS4 = 12
    ecClassXF1 = 13
    ecClassXF2 = 14
    ecClassXF3 = 15
    ecClassXF4 = 16
    ecClassXA1 = 17
    ecClassXA2 = 18
    ecClassXA3 = 19
    ecClassXA4 = 20
    ecClassXM1 = 21
    ecClassXM2 = 22
    ecClassXM3 = 23
    ecClassXD2B = 24


class ESlabLoadTransfer(Enum):
    slt_OneWay = 0
    slt_TwoWay = 1


class ESlabLoadTransferDirection(Enum):
    sltd_OneWayX = 0
    sltd_OneWayY = 1


class EReinforcementDirection(Enum):
    rdX = 0
    rdY = 1
    rdNone = 2


class ERCNonlinearSurfType(Enum):
    rcnlst_Shell = 0
    rcnlst_Wall = 1
    rcnlst_Slab = 2


class EReinforcementType(Enum):
    rtyp_Ortho = 0
    rtyp_Skew = 1


class ESurfaceType(Enum):
    stHole = 0
    stMembraneStress = 1
    stMembraneStrain = 2
    stPlate = 3
    stShell = 4


class ESurfaceCharacteristics(Enum):
    schLinear = 0
    schTensionOnly = 1
    schCompressionOnly = 2
    schBilinear = 3


class EEdgeConnectionError(Enum):
    eceLineIndexOutOfBounds = -100001
    eceDomainIndexOutOfBounds = -100002
    eceErrorAdding = -100003


class EBeamRibDistributionType(Enum):
    brdtLength = 0
    brdtProjected = 1


class EArcAngleOrientation(Enum):
    oClockwise = 0
    oCounterClockwise = 1


class EVSDefinitionType(Enum):
    vsdtCentroid = 0
    vsdtEccentric = 1


class EStiffnessUnitType(Enum):
    sut_Translational = 0
    sut_Rotational = 1
    sut_Line_translational = 2
    sut_Line_rotational = 3
    sut_Surface = 4


class ESeismicComponentSumType(Enum):
    scstUsual = 0
    scstCritical = 1
    scstNMyMz = 2
    scstMyVz = 3
    scstMzVy = 4
    scstN = 5
    scstNVyVz = 6
    scstNMyMx = 7
    scstNMzMx = 8
    scstNAbsMyMz = 9
    scstNMy = 10
    scstNMz = 11


class EResultComponent(Enum):
    rc_lsSmin = 0
    rc_lsSmax = 1
    rc_lsVmin = 2
    rc_lsVmax = 3
    rc_lsSomin = 4
    rc_lsSomax = 5
    rc_lsVymean = 6
    rc_lsVzmean = 7
    rc_lsSminMax = 8
    rc_lsVminMax = 9
    rc_lsSominMax = 10
    rc_lsSeffMin = 11
    rc_lsSeffMax = 12
    rc_lsSeffMinMax = 13
    rc_lsfyMin = 14
    rc_lsfyMax = 15
    rc_lsfyMinMax = 16
    rc_lsUMin = 17
    rc_lsUMax = 18
    rc_lsUMinMax = 19
    rc_lsBMin = 20
    rc_lsBMax = 21
    rc_lsBMinMax = 22
    rc_ssSxx_Top = 100
    rc_ssSyy_Top = 101
    rc_ssSxy_Top = 102
    rc_ssSxz_Top = 103
    rc_ssSyz_Top = 104
    rc_ssSVM_Top = 105
    rc_ssS1_Top = 106
    rc_ssS2_Top = 107
    rc_ssAs_Top = 108
    rc_ssSxx_Middle = 110
    rc_ssSyy_Middle = 111
    rc_ssSxy_Middle = 112
    rc_ssSxz_Middle = 113
    rc_ssSyz_Middle = 114
    rc_ssSVM_Middle = 115
    rc_ssS1_Middle = 116
    rc_ssS2_Middle = 117
    rc_ssAs_Middle = 118
    rc_ssSxx_Bottom = 120
    rc_ssSyy_Bottom = 121
    rc_ssSxy_Bottom = 122
    rc_ssSxz_Bottom = 123
    rc_ssSyz_Bottom = 124
    rc_ssSVM_Bottom = 125
    rc_ssS1_Bottom = 126
    rc_ssS2_Bottom = 127
    rc_ssAs_Bottom = 128
    rc_ssSzz_Top = 129
    rc_ssSeff_Top = 130
    rc_ssfy_Top = 131
    rc_ssU_Top = 132
    rc_ssState_Top = 133
    rc_ssByy_Top = 134
    rc_ssBzz_Top = 135
    rc_ssBxy_Top = 136
    rc_ssSzz_Middle = 137
    rc_ssSeff_Middle = 138
    rc_ssfy_Middle = 139
    rc_ssU_Middle = 140
    rc_ssState_Middle = 141
    rc_ssByy_Middle = 142
    rc_ssBzz_Middle = 143
    rc_ssBxy_Middle = 144
    rc_ssSzz_Bottom = 145
    rc_ssSeff_Bottom = 146
    rc_ssfy_Bottom = 147
    rc_ssU_Bottom = 148
    rc_ssState_Bottom = 149
    rc_ssByy_Bottom = 150
    rc_ssBzz_Bottom = 151
    rc_ssBxy_Bottom = 152
    rc_lfNx = 200
    rc_lfVy = 201
    rc_lfVz = 202
    rc_lfTx = 203
    rc_lfMy = 204
    rc_lfMz = 205
    rc_lfMyD = 206
    rc_lfVxz = 207
    rc_sfNx = 300
    rc_sfNy = 301
    rc_sfNxy = 302
    rc_sfMx = 303
    rc_sfMy = 304
    rc_sfMxy = 305
    rc_sfVxz = 306
    rc_sfVyz = 307
    rc_sfvSz = 308
    rc_sfN1 = 309
    rc_sfN2 = 310
    rc_sfAn = 311
    rc_sfM1 = 312
    rc_sfM2 = 313
    rc_sfAm = 314
    rc_sfNxD = 315
    rc_sfNyD = 316
    rc_sfMxDp = 319
    rc_sfMxDm = 320
    rc_sfMyDp = 321
    rc_sfMyDm = 322
    rc_sfAvRz = 323
    rc_sfAn1 = 324
    rc_sfAn2 = 325
    rc_sfAm1 = 326
    rc_sfAm2 = 327
    rc_nsfRx = 400
    rc_nsfRy = 401
    rc_nsfRz = 402
    rc_nsfRxx = 403
    rc_nsfRyy = 404
    rc_nsfRzz = 405
    rc_nsfRr = 406
    rc_nsfRrr = 407
    rc_nsfRxyz = 408
    rc_nsfRxxyyzz = 409
    rc_nsfRalpha = 410
    rc_lsfRx = 500
    rc_lsfRy = 501
    rc_lsfRz = 502
    rc_lsfRxx = 503
    rc_lsfRyy = 504
    rc_lsfRzz = 505
    rc_lsfRr = 506
    rc_lsfRrr = 507
    rc_ssfRx = 600
    rc_ssfRy = 601
    rc_ssfRz = 602
    rc_ssfRr = 603
    rc_sfRx = 700
    rc_sfRy = 701
    rc_sfRz = 702
    rc_sfRxx = 704
    rc_sfRyy = 705
    rc_sfRzz = 706
    rc_gfNx = 800
    rc_ecfNx = 900
    rc_ecfVy = 901
    rc_ecfVz = 902
    rc_ecfTx = 903
    rc_ecfMy = 904
    rc_ecfMz = 905
    rc_lefNx_NN = 1000
    rc_lefVy_NN = 1001
    rc_lefVz_NN = 1002
    rc_lefTx_NN = 1003
    rc_lefMy_NN = 1004
    rc_lefMz_NN = 1005
    rc_lefNx_LL = 1010
    rc_lefVy_LL = 1011
    rc_lefVz_LL = 1012
    rc_lefTx_LL = 1013
    rc_lefMy_LL = 1014
    rc_lefMz_LL = 1015
    rc_d_eX = 1101
    rc_d_eY = 1102
    rc_d_eZ = 1103
    rc_d_fX = 1104
    rc_d_fY = 1105
    rc_d_fZ = 1106
    rc_d_eR = 1107
    rc_d_fR = 1108
    rc_rAsbx = 1200
    rc_rAsby = 1201
    rc_rAstx = 1202
    rc_rAsty = 1203
    rc_rAsxbt = 1204
    rc_rAsybt = 1205
    rc_rAsxyb = 1206
    rc_rAsxyt = 1207
    rc_scVRdc = 1300
    rc_scVEdMinusVRdc = 1301
    rc_scVRdmax = 1302
    rc_scVEdDivVRdmax = 1303
    rc_scaVEd = 1304
    rc_scAsw = 1305
    rc_coBottom = 1400
    rc_cw_wkb = 1400
    rc_coTop = 1401
    rc_cw_wkt = 1401
    rc_cw_wk2b = 1402
    rc_cw_wk2t = 1403
    rc_cw_wRb = 1404
    rc_cw_wRt = 1405
    rc_cw_wS2b = 1406
    rc_cw_wS2t = 1407
    rc_veX = 1500
    rc_veY = 1501
    rc_veZ = 1502
    rc_veXX = 1503
    rc_veYY = 1504
    rc_veZZ = 1505
    rc_veR = 1506
    rc_veRR = 1507
    rc_acX = 1600
    rc_acY = 1601
    rc_acZ = 1602
    rc_acXX = 1603
    rc_acYY = 1604
    rc_acZZ = 1605
    rc_acR = 1606
    rc_acRR = 1607
    rc_arAsxb = 1700
    rc_arAsyb = 1701
    rc_arAsxt = 1702
    rc_arAsyt = 1703
    rc_arAsxbt = 1704
    rc_arAsybt = 1705
    rc_rdAsxb = 1800
    rc_rdAsyb = 1801
    rc_rdAsxt = 1802
    rc_rdAsyt = 1803
    rc_ilPx1 = 1900
    rc_ilPy1 = 1901
    rc_ilPz1 = 1902
    rc_sstExx = 2000
    rc_sstEyy = 2001
    rc_sstExy = 2002
    rc_sstFzz = 2003
    rc_sstKxx = 2004
    rc_sstKyy = 2005
    rc_sstKxy = 2006
    rc_sstExz = 2007
    rc_sstEyz = 2008
    rc_sstEsz = 2009
    rc_sstE1 = 2010
    rc_sstE2 = 2011
    rc_sstAe = 2012
    rc_sstK1 = 2013
    rc_sstK2 = 2014
    rc_sstAk = 2015
    rc_ivDnx = 2100
    rc_ivDny = 2101
    rc_ivDnxy = 2102
    rc_ivDmx = 2103
    rc_ivDmy = 2104
    rc_ivDmxy = 2105
    rc_ivDqx = 2106
    rc_ivDqy = 2107
    rc_bd_eX = 2200
    rc_bd_eY = 2201
    rc_bd_eZ = 2202
    rc_bd_fX = 2203
    rc_bd_fY = 2204
    rc_bd_fZ = 2205
    rc_bd_eR = 2206
    rc_bd_fR = 2207
    rc_rsSxb = 2300
    rc_rsSyb = 2301
    rc_rsSxt = 2302
    rc_rsSyt = 2303
    rc_rsSxbt = 2304
    rc_rsSybt = 2305
    rc_rReinfCheck = 2400
    rc_ymEx = 2500
    rc_ymEy = 2501
    rc_vd_eX = 2600
    rc_vd_eY = 2601
    rc_vd_eZ = 2602
    rc_vd_fX = 2603
    rc_vd_fY = 2604
    rc_vd_fZ = 2605
    rc_vd_eR = 2606
    rc_vd_fR = 2607
    rc_sfMxD = 2700
    rc_sfMyD = 2701
    rc_sfMxU = 2702
    rc_sfMyU = 2703
    rc_sfMxDU = 2704
    rc_sfMyDU = 2705
    rc_sfMxDcr = 2800
    rc_sfMyDcr = 2801
    rc_sfMxUcr = 2802
    rc_sfMyUcr = 2803
    rc_sfMxDUcr = 2804
    rc_sfMyDUcr = 2805
    rc_arcrUtil = 2901
    rc_arcrAvgUtil = 2902
    rc_arcrVx = 3000
    rc_arcrN = 3001
    rc_arcrVz = 3002
    rc_arcrM = 3003
    rc_arcrDez = 3004
    rc_berrdEx = 3100
    rc_berrdEy = 3101
    rc_berrdEz = 3102
    rc_berrdFx = 3103
    rc_berrdFy = 3104
    rc_berrdFz = 3105
    rc_berrdEr = 3106
    rc_berrdFr = 3107
    rc_bstExx = 3200
    rc_bstKyy = 3201
    rc_bstKzz = 3202
    rc_bstEyz = 3203
    rc_bstExy = 3204
    rc_bstExz = 3205
    rc_vbifNx = 3300
    rc_vbifVy = 3301
    rc_vbifVz = 3302
    rc_vbifTx = 3303
    rc_vbifMy = 3304
    rc_vbifMz = 3305
    rc_bstspExxTMin = 3400
    rc_bstspExxTMax = 3401
    rc_bstspExxTMinMax = 3402
    rc_bstspExxEMin = 3403
    rc_bstspExxEMax = 3404
    rc_bstspExxEMinMax = 3405
    rc_bstspExxPMin = 3406
    rc_bstspExxPMax = 3407
    rc_bstspExxPMinMax = 3408
    rc_bstspEeffMin = 3409
    rc_bstspEeffMax = 3410
    rc_bstspEeffMinMax = 3411
    rc_bstspDeeffMin = 3412
    rc_bstspDeeffMax = 3413
    rc_bstspDeeffMinMax = 3414
    rc_bstspLeeffMin = 3415
    rc_bstspLeeffMax = 3416
    rc_bstspLeeffMinMax = 3417
    rc_vrfaRSelf = 3500
    rc_vrfaRExtr = 3501
    rc_vrfaRFull = 3502
    rc_vbdEx = 3600
    rc_vbdEy = 3601
    rc_vbdEz = 3602
    rc_vbdFx = 3603
    rc_vbdFy = 3604
    rc_vbdFz = 3605
    rc_vbdEr = 3606
    rc_vbdFr = 3607
    rc_sstspExxTT = 3700
    rc_sstspEyyTT = 3701
    rc_sstspExyTT = 3702
    rc_sstspE1TT = 3703
    rc_sstspE2TT = 3704
    rc_sstspAeTT = 3705
    rc_sstspExxET = 3706
    rc_sstspEyyET = 3707
    rc_sstspExyET = 3708
    rc_sstspE1ET = 3709
    rc_sstspE2ET = 3710
    rc_sstspAeET = 3711
    rc_sstspExxPT = 3712
    rc_sstspEyyPT = 3713
    rc_sstspExyPT = 3714
    rc_sstspE1PT = 3715
    rc_sstspE2PT = 3716
    rc_sstspAePT = 3717
    rc_sstspEeffPT = 3718
    rc_sstspDeeffPT = 3719
    rc_sstspExxTC = 3720
    rc_sstspEyyTC = 3721
    rc_sstspExyTC = 3722
    rc_sstspE1TC = 3723
    rc_sstspE2TC = 3724
    rc_sstspAeTC = 3725
    rc_sstspExxEC = 3726
    rc_sstspEyyEC = 3727
    rc_sstspExyEC = 3728
    rc_sstspE1EC = 3729
    rc_sstspE2EC = 3730
    rc_sstspAeEC = 3731
    rc_sstspExxPC = 3732
    rc_sstspEyyPC = 3733
    rc_sstspExyPC = 3734
    rc_sstspE1PC = 3735
    rc_sstspE2PC = 3736
    rc_sstspAePC = 3737
    rc_sstspEeffPC = 3738
    rc_sstspDeeffPC = 3739
    rc_sstspExxTB = 3740
    rc_sstspEyyTB = 3741
    rc_sstspExyTB = 3742
    rc_sstspE1TB = 3743
    rc_sstspE2TB = 3744
    rc_sstspAeTB = 3745
    rc_sstspExxEB = 3746
    rc_sstspEyyEB = 3747
    rc_sstspExyEB = 3748
    rc_sstspE1EB = 3749
    rc_sstspE2EB = 3750
    rc_sstspAeEB = 3751
    rc_sstspExxPB = 3752
    rc_sstspEyyPB = 3753
    rc_sstspExyPB = 3754
    rc_sstspE1PB = 3755
    rc_sstspE2PB = 3756
    rc_sstspAePB = 3757
    rc_sstspEeffPB = 3758
    rc_sstspDeeffPB = 3759
    rc_sstspLeeffT = 3760
    rc_sstspLeeffC = 3761
    rc_sstspLeeffB = 3762
    rc_vdW1 = 3800
    rc_vdW2 = 3801
    rc_vdW3 = 3802
    rc_vdWTot = 3803
    rc_vdWbij = 3804
    rc_rccwUBeam = 3900
    rc_rccwUStrip = 3901
    rc_rccwUOverall = 3902
    rc_rsdEx = 4000
    rc_rsdEy = 4001
    rc_rsdEz = 4002
    rc_rsdFx = 4003
    rc_rsdFy = 4004
    rc_rsdFz = 4005
    rc_snlFyx = 4100
    rc_snlUx = 4101
    rc_snlEEx = 4102
    rc_snlPEx = 4103
    rc_snlPEeffx = 4104
    rc_snlPdeeffx = 4105
    rc_snlBx = 4106
    rc_snlFyy = 4107
    rc_snlUy = 4108
    rc_snlEEy = 4109
    rc_snlPEy = 4110
    rc_snlPEeffy = 4111
    rc_snlPdeeffy = 4112
    rc_snlBy = 4113
    rc_snlFyz = 4114
    rc_snlUz = 4115
    rc_snlEEz = 4116
    rc_snlPEz = 4117
    rc_snlPEeffz = 4118
    rc_snlPdeeffz = 4119
    rc_snlBz = 4120
    rc_snlMyxx = 4121
    rc_snlUxx = 4122
    rc_snlEExx = 4123
    rc_snlPExx = 4124
    rc_snlPEeffxx = 4125
    rc_snlPdeeffxx = 4126
    rc_snlBxx = 4127
    rc_snlMyyy = 4128
    rc_snlUyy = 4129
    rc_snlEEyy = 4130
    rc_snlPEyy = 4131
    rc_snlPEeffyy = 4132
    rc_snlPdeeffyy = 4133
    rc_snlByy = 4134
    rc_snlMyzz = 4135
    rc_snlUzz = 4136
    rc_snlEEzz = 4137
    rc_snlPEzz = 4138
    rc_snlPEeffzz = 4139
    rc_snlPdeeffzz = 4140
    rc_snlBzz = 4141
    rc_xsSxxmT = 4200
    rc_xsSyymT = 4201
    rc_xsSxymT = 4202
    rc_xsSxxmB = 4203
    rc_xsSyymB = 4204
    rc_xsSxymB = 4205
    rc_xsSxxn = 4206
    rc_xsSyyn = 4207
    rc_xsSxyn = 4208
    rc_xsSxzmax = 4209
    rc_xsSyzmax = 4210
    rc_xsSrxmax = 4211
    rc_xsSrymax = 4212
    rc_xuMN0 = 4300
    rc_xuMN90 = 4301
    rc_xuVt = 4302
    rc_xuVrN = 4303
    rc_xuMax = 4304
    rc_dcmwU = 4400
    rc_sdrVx = 4500
    rc_sdrRDx = 4501
    rc_sdrRSx = 4502
    rc_sdrVy = 4503
    rc_sdrRDy = 4504
    rc_sdrRSy = 4505
    rc_sdrVz = 4506
    rc_sdrRDz = 4507
    rc_sdrRSz = 4508
    rc_sdrVxx = 4509
    rc_sdrRDxx = 4510
    rc_sdrRSxx = 4511
    rc_sdrVyy = 4512
    rc_sdrRDyy = 4513
    rc_sdrRSyy = 4514
    rc_sdrVzz = 4515
    rc_sdrRDzz = 4516
    rc_sdrRSzz = 4517
    rc_rccolUNM = 4518
    rc_rccolUVT = 4519
    rc_rccolAsl = 4520
    rc_rccolUSum = 4521
    rc_cw_wkbt = 4522
    rc_cw_wk2bt = 4523
    rc_sd_eff = 10000
    rc_sd_1 = 10001
    rc_sd_2 = 10002
    rc_sd_3 = 10003
    rc_sd_4 = 10004
    rc_sd_5 = 10005
    rc_sd_6 = 10006
    rc_sd_7 = 10007
    rc_sd_8 = 10008
    rc_sd_9 = 10009
    rc_sd_10 = 10010
    rc_sd_11 = 10011
    rc_sd_12 = 10012
    rc_sd_13 = 10013
    rc_sd_14 = 10014
    rc_sd_15 = 10015
    rc_sd_16 = 10016
    rc_sd_17 = 10017
    rc_sd_18 = 10018
    rc_sd_19 = 10019
    rc_sd_20 = 10020
    rc_sd_21 = 10021
    rc_sd_22 = 10022
    rc_sd_23 = 10023
    rc_sd_24 = 10024
    rc_sd_25 = 10025
    rc_sd_26 = 10026
    rc_sd_27 = 10027
    rc_sd_28 = 10028
    rc_sd_29 = 10029
    rc_sd_30 = 10030
    rc_sd_31 = 10031
    rc_sd_util_ULS = 10090
    rc_sd_util_SLS = 10091
    rc_td_eff = 10100
    rc_td_1 = 10101
    rc_td_2 = 10102
    rc_td_3 = 10103
    rc_td_4 = 10104
    rc_td_5 = 10105
    rc_td_6 = 10106
    rc_td_7 = 10107
    rc_td_8 = 10108
    rc_td_9 = 10109
    rc_td_10 = 10110
    rc_td_11 = 10111
    rc_td_12 = 10112
    rc_td_13 = 10113
    rc_td_14 = 10114
    rc_td_15 = 10115
    rc_td_util_ULS = 10190
    rc_td_util_SLS = 10191
    rc_td_util = 10192


class ERCBeamDesignPlane(Enum):
    rcbdpQzMy = 0
    rcbdpQyMz = 1


class ESurfaceSupportType(Enum):
    sstSurfaceElasticFoundation = 0


class ESectionsError(Enum):
    seSegmentDefinitionError = -100001
    seSectionTypeIsNotSegment = -100002
    seLoadCaseIndexOutOfBounds = -100003
    seLoadCombinationIndexOutOfBounds = -100004
    seInvalidAnalysisType = -100005


class ERCBeamDesignError(Enum):
    rcbdePrestressedBeamsNotSupported = -100001
    rcbdeErrorSettingLines = -100002
    rcbdeInvalidLoadCaseId = -100003
    rcbdeInvalidLoadCombinationId = -100004
    rcbdeInvalidCombinationOfLoadCaseAndLoadLevel = -100005
    rcbdeInvalidCombinationOfLoadCombinationAndLoadLevel = -100006
    rcbdeInvalidMaterialId = -100007
    rcbdeInvalidArrayLength = -100008
    rcbdeInvalidAnalysisType = -100009
    rcbdeInvalidValue_bw = -100010
    rcbdeInvalidValue_h = -100011
    rcbdeInvalidValue_hf = -100012
    rcbdeInvalidValue_beff = -100013
    rcbdeInvalidRebarMaterial = -100014
    rcbdeInvalidStirrupMaterial = -100015
    rcbdeInvalidStirrupDiameter = -100016
    rcbdeInvalidStirrupLegs = -100017
    rcbdeInvalidBottomPos = -100018
    rcbdeInvalidTopPos = -100019
    rcbdeInvalidAst_min = -100020
    rcbdeInvalidAsb_min = -100021
    rcbdeErrorSettingMembers = -100022
    rcbdeInvalidThetaValue = -100023
    rcbdeDesignCodeParametersNotValidForUsedDesignCode = -100024
    rcbdeEnvironmentClassNotValidForUsedDesignCode = -100025
    rcbdeInvalidEnvelopeID = -100026
    rcbdeInvalidShrinkageValue = -100027
    rcbdeInvalidDesignParameters = -100028
    rcbdeInvalidPlasticHingeParams = -100029


class EWindowSplit(Enum):
    wsHorizontal = 0
    wsVertical = 1


class ECrossSectionObjectiveOfOptimization(Enum):
    csooMinimumWeight = 0
    csooMinimumHeight = 1
    csooMinimumWidth = 2


class ESmoothing(Enum):
    smthNone = 0
    smthSelective = 1
    smthAllSurf = 2


class ESeismicSensitivityResultsError(Enum):
    ssreOK = 0
    ssreEmptyStorey = 1
    ssreInclinedElementExists = 2
    ssreTorsionResultsMissing = 3


class EMemberMeshType(Enum):
    mmtMaxDeviationFromArc = 0
    mmtMaxElementSize = 1
    mmtSegments = 2
    mmtAngle = 3


class ECrossSectionOptimizationType(Enum):
    csotPreDefinedShapes = 0
    csotParametric = 1


class EDomainCompRibEccType(Enum):
    dcret_top = 1
    dcret_midplane = 2
    dcret_bottom = 3
    dcret_custom = 4


class EIntensityReferenceValue(Enum):
    irvAbsMaxModel = 0
    irvAbsMaxParts = 1
    irvCustomVal = 2


class ESeismicStoreysError(Enum):
    sseSeismicResultsMissing = -100001


class EMassMatrixType(Enum):
    mtDiagonal = 0
    mtConsistent = 1


class ECriticalCombinationFormula(Enum):
    ccfAuto = 0
    ccfCustom = 1
    ccfSemiAuto = 2


class EMemberExcType(Enum):
    mexcNone = 0
    mexcDomainRib = 1
    mexcLocal = 2
    mexcRelOffs = 3
    mexcGroup = 4
    mexcRefLine = 5


class ELineForce(Enum):
    lfNx = 0
    lfVy = 1
    lfVz = 2
    lfTx = 3
    lfMy = 4
    lfMz = 5
    lfMyD = 6


class ESurfaceForce(Enum):
    sfNx = 0
    sfNy = 1
    sfNxy = 2
    sfMx = 3
    sfMy = 4
    sfMxy = 5
    sfVxz = 6
    sfVyz = 7
    sfvSz = 8
    sfN1 = 9
    sfN2 = 10
    sfAn = 11
    sfM1 = 12
    sfM2 = 13
    sfAm = 14
    sfNxD = 15
    sfNyD = 16
    sfMxDp = 17
    sfMxDm = 18
    sfMyDp = 19
    sfMyDm = 20


class ENodalSupportForce(Enum):
    nsfRx = 0
    nsfRy = 1
    nsfRz = 2
    nsfRxx = 3
    nsfRyy = 4
    nsfRzz = 5
    nsfRr = 6
    nsfRrr = 7
    nsfRalpha = 8


class ELineSupportForce(Enum):
    lsfRx = 0
    lsfRy = 1
    lsfRz = 2
    lsfRxx = 3
    lsfRyy = 4
    lsfRzz = 5
    lsfRr = 6
    lsfRrr = 7


class ESurfaceSupportForce(Enum):
    ssfRx = 0
    ssfRy = 1
    ssfRz = 2


class ESpringForce(Enum):
    sfRx = 0
    sfRy = 1
    sfRz = 2
    sfRxx = 4
    sfRyy = 5
    sfRzz = 6


class EWindowColourMode(Enum):
    wcmColour = 0
    wcmGreyScale = 1
    wcmBlackAndWhite = 2


class EConnectedToNodeType(Enum):
    ctntAll = 1
    ctntSelected = 2
    ctntVisible = 3


class EMassesTakenIntoAccount(Enum):
    mtiaAll = 0
    mtiaAboveHeightZ = 1
    mtiaAboveSelectedStory = 2


class EDisplayMode(Enum):
    dmDiagram = 0
    dmDiagramAvgVals = 1
    dmSectionLine = 2
    dmIsolines = 3
    dmIsosurfaces2D = 4
    dmIsosurfaces3D = 5
    dmNone = 6
    dmDiagramFilled = 7
    dmSectionFilled = 8
    dmIsosurfacesAvgVals = 9
    dmSolidModel = 10


class EMaterialColour(Enum):
    mclOther = 44732672
    mclOtherContour = 0
    mclSteel = 39134390
    mclSteelContour = 39124992
    mclConcrete = 44742326
    mclConcreteContour = 33554432
    mclTimber = 33582518
    mclTimberContour = 33563720
    mclAluminium = 50313837
    mclAluminiumContour = 39143496
    mclBrick = 8031416
    mclBrickContour = 3424867


class EMathTextError(Enum):
    mteMathTextUIDandAPI_NameDontMatch = -100001
    mteAPI_NameNotFound = -100002
    mteMathTextUIDnotValid = -100003


class ELoadCombinationsError(Enum):
    lcoeDifferentFactorsAndCaseIdsCount = -100001
    lcoeNameExists = -100002
    lcoeAutoGenerationFailed = -100003
    lcoeAutoGenerationFailedNoCriticalGroup = -100004
    lcoeInvalidCombinationTypesValue = -100005


class EMemberExcOffsPos(Enum):
    offsNone = 0
    offsTopLeft = 1
    offsTopCenter = 2
    offsTopRight = 3
    offsCenterLeft = 4
    offsCenterRight = 5
    offsBottomLeft = 6
    offsBottomCenter = 7
    offsBottomRight = 8


class EDimensionLabelOrientation(Enum):
    dloAutomatic = 0
    dloHorizontal = 1
    dloVertical = 2
    dloAligned = 3
    dloRadial = 4
    dloTangential = 5
    dloLeft = 6
    dloCentre = 7
    dloRight = 8


class EDimensionStyle(Enum):
    dsNormalTick = 0
    dsBoldTick = 1
    dsArrow = 2
    dsTriangle = 3
    dsTriangleStr = 4
    dsTriangleFilled = 5
    dsCircleStr = 6
    dsCircleFilled = 7
    dsPlus = 8
    dsLevelCircleCheck = 9
    dsLevelCircle = 10
    dsLevelCircleExt = 11
    dsLevelCross = 12
    dsLevelCrossExt = 13
    dsElevCorner = 14
    dsElevTriangleExt = 15
    dsElevTriangleRight = 16
    dsElevTriangleTop = 17
    dsElevTriangleTopRight = 18
    dsNothing = 19
    dsExtLine = 20
    dsInBox = 21


class EDomainVariableThicknessType(Enum):
    dvtvNone = 0
    dvtvOneDirection = 1
    dvtvTwoDirections = 2


class EDomainExcentricityType(Enum):
    detNone = 0
    detConstant = 1
    detOneDirection = 2
    detTwoDirections = 3
    detTopSurface = 4
    detBottomSurface = 5


class EDisplayShape(Enum):
    dsUndeformed = 0
    dsDeformed = 1


class ECombinationMethod(Enum):
    cmULS = 0
    cmULSab = 1


class ERCColumnCheckingError(Enum):
    rccceInvalidLineId = -100001
    rccceInvalidMemberId = -100002
    rccceInvalidLoadCaseId = -100003
    rccceInvalidLoadCombinationId = -100004
    rccceInvalidCombinationOfLoadCaseAndLoadLevel = -100005
    rccceInvalidCombinationOfLoadCombinationAndLoadLevel = -100006
    rccceColumnReinforcementParametersNotSet = -100007
    rccceCapacityCurveCannotBeGenerated = -100008
    rccceInvalidRebarSteelGradeId = -100009
    rccceInvalidConcreteMaterialId = -100010
    rccceInvalidColumnRebarsId = -100011
    rccceCapacityCurveNotYetGenerated = -100012
    rccceDifferentColumnReinforcementParameters = -100013
    rccceInvalidArrayLength = -100014
    rccceInvalidAnalysisType = -100015
    rccceExcentricity = -100016
    rccceColumnReinforcementNoForces = -100017
    rccceInvalidEnvelopeID = -100018
    rccceInvalidDesignParameters = -100019
    rccceShrinkageEpsMustBePositive = -100020
    rccceVTCheckIsNotSupported = -100021
    rccceStirrupParametersAreInvalid = -100022
    rccceShearCrackAngleIsInvalid = -100023
    rccceVTCapacityDesignIsNotSupported = -100024
    rccceInvalidSteelMaterialId = -100025
    rccceColumnCheckingIsNotSupported = -100026


class EMaterialError(Enum):
    meEmtpy_Name = -100001
    meNegative_Nux = -100002
    meNegative_Nuy = -100003
    meNegative_Nuz = -100004
    meGreaterThan05_Nux = -100005
    meGreaterThan05_Nuy = -100006
    meGreaterThan05_Nuz = -100007
    meNegative_Alfax = -100008
    meNegative_Alfay = -100009
    meNegative_Alfaz = -100010
    meNonPositive_Ex = -100011
    meNonPositive_Ey = -100012
    meNonPositive_Ez = -100013
    meNonPositive_Rho = -100014
    meNonPositive_SigmaH = -100015
    meNonPositive_SigmapH = -100016
    meNonPositive_Ry = -100017
    meNonPositive_Fy = -100018
    meNonPositive_Fu = -100019
    meNonPositive_Fy40 = -100020
    meNonPositive_Fu40 = -100021
    meNonPositive_R = -100022
    meNonPositive_Rc = -100023
    meNonPositive_SigmabH = -100024
    meNonPositive_SigmahH = -100025
    meNonPositive_Fit = -100026
    meNonPositive_Fck = -100027
    meNonPositive_GammaC = -100028
    meNonPositive_Alfacc = -100029
    meNonPositive_Fck_cube = -100030
    meInvalid_MaterialType = -100031
    meInvalid_NationalDesignCode = -100032
    meNameAlreadyExists = -100033
    meNonPositive_E005 = -100034
    meNonPositive_Gmean = -100035
    meNonPositive_fmk = -100036
    meNonPositive_ft0k = -100037
    meNonPositive_ft90k = -100038
    meNonPositive_fc0k = -100039
    meNonPositive_fc90kz = -100040
    meNonPositive_fvkz = -100041
    meNonPositive_GammaM = -100042
    meNonPositive_fc90ky = -100043
    meNonPositive_fvky = -100044
    meNonPositive_s = -100045
    meErrorAdding = -100046


class ETorsion(Enum):
    tFree = 0
    tPartial = 1
    tFixed = 2


class EColumnRebarsError(Enum):
    crbeInvalidCrossSectionId = -100001


class EDisplayAnalysisType(Enum):
    datLinear = 0
    datNonLinear = 1


class ELoadPositionType(Enum):
    lptUpper = 0
    lptAxis = 1
    lptLower = 2


class ETimberGrain(Enum):
    tgTopEdge = 0
    tgBottomEdge = 1


class EXLAMpanelsError(Enum):
    xpeInvalidLayers = -100001
    xpeLayersNotSymmetric = -100002
    xpeThicknessesMustBePositive = -100003


class EWindLoadError(Enum):
    wleNoWindLoadDefined = -100001


class ETimberSLSEMethod(Enum):
    tslsem_No = 0
    tslsem_2 = 1
    tslsem_Left = 2
    tslsem_Right = 3


class ETimberSLSLMethod(Enum):
    tslslm_Member = 0
    tslslm_Custom = 1
    tslslm_Conn = 2


class ETimberSLSPreCamberCurve(Enum):
    tslspcc_Quadratic = 0
    tslslm_Linear = 1


class ETimberSLSDesignCreepMode(Enum):
    tslsdcm_Code = 0
    tslsdcm_User = 1


class EActualReinforcementLabelType(Enum):
    arltRebarsAndReinfValues = 0
    arltRebarsAndQuantity = 1


class EGridType(Enum):
    gtGridLines = 0
    gtDotGrid = 1


class ELoadDistributionType(Enum):
    ldtConst = 0
    ldtLinear = 1


class ECriticalGroupCombinationsError(Enum):
    cgceLoadGroupIdOutOfBounds = 0
    cgceNotEditable = 1


class ELayerError(Enum):
    laeInvalidName = -100001
    laeInvalidPenWidth = -100002
    laeInvalidFontName = -100003


class EPadFootingStepMeasureSource(Enum):
    pfsms_Interior = 0
    pfsms_Edge = 1


class EAttachmentsError(Enum):
    attaeCannotAddAttachment = -100001
    attaeCannotGetAttachment = -100002
    attaeInvalidName = -100003
    attaeInvalidOrEmptyItemData = -100004
    attaeAttachmentNotFound = -100005
    attaeItemIndexOutOfBounds = -100006
    attaeCannotDeleteAttachment = -100007
    attaeItemHasNoAttachment = -100008
    attaeInvalidOrEmptyItemIndexes = -100009


class ELoadsUnitType(Enum):
    lut_Force = 0
    lut_Moment = 1
    lut_Line_force = 2
    lut_Line_force_moment = 3
    lut_Surface_force = 4
    lut_Temperature = 5
    lut_Temperature_variation = 6
    lut_Design_fire_load_density = 7
    lut_Specific_heat = 8
    lut_Section_factor = 9
    lut_Fire_duration = 10


class EReinforcementCheckError(Enum):
    rceCOMError = -100001
    rceLoadCaseIdIndexOutOfBounds = -100002
    rceLoadCombinationIdIndexOutOfBounds = -100003
    rceInvalidAnalysisType = -100004
    rceCombinationTypeNotValidForCurrentNationalDesignCode = -100005
    rceInvalidCombinationOfLoadCaseAndLoadLevel = -100006
    rceInvalidCombinationOfLoadCombinationAndLoadLevel = -100007


class EDisplacementsError(Enum):
    deNodeIndexOutOfBounds = -100001
    deLoadCaseIndexOutofBounds = -100002
    deLoadCombinationIndexOutofBounds = -100003
    deCombinationTypeNotValidForCurrentNationalDesignCode = -100004
    deCOMError = -100005
    deNoNodesInTheModel = -100006
    deNoLoadCasesInTheModel = -100007
    deNoLoadCombinationsInTheModel = -100008
    deSectionIndexOutOfBounds = -100009
    deLineIndexOutOfBounds = -100010
    deLineHasNoSections = -100011
    deNoValidLinesInTheModel = -100012
    deInvalidAnalysisType = -100013
    deInvalidCombinationOfLoadCaseAndLoadLevel = -100014
    deInvalidCombinationOfLoadCombinationAndLoadLevel = -100015
    deNoResultBlocksInTheModel = -100016
    deInvalidLineType = -100017
    deMemberIndexOutOfBounds = -100018
    deVirtualBeamIndexOutOfBounds = -100019
    deVirtualBeamChainIndexOutOfBounds = -100020
    deVirtualBeamSectionIndexOutOfBounds = -100021


class EDomainSupportType(Enum):
    dstDomainElasticFoundation = 0


class ERoofType(Enum):
    rtUndefined = 0
    rtFlat = 1
    rtMonopitch = 2
    rtDuopitch = 3
    rtHip = 4
    rtBarrel = 5


class EShearCapacitiesError(Enum):
    sceCOMError = -100001
    sceLoadCaseIdIndexOutOfBounds = -100002
    sceLoadCombinationIdIndexOutOfBounds = -100003
    sceInvalidAnalysisType = -100004
    sceCombinationTypeNotValidForCurrentNationalDesignCode = -100005
    sceInvalidCombinationOfLoadCaseAndLoadLevel = -100006
    sceInvalidCombinationOfLoadCombinationAndLoadLevel = -100007


class EAxisVMPlatform(Enum):
    avmp32 = 0
    avmp64 = 1


class EDisplayedEnvelopes(Enum):
    de_Current = 0
    de_Custom = 1
    de_All = 2


class EStaticUnitType(Enum):
    sut_Displacement = 0
    sut_Rotation = 1
    sut_Force = 2
    sut_Moment = 3
    sut_DistrForce = 4
    sut_DistrMoment = 5
    sut_DistrSurfaceForce = 6
    sut_Stress = 7


class ELoadGroupType(Enum):
    lgtPermanent = 0
    lgtIncidental = 1
    lgtExceptional = 2
    lgtSeismic = 3
    lgtPrestress = 4
    lgtMoving = 5
    lgtImperfection = 6
    lgtSnow = 7
    lgtSnowExcept = 8
    lgtWind = 9
    lgtManualSeismic = 10
    lgtManualPreStress = 11
    lgtFire = 12


class ESurfaceDomainDistributionType(Enum):
    sddtSurface = 0
    sddtProjected = 1


class ELoadsError(Enum):
    leInvalidLineType = -100001
    leErrorAddingLoad = -100002
    leErrorSettingLoad = -100003
    leInvalidLoadType = -100004
    leNotValidLineTypeForThisLoad = -100005
    leErrorSettingLines = -100006
    leErrorSettingPoly = -100007
    leLoadCaseIndexOutOfBounds = -100008
    leErrorSettingLoadCaseId = -100009
    leDomainIndexOutOfBounds = -100010
    leMemberIndexOutOfBounds = -100011
    leThereAreNoSeismicStoreys = -100012
    loeNotDynamicLoadCase = -100013
    loeReferenceIndexOutOfBounds = -100014
    loeErrorCreatingPushOverLoads = -100015
    loeInvalidLoadCaseType = -100016
    loeInvalidRoofType = -100017
    loeLoadPanelIndexlListEmpty = -100018
    loeNoPushOverLoadCase = -100019
    loeSE1moduleNotAvailable = -100020
    loeSE2moduleNotAvailable = -100021
    loeDYNmoduleNotAvailable = -100022
    loeSWGmoduleNotAvailable = -100023
    loeNoSnowLoadCase = -100024
    loeNoWindLoadCase = -100025
    loeNoSeismicLoadCase = -100026
    loePointIsOutOfLoadPanel = -100027
    loeZeroLoadValueOnLoadPanel = -100028
    loeDerivedSurfaceLoadsNotConverted = -100029
    loeLoadComponentMustBeZero = -100030
    loeInvalidLoad = -100031
    loeNoMassLoadOnNode = -100032


class ESpringParError(Enum):
    speNLEInconsistency = -100001
    speNegativeValueMustBePositive = -100002
    speNLPInconsistency = -100003
    speWFOutOfRange = -100004


class ERCDesignUnitType(Enum):
    rcdut_RebarDia = 0
    rcdut_RebarDistance = 1
    rcdut_ReinfArea = 2
    rcdut_ShearReinfArea = 3
    rcdut_Cracking = 4
    rcdut_Eccentricity = 5


class ESeismicLimitState(Enum):
    selsOther = 0
    selsOperational = 1
    selsDamage = 2
    selsLifeSafety = 3
    selsCollapse = 4


class ESurfaceCheck(Enum):
    sch_CanBeChecked = 0
    sch_CanNotBeChecked = 1
    sch_ManipulatedAfterwards = 2


class ECrackWidthsError(Enum):
    cweCOMError = -100001
    cweLoadCaseIdIndexOutOfBounds = -100002
    cweLoadCombinationIdIndexOutOfBounds = -100003
    cweInvalidAnalysisType = -100004
    cweCombinationTypeNotValidForCurrentNationalDesignCode = -100005
    cweInvalidCombinationOfLoadCaseAndLoadLevel = -100006
    cweInvalidCombinationOfLoadCombinationAndLoadLevel = -100007


class ESubsoilClass(Enum):
    scA_Type1 = 1
    scB_Type1 = 2
    scC_Type1 = 3
    scD_Type1 = 4
    scE_Type1 = 5
    scA_Type2 = 6
    scB_Type2 = 7
    scC_Type2 = 8
    scD_Type2 = 9
    scE_Type2 = 10


class ETopographicCategory(Enum):
    tcT1 = 1
    tcT2 = 2
    tcT3 = 3
    tcT4 = 4


class EGroupCombinationType(Enum):
    gctOld = 0
    gctExclusive = 1
    gctAdditive = 2


class EDisplacement(Enum):
    d_eX = 1
    d_eY = 2
    d_eZ = 3
    d_fX = 4
    d_fY = 5
    d_fZ = 6
    d_eR = 7
    d_fR = 8


class EDimensioningUnitType(Enum):
    dut_Dim_Distance = 0
    dut_Dim_Angle = 1
    dut_Level_symobol = 2
    dut_Graphics_size = 3


class ESteelDesignUnitType(Enum):
    sdut_Buckling_factor = 0
    sdut_Check_components = 1


class ETimberDesignUnitType(Enum):
    tdut_Check_components = 0


class ECrackWidth(Enum):
    cwBottom = 0
    cwTop = 1


class EStructuralGridVisibility(Enum):
    sgvDefault = 0
    sgvVisibleAtAllStories = 1
    sgvOnlyIfActive = 2


class ETimberDesignMemberError(Enum):
    tdmeLineListIsEmpty = -100001
    tdmeNotConnectingLines = -100002
    tdmeInvalidNationalDesignCode = -100003


class EVerticalDisplacement(Enum):
    vd_w1 = 1
    vd_w2 = 2
    vd_w3 = 3
    vd_wtot = 4
    vd_wbij = 5


class ENL_ConsequenceClass(Enum):
    nlcc_Invalid = 0
    nlcc_CC1 = 1
    nlcc_CC2 = 2
    nlcc_CC3 = 3


class EFunctionsError(Enum):
    fuePointIndexOutOfBounds = -100001
    fueFailedToModifyFunction = -100002
    fueFileExists = -100003
    fueFailedToAddFromFile = -100004
    fueNameAlreadyExists = -100005
    fueInvalidFunction = -100006


class ELine2dPointIndex(Enum):
    piStart = 0
    piEnd = 1


class EStructuralGridLabelType(Enum):
    sgltLetters = 0
    sgltNumbers = 1


class EVerticalDisplacementsError(Enum):
    vdeNoNonlinearResults = 100001
    vdeNoVerticalDisplacements = 100002


class ELoadGroupsError(Enum):
    lgePropertyNotValidForThisType = -100001
    lgeNameExists = -100002
    lgeInvalidType = -100003


class EWindowState(Enum):
    wsMaximized = 0
    wsMinimized = 1
    wsNormal = 2


class ESelectMode(Enum):
    smSelect = 0
    smDeselect = 1
    smInvert = 2


class EArchitecturalLineElementType(Enum):
    aletColumn = 0
    aletBeam = 1
    aletDiagonal = 2


class EDomainElementType(Enum):
    detMembrane = 0
    detPlate = 1
    detShell = 2


class EArchitecturalDomainElementType(Enum):
    adetWall = 0
    adetSlab = 1
    adetRamp = 2


class ELineSupportsError(Enum):
    lseSectionIdOutOfBounds = -100001
    lsePadFootingNotDefined = -100002
    lseMaterialIndexOutOfBounds = -100003


class ESurfacesError(Enum):
    seLineCountCanBeOnly3Or4 = -100001
    seCannotModify = -100002
    seCOMError = -100003
    seReinforcementParametersNotExists = -100004
    seConcreteIdIndexOutOfBounds = -100005
    seRebarSteelGradeIdIndexOutOfBounds = -100006
    seThicknessMustBePositive = -100007
    seRebarPosMustBePositive = -100008
    sePhiMustBePositiveOrZero = -100009
    seNuMustBePositiveOrZero = -100010
    seTauaMustBePositiveOrZero = -100011
    seAggregateSizeMustBePositive = -100012
    sePropertyNotValidForThisSurfaceType = -100013
    sefseMustBePositive = -100014
    seParametersRecordNotValidForUsedDesignCode = -100015
    seConcreteCoverMustBePositive = -100016
    seRebarDiameterMustBePositive = -100017
    seEnvironmentClassNotValidForUsedDesignCode = -100018
    seAlphaVRdmaxIsInvalid = -100019
    seThetaVRdmaxIsInvalid = -100020
    seShrinkageEpsMustBePositive = -100021
    seRCNonlinearSurfTypeIsInvalid = -100022
    seAlphaAngleIsInvalid = -100023
    seBetaAngleIsInvalid = -100024
    se_k_torsionIsInvalid = -100025
    se_k_shearIsInvalid = -100026
    se_k_bendingIsInvalid = -100027
    seLimitingCrackWidthIsInvalid = -100028
    seMaterialIndex = -100029
    seSurfaceReferenceIndexOutOfBounds = -100030
    seInvalidType = -100031
    seElasticFoundationNegative = -100032
    seInvalidCharacteristics = -100033
    seInvalidStiffnessReduction = -100034
    seStiffnessReductionNotAllowed = -100035
    seInvalidStiffnessReductionMat = -100036
    seInvalidReinfParamForTrapezoidal = -100037


class EForcesError(Enum):
    feLineIndexOutOfBounds = -100001
    feLoadCaseIndexOutofBounds = -100002
    feLoadCombinationIndexOutofBounds = -100003
    feNotValidLineType = -100004
    feSectionIndexOutOfBounds = -100005
    feCombinationTypeNotValidForCurrentNationalDesignCode = -100006
    feCOMError = -100007
    feLineHasNoSections = -100008
    feNoValidLinesInTheModel = -100009
    feSurfaceIndexOutOfBounds = -100010
    feInvalidSurfaceVertexType = -100011
    feInvalidAnalysisType = -100012
    feInvalidCombinationOfLoadCaseAndLoadLevel = -100013
    feInvalidCombinationOfLoadCombinationAndLoadLevel = -100014
    feNoResultBlocksInTheModel = -100015
    feNodeIndexOutOfBounds = -100016
    feNoSurfacesInTheModel = -100017
    feNodalSupportIndexOutOfBounds = -100018
    feLineSupportIndexOutOfBounds = -100019
    feNoNodalSupportsInTheModel = -100020
    feNoLineSupportsInTheModel = -100021
    feSurfaceSupportIndexOutOfBounds = -100022
    feNoSurfaceSupportsInTheModel = -100023
    feInvalidLineType = -100024
    feNoSpringsInTheModel = -100025
    feNoGapsInTheModel = -100026
    feEdgeConnectionIndexOutOfBounds = -100027
    feNoEdgeConnectionsInTheModel = -100028
    feLinkElementIndexOutOfBounds = -100029
    feNoLinkElementsInTheModel = -100030
    feMemberIndexOutOfBounds = -100031
    feInvalidEnvelopeUID = -100032
    feZeroValidLineNumber = -100033
    feVirtualBeamIndexOutOfBounds = -100034
    feVirtualBeamChainIndexOutOfBounds = -100035
    feVirtualBeamSectionIndexOutOfBounds = -100036
    feWindowIdNotValid = -100037
    feMembersSupportIndexOutOfBounds = -100038


class EMainFormTab(Enum):
    mftGeometry = 0
    mftElements = 1
    mftLoads = 2
    mftMesh = 3
    mftStatic = 4
    mftVibration = 5
    mftDynamic = 6
    mftBuckling = 7
    mftRCDesign = 8
    mftSteelDesign = 9
    mftTimberDesign = 10


class EApplicationClose(Enum):
    acEnableShowWarning = 0
    acEnableNoWarning = 1
    acDisable = 2


class EClientAliveTest(Enum):
    catNone = 0
    catShowWarning = 1
    catExitApplication = 2


class EActualReinforcementType(Enum):
    artDomain = 0
    artPolygon = 1


class ESurfaceVertexIndex(Enum):
    sviCenterPoint = 0
    sviContourPoint1 = 1
    sviContourPoint2 = 2
    sviContourPoint3 = 3
    sviContourPoint4 = 4
    sviContourLineMidPoint1 = 5
    sviContourLineMidPoint2 = 6
    sviContourLineMidPoint3 = 7
    sviContourLineMidPoint4 = 8


class EDomainsError(Enum):
    deEmptyContour = -100001
    deMoreThanOneCountourFound = -100002
    deEmptyHole = -100003
    deMoreThanOneHoleFound = -100004
    doeCOMError = -100005
    deConcreteIdIndexOutOfBounds = -100006
    deRebarSteelGradeIdIndexOutOfBounds = -100007
    deThicknessMustBePositive = -100008
    deRebarPosMustBePositive = -100009
    dePhiMustBePositiveOrZero = -100010
    deNuMustBePositiveOrZero = -100011
    deTauaMustBePositiveOrZero = -100012
    deAggregateSizeMustBePositive = -100013
    deStoreyIdOutOfBounds = -100014
    deReinforcementParametersNotExists = -100015
    deHoleNotInDomainPlane = -100016
    dePropertyNotValidForThisDomainSurfaceType = -100017
    defseMustBePositive = -100018
    deParametersRecordNotValidForUsedDesignCode = -100019
    deConcreteCoverMustBePositive = -100020
    deRebarDiameterMustBePositive = -100021
    deInvalidGroupID = -100022
    deXLMmoduleNotAvailable = -100023
    deEnvironmentClassNotValidForUsedDesignCode = -100024
    deDomainIsNotMeshed = -100025
    deAlphaVRdmaxIsInvalid = -100026
    deThetaVRdmaxIsInvalid = -100027
    deShrinkageEpsMustBePositive = -100028
    deRCNonlinearSurfTypeIsInvalid = -100029
    deAlphaAngleIsInvalid = -100030
    deBetaAngleIsInvalid = -100031
    de_k_torsionIsInvalid = -100032
    de_k_shearIsInvalid = -100033
    de_k_bendingIsInvalid = -100034
    deCustomStiffnessMatrixUndefined = -100035
    deCustomStiffnessMatrixNonSymetric = -100036
    deCustomStiffnessMatrixNonPositiveDefine = -100037
    deLimitingCrackWidthIsInvalid = -100038
    dePolyLineIsNotContinuous = -100039
    deLineDoesNotReachDomainEdge = -100040
    deNoSelectedLine = -100041
    deNoSelectedLineAndDomain = -100042
    deMaterialIndex = -100043
    deReferenceIndexOutOfBounds = -100044
    deDomainInvalidType = -100045
    deElasticFoundationNegative = -100046
    deInvalidCharacteristics = -100047
    deInvalidStiffnessReduction = -100048
    deStiffnessReductionNotAllowed = -100049
    deInvalidStiffnessReductionMat = -100050
    deInvalidReinfParamForTrapezoidal = -100051
    deInvalidHollowCoreDirection = -100052
    deInvalidHollowCoreHoletype = -100053
    deHollowCoreDMustBePositive = -100054
    deHollowCoreFiMustBePositive = -100055
    deHollowCoreBMustBePositive = -100056
    deHollowCoreHMustBePositive = -100057
    deTrapezoidalInvalidDirection = -100058
    deTrapezoidalInvalidMaterial = -100059
    deTrapezoidal_h_MustBePositive = -100060
    deTrapezoidal_t_MustBePositive = -100061
    deTrapezoidal_v_MustBePositive = -100062
    deTrapezoidal_d_MustBePositive = -100063
    deTrapezoidal_b_MustBePositive = -100064
    deTrapezoidal_w_MustBePositive = -100065
    deTrapezoidal_p_MustNotBeNegative = -100066
    deTrapezoidal_eta_OutOfRange = -100067
    deTrapezoidal_ht_Mismatch = -100068
    deTrapezoidal_dbw_Mismatch = -100069
    deCompositeRibInvalidMaterial = -100070
    deCompositeRibInvalidCrossSection = -100071
    deCompositeRibInvalidDirection = -100072
    deCompositeRib_d_TooSmall = -100073
    deCompositeRibInvalidEccType = -100074
    deNotARibbedDomain = -100075


class EXLAMTopLayerDirection(Enum):
    xtldLocalX = 0
    xtldLocalY = 1


class EXLAMServiceClass(Enum):
    xlscClass1 = 1
    xlscClass2 = 2


class ELine2dType(Enum):
    ltStraightLine = 0
    ltCircleArc = 1


class ELoadDomainPolyLineItemType(Enum):
    ldplitDomain = 0
    ldplitSurface = 1
    ldplitBlankLine = 2
    ldplitLoadPanel = 3


class ECombinationTypeBits(Enum):
    ctb_Other = 0
    ctb_SLS1 = 1
    ctb_SLSChar = 1
    ctb_SLS2 = 2
    ctb_SLSFreq = 2
    ctb_SLS3 = 4
    ctb_SLSQuasi = 4
    ctb_ULS1 = 8
    ctb_ULS = 8
    ctb_ULS2 = 16
    ctb_ULSSeismic = 16
    ctb_ULS3 = 32
    ctb_ULSExceptional = 32
    ctb_ULSALL = 64
    ctb_ULSab = 128
    ctb_ULSa = 256
    ctb_ULSb = 512
    ctb_ULSALLab = 1024
    ctb_ULSA1 = 2048
    ctb_ULSA2 = 4096
    ctb_ULSA3 = 8192
    ctb_ULSA4 = 16384
    ctb_ULSA5 = 32768
    ctb_ULSA6 = 65536
    ctb_ULSA7 = 131072
    ctb_ULSA8 = 262144
    ctb_ULSAllSE1 = 524288
    ctb_ULSAllSE2 = 1048576
    ctb_ULSAllSE3 = 2097152
    ctb_ULSAllSE4 = 4194304
    ctb_ULSAllSE5 = 8388608
    ctb_ULSAllSE6 = 16777216
    ctb_ULSAllSE7 = 33554432
    ctb_ULSAllSE8 = 67108864


class ESurfaceStress(Enum):
    ssSxx = 0
    ssSyy = 1
    ssSxy = 2
    ssSxz = 3
    ssSyz = 4
    ssSVM = 5
    ssS1 = 6
    ssS2 = 7
    ssAs = 8


class ELayerPenStyle(Enum):
    lpsSolid = 0
    lpsDash = 1
    lpsDot = 2
    lpsDashDot = 3
    lpsDashDotDot = 4


class ELayerShapeType(Enum):
    lst3DLine = 0
    lst3DPolygon = 1
    lst3DPolygonFilled = 2


class ELayerType(Enum):
    ltAxisVM = 0
    ltDXF = 1
    ltPDF = 2


class ETextHorizontalAlignment(Enum):
    thaLeft = 0
    thaCenter = 1
    thaRight = 2
    thaAligned = 3
    thaMiddle = 4
    thaFit = 5


class ETextVerticalAlignment(Enum):
    tvaBaseline = 0
    tvaBottom = 1
    tvaCenter = 2
    tvaTop = 3


class EMomentDiagramType(Enum):
    mdtOnTensionSide = 0
    mdtOnCompressionSide = 1


class EEnvelopeGroup(Enum):
    egDefault = 0
    egLoadCases = 1
    egLoadCombinations = 2
    egULS_ALL = 3
    egULS = 4
    egULSSeismic = 5
    egULSExceptional = 6
    egULSab = 7
    egSLS_ALL = 8
    egSLSCharacteristic = 9
    egSLSFrequent = 10
    egSLSQuasipermanent = 11
    egCustomCombinations = 12
    egGeo = 13
    egGeoULS_A1 = 14
    egGeoULS_A2 = 15
    egGeoULSab_A1 = 16
    egGeoULSab_A2 = 17


class ETempFolderType(Enum):
    tftModel = 0
    tftSystem = 1
    tftCustom = 2


class ELoadCaseType(Enum):
    lctStandard = 0
    lctInfluenceLine = 1
    lctSeismic = 2
    lctVibration = 3
    lctPreStress = 4
    lctMoving = 5
    lctDynamic = 6
    lctPushOver = 7
    lctImperfection = 8
    lctSnow = 9
    lctSnowExcept = 10
    lctWind = 11
    lctManualSeismic = 12
    lctManualPreStress = 13
    lctFire = 14
    lctLocalImperfection = 15


class ELoadDurationClass(Enum):
    ldcOther = 0
    ldcPermanent = 1
    ldcLong = 2
    ldcMedium = 3
    ldcShort = 4
    ldcInstant = 5


class EStressesError(Enum):
    steLineIndexOutOfBounds = -100001
    steLoadCaseIndexOutofBounds = -100002
    steLoadCombinationIndexOutofBounds = -100003
    steNotValidLineType = -100004
    steSectionIndexOutOfBounds = -100005
    steCombinationTypeNotValidForCurrentNationalDesignCode = -100006
    steCOMError = -100007
    steLineHasNoSections = -100008
    steNoValidLinesInTheModel = -100009
    steLineStressComponentNotValidForThisLineType = -100010
    steInvalidAnalysisType = -100011
    steInvalidCombinationOfLoadCaseAndLoadLevel = -100012
    steInvalidCombinationOfLoadCombinationAndLoadLevel = -100013
    steNoResultBlocksInTheModel = -100014
    steNodeIndexOutOfBounds = -100015
    steSurfaceIndexOutOfBounds = -100016
    steNoSurfacesInTheModel = -100017
    steMemberIndexOutOfBounds = -100018
    steReadXLAMSurfaceStresses = -100019
    steInvalidSurfaceVertexType = -100020
    steReadSurfaceStresses = -100021
    steNotXLAMpanel = -100022
    steXLAMmoduleNotAvailable = -100023
    steStressPointIDOutOfBounds = -100024


class EDimensionsError(Enum):
    deInvalidText = -100001
    deInvalidType = -100002
    deInvalidMarkType = -100003
    deInvalidLayerID = -100004
    deInvalidNodeID = -100005


class EBackgroundColour(Enum):
    bcWhite = 0
    bcBlack = 1
    bcLightGrey = 2
    bcDarkGrey = 3


class EDimensionType(Enum):
    dtOrtho = 0
    dtAligned = 1
    dtAngle = 2
    dtArcLength = 3
    dtCoordinate = 4
    dtLevel = 5
    dtElevation = 6
    dtTextBox = 7
    dtNodeAssoc = 8
    dtLineAssoc = 9
    dtDomainAssoc = 10
    dtLineIntegrated = 11
    dtLowLevel = 12
    dtIsoLabel = 13
    dtNone = 14
    dtInfoHint = 15
    dtRadius = 16


class ECapacityCurveType(Enum):
    cctImportantCharacteristics = 0
    cctMDOF = 1
    cctSDOF = 2
    cctEquivalentBilinear = 3
    cctElasticADRS = 4
    cctInelasticADRS = 5
    cctBilinearAD = 6
    cctSDOFinADSpace = 7
    cctInitialPeriod = 8


class ESupportError(Enum):
    seNodeIndexOutOfBounds = -100001
    seLineIndexOutOfBounds = -100002
    seReferenceIndexOutOfBounds = -100003
    seIncompatibleReferences = -100004


class EPartControl(Enum):
    pcDeleteParts = 0
    pcMoveToUpperFolder = 1
    pcMoveToRootFolder = 2


class EXLAMSurfaceStress(Enum):
    xssSxx_m_T = 0
    xssSyy_m_T = 1
    xssSxx_m_B = 2
    xssSyy_m_B = 3
    xssSxx_n = 4
    xssSyy_n = 5
    xssSxy_max = 6
    xssSxz_max = 7
    xssSrx_max = 8
    xssSry_max = 9


class ESeismicCombType(Enum):
    sctQuadratic = 0
    sctMax = 1
    sctAuto = 2


class EModalCombType(Enum):
    mctAuto = 0
    mctSRSS = 1
    mctCQC = 2


class ELineStress(Enum):
    lsSmin = 0
    lsSmax = 1
    lsVmin = 2
    lsVmax = 3
    lsSomin = 4
    lsSomax = 5
    lsVymean = 6
    lsVzmean = 7


class ESurfaceStressPosition(Enum):
    sspTop = 0
    sspMiddle = 1
    sspBottom = 2


class ESectionSegmentChainIntegratedResultant(Enum):
    sscir_N = 0
    sscir_Q = 1
    sscir_M = 2


class EWindowsError(Enum):
    weLoadCaseIdOutOfBounds = -100001
    weLoadCombinationIdOutOfBounds = -100002
    weEnvelopeIdOutOfBounds = -100003


class EVibrationType(Enum):
    vtFirstOrder = 0
    vtSecondOrder = 1


class EActualReinforcementError(Enum):
    areCOMError = -100001
    areDomainIdOutOfBounds = -100002
    areErrorAddingPolygonReinforcement = -100003
    areDomainReinforcementNotFound = -100004
    areSurfaceIdOutOfBounds = -100005
    areSurfaceVertexIndexOutOfBounds = -100006
    areDiameterIsInvalid = -100007
    areSpacingIsInvalid = -100008
    areCoverIsInvalid = -100009
    areReinfParamMissing = -100010


class EVelocityError(Enum):
    veeLoadCaseIdIndexOutOfBounds = -100001
    veeInvalidCombinationOfLoadCaseAndTimeStep = -100002
    veeInvalidAnalysisType = -100003
    veeLoadCombinationHasNoDynamicResult = -100004


class ESteelDesignMemberError(Enum):
    sdmeCOMError = -100001
    sdmeLineListIsEmpty = -100002
    sdmeInvalidNationalDesignCode = -100003
    sdmeNotConnectingLines = -100004
    sdmeDesignParametersNotValidForUsedDesignCode = -100005


class ESteelDesignResultsError(Enum):
    sdreCOMError = -100001
    sdreLoadCaseIdIndexOutOfBounds = -100002
    sdreLoadCombinationIdIndexOutOfBounds = -100003
    sdreInvalidAnalysisType = -100004
    sdreCombinationTypeNotValidForCurrentNationalDesignCode = -100005


class ETaskError(Enum):
    teCanNotStartTask = -100001
    teCanNotChangeMainTab = -100002


class EXLAMSurfaceEfficiency(Enum):
    xse_M_N_0 = 0
    xse_M_N_90 = 1
    xse_V_T = 2
    xse_Vr_N = 3
    xse_Max = 4


class EaxsImportCustomParts(Enum):
    aicpToActiveCustomParts = 0
    aicpPreserveNames = 1
    aicpNoCustomParts = 2


class EModelError(Enum):
    meCannotExport = -100001
    meNoSeismicParams = -100002
    meErrorSettingSeismicParams = -100003
    meLoadCaseLoadCombinationNotFound = -100004
    mePianoCanNotUpdate = -100005
    mePianoCanNotFindFile = -100006
    mePianoInternalException = -100007
    meRCBeamDesignDisabled = -100008
    meRCColumnCheckingDisabled = -100009
    meSteelDesignMembersDisabled = -100010
    meActualReinforcementDisabled = -100011
    meIFCmoduleNotAvailable = -100012
    meDXFmoduleNotAvailable = -100013
    meSE1moduleNotAvailable = -100014
    meTD1moduleNotAvailable = -100015
    meSWGmoduleNotAvailable = -100016
    meSE2moduleNotAvailable = -100017
    meDYNmoduleNotAvailable = -100018
    meCannotSaveGlobalData = -100019
    meCannotReadGlobalData = -100020
    meInvalidDataName = -100021
    meInvalidOrEmptyGlobalData = -100022
    meGlobalDataNotFound = -100023
    meDataNameAlreadyExists = -100024
    meFileNotExists = -100025
    mePDFmoduleNotAvailable = -100026
    meReinforcementForExportNotAvailable = -100027
    mePDFimportCannotReadAllObjects = -100028
    mePDFimportNoEOF = -100029
    mePDFimportNoGraphicElements = -100030
    mePDFimportFailure = -100031
    mePDFimportErrorInCompressedData = -100032
    mePDFimportObjectMissing = -100033
    mePDFimportUnknownCompression = -100034
    mePDFimportStreamDataNotFound = -100035
    mePDFimportStreamLengthNotFound = -100036
    mePDFimportNoGraphicElementsOnPage = -100037
    mePDFimportPageNotFound = -100038
    mePDFimportUnknownLinearization = -100039
    mePDFimportReferenceStreamParsingError = -100040
    mePDFimportUnknownEmbeddedObject = -100041
    mePDFimportReferenceTableParsingError = -100042
    mePDFimportUnknownError = -100043
    mePDFimportFileGlyphlistNotFound = -100044
    mePDFimportPDFfileIsEncrypted = -100045
    mePDFimportPagesCannotBeFound = -100046
    meIFCInvalidDeviationOrByAngle = -100047
    meIFCNoStaticData = -100048
    meIFCVersionNotFound = -100049
    meIFCOtherError = -100050
    meIFCMaxDeviationAndByAngleIsZero = -100051
    meSD9moduleNotAvailable = -100052
    meTD9moduleNotAvailable = -100053
    meRevitModuleNotAvailable = -100054
    meRevitImportTessDegreeOutOfRange = -100055


class ELoadCasesError(Enum):
    lcaePropertyNotValidForThisType = -100001
    lcaeNameExists = -100002
    lcaeErrorCreatingStandardSeismicCases = -100003
    lcaeGroupIdOutOfBounds = -100004
    lcaeErrorCreatingPushOverCases = -100005
    lcaeInvalidAnalysisTypeDirX = -100006
    lcaeLoadCaseIndexOutOfBoundsDirX = -100007
    lcaeVibrationModeIndexOfOutBoundsDirX = -100008
    lcaeInvalidAnalysisTypeDirY = -100009
    lcaeLoadCaseIndexOutOfBoundsDirY = -100010
    lcaeVibrationModeIndexOfOutBoundsDirY = -100011
    lcaeErrorCreatingPreStressCases = -100012
    lcaeNoPushOverCases = -100013
    lcaeInvalidLoadCaseType = -100014
    lcaeNoModeShapesForLoadCaseInDirectionX = -100015
    lcaeNoModeShapesForLoadCaseInDirectionY = -100016
    lcaeNoModeShapesInDirectionX = -100017
    lcaeNoModeShapesInDirectionY = -100018
    lcaeInvalidLoadGroupType = -100019
    lcaeSWGmoduleNotAvailable = -100020
    lcaeNoSnowLoadCases = -100021
    lcaeNoWindLoadCases = -100022
    lcaeInvalidName = -100023
    lcaeNoSeismicLoadCases = -100024
    lcaeSE1moduleNotAvailable = -100025
    lcaeErrorSetingSeismicParams = -100026
    lcaeLoadCaseLoadCombinationNotFound = -100027
    lcaeErrorTooManySeismicGroups = -100003
    lcaeSeismicInvalidGroupID = -100028


class ELoadPanelsError(Enum):
    lopeInvalidContourParams = -100001
    lopeLineIndexlListEmpty = -100002
    lopeLineIndexOutOfBounds = -100003
    lopeInvalidContour = -100004
    lopeSameLoadPanelExists = -100005
    lopeMemberIndexlListEmpty = -100006
    lopeMemberIndexOutOfBounds = -100007
    lopeInvalidContourType = -100008
    lopeNodeIndexlListEmpty = -100009
    lopeDomainIndexlListEmpty = -1000010


class EAccelerationError(Enum):
    aeLoadCaseIdIndexOutOfBounds = -100001
    aeInvalidCombinationOfLoadCaseAndTimeStep = -100002
    aeInvalidAnalysisType = -100003
    aeLoadCombinationHasNoDynamicResult = -100004


class EPadFootingType2(Enum):
    pft_NodeRectangular = 0
    pft_NodeCircular = 1
    pft_Linear = 2


class ECalculatedReinforcementError(Enum):
    creCOMError = -100001
    creLoadCaseIdIndexOutOfBounds = -100002
    creLoadCombinationIdIndexOutOfBounds = -100003
    creInvalidAnalysisType = -100004
    creCombinationTypeNotValidForCurrentNationalDesignCode = -100005
    creInvalidCombinationOfLoadCaseAndLoadLevel = -100006
    creInvalidCombinationOfLoadCombinationAndLoadLevel = -100007


class ESpectrumError(Enum):
    seLoadingFailed = -100001
    seSavingFailed = -100002
    seSpectrumDataNotAvailable = -100003
    seSpectrumDataNotParametric = -100004
    seInvalidNationalDesignCode = -100005
    seFunctionPointsEmpty = -100006
    seSpectrumNotValid = -100007
    seNonParametricSpectrumIsNotAllowed = -100008


class ERigidBodiesError(Enum):
    rbeLineListIsEmpty = -100001
    rbeNoLinesAreSelected = -100002
    rbeLineIndexOutOfBounds = -100003


class ENodesSupportsError(Enum):
    nsePropertyNotValidForThisType = -100001
    nseNodeIndexOutOfBounds = -100002
    nseMemberIndexOutOfBounds = -100003
    nseReferenceIndexOutOfBounds = -100004
    nseInvalidType = -100005
    nsePadFootingNotDefined = -100006
    nseInvalidMemberAndNodeCombination = -100007
    nseStiffnessCalcParamsNotDefined = -100008
    nseMaterialIndexOutOfBounds = -100009
    nseCrossSectionIndexOutOfBounds = -100010


class ECalculationError(Enum):
    ceSE2moduleNotAvailable = -100001
    ceNLpackageNotAvailable = -100002
    ceDYNmoduleNotAvailable = -100003
    ceStoryIDOutOfBounds = -100004


class EDiaphragmError(Enum):
    dpheLineListIsEmpty = -100001
    dpheNoLinesAreSelected = -100002
    dpheLineIndexOutOfBounds = -100003
    dpheIllegalDOFValue = -100004


class EColour(Enum):
    cColourByMaterial = -1


class EGravityDirection(Enum):
    gdXp = 0
    gdYp = 1
    gdZp = 2
    gdXm = 3
    gdYm = 4
    gdZm = 5


class EStructuralGridsError(Enum):
    sgeInvalidName = -100001
    sgeInvalidWorkPlaneindex = -100002
    sgeInvalidStoreyIndex = -100003
    sgwInvalidStartCharX = -100004
    sgwInvalidStartCharY = -100005
    sqwNormalVectorVaries = -100006
    sqwGridLineNotInPlane = -100007


class ECrossSectionOptimizationError(Enum):
    csoGroupNameAlreadyExists = -100001
    csoGroupIsForPredefinedShapes = -100002
    csoGroupIsForParametricOptimization = -100003
    csoOptimizationChecksNotValid = -100004
    csoGroupNameInvalid = -100005
    csoMemberDesignIDsEmpty = -100006
    csoVariousCrossSectionsAreNotSupported = -100007
    csoCrossSectionTypeIsNotSupported = -100008
    csoUsedMaterialIsNotSupported = -100009
    csoInvalid_b = -100010
    csoInvalid_h = -100011
    csoInvalid_tw = -100012
    csoInvalid_tf = -100013
    csoInvalid_b2 = -100014
    csoInvalid_tf2 = -100015
    csoInvalid_a = -100016
    csoInvalidManufacturingProcess = -100017
    csoDesignMemberIDOutOfBounds = -100018
    csoGroupCrossSectionTypeIsDifferent = -100019
    csoOptimizationCheckCombinationIsNotValid = -100020
    csoGroupCrossSectionIndexOutOfBounds = -100021
    csoOutOfConstraintLimits = -100022
    csoMaterialVariesInTheGroup = -100023
    csoCrossSectionVariesInTheGroup = -100024
    csoManufacturingProcessIsNotSupported = -100025
    csoCrossSectionsInTheGroupAreNotUsable = -100026
    csoLoadCaseIdIndexOutOfBounds = -100027
    csoLoadCombinationIdIndexOutOfBounds = -100028
    csoInvalidAnalysisType = -100029
    csoCombinationTypeNotValidForCurrentNationalDesignCode = -100030
    csoInvalidMaterial = -100031
    csoInvalisOptimizationType = -100032
    csoNoneOfTheCrossSectionsIsValid = -100033


class ELogicalPartsError(Enum):
    lpeMaterialIdOutOfBounds = -100001
    lpeCrossSectionIdOutOfBounds = -100002
    lpeInvalidLineType = -100003
    lpeNotFound = -100004
    lpeStoreyIdOutOfBounds = -100005
    lpeStructuralGridLineUIDOutOfBounds = -100006


class ECrossSectionBasicType(Enum):
    csbtAll = 0
    csbtSolid = 1
    csbtThinWalled = 2
    csbtCompositeThinWalled = 4
    csbtCompositeSolid = 8


class EApplicationError(Enum):
    appeUnknownUnitSystem = -100001


class EMembersError(Enum):
    mbeEmptyLineList = -100001
    mbePropertyNotValidForThisLineType = -100002
    mbeNotBeam = -100003
    mbeNotRib = -100004
    mbeIllegalServiceClassValue = -100005
    mbeDomainIndexOutOfBounds = -100006
    mbeStoreyIdOutOfBounds = -100007
    mbeMustBeBeamOrRibOrTuss = -100008
    mbeInvalidMemberType = -100009
    mbeReinforcementParametersNotExsist = -100010
    mbeInvalidColumnRebarsId = -100011
    mbeInvalidConcreteMaterialId = -100012
    mbeInvalidRebarSteelGradeId = -100013
    mbeNotTruss = -100014
    mbeInvalidRelease = -100015
    mbeInvalidFunctionIDofRelease = -100016
    mbeReleaseInitAndLimitMustBe0 = -100017
    mbeFunctionIdMustBe0 = -100018
    mbeMembersNotContinuous = -100019
    mbeStartEndCrossSectionTypeIncompatible = -100020
    mbeInvalidRCCheckingParameters = -100021
    mbeRCShrinkageEpsMustBePositive = -100022
    mbeStirrupParametersAreInvalid = -100023
    mbeShearCrackAngleIsInvalid = -100024
    mbeInvalidSteelMaterialId = -100025
    mbeInvalidStiffnessReduction = -100026
    mbeStiffnessReductionNotAllowed = -100027
    mbeInvalidStiffnessReductionMat = -100028
    mbeRibEccTypeUsedOnBeam = -100029
    mbeReleaseFunctionIndexError = -100030
    mbeReleaseInvalidType = -100031
    mbeInvalidRefZ = -100032
    mbeInvalidLineType = -100033
    mbeReleaseInvalidMaterial = -100034
    mbeReleaseInvalidComponent = -100035


class ECrossSectionEditorError(Enum):
    cseeEditorNotOpened = -100001
    cseeEditorModeIsNotSolidCrossSection = -100002


class EEnvelopesError(Enum):
    eeLoadCaseIdOutOfBounds = -100001
    eeLoadCombinationIdOutOfBounds = -100002
    eeErrorAddingEnvelope = -100003
    eeErrorModifyingEnvelope = -100004
    eeNotUserDefinedEnvelope = -100005


class ECalculatioFinishedType(Enum):
    cft_OK = 1
    cft_Canceled = 2
    cft_Warning = 3
    cft_Error = 4


class ESelectionType(Enum):
    seltNode = 1
    seltMidPoint = 2
    seltAllLines = 3
    seltTruss = 4
    seltBeam = 5
    seltRib = 6
    seltSurfaceEdge = 7
    seltRigidBody = 8
    seltDiaphragm = 9
    seltGap = 10
    seltSpring = 11
    seltLink = 12
    seltAllSurfaces = 13
    seltSurfaceMembrane = 14
    seltSurfacePlate = 15
    seltSurfaceShell = 16
    seltAllDomains = 17
    seltDomainMembrane = 18
    seltDomainPlate = 19
    seltDomainShell = 20
    seltHole = 21
    seltAllSupports = 22
    seltNodalSupport = 23
    seltLineSupport = 24
    seltSurfaceSupport = 25
    seltReference = 26
    seltAllLoads = 27
    seltLoadDomainConcentrated = 28
    seltLoadDomainPoly = 29
    seltLoadNodalConcentrated = 30
    seltLoadBeamConcentrated = 31
    seltLoadBeamDistributed = 32
    seltLoadDomainDistributed = 33
    seltLoadDomainFluid = 34
    seltLoadMoving = 35
    seltLoadDynamic = 36
    seltArchColumn = 37
    seltArchBeam = 38
    seltArchWall = 39
    seltArchSlab = 40
    seltArchRamp = 41
    seltLoadPanel = 42
    seltLoadPanelEdge = 43
    seltVirtualBeam = 44
    seltLinesOnly = 45


class ERebarSteelGradesError(Enum):
    rsgeIllegalNationalDesignCode = -100001
    rsgeNonPositive_E = -100002
    rsgeNonPositive_ssh = -100003
    rsgeNonPositive_es0 = -100004
    rsgeNonPositive_esh = -100005
    rsgeNonPositive_fyd = -100006
    rsgeNonPositive_es1 = -100007
    rsgeNonPositive_esu = -100008
    rsgeNonPositive_Ra = -100009
    rsgeNonPositive_mat = -100010
    rsgeNonPositive_fsrep = -100011
    rsgeNonPositive_fs = -100012
    rsgeNonPositive_fyk = -100013
    rsgeNonPositive_Epsuk = -100014
    rsgeNonPositive_GammaS = -100015
    rsgeNonPositive_fsk = -100016
    rsgeNonPositive_ks = -100017
    rsgeNonPositive_Epsud = -100018
    rsgeNotFound = -100019


class ECustomPartsError(Enum):
    cpeErrorRenamingPartFolder = -100001
    cpePartNameAlreadyExists = -100002
    cpeInvalidPath = -100003
