Records
=======

.. py:class:: axisvm.com.tlb.RCrossSectionTable

   :param CrossSectionShape: <class 'ctypes.c_long'>
   :param ProviderID: <class 'ctypes.c_long'>
   :param CrossSectionRegion: <class 'ctypes.c_long'>
   :param Id: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade

   :param NationalDesignCode: <class 'ctypes.c_long'>
   :param E: <class 'ctypes.c_double'>
   :param RebarSteelGrade_EC_ITA: <class 'axisvm.com.core.tlb._16_100.RRebarSteelGrade_EC_ITA'>
   :param RebarSteelGrade_MSZ: <class 'axisvm.com.core.tlb._16_100.RRebarSteelGrade_MSZ'>
   :param RebarSteelGrade_STAS: <class 'axisvm.com.core.tlb._16_100.RRebarSteelGrade_STAS'>
   :param RebarSteelGrade_DIN: <class 'axisvm.com.core.tlb._16_100.RRebarSteelGrade_DIN'>
   :param RebarSteelGrade_SIA: <class 'axisvm.com.core.tlb._16_100.RRebarSteelGrade_SIA'>
   :param RebarSteelGrade_NEN: <class 'axisvm.com.core.tlb._16_100.RRebarSteelGrade_NEN'>

.. py:class:: axisvm.com.tlb.RStiffnesses

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>
   :param xx: <class 'ctypes.c_double'>
   :param yy: <class 'ctypes.c_double'>
   :param zz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNonLinearity

   :param x: <class 'ctypes.c_long'>
   :param y: <class 'ctypes.c_long'>
   :param z: <class 'ctypes.c_long'>
   :param xx: <class 'ctypes.c_long'>
   :param yy: <class 'ctypes.c_long'>
   :param zz: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RResistances

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>
   :param xx: <class 'ctypes.c_double'>
   :param yy: <class 'ctypes.c_double'>
   :param zz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMatrix3x3

   :param e11: <class 'ctypes.c_double'>
   :param e12: <class 'ctypes.c_double'>
   :param e13: <class 'ctypes.c_double'>
   :param e21: <class 'ctypes.c_double'>
   :param e22: <class 'ctypes.c_double'>
   :param e23: <class 'ctypes.c_double'>
   :param e31: <class 'ctypes.c_double'>
   :param e32: <class 'ctypes.c_double'>
   :param e33: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNodalSupportSpringParams

   :param SpringParamIndexes: <class 'axisvm.com.core.tlb._16_100.RSpringParamIndexes'>
   :param IsolatorParamIndex: <class 'ctypes.c_long'>
   :param IsolatorD2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMemberMeshParameters

   :param MeshType: <class 'ctypes.c_long'>
   :param MeshParam: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLineAttr

   :param LineType: <class 'ctypes.c_long'>
   :param MaterialIndex: <class 'ctypes.c_long'>
   :param StartCrossSectionIndex: <class 'ctypes.c_long'>
   :param EndCrossSectionIndex: <class 'ctypes.c_long'>
   :param AutoEccentricityType: <class 'ctypes.c_long'>
   :param StartEccentricity: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param EndEccentricity: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param TrussType: <class 'ctypes.c_long'>
   :param Resistance: <class 'ctypes.c_double'>
   :param ServiceClass: <class 'ctypes.c_long'>
   :param kdef: <class 'ctypes.c_double'>
   :param kx: <class 'ctypes.c_double'>
   :param Domain1: <class 'ctypes.c_long'>
   :param Domain2: <class 'ctypes.c_long'>
   :param GapType: <class 'ctypes.c_long'>
   :param ActiveStiffness: <class 'ctypes.c_double'>
   :param InactiveStiffness: <class 'ctypes.c_double'>
   :param InitialOpening: <class 'ctypes.c_double'>
   :param MinPenetration: <class 'ctypes.c_double'>
   :param MaxPenetration: <class 'ctypes.c_double'>
   :param AdjustmentRatio: <class 'ctypes.c_double'>
   :param SpringDirection: <class 'ctypes.c_long'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>

.. py:class:: axisvm.com.tlb.RPoint3d

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLineAttr_V161

   :param LineType: <class 'ctypes.c_long'>
   :param MaterialIndex: <class 'ctypes.c_long'>
   :param StartCrossSectionIndex: <class 'ctypes.c_long'>
   :param EndCrossSectionIndex: <class 'ctypes.c_long'>
   :param LocalXOrientation: <class 'ctypes.c_long'>
   :param StartRelease: <class 'axisvm.com.core.tlb._16_100.RReleases_V161'>
   :param EndRelease: <class 'axisvm.com.core.tlb._16_100.RReleases_V161'>
   :param Reference: <class 'ctypes.c_long'>
   :param RibAutoEccentricityType: <class 'ctypes.c_long'>
   :param StartEccentricity: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param EndEccentricity: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param StartEccentricityType: <class 'ctypes.c_long'>
   :param EndEccentricityType: <class 'ctypes.c_long'>
   :param StartAlignementPoint: <class 'ctypes.c_long'>
   :param EndAlignementPoint: <class 'ctypes.c_long'>
   :param EccGroupIndex: <class 'ctypes.c_long'>
   :param StartRefLine: <class 'ctypes.c_long'>
   :param EndRefLine: <class 'ctypes.c_long'>
   :param RefStartAlignementPoint: <class 'ctypes.c_long'>
   :param RefEndAlignementPoint: <class 'ctypes.c_long'>
   :param StartEccRelease: <class 'axisvm.com.core.tlb._16_100.REccReleases'>
   :param EndEccRelease: <class 'axisvm.com.core.tlb._16_100.REccReleases'>
   :param TrussType: <class 'ctypes.c_long'>
   :param Resistance: <class 'ctypes.c_double'>
   :param ServiceClass: <class 'ctypes.c_long'>
   :param kdef: <class 'ctypes.c_double'>
   :param kx: <class 'ctypes.c_double'>
   :param Domain1: <class 'ctypes.c_long'>
   :param Domain2: <class 'ctypes.c_long'>
   :param Beam7DOF: <class 'ctypes.c_long'>
   :param MaterialColor: <class 'ctypes.c_long'>
   :param ContourColor: <class 'ctypes.c_long'>
   :param GapType: <class 'ctypes.c_long'>
   :param ActiveStiffness: <class 'ctypes.c_double'>
   :param InactiveStiffness: <class 'ctypes.c_double'>
   :param InitialOpening: <class 'ctypes.c_double'>
   :param MinPenetration: <class 'ctypes.c_double'>
   :param MaxPenetration: <class 'ctypes.c_double'>
   :param AdjustmentRatio: <class 'ctypes.c_double'>
   :param SpringType: <class 'ctypes.c_long'>
   :param SpringCharacteristics: <class 'axisvm.com.core.tlb._16_100.RSpringCharacteristics'>
   :param SeismicIsolatorIndex: <class 'ctypes.c_long'>
   :param IsolatorD2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReleases_V161

   :param x: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>
   :param y: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>
   :param z: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>
   :param xx: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>
   :param yy: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>
   :param zz: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>
   :param ew: <class 'axisvm.com.core.tlb._16_100.RRelease_V161'>

.. py:class:: axisvm.com.tlb.RRelease_V161

   :param ReleaseType: <class 'ctypes.c_long'>
   :param FunctionId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.REccReleases

   :param x: <class 'ctypes.c_long'>
   :param y: <class 'ctypes.c_long'>
   :param z: <class 'ctypes.c_long'>
   :param xx: <class 'ctypes.c_long'>
   :param yy: <class 'ctypes.c_long'>
   :param zz: <class 'ctypes.c_long'>
   :param PosType: <class 'ctypes.c_long'>
   :param Pos: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpringCharacteristics

   :param x: <class 'ctypes.c_long'>
   :param y: <class 'ctypes.c_long'>
   :param z: <class 'ctypes.c_long'>
   :param xx: <class 'ctypes.c_long'>
   :param yy: <class 'ctypes.c_long'>
   :param zz: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadRibMemberConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param Fgx: <class 'ctypes.c_double'>
   :param Fgy: <class 'ctypes.c_double'>
   :param Fgz: <class 'ctypes.c_double'>
   :param Mgx: <class 'ctypes.c_double'>
   :param Mgy: <class 'ctypes.c_double'>
   :param Mgz: <class 'ctypes.c_double'>
   :param Position: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPoint2d

   :param Coord1: <class 'ctypes.c_double'>
   :param Coord2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RWindLoadParams_V161

   :param a: <class 'ctypes.c_double'>
   :param v_b0: <class 'ctypes.c_double'>
   :param c_dir_xp: <class 'ctypes.c_double'>
   :param c_dir_xm: <class 'ctypes.c_double'>
   :param c_dir_yp: <class 'ctypes.c_double'>
   :param c_dir_ym: <class 'ctypes.c_double'>
   :param c_season: <class 'ctypes.c_double'>
   :param TerrainCategoryDifferent: <class 'ctypes.c_long'>
   :param CustomDirectionalFactors: <class 'ctypes.c_long'>
   :param TerrainCat_Xp: <class 'ctypes.c_long'>
   :param TerrainCat_Xm: <class 'ctypes.c_long'>
   :param TerrainCat_Yp: <class 'ctypes.c_long'>
   :param TerrainCat_Ym: <class 'ctypes.c_long'>
   :param c_o: <class 'ctypes.c_double'>
   :param Iw: <class 'ctypes.c_double'>
   :param Zone: <class 'ctypes.c_long'>
   :param AltitudeFactor: <class 'ctypes.c_double'>
   :param TurbulenceFactor: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RWindSubStructParams

   :param Name: <class 'comtypes.BSTR'>
   :param RoofType: <class 'ctypes.c_long'>
   :param TorsionalEffect: <class 'ctypes.c_long'>
   :param InternalPressure: <class 'ctypes.c_long'>
   :param Mu_Xp: <class 'ctypes.c_double'>
   :param Mu_Xm: <class 'ctypes.c_double'>
   :param Mu_Yp: <class 'ctypes.c_double'>
   :param Mu_Ym: <class 'ctypes.c_double'>
   :param cpi_Xp: <class 'ctypes.c_double'>
   :param cpi_Xm: <class 'ctypes.c_double'>
   :param cpi_Yp: <class 'ctypes.c_double'>
   :param cpi_Ym: <class 'ctypes.c_double'>
   :param FricionEffect: <class 'ctypes.c_long'>
   :param CustomFriction: <class 'ctypes.c_double'>
   :param IsRelativeElevation: <class 'ctypes.c_long'>
   :param RelativeElevation: <class 'ctypes.c_double'>
   :param IsMultiSpan: <class 'ctypes.c_long'>
   :param MultiSpanPos: <class 'ctypes.c_long'>
   :param MultiSpanDir: <class 'ctypes.c_long'>
   :param FlatRoofEdgeType: <class 'ctypes.c_long'>
   :param FlatRoofEdgeParam: <class 'ctypes.c_double'>
   :param Blockage_Xp: <class 'ctypes.c_double'>
   :param Blockage_Xm: <class 'ctypes.c_double'>
   :param Blockage_Yp: <class 'ctypes.c_double'>
   :param Blockage_Ym: <class 'ctypes.c_double'>
   :param Solidity: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurfaceAttr

   :param Thickness: <class 'ctypes.c_double'>
   :param SurfaceType: <class 'ctypes.c_long'>
   :param RefZId: <class 'ctypes.c_long'>
   :param RefXId: <class 'ctypes.c_long'>
   :param MaterialId: <class 'ctypes.c_long'>
   :param ElasticFoundation: <class 'axisvm.com.core.tlb._16_100.RElasticFoundationXYZ'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearityXYZ'>
   :param Resistance: <class 'axisvm.com.core.tlb._16_100.RResistancesXYZ'>
   :param Charactersitics: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDomainMeshParameters

   :param MeshSize: <class 'ctypes.c_double'>
   :param MeshType: <class 'ctypes.c_long'>
   :param IsFitToPointLoad: <class 'ctypes.c_long'>
   :param FitToPointLoadValue: <class 'ctypes.c_double'>
   :param IsFitToLineLoad: <class 'ctypes.c_long'>
   :param FitToLineLoadValue: <class 'ctypes.c_double'>
   :param IsFitToSurfaceLoad: <class 'ctypes.c_long'>
   :param FitToSurfaceLoadValue: <class 'ctypes.c_double'>
   :param MeshGeometryType: <class 'ctypes.c_long'>
   :param QuadMeshQuality: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSurfaceCoordinates

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param pContourPoint1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourPoint2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourPoint3: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourPoint4: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param pContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters

   :param ConcreteId: <class 'ctypes.c_long'>
   :param RebarSteelGradeId: <class 'ctypes.c_long'>
   :param Thickness: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RStiffnessesXYZ

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNonLinearityXYZ

   :param x: <class 'ctypes.c_long'>
   :param y: <class 'ctypes.c_long'>
   :param z: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RResistancesXYZ

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurfaceStiffnessFactors

   :param k_torsion: <class 'ctypes.c_double'>
   :param k_shear: <class 'ctypes.c_double'>
   :param k_bending: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMatrix2x2

   :param e11: <class 'ctypes.c_double'>
   :param e12: <class 'ctypes.c_double'>
   :param e21: <class 'ctypes.c_double'>
   :param e22: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadNodalForce

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param NodeId: <class 'ctypes.c_long'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RNode

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>
   :param dof: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RResultTreeIteratorRec

   :param AnalysisType: <class 'ctypes.c_long'>
   :param ResultCase: <class 'ctypes.c_long'>
   :param LoadLevelOrTimeStep: <class 'ctypes.c_long'>
   :param Creep: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RTableCrossSectionID

   :param TableID: <class 'ctypes.c_long'>
   :param CrossSectionID: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RVelocityValues

   :param vvX: <class 'ctypes.c_double'>
   :param vvY: <class 'ctypes.c_double'>
   :param vvZ: <class 'ctypes.c_double'>
   :param vvXX: <class 'ctypes.c_double'>
   :param vvYY: <class 'ctypes.c_double'>
   :param vvZZ: <class 'ctypes.c_double'>
   :param vvR: <class 'ctypes.c_double'>
   :param vvRR: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpringParam_V161

   :param SpringType: <class 'ctypes.c_long'>
   :param NNType: <class 'ctypes.c_long'>
   :param DOFType: <class 'ctypes.c_long'>
   :param NLESimplified: <class 'ctypes.c_long'>
   :param K: <class 'ctypes.c_double'>
   :param KVib: <class 'ctypes.c_double'>
   :param DampingType: <class 'ctypes.c_long'>
   :param C: <class 'ctypes.c_double'>
   :param NonLinearity: <class 'ctypes.c_long'>
   :param NLDefType: <class 'ctypes.c_long'>
   :param K_T: <class 'ctypes.c_double'>
   :param K_C: <class 'ctypes.c_double'>
   :param ResistanceDef_T: <class 'ctypes.c_long'>
   :param ResistanceDef_C: <class 'ctypes.c_long'>
   :param TangentStiffness_T: <class 'ctypes.c_double'>
   :param TangentStiffness_C: <class 'ctypes.c_double'>
   :param Resistance_T: <class 'ctypes.c_double'>
   :param Resistance_C: <class 'ctypes.c_double'>
   :param HardeningRule: <class 'ctypes.c_long'>
   :param MatrixType: <class 'ctypes.c_long'>
   :param C_t: <class 'ctypes.c_double'>
   :param C_C: <class 'ctypes.c_double'>
   :param VerticalStiffness: <class 'ctypes.c_double'>
   :param IsolatorType: <class 'ctypes.c_long'>
   :param K1: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param F1: <class 'ctypes.c_double'>
   :param Mu: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param HorizontalStiffness: <class 'ctypes.c_double'>
   :param Ksi: <class 'ctypes.c_double'>
   :param WF: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RIFCExportReinforcementParams

   :param EdgeReinforcementNeeded: <class 'ctypes.c_long'>
   :param AdditionalHoleReinforcement: <class 'ctypes.c_long'>
   :param TypicalLapLengthByDesignCode: <class 'ctypes.c_long'>
   :param ConcaveCornerLapLengthByDesignCode: <class 'ctypes.c_long'>
   :param TypicalLapLengthByUser: <class 'ctypes.c_double'>
   :param ConcaveCornerLapLengthByUser: <class 'ctypes.c_double'>
   :param AdditionalHoleRebarDiameter: <class 'ctypes.c_double'>
   :param DomainReinforcementLinkType: <class 'ctypes.c_long'>
   :param QuestionableDomainLink: <class 'ctypes.c_long'>
   :param DomainOverlap_Larger: <class 'ctypes.c_long'>
   :param DomainOverlap_Smaller: <class 'ctypes.c_long'>
   :param ModifyClosedLinks: <class 'ctypes.c_long'>
   :param ClosedLinkRatio: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RShearCapacities

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param scvCenterPoint: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourPoint1: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourPoint2: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourPoint3: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourPoint4: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>
   :param scvContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RShearCapacityValues'>

.. py:class:: axisvm.com.tlb.RShearCapacityValues

   :param VRdc: <class 'ctypes.c_double'>
   :param VEdMinusVRdc: <class 'ctypes.c_double'>
   :param VRdmax: <class 'ctypes.c_double'>
   :param VEdDivVRdmax: <class 'ctypes.c_double'>
   :param aVEd: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCrossSectionSFB

   :param h: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param b2: <class 'ctypes.c_double'>
   :param v2: <class 'ctypes.c_double'>
   :param Process: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RStructuralGridLineParams

   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param NormalVector: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param Colour: <class 'ctypes.c_long'>
   :param Extension: <class 'ctypes.c_double'>
   :param ShowTitle: <class 'ctypes.c_long'>
   :param ToLogicalPart: <class 'ctypes.c_long'>
   :param PlaneTolerance: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RBulkLineSupport

   :param SupportType: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearity'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>
   :param SurfaceId1: <class 'ctypes.c_long'>
   :param SurfaceId2: <class 'ctypes.c_long'>
   :param DomainId1: <class 'ctypes.c_long'>
   :param DomainId2: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSupportDisplacement

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param SupportId: <class 'ctypes.c_long'>
   :param ex: <class 'ctypes.c_double'>
   :param ey: <class 'ctypes.c_double'>
   :param ez: <class 'ctypes.c_double'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSeismicParams

   :param VibrType: <class 'ctypes.c_long'>
   :param kg: <class 'ctypes.c_double'>
   :param ks: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param psi: <class 'ctypes.c_double'>
   :param SeismicCombType: <class 'ctypes.c_long'>
   :param qd: <class 'ctypes.c_double'>
   :param ksiV: <class 'ctypes.c_double'>
   :param ModalCombType: <class 'ctypes.c_long'>
   :param Torsion: <class 'ctypes.c_long'>
   :param ExcCoeff: <class 'ctypes.c_double'>
   :param C: <class 'ctypes.c_double'>
   :param nu: <class 'ctypes.c_double'>
   :param LoadCaseLoadCombination: <class 'ctypes.c_long'>
   :param Eta: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDXFimportParameters

   :param CoordinateUnit: <class 'ctypes.c_long'>
   :param MaxDeviation: <class 'ctypes.c_double'>
   :param GeometryCheckTolerance: <class 'ctypes.c_double'>
   :param CoordinateScaleFactor: <class 'ctypes.c_double'>
   :param ImportAs: <class 'ctypes.c_long'>
   :param ImportMode: <class 'ctypes.c_long'>
   :param BasePlane: <class 'ctypes.c_long'>
   :param WorkPlaneIndex: <class 'ctypes.c_long'>
   :param PlaceOffset: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param VisibleLayersOnly: <class 'ctypes.c_long'>
   :param ImportHatch: <class 'ctypes.c_long'>
   :param ActivateDXFonAllDrawings: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPDFimportParameters

   :param PageNumber: <class 'ctypes.c_long'>
   :param MaxDeviation: <class 'ctypes.c_double'>
   :param GeometryCheckTolerance: <class 'ctypes.c_double'>
   :param Scale: <class 'ctypes.c_double'>
   :param ImportLineWidth: <class 'ctypes.c_long'>
   :param ImportText: <class 'ctypes.c_long'>
   :param BasePlane: <class 'ctypes.c_long'>
   :param WorkPlaneIndex: <class 'ctypes.c_long'>
   :param ImportAs: <class 'ctypes.c_long'>
   :param ImportMode: <class 'ctypes.c_long'>
   :param PlaceOffset: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RIFCimportParameters

   :param ImportMode: <class 'ctypes.c_long'>
   :param ImportMethod: <class 'ctypes.c_long'>
   :param MaxDeviation: <class 'ctypes.c_double'>
   :param ByAngle: <class 'ctypes.c_double'>
   :param JoinIfObjectsAreCloserThan: <class 'ctypes.c_double'>
   :param ImportAs: <class 'ctypes.c_long'>
   :param OpeningsAlignedToDomainEdge: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCompanyLogoParameters

   :param ShowInHeader: <class 'ctypes.c_long'>
   :param HeaderPosition: <class 'ctypes.c_long'>
   :param HeaderSizeOption: <class 'ctypes.c_long'>
   :param HeaderSize: <class 'ctypes.c_double'>
   :param ShowOnCover: <class 'ctypes.c_long'>
   :param CoverAlignment: <class 'ctypes.c_long'>
   :param TopMargin: <class 'ctypes.c_double'>
   :param SpacingAfter: <class 'ctypes.c_double'>
   :param CoverSizeOption: <class 'ctypes.c_long'>
   :param CoverSize: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RAXSimportParameters

   :param Place: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param CheckTolerance: <class 'ctypes.c_double'>
   :param MergeLoadCases: <class 'ctypes.c_long'>
   :param UserInteraction: <class 'ctypes.c_long'>
   :param IgnoreDesignCode: <class 'ctypes.c_long'>
   :param MergeLayers: <class 'ctypes.c_long'>
   :param CustomParts: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDomainHollowCore

   :param Direction: <class 'ctypes.c_long'>
   :param d: <class 'ctypes.c_double'>
   :param Origin: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param HoleType: <class 'ctypes.c_long'>
   :param fi: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param h: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpringParam

   :param SpringType: <class 'ctypes.c_long'>
   :param NNType: <class 'ctypes.c_long'>
   :param DOFType: <class 'ctypes.c_long'>
   :param NLESimplified: <class 'ctypes.c_long'>
   :param K: <class 'ctypes.c_double'>
   :param KVib: <class 'ctypes.c_double'>
   :param DampingType: <class 'ctypes.c_long'>
   :param C: <class 'ctypes.c_double'>
   :param NonLinearity: <class 'ctypes.c_long'>
   :param NLDefType: <class 'ctypes.c_long'>
   :param K_T: <class 'ctypes.c_double'>
   :param K_C: <class 'ctypes.c_double'>
   :param ResistanceDef_T: <class 'ctypes.c_long'>
   :param ResistanceDef_C: <class 'ctypes.c_long'>
   :param TangentStiffness_T: <class 'ctypes.c_double'>
   :param TangentStiffness_C: <class 'ctypes.c_double'>
   :param Resistance_T: <class 'ctypes.c_double'>
   :param Resistance_C: <class 'ctypes.c_double'>
   :param HardeningRule: <class 'ctypes.c_long'>
   :param MatrixType: <class 'ctypes.c_long'>
   :param C_t: <class 'ctypes.c_double'>
   :param C_C: <class 'ctypes.c_double'>
   :param VerticalStiffness: <class 'ctypes.c_double'>
   :param IsolatorType: <class 'ctypes.c_long'>
   :param K1: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param F1: <class 'ctypes.c_double'>
   :param Mu: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param HorizontalStiffness: <class 'ctypes.c_double'>
   :param Ksi: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpringParamIndexes

   :param x: <class 'ctypes.c_long'>
   :param y: <class 'ctypes.c_long'>
   :param z: <class 'ctypes.c_long'>
   :param xx: <class 'ctypes.c_long'>
   :param yy: <class 'ctypes.c_long'>
   :param zz: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadBeamThermal

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Tref: <class 'ctypes.c_double'>
   :param Ttop: <class 'ctypes.c_double'>
   :param Tbot: <class 'ctypes.c_double'>
   :param Axis: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RColumnRebarPos

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param d: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSnowLoadParams

   :param a: <class 'ctypes.c_double'>
   :param C_e: <class 'ctypes.c_double'>
   :param C_t: <class 'ctypes.c_double'>
   :param C_esl: <class 'ctypes.c_double'>
   :param s_k: <class 'ctypes.c_double'>
   :param s_Ad: <class 'ctypes.c_double'>
   :param Iw: <class 'ctypes.c_double'>
   :param Zone: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceThermal

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param SurfaceId: <class 'ctypes.c_long'>
   :param Tref: <class 'ctypes.c_double'>
   :param Ttop: <class 'ctypes.c_double'>
   :param Tbot: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMovingLoadOnBeamItem

   :param ItemType: <class 'ctypes.c_long'>
   :param Concentrated: <class 'axisvm.com.core.tlb._16_100.RConcentratedMovingLoadOnBeam'>
   :param Distributed: <class 'axisvm.com.core.tlb._16_100.RDistributedMovingLoadOnBeam'>

.. py:class:: axisvm.com.tlb.RLoadBeamInfluence

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param ex: <class 'ctypes.c_double'>
   :param ey: <class 'ctypes.c_double'>
   :param ez: <class 'ctypes.c_double'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Position: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadBeamStress

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param P: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNodalSupportForceValues

   :param Rx: <class 'ctypes.c_double'>
   :param Ry: <class 'ctypes.c_double'>
   :param Rz: <class 'ctypes.c_double'>
   :param Rxx: <class 'ctypes.c_double'>
   :param Ryy: <class 'ctypes.c_double'>
   :param Rzz: <class 'ctypes.c_double'>
   :param Rr: <class 'ctypes.c_double'>
   :param Rrr: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RBulkWSLineSupport

   :param SupportType: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearity'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>
   :param ShearStiffness: <class 'ctypes.c_double'>
   :param SurfaceId1: <class 'ctypes.c_long'>
   :param SurfaceId2: <class 'ctypes.c_long'>
   :param DomainId1: <class 'ctypes.c_long'>
   :param DomainId2: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainThermal

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>
   :param Tref: <class 'ctypes.c_double'>
   :param Tsup: <class 'ctypes.c_double'>
   :param Tinf: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLineSupportForceValues

   :param Rx: <class 'ctypes.c_double'>
   :param Ry: <class 'ctypes.c_double'>
   :param Rz: <class 'ctypes.c_double'>
   :param Rxx: <class 'ctypes.c_double'>
   :param Ryy: <class 'ctypes.c_double'>
   :param Rzz: <class 'ctypes.c_double'>
   :param Rr: <class 'ctypes.c_double'>
   :param Rrr: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadPanelEdgeParams

   :param LoadPanelEdgeType: <class 'ctypes.c_long'>
   :param h: <class 'ctypes.c_double'>
   :param Alpha: <class 'ctypes.c_double'>
   :param b_1: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RShowLocalSystems

   :param Beam: <class 'ctypes.c_long'>
   :param Rib: <class 'ctypes.c_long'>
   :param Surface: <class 'ctypes.c_long'>
   :param Domain: <class 'ctypes.c_long'>
   :param Support: <class 'ctypes.c_long'>
   :param Spring: <class 'ctypes.c_long'>
   :param Gap: <class 'ctypes.c_long'>
   :param Link: <class 'ctypes.c_long'>
   :param EdgeHinge: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceToBeamAssoc

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Px: <class 'ctypes.c_double'>
   :param Py: <class 'ctypes.c_double'>
   :param Pz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReinforcements

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param rvCenterPoint: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourPoint1: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourPoint2: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourPoint3: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourPoint4: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>
   :param rvContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RReinforcementValues'>

.. py:class:: axisvm.com.tlb.RReinforcementValues

   :param Asbx: <class 'ctypes.c_double'>
   :param Asby: <class 'ctypes.c_double'>
   :param Astx: <class 'ctypes.c_double'>
   :param Asty: <class 'ctypes.c_double'>
   :param AsbxStatus: <class 'ctypes.c_long'>
   :param AsbyStatus: <class 'ctypes.c_long'>
   :param AstxStatus: <class 'ctypes.c_long'>
   :param AstyStatus: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RTimberDesignParameters

   :param BreakAtElements: <class 'ctypes.c_long'>
   :param EC_SIA_ITA: <class 'axisvm.com.core.tlb._16_100.RTimberDesignParameters_EC_SIA_ITA'>

.. py:class:: axisvm.com.tlb.RTimberDesignParameters_V153

   :param BreakAtElements: <class 'ctypes.c_long'>
   :param EC: <class 'axisvm.com.core.tlb._16_100.RTimberDesignParameters_EC_V153'>

.. py:class:: axisvm.com.tlb.REdgeConnectionRec

   :param LineId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters

   :param ConcreteMaterial: <class 'ctypes.c_long'>
   :param Dmax: <class 'ctypes.c_double'>
   :param RebarMaterial: <class 'ctypes.c_long'>
   :param RebarType: <class 'ctypes.c_long'>
   :param StirrupMaterial: <class 'ctypes.c_long'>
   :param StirrupDiameter: <class 'ctypes.c_double'>
   :param StirrupLegs: <class 'ctypes.c_long'>
   :param Shape: <class 'ctypes.c_long'>
   :param c_top: <class 'ctypes.c_double'>
   :param c_bottom: <class 'ctypes.c_double'>
   :param ds_top: <class 'ctypes.c_double'>
   :param ds_bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrengthNL: <class 'ctypes.c_long'>
   :param UseFctmflNL: <class 'ctypes.c_long'>
   :param ShrinkageEpsNL: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RAccelerationValues

   :param avX: <class 'ctypes.c_double'>
   :param avY: <class 'ctypes.c_double'>
   :param avZ: <class 'ctypes.c_double'>
   :param avXX: <class 'ctypes.c_double'>
   :param avYY: <class 'ctypes.c_double'>
   :param avZZ: <class 'ctypes.c_double'>
   :param avR: <class 'ctypes.c_double'>
   :param avRR: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSteelDesignParameters_EC_SIA_ITA_V153

   :param BreakAtElements: <class 'ctypes.c_long'>
   :param Ky: <class 'ctypes.c_double'>
   :param Kz: <class 'ctypes.c_double'>
   :param Kw: <class 'ctypes.c_double'>
   :param C1: <class 'ctypes.c_double'>
   :param C2: <class 'ctypes.c_double'>
   :param C3: <class 'ctypes.c_double'>
   :param Za: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param akr: <class 'ctypes.c_double'>
   :param a: <class 'ctypes.c_double'>
   :param Stiffeners: <class 'ctypes.c_long'>
   :param SDP_Class: <class 'ctypes.c_long'>
   :param YBraced: <class 'ctypes.c_long'>
   :param ZBraced: <class 'ctypes.c_long'>
   :param McrMethod: <class 'ctypes.c_long'>
   :param DesignApproach: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param Cantilever: <class 'ctypes.c_long'>
   :param CantileverFixedEnd: <class 'ctypes.c_long'>
   :param FlexuralBuckling: <class 'ctypes.c_long'>
   :param LateralTorsionalBuckling: <class 'ctypes.c_long'>
   :param WebShearBuckling: <class 'ctypes.c_long'>
   :param BucklingLengthModeY: <class 'ctypes.c_long'>
   :param BucklingLengthModeZ: <class 'ctypes.c_long'>
   :param Ly: <class 'ctypes.c_double'>
   :param Lz: <class 'ctypes.c_double'>
   :param ConsiderN: <class 'ctypes.c_long'>
   :param Eta: <class 'ctypes.c_double'>
   :param LateralSupports: <class 'ctypes.c_long'>
   :param Mcr: <class 'ctypes.c_double'>
   :param FireResistDef: <class 'ctypes.c_long'>
   :param fpOnlyPrescribed: <class 'ctypes.c_long'>
   :param fpKy: <class 'ctypes.c_double'>
   :param fpKz: <class 'ctypes.c_double'>
   :param fpKw: <class 'ctypes.c_double'>
   :param fpC1: <class 'ctypes.c_double'>
   :param fpC2: <class 'ctypes.c_double'>
   :param fpC3: <class 'ctypes.c_double'>
   :param fpLy: <class 'ctypes.c_double'>
   :param fpLz: <class 'ctypes.c_double'>
   :param fpMcr: <class 'ctypes.c_double'>
   :param fpBetaMethod: <class 'ctypes.c_long'>
   :param fpBetaMy: <class 'ctypes.c_double'>
   :param fpBetaMz: <class 'ctypes.c_double'>
   :param fpBetaLT: <class 'ctypes.c_double'>
   :param slsAngle: <class 'ctypes.c_double'>
   :param slsEyLimitDef: <class 'ctypes.c_long'>
   :param slsEzLimitDef: <class 'ctypes.c_long'>
   :param slsHxLimitDef: <class 'ctypes.c_long'>
   :param slsHyLimitDef: <class 'ctypes.c_long'>
   :param slsUyDef: <class 'ctypes.c_long'>
   :param slsUzDef: <class 'ctypes.c_long'>
   :param slsHGlob: <class 'ctypes.c_long'>
   :param slsHMode: <class 'ctypes.c_long'>
   :param slsEMode: <class 'ctypes.c_long'>
   :param slsLMode: <class 'ctypes.c_long'>
   :param slsPreCamberCurve: <class 'ctypes.c_long'>
   :param slsEyLimit: <class 'ctypes.c_double'>
   :param slsEzLimit: <class 'ctypes.c_double'>
   :param slsHxLimit: <class 'ctypes.c_double'>
   :param slsHyLimit: <class 'ctypes.c_double'>
   :param slsUy: <class 'ctypes.c_double'>
   :param slsUz: <class 'ctypes.c_double'>
   :param slsCustomLy: <class 'ctypes.c_double'>
   :param slsCustomLz: <class 'ctypes.c_double'>
   :param slsCustomH: <class 'ctypes.c_double'>
   :param slsRatio: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNodalSupportStiffParams

   :param Top: <class 'axisvm.com.core.tlb._16_100.RColumnStiffnessParams'>
   :param Bottom: <class 'axisvm.com.core.tlb._16_100.RColumnStiffnessParams'>

.. py:class:: axisvm.com.tlb.RPadFootingDimensions

   :param UpperThickness: <class 'ctypes.c_double'>
   :param LowerThickness: <class 'ctypes.c_double'>
   :param UpperCornerA: <class 'axisvm.com.core.tlb._16_100.RPoint2d'>
   :param UpperCornerB: <class 'axisvm.com.core.tlb._16_100.RPoint2d'>
   :param LowerCornerA: <class 'axisvm.com.core.tlb._16_100.RPoint2d'>
   :param LowerCornerB: <class 'axisvm.com.core.tlb._16_100.RPoint2d'>

.. py:class:: axisvm.com.tlb.RPadFootingParams

   :param HeightTop: <class 'ctypes.c_double'>
   :param HeightBottom: <class 'ctypes.c_double'>
   :param BaseThickness: <class 'ctypes.c_double'>
   :param bx: <class 'ctypes.c_double'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param by: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param dy1: <class 'ctypes.c_double'>
   :param dy2: <class 'ctypes.c_double'>
   :param MaterialId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPadFootingParams_V153

   :param FootingType: <class 'ctypes.c_long'>
   :param VerticalType: <class 'ctypes.c_long'>
   :param MaterialId: <class 'ctypes.c_long'>
   :param GroundToBottom: <class 'ctypes.c_double'>
   :param HeightMain: <class 'ctypes.c_double'>
   :param HeightStep: <class 'ctypes.c_double'>
   :param BlindThickness: <class 'ctypes.c_double'>
   :param RectangularFootingSpec: <class 'axisvm.com.core.tlb._16_100.RRectangularFootingSpec'>
   :param RectangularFootingCalced: <class 'axisvm.com.core.tlb._16_100.RRectanularFootingCalced'>
   :param CircularFootingSpec: <class 'axisvm.com.core.tlb._16_100.RCircularFootingSpec'>
   :param CircularFootingCalced: <class 'axisvm.com.core.tlb._16_100.RCircularFootingCalced'>

.. py:class:: axisvm.com.tlb.RShowGraphicSymbols

   :param Mesh: <class 'ctypes.c_long'>
   :param Node: <class 'ctypes.c_long'>
   :param SurfaceCentre: <class 'ctypes.c_long'>
   :param CentreOfCircle: <class 'ctypes.c_long'>
   :param Domain: <class 'ctypes.c_long'>
   :param NodalSupport: <class 'ctypes.c_long'>
   :param LineSupport: <class 'ctypes.c_long'>
   :param SurfaceSupport: <class 'ctypes.c_long'>
   :param Foundation: <class 'ctypes.c_long'>
   :param AutoFoundationDimension: <class 'ctypes.c_long'>
   :param Links: <class 'ctypes.c_long'>
   :param Rigids: <class 'ctypes.c_long'>
   :param Diaphragm: <class 'ctypes.c_long'>
   :param Reference: <class 'ctypes.c_long'>
   :param CrossSectionShape: <class 'ctypes.c_long'>
   :param EndReleases: <class 'ctypes.c_long'>
   :param StructuralMembers: <class 'ctypes.c_long'>
   :param ReinfParams: <class 'ctypes.c_long'>
   :param ReinfDomain: <class 'ctypes.c_long'>
   :param Mass: <class 'ctypes.c_long'>
   :param StoreyCentGrav: <class 'ctypes.c_long'>
   :param StoreyShearCent: <class 'ctypes.c_long'>
   :param ARBO_CRETelems: <class 'ctypes.c_long'>
   :param COBIAXelems: <class 'ctypes.c_long'>
   :param Trusses: <class 'ctypes.c_long'>
   :param Beams: <class 'ctypes.c_long'>
   :param Ribs: <class 'ctypes.c_long'>
   :param Springs: <class 'ctypes.c_long'>
   :param IsolineLabels: <class 'ctypes.c_long'>
   :param RoundIsoValues: <class 'ctypes.c_long'>
   :param Gaps: <class 'ctypes.c_long'>
   :param StructuralGrids: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RShowLoads

   :param Concentrated: <class 'ctypes.c_long'>
   :param Line: <class 'ctypes.c_long'>
   :param Surface: <class 'ctypes.c_long'>
   :param Temperature: <class 'ctypes.c_long'>
   :param SelfWeight: <class 'ctypes.c_long'>
   :param Miscel: <class 'ctypes.c_long'>
   :param LoadDistrScheme: <class 'ctypes.c_long'>
   :param DerivedBeamLoad: <class 'ctypes.c_long'>
   :param MovingLoadPhases: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSteelDesignParameters_EC_SIA_ITA

   :param BreakAtElements: <class 'ctypes.c_long'>
   :param Ky: <class 'ctypes.c_double'>
   :param Kz: <class 'ctypes.c_double'>
   :param Kw: <class 'ctypes.c_double'>
   :param C1: <class 'ctypes.c_double'>
   :param C2: <class 'ctypes.c_double'>
   :param C3: <class 'ctypes.c_double'>
   :param Za: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param akr: <class 'ctypes.c_double'>
   :param a: <class 'ctypes.c_double'>
   :param Stiffeners: <class 'ctypes.c_long'>
   :param SDP_Class: <class 'ctypes.c_long'>
   :param YBraced: <class 'ctypes.c_long'>
   :param ZBraced: <class 'ctypes.c_long'>
   :param McrMethod: <class 'ctypes.c_long'>
   :param DesignApproach: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param Cantilever: <class 'ctypes.c_long'>
   :param CantileverFixedEnd: <class 'ctypes.c_long'>
   :param FlexuralBuckling: <class 'ctypes.c_long'>
   :param LateralTorsionalBuckling: <class 'ctypes.c_long'>
   :param WebShearBuckling: <class 'ctypes.c_long'>
   :param BucklingLengthModeY: <class 'ctypes.c_long'>
   :param BucklingLengthModeZ: <class 'ctypes.c_long'>
   :param Ly: <class 'ctypes.c_double'>
   :param Lz: <class 'ctypes.c_double'>
   :param ConsiderN: <class 'ctypes.c_long'>
   :param Eta: <class 'ctypes.c_double'>
   :param LateralSupports: <class 'ctypes.c_long'>
   :param Mcr: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSteelDesignParameters_MSZ_STAS

   :param BreakAtElements: <class 'ctypes.c_long'>
   :param nuy: <class 'ctypes.c_double'>
   :param nuz: <class 'ctypes.c_double'>
   :param nuw: <class 'ctypes.c_double'>
   :param d: <class 'ctypes.c_double'>
   :param a: <class 'ctypes.c_double'>
   :param Stiffeners: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadPanelConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LoadPanelId: <class 'ctypes.c_long'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade_EC_ITA

   :param fyd: <class 'ctypes.c_double'>
   :param es1: <class 'ctypes.c_double'>
   :param esu: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNNLinkElementRec

   :param LineId: <class 'ctypes.c_long'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param MasterPoint: <class 'ctypes.c_long'>
   :param RefZId: <class 'ctypes.c_long'>
   :param PositionType: <class 'ctypes.c_long'>
   :param Position: <class 'ctypes.c_double'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearity'>

.. py:class:: axisvm.com.tlb.RLLLinkElementRec

   :param MasterLine: <class 'ctypes.c_long'>
   :param SlaveLine: <class 'ctypes.c_long'>
   :param MasterStartLink: <class 'ctypes.c_long'>
   :param MasterEndLink: <class 'ctypes.c_long'>
   :param PositionType: <class 'ctypes.c_long'>
   :param Position: <class 'ctypes.c_double'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearity'>

.. py:class:: axisvm.com.tlb.RLinkElementRec

   :param NNLinkElementRec: <class 'axisvm.com.core.tlb._16_100.RNNLinkElementRec'>
   :param LLLinkElementRec: <class 'axisvm.com.core.tlb._16_100.RLLLinkElementRec'>

.. py:class:: axisvm.com.tlb.REdgeConnectionForces

   :param ecfSection1: <class 'axisvm.com.core.tlb._16_100.REdgeConnectionForceValues'>
   :param ecfSection2: <class 'axisvm.com.core.tlb._16_100.REdgeConnectionForceValues'>
   :param ecfSection3: <class 'axisvm.com.core.tlb._16_100.REdgeConnectionForceValues'>

.. py:class:: axisvm.com.tlb.REdgeConnectionForceValues

   :param ecfvNx: <class 'ctypes.c_double'>
   :param ecfvVy: <class 'ctypes.c_double'>
   :param ecfvVz: <class 'ctypes.c_double'>
   :param ecfvTx: <class 'ctypes.c_double'>
   :param ecfvMy: <class 'ctypes.c_double'>
   :param ecfvMz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade_MSZ

   :param ssh: <class 'ctypes.c_double'>
   :param es0: <class 'ctypes.c_double'>
   :param esh: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_ITA

   :param AggregateSize: <class 'ctypes.c_double'>
   :param StructClass: <class 'ctypes.c_long'>
   :param EnvClass_T: <class 'ctypes.c_long'>
   :param EnvClass_B: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Npos: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Nneg: <class 'ctypes.c_double'>
   :param dxt: <class 'ctypes.c_double'>
   :param dxb: <class 'ctypes.c_double'>
   :param dyt: <class 'ctypes.c_double'>
   :param dyb: <class 'ctypes.c_double'>
   :param SlabLoadTransfer: <class 'ctypes.c_long'>
   :param SlabLoadTransferDirection: <class 'ctypes.c_long'>
   :param MainDirectionTop: <class 'ctypes.c_long'>
   :param MainDirectionBottom: <class 'ctypes.c_long'>
   :param ct: <class 'ctypes.c_double'>
   :param cb: <class 'ctypes.c_double'>
   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param ShortTerm: <class 'ctypes.c_long'>
   :param ShearReinforcementAngle: <class 'ctypes.c_double'>
   :param ShearCrackAngle: <class 'ctypes.c_double'>
   :param TakeConcTensileStrengthNL: <class 'ctypes.c_long'>
   :param UseFctmfl: <class 'ctypes.c_long'>
   :param ShrinkageEps: <class 'ctypes.c_double'>
   :param RCNonlinearSurfType: <class 'ctypes.c_long'>
   :param ReinforcementType: <class 'ctypes.c_long'>
   :param AlphaAngle: <class 'ctypes.c_double'>
   :param BetaAngle: <class 'ctypes.c_double'>
   :param CalcFromLimitingCrackWidth: <class 'ctypes.c_long'>
   :param wk_b: <class 'ctypes.c_double'>
   :param wk2_b: <class 'ctypes.c_double'>
   :param wk_t: <class 'ctypes.c_double'>
   :param wk2_t: <class 'ctypes.c_double'>
   :param ApproximateLevelArm: <class 'ctypes.c_long'>
   :param SeelhoferMartiEquation: <class 'ctypes.c_long'>
   :param TrapSheetOnlyFormWork: <class 'ctypes.c_long'>
   :param TrapSheetOneLayerReinf: <class 'ctypes.c_long'>
   :param TrapSheetConsidered: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLinkElementForces

   :param lefLinkElementType: <class 'ctypes.c_long'>
   :param lefSection1: <class 'axisvm.com.core.tlb._16_100.RLinkElementForceValues'>
   :param lefSection2: <class 'axisvm.com.core.tlb._16_100.RLinkElementForceValues'>
   :param lefSection3: <class 'axisvm.com.core.tlb._16_100.RLinkElementForceValues'>

.. py:class:: axisvm.com.tlb.RLinkElementForceValues

   :param lefvNx: <class 'ctypes.c_double'>
   :param lefvVy: <class 'ctypes.c_double'>
   :param lefvVz: <class 'ctypes.c_double'>
   :param lefvTx: <class 'ctypes.c_double'>
   :param lefvMy: <class 'ctypes.c_double'>
   :param lefvMz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurface

   :param N: <class 'ctypes.c_long'>
   :param LineIndex1: <class 'ctypes.c_long'>
   :param LineIndex2: <class 'ctypes.c_long'>
   :param LineIndex3: <class 'ctypes.c_long'>
   :param LineIndex4: <class 'ctypes.c_long'>
   :param Attr: <class 'axisvm.com.core.tlb._16_100.RSurfaceAttr'>
   :param DomainIndex: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RElasticFoundationXYZ

   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadBeamDistributed

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param qx1: <class 'ctypes.c_double'>
   :param qy1: <class 'ctypes.c_double'>
   :param qz1: <class 'ctypes.c_double'>
   :param mx1: <class 'ctypes.c_double'>
   :param my1: <class 'ctypes.c_double'>
   :param mz1: <class 'ctypes.c_double'>
   :param qx2: <class 'ctypes.c_double'>
   :param qy2: <class 'ctypes.c_double'>
   :param qz2: <class 'ctypes.c_double'>
   :param mx2: <class 'ctypes.c_double'>
   :param my2: <class 'ctypes.c_double'>
   :param mz2: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param Position1: <class 'ctypes.c_double'>
   :param Position2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Trapezoid: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSurfaceStressValues

   :param ssvSxx: <class 'ctypes.c_double'>
   :param ssvSyy: <class 'ctypes.c_double'>
   :param ssvSxy: <class 'ctypes.c_double'>
   :param ssvSxz: <class 'ctypes.c_double'>
   :param ssvSyz: <class 'ctypes.c_double'>
   :param ssvSVM: <class 'ctypes.c_double'>
   :param ssvS1: <class 'ctypes.c_double'>
   :param ssvS2: <class 'ctypes.c_double'>
   :param ssvAs: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLine3d

   :param LineType: <class 'ctypes.c_long'>
   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param ArcCenter: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param ArcOrientation: <class 'ctypes.c_long'>
   :param NormVect: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RRCBeamCrossSections

   :param StartSection: <class 'axisvm.com.core.tlb._16_100.RRCBeamSection'>
   :param EndSection: <class 'axisvm.com.core.tlb._16_100.RRCBeamSection'>

.. py:class:: axisvm.com.tlb.RRCBeamSection

   :param bw: <class 'ctypes.c_double'>
   :param h: <class 'ctypes.c_double'>
   :param hf: <class 'ctypes.c_double'>
   :param beff: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadRibDistributed

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param qx1: <class 'ctypes.c_double'>
   :param qy1: <class 'ctypes.c_double'>
   :param qz1: <class 'ctypes.c_double'>
   :param mx1: <class 'ctypes.c_double'>
   :param my1: <class 'ctypes.c_double'>
   :param mz1: <class 'ctypes.c_double'>
   :param qx2: <class 'ctypes.c_double'>
   :param qy2: <class 'ctypes.c_double'>
   :param qz2: <class 'ctypes.c_double'>
   :param mx2: <class 'ctypes.c_double'>
   :param my2: <class 'ctypes.c_double'>
   :param mz2: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param Position1: <class 'ctypes.c_double'>
   :param Position2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Trapezoid: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RResultBlock

   :param ResultType: <class 'ctypes.c_long'>
   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LoadCombinationId: <class 'ctypes.c_long'>
   :param LoadLevel: <class 'ctypes.c_long'>
   :param AnalysisType: <class 'ctypes.c_long'>
   :param MinMaxType: <class 'ctypes.c_long'>
   :param EnvelopeUID: <class 'ctypes.c_long'>
   :param CombinationType: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade_DIN

   :param fyk: <class 'ctypes.c_double'>
   :param Epsuk: <class 'ctypes.c_double'>
   :param GammaS: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLineStressValues

   :param lsvLineType: <class 'ctypes.c_long'>
   :param lsvPointCount: <class 'ctypes.c_long'>
   :param lsvS1: <class 'ctypes.c_double'>
   :param lsvS2: <class 'ctypes.c_double'>
   :param lsvS3: <class 'ctypes.c_double'>
   :param lsvS4: <class 'ctypes.c_double'>
   :param lsvS5: <class 'ctypes.c_double'>
   :param lsvS6: <class 'ctypes.c_double'>
   :param lsvS7: <class 'ctypes.c_double'>
   :param lsvS8: <class 'ctypes.c_double'>
   :param lsvS9: <class 'ctypes.c_double'>
   :param lsvV1: <class 'ctypes.c_double'>
   :param lsvV2: <class 'ctypes.c_double'>
   :param lsvV3: <class 'ctypes.c_double'>
   :param lsvV4: <class 'ctypes.c_double'>
   :param lsvV5: <class 'ctypes.c_double'>
   :param lsvV6: <class 'ctypes.c_double'>
   :param lsvV7: <class 'ctypes.c_double'>
   :param lsvV8: <class 'ctypes.c_double'>
   :param lsvV9: <class 'ctypes.c_double'>
   :param lsvSo1: <class 'ctypes.c_double'>
   :param lsvSo2: <class 'ctypes.c_double'>
   :param lsvSo3: <class 'ctypes.c_double'>
   :param lsvSo4: <class 'ctypes.c_double'>
   :param lsvSo5: <class 'ctypes.c_double'>
   :param lsvSo6: <class 'ctypes.c_double'>
   :param lsvSo7: <class 'ctypes.c_double'>
   :param lsvSo8: <class 'ctypes.c_double'>
   :param lsvSo9: <class 'ctypes.c_double'>
   :param lsvSeff1: <class 'ctypes.c_double'>
   :param lsvSeff2: <class 'ctypes.c_double'>
   :param lsvSeff3: <class 'ctypes.c_double'>
   :param lsvSeff4: <class 'ctypes.c_double'>
   :param lsvSeff5: <class 'ctypes.c_double'>
   :param lsvSeff6: <class 'ctypes.c_double'>
   :param lsvSeff7: <class 'ctypes.c_double'>
   :param lsvSeff8: <class 'ctypes.c_double'>
   :param lsvSeff9: <class 'ctypes.c_double'>
   :param lsvfy1: <class 'ctypes.c_double'>
   :param lsvfy2: <class 'ctypes.c_double'>
   :param lsvfy3: <class 'ctypes.c_double'>
   :param lsvfy4: <class 'ctypes.c_double'>
   :param lsvfy5: <class 'ctypes.c_double'>
   :param lsvfy6: <class 'ctypes.c_double'>
   :param lsvfy7: <class 'ctypes.c_double'>
   :param lsvfy8: <class 'ctypes.c_double'>
   :param lsvfy9: <class 'ctypes.c_double'>
   :param lsvKih1: <class 'ctypes.c_double'>
   :param lsvKih2: <class 'ctypes.c_double'>
   :param lsvKih3: <class 'ctypes.c_double'>
   :param lsvKih4: <class 'ctypes.c_double'>
   :param lsvKih5: <class 'ctypes.c_double'>
   :param lsvKih6: <class 'ctypes.c_double'>
   :param lsvKih7: <class 'ctypes.c_double'>
   :param lsvKih8: <class 'ctypes.c_double'>
   :param lsvKih9: <class 'ctypes.c_double'>
   :param lsvVymean: <class 'ctypes.c_double'>
   :param lsvVzmean: <class 'ctypes.c_double'>
   :param lsvSmin: <class 'ctypes.c_long'>
   :param lsvSmax: <class 'ctypes.c_long'>
   :param lsvVmin: <class 'ctypes.c_long'>
   :param lsvVmax: <class 'ctypes.c_long'>
   :param lsvSomin: <class 'ctypes.c_long'>
   :param lsvSomax: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSurfaceStressValuesTMB

   :param ssvTop: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValues'>
   :param ssvMiddle: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValues'>
   :param ssvBottom: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValues'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade_STAS

   :param Ra: <class 'ctypes.c_double'>
   :param es1: <class 'ctypes.c_double'>
   :param esu: <class 'ctypes.c_double'>
   :param mat: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamSupport

   :param OverWrite: <class 'ctypes.c_long'>
   :param ActualHalfWidth: <class 'ctypes.c_double'>
   :param TheoreticalHalfWidth: <class 'ctypes.c_double'>
   :param ShearReduction: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_SIA

   :param AggregateSize: <class 'ctypes.c_double'>
   :param StructClass: <class 'ctypes.c_long'>
   :param EnvClass_T: <class 'ctypes.c_long'>
   :param EnvClass_B: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param dxt: <class 'ctypes.c_double'>
   :param dxb: <class 'ctypes.c_double'>
   :param dyt: <class 'ctypes.c_double'>
   :param dyb: <class 'ctypes.c_double'>
   :param SlabLoadTransfer: <class 'ctypes.c_long'>
   :param SlabLoadTransferDirection: <class 'ctypes.c_long'>
   :param MainDirectionTop: <class 'ctypes.c_long'>
   :param MainDirectionBottom: <class 'ctypes.c_long'>
   :param ct: <class 'ctypes.c_double'>
   :param cb: <class 'ctypes.c_double'>
   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param MaxCompressionHeight: <class 'ctypes.c_double'>
   :param kc_compression: <class 'ctypes.c_double'>
   :param kc_tension: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param ShortTerm: <class 'ctypes.c_long'>
   :param ShearReinforcementAngle: <class 'ctypes.c_double'>
   :param ShearCrackAngle: <class 'ctypes.c_double'>
   :param TakeConcTensileStrengthNL: <class 'ctypes.c_long'>
   :param ShrinkageEps: <class 'ctypes.c_double'>
   :param RCNonlinearSurfType: <class 'ctypes.c_long'>
   :param ReinforcementType: <class 'ctypes.c_long'>
   :param AlphaAngle: <class 'ctypes.c_double'>
   :param BetaAngle: <class 'ctypes.c_double'>
   :param CalcFromLimitingCrackWidth: <class 'ctypes.c_long'>
   :param wk_b: <class 'ctypes.c_double'>
   :param wk2_b: <class 'ctypes.c_double'>
   :param wk_t: <class 'ctypes.c_double'>
   :param wk2_t: <class 'ctypes.c_double'>
   :param ApproximateLevelArm: <class 'ctypes.c_long'>
   :param SeelhoferMartiEquation: <class 'ctypes.c_long'>
   :param TrapSheetOnlyFormWork: <class 'ctypes.c_long'>
   :param TrapSheetOneLayerReinf: <class 'ctypes.c_long'>
   :param TrapSheetConsidered: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade_SIA

   :param fsk: <class 'ctypes.c_double'>
   :param ks: <class 'ctypes.c_double'>
   :param Epsuk: <class 'ctypes.c_double'>
   :param Epsud: <class 'ctypes.c_double'>
   :param GammaS: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadBeamConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Fgx: <class 'ctypes.c_double'>
   :param Fgy: <class 'ctypes.c_double'>
   :param Fgz: <class 'ctypes.c_double'>
   :param Mgx: <class 'ctypes.c_double'>
   :param Mgy: <class 'ctypes.c_double'>
   :param Mgz: <class 'ctypes.c_double'>
   :param Position: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLineSupportStiffParams

   :param Top: <class 'axisvm.com.core.tlb._16_100.RWallStiffnessParams'>
   :param Bottom: <class 'axisvm.com.core.tlb._16_100.RWallStiffnessParams'>

.. py:class:: axisvm.com.tlb.RLinearFootingParams

   :param VerticalType: <class 'ctypes.c_long'>
   :param MaterialId: <class 'ctypes.c_long'>
   :param GroundToBottom: <class 'ctypes.c_double'>
   :param HeightMain: <class 'ctypes.c_double'>
   :param HeightStep: <class 'ctypes.c_double'>
   :param BlindThickness: <class 'ctypes.c_double'>
   :param FootingSpec: <class 'axisvm.com.core.tlb._16_100.RLinearFootingSpec'>
   :param FootingCalced: <class 'axisvm.com.core.tlb._16_100.RLinearFootingCalced'>

.. py:class:: axisvm.com.tlb.RBulkMemberSupport

   :param SupportType: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearity'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>
   :param SurfaceId1: <class 'ctypes.c_long'>
   :param SurfaceId2: <class 'ctypes.c_long'>
   :param DomainId1: <class 'ctypes.c_long'>
   :param DomainId2: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RBulkMemberWSSupport

   :param SupportType: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param Stiffnesses: <class 'axisvm.com.core.tlb._16_100.RStiffnesses'>
   :param NonLinearity: <class 'axisvm.com.core.tlb._16_100.RNonLinearity'>
   :param Resistances: <class 'axisvm.com.core.tlb._16_100.RResistances'>
   :param ShearStiffness: <class 'ctypes.c_double'>
   :param SurfaceId1: <class 'ctypes.c_long'>
   :param SurfaceId2: <class 'ctypes.c_long'>
   :param DomainId1: <class 'ctypes.c_long'>
   :param DomainId2: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSectionSegmentIntegratedResultant

   :param N: <class 'ctypes.c_double'>
   :param M: <class 'ctypes.c_double'>
   :param V: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReference

   :param ReferenceType: <class 'ctypes.c_long'>
   :param ReferenceData: <class 'axisvm.com.core.tlb._16_100.RRefData'>

.. py:class:: axisvm.com.tlb.RSteelLateralSupport

   :param Pos: <class 'ctypes.c_double'>
   :param Ecc: <class 'ctypes.c_double'>
   :param Ry: <class 'ctypes.c_double'>
   :param Rxx: <class 'ctypes.c_double'>
   :param Rzz: <class 'ctypes.c_double'>
   :param Rw: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignDeflectionResult

   :param CombinationOrLoadCaseID: <class 'ctypes.c_long'>
   :param ez: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLineForceValues

   :param lfvLineType: <class 'ctypes.c_long'>
   :param lfvNx: <class 'ctypes.c_double'>
   :param lfvVy: <class 'ctypes.c_double'>
   :param lfvVz: <class 'ctypes.c_double'>
   :param lfvTx: <class 'ctypes.c_double'>
   :param lfvMy: <class 'ctypes.c_double'>
   :param lfvMz: <class 'ctypes.c_double'>
   :param lfvMyD: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RResultBlockInfo

   :param ResultCase: <class 'ctypes.c_long'>
   :param LoadLevelOrModeShapeOrTimeStep: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSurfaceForceValues

   :param sfvNx: <class 'ctypes.c_double'>
   :param sfvNy: <class 'ctypes.c_double'>
   :param sfvNxy: <class 'ctypes.c_double'>
   :param sfvMx: <class 'ctypes.c_double'>
   :param sfvMy: <class 'ctypes.c_double'>
   :param sfvMxy: <class 'ctypes.c_double'>
   :param sfvVxz: <class 'ctypes.c_double'>
   :param sfvVyz: <class 'ctypes.c_double'>
   :param sfvVSz: <class 'ctypes.c_double'>
   :param sfvN1: <class 'ctypes.c_double'>
   :param sfvN2: <class 'ctypes.c_double'>
   :param sfvAn: <class 'ctypes.c_double'>
   :param sfvM1: <class 'ctypes.c_double'>
   :param sfvM2: <class 'ctypes.c_double'>
   :param sfvAm: <class 'ctypes.c_double'>
   :param sfvNxD: <class 'ctypes.c_double'>
   :param sfvNyD: <class 'ctypes.c_double'>
   :param sfvMxDp: <class 'ctypes.c_double'>
   :param sfvMxDm: <class 'ctypes.c_double'>
   :param sfvMyDp: <class 'ctypes.c_double'>
   :param sfvMyDm: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurfaceForces

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param sfvCenterPoint: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourPoint1: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourPoint2: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourPoint3: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourPoint4: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>
   :param sfvContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RSurfaceForceValues'>

.. py:class:: axisvm.com.tlb.RSurfaceSupportForceValues

   :param Rx: <class 'ctypes.c_double'>
   :param Ry: <class 'ctypes.c_double'>
   :param Rz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurfaceSupportForces

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param ssfvCenterPoint: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourPoint1: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourPoint2: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourPoint3: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourPoint4: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>
   :param ssfvContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RSurfaceSupportForceValues'>

.. py:class:: axisvm.com.tlb.RSpringForceValues

   :param Rx: <class 'ctypes.c_double'>
   :param Ry: <class 'ctypes.c_double'>
   :param Rz: <class 'ctypes.c_double'>
   :param Rxx: <class 'ctypes.c_double'>
   :param Ryy: <class 'ctypes.c_double'>
   :param Rzz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RVirtualBeamForceValues

   :param vbfvNx: <class 'ctypes.c_double'>
   :param vbfvVy: <class 'ctypes.c_double'>
   :param vbfvVz: <class 'ctypes.c_double'>
   :param vbfvTx: <class 'ctypes.c_double'>
   :param vbfvMy: <class 'ctypes.c_double'>
   :param vbfvMz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCombinationElement

   :param LoadCase: <class 'ctypes.c_long'>
   :param Factor: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignDeflectionResults

   :param Min: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignDeflectionResult'>
   :param Max: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignDeflectionResult'>

.. py:class:: axisvm.com.tlb.RWallStiffnessParams

   :param CalcParams: <class 'axisvm.com.core.tlb._16_100.RElementStiffnessParams'>
   :param WallThickness: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RElementStiffnessParams

   :param MaterialId: <class 'ctypes.c_long'>
   :param Height: <class 'ctypes.c_double'>
   :param EndReleaseXTop: <class 'ctypes.c_long'>
   :param EndReleaseXBottom: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRefPoint

   :param P: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RLoadBeamMemberDistributed

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param qx1: <class 'ctypes.c_double'>
   :param qy1: <class 'ctypes.c_double'>
   :param qz1: <class 'ctypes.c_double'>
   :param mx1: <class 'ctypes.c_double'>
   :param my1: <class 'ctypes.c_double'>
   :param mz1: <class 'ctypes.c_double'>
   :param qx2: <class 'ctypes.c_double'>
   :param qy2: <class 'ctypes.c_double'>
   :param qz2: <class 'ctypes.c_double'>
   :param mx2: <class 'ctypes.c_double'>
   :param my2: <class 'ctypes.c_double'>
   :param mz2: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param Position1: <class 'ctypes.c_double'>
   :param Position2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Trapezoid: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RMyMzFi

   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param fi: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnReinforcementParameters

   :param ColumnRebarsId: <class 'ctypes.c_long'>
   :param ConcreteMaterialId: <class 'ctypes.c_long'>
   :param RebarSteelGradeId: <class 'ctypes.c_long'>
   :param CheckingParameters: <class 'axisvm.com.core.tlb._16_100.RColumnCheckingParameters'>
   :param fse: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param UseFctmfl: <class 'ctypes.c_long'>
   :param ShrinkageEps: <class 'ctypes.c_double'>
   :param SpiralStirrup: <class 'ctypes.c_long'>
   :param StirrupSpacing: <class 'axisvm.com.core.tlb._16_100.RColumnStirrupSpacing'>
   :param StirrupDiameters: <class 'axisvm.com.core.tlb._16_100.RColumnStirrupDiameters'>
   :param StirrupZones: <class 'axisvm.com.core.tlb._16_100.RColumnStirrupZones'>
   :param StirrupLegNumY: <class 'ctypes.c_long'>
   :param StirrupLegNumZ: <class 'ctypes.c_long'>
   :param ShearCrackAngle: <class 'ctypes.c_long'>
   :param CapacityDesignParams: <class 'axisvm.com.core.tlb._16_100.RRCColumnCapacityDesignParams'>
   :param CBDetailingRules: <class 'ctypes.c_long'>
   :param SteelMaterialId: <class 'ctypes.c_long'>
   :param ShearRhoFactor: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMyMz

   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNMInteractionDiagMinMax

   :param NMin: <class 'ctypes.c_double'>
   :param NMax: <class 'ctypes.c_double'>
   :param MyMin: <class 'ctypes.c_double'>
   :param MyMax: <class 'ctypes.c_double'>
   :param MzMin: <class 'ctypes.c_double'>
   :param MzMax: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnCheckResult

   :param xRelPos: <class 'ctypes.c_double'>
   :param Passed: <class 'ctypes.c_long'>
   :param Eff_Const_N: <class 'ctypes.c_double'>
   :param Eff_Const_e: <class 'ctypes.c_double'>
   :param My_c: <class 'ctypes.c_double'>
   :param My_e2y_P: <class 'ctypes.c_double'>
   :param My_e2y_N: <class 'ctypes.c_double'>
   :param My_e2z_P: <class 'ctypes.c_double'>
   :param My_e2z_N: <class 'ctypes.c_double'>
   :param Mz_c: <class 'ctypes.c_double'>
   :param Mz_e2y_P: <class 'ctypes.c_double'>
   :param Mz_e2y_N: <class 'ctypes.c_double'>
   :param Mz_e2z_P: <class 'ctypes.c_double'>
   :param Mz_e2z_N: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnForces

   :param Nx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param Vy: <class 'ctypes.c_double'>
   :param Vz: <class 'ctypes.c_double'>
   :param Tx: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnVTCheckResult

   :param xRelPos: <class 'ctypes.c_double'>
   :param Passed: <class 'ctypes.c_long'>
   :param VyR: <class 'ctypes.c_double'>
   :param VzR: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param Ast: <class 'ctypes.c_double'>
   :param Eff_Vy: <class 'ctypes.c_double'>
   :param Eff_Vz: <class 'ctypes.c_double'>
   :param Eff_Vy_Vz: <class 'ctypes.c_double'>
   :param Eff_Vy_Vz_Tx: <class 'ctypes.c_double'>
   :param Eff_Vy_Vz_Tx_max: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRefVector

   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RInfoWindowSwitch

   :param Coordinates: <class 'ctypes.c_long'>
   :param Info: <class 'ctypes.c_long'>
   :param ColourCoding: <class 'ctypes.c_long'>
   :param ColourLegend: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPartialRCBeamDesignParameters

   :param RCBeamCrossSections: <class 'axisvm.com.core.tlb._16_100.RRCBeamCrossSections'>
   :param RCBeamSupports: <class 'axisvm.com.core.tlb._16_100.RRCBeamSupports'>

.. py:class:: axisvm.com.tlb.RRCBeamSupports

   :param StartSupport: <class 'axisvm.com.core.tlb._16_100.RRCBeamSupport'>
   :param EndSupport: <class 'axisvm.com.core.tlb._16_100.RRCBeamSupport'>

.. py:class:: axisvm.com.tlb.RColumnStiffnessParams

   :param CalcParams: <class 'axisvm.com.core.tlb._16_100.RElementStiffnessParams'>
   :param CrossSectionID: <class 'ctypes.c_long'>
   :param EndReleaseYTop: <class 'ctypes.c_long'>
   :param EndReleaseYBottom: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RImperfectionParams

   :param SwayDirection: <class 'ctypes.c_long'>
   :param SwayAngle: <class 'ctypes.c_double'>
   :param BaseHeightType: <class 'ctypes.c_long'>
   :param BaseHeight: <class 'ctypes.c_double'>
   :param StructureAutoHeight: <class 'ctypes.c_long'>
   :param StructureHeight: <class 'ctypes.c_double'>
   :param ColumnsInvolved: <class 'ctypes.c_long'>
   :param Alpha_h: <class 'ctypes.c_double'>
   :param Alpha_m: <class 'ctypes.c_double'>
   :param Phi0: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RTextBoxParameters

   :param NodeId: <class 'ctypes.c_long'>
   :param LayerID: <class 'ctypes.c_long'>
   :param Position: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param LabelOrientation: <class 'ctypes.c_long'>
   :param TextBoxStyle: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCSOptimizationParamsGeneral

   :param ObjectiveOfOptimization: <class 'ctypes.c_long'>
   :param Constraint_h_min: <class 'ctypes.c_double'>
   :param Constraint_h_max: <class 'ctypes.c_double'>
   :param Constraint_b_min: <class 'ctypes.c_double'>
   :param Constraint_b_max: <class 'ctypes.c_double'>
   :param MaximumEfficiency: <class 'ctypes.c_double'>
   :param Custom: <class 'ctypes.c_long'>
   :param NumberOfIterations: <class 'ctypes.c_long'>
   :param Beams: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RNodalMass

   :param Node: <class 'ctypes.c_long'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRefAxis

   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RLoadCombinationGenParameters

   :param ConsiderImperfections: <class 'ctypes.c_long'>
   :param OverwriteGeneratedCombos: <class 'ctypes.c_long'>
   :param OverWriteDuplComboSameType: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRefData

   :param Point: <class 'axisvm.com.core.tlb._16_100.RRefPoint'>
   :param Vector: <class 'axisvm.com.core.tlb._16_100.RRefVector'>
   :param Axis: <class 'axisvm.com.core.tlb._16_100.RRefAxis'>
   :param Plane: <class 'axisvm.com.core.tlb._16_100.RRefPlane'>
   :param Beta: <class 'axisvm.com.core.tlb._16_100.RRefBeta'>

.. py:class:: axisvm.com.tlb.RRefPlane

   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P3: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RRefBeta

   :param Beta: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDisplaySwitch

   :param Parts: <class 'ctypes.c_long'>
   :param NonVisiblePartsGreyed: <class 'ctypes.c_long'>
   :param Guidlines: <class 'ctypes.c_long'>
   :param StructuralGrid: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDomainTrapezoidal

   :param PlateMaterial: <class 'ctypes.c_long'>
   :param InfillMaterial: <class 'ctypes.c_long'>
   :param Direction: <class 'ctypes.c_long'>
   :param Origin: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param h: <class 'ctypes.c_double'>
   :param t: <class 'ctypes.c_double'>
   :param V: <class 'ctypes.c_double'>
   :param d: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param w: <class 'ctypes.c_double'>
   :param P: <class 'ctypes.c_double'>
   :param Eta: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSteelDesignResult

   :param PosX: <class 'ctypes.c_double'>
   :param DesignValue: <class 'ctypes.c_double'>
   :param LimitValue: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSectionSegmentChainIntegratedParameters

   :param StartPoint: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param EndPoint: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param CentreRatio: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RGlobalForces

   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMiscellaneousSettings

   :param Smoothing: <class 'ctypes.c_long'>
   :param MaxAngleLocZ: <class 'ctypes.c_double'>
   :param MaxAngleLocX: <class 'ctypes.c_double'>
   :param IntensityRefVal: <class 'ctypes.c_long'>
   :param CustomVal: <class 'ctypes.c_double'>
   :param SupportsAvgResultsPerMember: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCommonDisplayParameters

   :param CriticalResSettings: <class 'axisvm.com.core.tlb._16_100.RCommonCriticalResultsSettings'>
   :param CutMomentPeaks: <class 'ctypes.c_long'>
   :param DrawInPlane: <class 'ctypes.c_long'>
   :param MiscelSettings: <class 'axisvm.com.core.tlb._16_100.RMiscellaneousSettings'>

.. py:class:: axisvm.com.tlb.RCommonCriticalResultsSettings

   :param InvestigateAllCombos: <class 'ctypes.c_long'>
   :param CritComboFormula: <class 'ctypes.c_long'>
   :param InPersistentAndTransientDesignSituations: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCircleArcGeomData

   :param Center: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param NormalVector: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param Alfa: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RShowSwitches

   :param InfoWindowSwitch: <class 'axisvm.com.core.tlb._16_100.RInfoWindowSwitch'>
   :param DisplaySwitch: <class 'axisvm.com.core.tlb._16_100.RDisplaySwitch'>

.. py:class:: axisvm.com.tlb.RFrequencyParameters

   :param Frequency: <class 'ctypes.c_double'>
   :param EigenValConv: <class 'ctypes.c_double'>
   :param EigenVecConv: <class 'ctypes.c_double'>
   :param EigenValConvLimit: <class 'ctypes.c_double'>
   :param EigenVecConvLimit: <class 'ctypes.c_double'>
   :param Iteration: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSteelDesignParameters

   :param MSZ_STAS: <class 'axisvm.com.core.tlb._16_100.RSteelDesignParameters_MSZ_STAS'>
   :param EC_SIA_ITA: <class 'axisvm.com.core.tlb._16_100.RSteelDesignParameters_EC_SIA_ITA'>
   :param NEN: <class 'axisvm.com.core.tlb._16_100.RSteelDesignParameters_NEN'>

.. py:class:: axisvm.com.tlb.RSteelDesignParameters_NEN

   :param BreakAtElements: <class 'ctypes.c_long'>
   :param Kapy: <class 'ctypes.c_double'>
   :param Kapz: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param l1F: <class 'ctypes.c_double'>
   :param l1A: <class 'ctypes.c_double'>
   :param lgF: <class 'ctypes.c_double'>
   :param lgA: <class 'ctypes.c_double'>
   :param ak: <class 'ctypes.c_double'>
   :param Fytot: <class 'ctypes.c_double'>
   :param Fztot: <class 'ctypes.c_double'>
   :param YBraced: <class 'ctypes.c_long'>
   :param ZBraced: <class 'ctypes.c_long'>
   :param Torsion: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCursorSnap

   :param MouseSnap: <class 'ctypes.c_long'>
   :param DeltaX: <class 'ctypes.c_double'>
   :param DeltaY: <class 'ctypes.c_double'>
   :param DeltaZ: <class 'ctypes.c_double'>
   :param CtrlX: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RTimberDesignParameters_EC_SIA_ITA

   :param Ky: <class 'ctypes.c_double'>
   :param Kz: <class 'ctypes.c_double'>
   :param Klt: <class 'ctypes.c_double'>
   :param LoadPosition: <class 'ctypes.c_long'>
   :param Grain: <class 'ctypes.c_long'>
   :param LayerThickness: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCSOptimizationResultsParametric

   :param OptimizationEfficiency: <class 'ctypes.c_double'>
   :param Efficiency: <class 'ctypes.c_double'>
   :param M: <class 'ctypes.c_double'>
   :param DeltaM: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param h: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>
   :param b2: <class 'ctypes.c_double'>
   :param tf2: <class 'ctypes.c_double'>
   :param a: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.REllipseArcGeomData

   :param Center: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param NormalVector: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param Alfa: <class 'ctypes.c_double'>
   :param MajorEndPoint: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param Ratio: <class 'ctypes.c_double'>
   :param StartAlfa: <class 'ctypes.c_double'>
   :param EndAlfa: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNcrParameters

   :param Ncr: <class 'ctypes.c_double'>
   :param EigenValConv: <class 'ctypes.c_double'>
   :param EigenVecConv: <class 'ctypes.c_double'>
   :param EigenValConvLimit: <class 'ctypes.c_double'>
   :param EigenVecConvLimit: <class 'ctypes.c_double'>
   :param Iteration: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RReinforcementCheckValues

   :param rmxdmin_ULS: <class 'ctypes.c_double'>
   :param rmxdmax_ULS: <class 'ctypes.c_double'>
   :param rmydmin_ULS: <class 'ctypes.c_double'>
   :param rmydmax_ULS: <class 'ctypes.c_double'>
   :param rmxumin_ULS: <class 'ctypes.c_double'>
   :param rmxumax_ULS: <class 'ctypes.c_double'>
   :param rmyumin_ULS: <class 'ctypes.c_double'>
   :param rmyumax_ULS: <class 'ctypes.c_double'>
   :param rmxdmin_SLS: <class 'ctypes.c_double'>
   :param rmxdmax_SLS: <class 'ctypes.c_double'>
   :param rmydmin_SLS: <class 'ctypes.c_double'>
   :param rmydmax_SLS: <class 'ctypes.c_double'>
   :param rmxumin_SLS: <class 'ctypes.c_double'>
   :param rmxumax_SLS: <class 'ctypes.c_double'>
   :param rmyumin_SLS: <class 'ctypes.c_double'>
   :param rmyumax_SLS: <class 'ctypes.c_double'>
   :param Status: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCSParametricOptimizationParams

   :param General: <class 'axisvm.com.core.tlb._16_100.RCSOptimizationParamsGeneral'>
   :param fixed_h: <class 'ctypes.c_long'>
   :param delta_h: <class 'ctypes.c_double'>
   :param fixed_b: <class 'ctypes.c_long'>
   :param delta_b: <class 'ctypes.c_double'>
   :param fixed_tw: <class 'ctypes.c_long'>
   :param delta_tw: <class 'ctypes.c_double'>
   :param fixed_tf: <class 'ctypes.c_long'>
   :param delta_tf: <class 'ctypes.c_double'>
   :param fixed_b2: <class 'ctypes.c_long'>
   :param b2_min: <class 'ctypes.c_double'>
   :param b2_max: <class 'ctypes.c_double'>
   :param delta_b2: <class 'ctypes.c_double'>
   :param fixed_tf2: <class 'ctypes.c_long'>
   :param tf2_min: <class 'ctypes.c_double'>
   :param tf2_max: <class 'ctypes.c_double'>
   :param delta_tf2: <class 'ctypes.c_double'>
   :param fixed_a: <class 'ctypes.c_long'>
   :param a_min: <class 'ctypes.c_double'>
   :param a_max: <class 'ctypes.c_double'>
   :param delta_a: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSteelLTBSupport

   :param AbsPos: <class 'ctypes.c_double'>
   :param Ecc: <class 'ctypes.c_double'>
   :param Ry: <class 'ctypes.c_double'>
   :param Rxx: <class 'ctypes.c_double'>
   :param Rzz: <class 'ctypes.c_double'>
   :param Rw: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadEmptySurfaceLine

   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param SegmentId: <class 'ctypes.c_long'>
   :param GlbStartx: <class 'ctypes.c_double'>
   :param GlbStarty: <class 'ctypes.c_double'>
   :param GlbStartz: <class 'ctypes.c_double'>
   :param GlbEndx: <class 'ctypes.c_double'>
   :param GlbEndy: <class 'ctypes.c_double'>
   :param GlbEndz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RTimberDesignParameters_EC_V153

   :param Ky: <class 'ctypes.c_double'>
   :param Kz: <class 'ctypes.c_double'>
   :param Klt: <class 'ctypes.c_double'>
   :param LoadPosition: <class 'ctypes.c_long'>
   :param Grain: <class 'ctypes.c_long'>
   :param LayerThickness: <class 'ctypes.c_double'>
   :param slsEyLimitDef: <class 'ctypes.c_long'>
   :param slsEzLimitDef: <class 'ctypes.c_long'>
   :param slsUyDef: <class 'ctypes.c_long'>
   :param slsUzDef: <class 'ctypes.c_long'>
   :param slsEMode: <class 'ctypes.c_long'>
   :param slsLMode: <class 'ctypes.c_long'>
   :param slsPreCamberCurve: <class 'ctypes.c_long'>
   :param slsEyLimit: <class 'ctypes.c_double'>
   :param slsEzLimit: <class 'ctypes.c_double'>
   :param slsCustomLy: <class 'ctypes.c_double'>
   :param slsCustomLz: <class 'ctypes.c_double'>
   :param slsUy: <class 'ctypes.c_double'>
   :param slsUz: <class 'ctypes.c_double'>
   :param slsCreepMode: <class 'ctypes.c_long'>
   :param slsPhi: <class 'ctypes.c_double'>
   :param FireResistDef: <class 'ctypes.c_long'>
   :param fpKy: <class 'ctypes.c_double'>
   :param fpKz: <class 'ctypes.c_double'>
   :param fpKLT: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCrackWidths

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param cwvCenterPoint_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvCenterPoint_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint1_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint1_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint2_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint2_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint3_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint3_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint4_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourPoint4_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint1_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint1_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint2_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint2_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint3_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint3_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint4_Bottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param cwvContourLineMidPoint4_Top: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>

.. py:class:: axisvm.com.tlb.RCrackWidthValues

   :param Asbx: <class 'ctypes.c_double'>
   :param Asby: <class 'ctypes.c_double'>
   :param Astx: <class 'ctypes.c_double'>
   :param Asty: <class 'ctypes.c_double'>
   :param Nx: <class 'ctypes.c_double'>
   :param Ny: <class 'ctypes.c_double'>
   :param Nxy: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mxy: <class 'ctypes.c_double'>
   :param wR_p: <class 'ctypes.c_double'>
   :param wR_s: <class 'ctypes.c_double'>
   :param wk_p: <class 'ctypes.c_double'>
   :param wk_s: <class 'ctypes.c_double'>
   :param wk2_p: <class 'ctypes.c_double'>
   :param wk2_s: <class 'ctypes.c_double'>
   :param xs2_p: <class 'ctypes.c_double'>
   :param xs2_s: <class 'ctypes.c_double'>
   :param Ss2_p: <class 'ctypes.c_double'>
   :param Ss2_s: <class 'ctypes.c_double'>
   :param Sb1_p: <class 'ctypes.c_double'>
   :param Sb1_s: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCommonCriticalResultsSettings_V161

   :param InvestigateAllCombos: <class 'ctypes.c_long'>
   :param CritComboFormula: <class 'ctypes.c_long'>
   :param InPersistentAndTransientDesignSituations: <class 'ctypes.c_long'>
   :param SemiAutoSLS: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RGridOptions

   :param DisplayGrid: <class 'ctypes.c_long'>
   :param DeltaX: <class 'ctypes.c_double'>
   :param DeltaY: <class 'ctypes.c_double'>
   :param DeltaZ: <class 'ctypes.c_double'>
   :param GridType: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceLine

   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param SegmentId: <class 'ctypes.c_long'>
   :param GlbStartx: <class 'ctypes.c_double'>
   :param GlbStarty: <class 'ctypes.c_double'>
   :param GlbStartz: <class 'ctypes.c_double'>
   :param GlbEndx: <class 'ctypes.c_double'>
   :param GlbEndy: <class 'ctypes.c_double'>
   :param GlbEndz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.REditingOptions

   :param ConstAngle_DeltaAlpha: <class 'ctypes.c_double'>
   :param ConstAngle_CustomAlpha: <class 'ctypes.c_double'>
   :param EditingToler: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RTotalLoads

   :param ExternalForces: <class 'axisvm.com.core.tlb._16_100.RGlobalForces'>
   :param UnbalancedLoads: <class 'axisvm.com.core.tlb._16_100.RGlobalForces'>

.. py:class:: axisvm.com.tlb.RLoadDomainPolyArea

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param LoadDistributionType: <class 'ctypes.c_long'>
   :param Component: <class 'ctypes.c_long'>
   :param P1: <class 'ctypes.c_double'>
   :param P2: <class 'ctypes.c_double'>
   :param P3: <class 'ctypes.c_double'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param x3: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param y3: <class 'ctypes.c_double'>
   :param z1: <class 'ctypes.c_double'>
   :param z2: <class 'ctypes.c_double'>
   :param z3: <class 'ctypes.c_double'>
   :param WindowLoad: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSegmentChainPointCrackWidthValues

   :param covBottom: <class 'axisvm.com.core.tlb._16_100.RSegmentChainCrackWidthValues'>
   :param covTop: <class 'axisvm.com.core.tlb._16_100.RSegmentChainCrackWidthValues'>

.. py:class:: axisvm.com.tlb.RSegmentChainCrackWidthValues

   :param wk_p: <class 'ctypes.c_double'>
   :param wk_s: <class 'ctypes.c_double'>
   :param wk2_p: <class 'ctypes.c_double'>
   :param wk2_s: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RActualReinforcement

   :param ds: <class 'ctypes.c_double'>
   :param spacing: <class 'ctypes.c_double'>
   :param RebarType: <class 'ctypes.c_long'>
   :param Cover: <class 'ctypes.c_double'>
   :param Alpha: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSteelDesignParameters_V153

   :param EC_SIA_ITA: <class 'axisvm.com.core.tlb._16_100.RSteelDesignParameters_EC_SIA_ITA_V153'>
   :param MSZ_STAS: <class 'axisvm.com.core.tlb._16_100.RSteelDesignParameters_MSZ_STAS'>
   :param NEN: <class 'axisvm.com.core.tlb._16_100.RSteelDesignParameters_NEN'>

.. py:class:: axisvm.com.tlb.RCircularFootingCalced

   :param Calculated: <class 'ctypes.c_long'>
   :param Diam: <class 'ctypes.c_double'>
   :param StepMeasureSource: <class 'ctypes.c_long'>
   :param DeltaR: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLineGeomData

   :param CircleArc: <class 'axisvm.com.core.tlb._16_100.RCircleArcGeomData'>
   :param EllipseArc: <class 'axisvm.com.core.tlb._16_100.REllipseArcGeomData'>

.. py:class:: axisvm.com.tlb.RLineData

   :param NodeId1: <class 'ctypes.c_long'>
   :param NodeId2: <class 'ctypes.c_long'>
   :param GeomType: <class 'ctypes.c_long'>
   :param CircleArc: <class 'axisvm.com.core.tlb._16_100.RCircleArcGeomData'>
   :param EllipseArc: <class 'axisvm.com.core.tlb._16_100.REllipseArcGeomData'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_ITA

   :param VariableAngleTrussMethod: <class 'ctypes.c_long'>
   :param Theta: <class 'ctypes.c_double'>
   :param fse: <class 'ctypes.c_double'>
   :param CrackWidthCheck: <class 'ctypes.c_long'>
   :param MaxCrackWidth_Top: <class 'ctypes.c_double'>
   :param MaxCrackWidth_Bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param ShortTerm: <class 'ctypes.c_long'>
   :param Deflection_Beam_L_div: <class 'ctypes.c_double'>
   :param Deflection_Cantilever_L_div: <class 'ctypes.c_double'>
   :param SeismicZone: <class 'ctypes.c_long'>
   :param PlasticHinges: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHinges'>

.. py:class:: axisvm.com.tlb.RRCBeamPlasticHinges

   :param EnablePlasticHinges: <class 'ctypes.c_long'>
   :param Hinge1: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHingeParams'>
   :param Hinge2: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHingeParams'>
   :param Pos_Hinge1: <class 'ctypes.c_double'>
   :param Pos_Hinge2: <class 'ctypes.c_double'>
   :param MinRebarDiameter: <class 'ctypes.c_double'>
   :param GammaRd: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamPlasticHingeParams

   :param Active: <class 'ctypes.c_long'>
   :param AppliedReinforcement: <class 'ctypes.c_long'>
   :param As_Bottom: <class 'ctypes.c_double'>
   :param As_Top: <class 'ctypes.c_double'>
   :param Depth_Bottom: <class 'ctypes.c_double'>
   :param Depth_Top: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpectrumData_ITA

   :param SubsoilClass: <class 'ctypes.c_long'>
   :param agr: <class 'ctypes.c_double'>
   :param F0: <class 'ctypes.c_double'>
   :param Tsc: <class 'ctypes.c_double'>
   :param TopographicCategory: <class 'ctypes.c_long'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_EC

   :param VariableAngleTrussMethod: <class 'ctypes.c_long'>
   :param Theta: <class 'ctypes.c_double'>
   :param fse: <class 'ctypes.c_double'>
   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param CrackWidthCheck: <class 'ctypes.c_long'>
   :param MaxCrackWidth_Top: <class 'ctypes.c_double'>
   :param MaxCrackWidth_Bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param ShortTerm: <class 'ctypes.c_long'>
   :param Deflection_Beam_L_div: <class 'ctypes.c_double'>
   :param Deflection_Cantilever_L_div: <class 'ctypes.c_double'>
   :param TopSurface: <class 'ctypes.c_long'>
   :param BottomSurface: <class 'ctypes.c_long'>
   :param StructClass: <class 'ctypes.c_long'>
   :param SeismicZone: <class 'ctypes.c_long'>
   :param PlasticHinges: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHinges'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_SIA

   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param TopSurface: <class 'ctypes.c_long'>
   :param BottomSurface: <class 'ctypes.c_long'>
   :param Deflection_Beam_L_div: <class 'ctypes.c_double'>
   :param Deflection_Cantilever_L_div: <class 'ctypes.c_double'>
   :param VariableAngleTrussMethod: <class 'ctypes.c_long'>
   :param Theta: <class 'ctypes.c_double'>
   :param CrackWidthCheck: <class 'ctypes.c_long'>
   :param MaxCrackWidth_Top: <class 'ctypes.c_double'>
   :param MaxCrackWidth_Bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param SeismicZone: <class 'ctypes.c_long'>
   :param PlasticHinges: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHinges'>

.. py:class:: axisvm.com.tlb.RSeismicSensitivityResults

   :param ResultsValidX: <class 'ctypes.c_long'>
   :param ResultsValidY: <class 'ctypes.c_long'>
   :param ThetaMax_x: <class 'ctypes.c_double'>
   :param ThetaMax_y: <class 'ctypes.c_double'>
   :param Ptot: <class 'ctypes.c_double'>
   :param Vtot_x: <class 'ctypes.c_double'>
   :param Vtot_y: <class 'ctypes.c_double'>
   :param d_max_x: <class 'ctypes.c_double'>
   :param d_max_y: <class 'ctypes.c_double'>
   :param S_x: <class 'ctypes.c_double'>
   :param S_y: <class 'ctypes.c_double'>
   :param Gm_x: <class 'ctypes.c_double'>
   :param Gm_y: <class 'ctypes.c_double'>
   :param M_x: <class 'ctypes.c_double'>
   :param M_y: <class 'ctypes.c_double'>
   :param M_z: <class 'ctypes.c_double'>
   :param Imz: <class 'ctypes.c_double'>
   :param Error: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSpectrumData_STAS

   :param SubsoilClass: <class 'ctypes.c_long'>
   :param agr: <class 'ctypes.c_double'>
   :param beta0: <class 'ctypes.c_double'>
   :param TB: <class 'ctypes.c_double'>
   :param TC: <class 'ctypes.c_double'>
   :param TD: <class 'ctypes.c_double'>
   :param gammaI: <class 'ctypes.c_double'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RStructuralGridParams

   :param Plane: <class 'ctypes.c_long'>
   :param WorkPlaneOrStoreyIndex: <class 'ctypes.c_long'>
   :param PlaneOffset: <class 'ctypes.c_double'>
   :param Visibility: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSpectrumData_SIA

   :param SubsoilClass: <class 'ctypes.c_long'>
   :param agr: <class 'ctypes.c_double'>
   :param S: <class 'ctypes.c_double'>
   :param TB: <class 'ctypes.c_double'>
   :param TC: <class 'ctypes.c_double'>
   :param TD: <class 'ctypes.c_double'>
   :param gammaI: <class 'ctypes.c_double'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpectrumData_DIN

   :param SubsoilClass: <class 'ctypes.c_long'>
   :param agr: <class 'ctypes.c_double'>
   :param S: <class 'ctypes.c_double'>
   :param beta0: <class 'ctypes.c_double'>
   :param TB: <class 'ctypes.c_double'>
   :param TC: <class 'ctypes.c_double'>
   :param TD: <class 'ctypes.c_double'>
   :param gammaI: <class 'ctypes.c_double'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RXLAMSurfaceEfficiencies

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param xsevCenterPoint: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourPoint1: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourPoint2: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourPoint3: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourPoint4: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>
   :param xsevContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceEfficiencyValues'>

.. py:class:: axisvm.com.tlb.RXLAMSurfaceEfficiencyValues

   :param xsev_M_N_0: <class 'ctypes.c_double'>
   :param xsev_M_N_90: <class 'ctypes.c_double'>
   :param xsev_V_T: <class 'ctypes.c_double'>
   :param xsev_Vr_N: <class 'ctypes.c_double'>
   :param xsev_Max: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RStructuralGridGenerationParams

   :param Offset: <class 'axisvm.com.core.tlb._16_100.RPoint2d'>
   :param RotDeg: <class 'ctypes.c_double'>
   :param Colour: <class 'ctypes.c_long'>
   :param Extension: <class 'ctypes.c_double'>
   :param LabelTypeX: <class 'ctypes.c_long'>
   :param GenerateInPositiveX: <class 'ctypes.c_long'>
   :param LabelTypeY: <class 'ctypes.c_long'>
   :param GenerateInPositiveY: <class 'ctypes.c_long'>
   :param ShowStructuralGridLineTitle: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RVerticalDisplacementValues

   :param w1: <class 'ctypes.c_double'>
   :param w2: <class 'ctypes.c_double'>
   :param w3: <class 'ctypes.c_double'>
   :param wtot: <class 'ctypes.c_double'>
   :param wbij: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RTimberDesignResult

   :param PosX: <class 'ctypes.c_double'>
   :param DesignValue: <class 'ctypes.c_double'>
   :param LimitValue: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RPartItem

   :param ItemType: <class 'ctypes.c_long'>
   :param Id: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.REnabledLogicalParts

   :param By_Material: <class 'ctypes.c_long'>
   :param By_CrossSection: <class 'ctypes.c_long'>
   :param By_CrossSection_LineType: <class 'ctypes.c_long'>
   :param By_CrossSection_ArchitecturalLineElementType: <class 'ctypes.c_long'>
   :param By_DomainType_Thickness: <class 'ctypes.c_long'>
   :param By_ArchitecturalDomainElementType_Thickness: <class 'ctypes.c_long'>
   :param By_Stories: <class 'ctypes.c_long'>
   :param By_StructuralGridLines: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RReinforcementCheck

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param rcvCenterPoint: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourPoint1: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourPoint2: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourPoint3: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourPoint4: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>
   :param rcvContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RReinforcementCheckValues'>

.. py:class:: axisvm.com.tlb.RWindowPosition

   :param Top: <class 'ctypes.c_long'>
   :param Left: <class 'ctypes.c_long'>
   :param Width: <class 'ctypes.c_long'>
   :param Height: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCrossSectionUserParams

   :param lParam: <class 'ctypes.c_long'>
   :param dParam1: <class 'ctypes.c_double'>
   :param dParam2: <class 'ctypes.c_double'>
   :param dParam3: <class 'ctypes.c_double'>
   :param dParam4: <class 'ctypes.c_double'>
   :param dParam5: <class 'ctypes.c_double'>
   :param dParam6: <class 'ctypes.c_double'>
   :param dParam7: <class 'ctypes.c_double'>
   :param dParam8: <class 'ctypes.c_double'>
   :param dParam9: <class 'ctypes.c_double'>
   :param dParam10: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDoubleWedgedI

   :param Process: <class 'ctypes.c_long'>
   :param h1: <class 'ctypes.c_double'>
   :param b1: <class 'ctypes.c_double'>
   :param tw1: <class 'ctypes.c_double'>
   :param tf1: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param h2: <class 'ctypes.c_double'>
   :param b2: <class 'ctypes.c_double'>
   :param tw2: <class 'ctypes.c_double'>
   :param tf2: <class 'ctypes.c_double'>
   :param h3: <class 'ctypes.c_double'>
   :param b3: <class 'ctypes.c_double'>
   :param tw3: <class 'ctypes.c_double'>
   :param tf3: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCrossSectionHSQ

   :param h: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param b1: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf1: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCrossSectionHSQA

   :param h: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param b1: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf1: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>
   :param C: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCrossSection2IX

   :param h: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param Process: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCrossSectionComposite

   :param CrossSectionIndex: <class 'ctypes.c_long'>
   :param OuterMaterialIndex: <class 'ctypes.c_long'>
   :param CrossSectionMaterialIndex: <class 'ctypes.c_long'>
   :param CrossSectionFillMaterialIndex: <class 'ctypes.c_long'>
   :param CrossSectionAlign: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCrossSectionIFB

   :param h: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param b2: <class 'ctypes.c_double'>
   :param v2: <class 'ctypes.c_double'>
   :param Process: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDoubleLClosed

   :param h: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param tw: <class 'ctypes.c_double'>
   :param tf: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param a: <class 'ctypes.c_double'>
   :param Process: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceDistributed

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param SurfaceId: <class 'ctypes.c_long'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>
   :param qz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRebarSteelGrade_NEN

   :param fsrep: <class 'ctypes.c_double'>
   :param fs: <class 'ctypes.c_double'>
   :param esu: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignBendingResult

   :param M: <class 'ctypes.c_double'>
   :param Ast: <class 'ctypes.c_double'>
   :param Astmin: <class 'ctypes.c_double'>
   :param Asc: <class 'ctypes.c_double'>
   :param Ascmin: <class 'ctypes.c_double'>
   :param xc: <class 'ctypes.c_double'>
   :param MErrorMessage: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadTrussStress

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param P: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSection

   :param SectionType: <class 'ctypes.c_long'>
   :param Name: <class 'comtypes.BSTR'>
   :param Visible: <class 'ctypes.c_long'>
   :param P: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param N: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param SegmentEndP: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param InAllResultBlocks: <class 'ctypes.c_long'>
   :param ResultBlock: <class 'axisvm.com.core.tlb._16_100.RResultBlock'>
   :param ForAllResultComponents: <class 'ctypes.c_long'>
   :param ResultComponent: <class 'ctypes.c_long'>
   :param DisplayMode: <class 'ctypes.c_long'>
   :param L: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param DiagOnBothSide: <class 'ctypes.c_long'>
   :param DiagInPlane: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RXLAMParams

   :param XLAMindex: <class 'ctypes.c_long'>
   :param TopLayerDirection: <class 'ctypes.c_long'>
   :param ServiceClass: <class 'ctypes.c_long'>
   :param k_def: <class 'ctypes.c_double'>
   :param k_sys: <class 'ctypes.c_long'>
   :param k_fin: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDistributedMovingLoadOnBeam

   :param SystemGL: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Position1: <class 'ctypes.c_double'>
   :param Fx1: <class 'ctypes.c_double'>
   :param Fy1: <class 'ctypes.c_double'>
   :param Fz1: <class 'ctypes.c_double'>
   :param Position2: <class 'ctypes.c_double'>
   :param Fx2: <class 'ctypes.c_double'>
   :param Fy2: <class 'ctypes.c_double'>
   :param Fz2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadBeamFault

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param DL: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadDomainConstant

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>
   :param qz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignResult

   :param Top: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignBendingResult'>
   :param Bottom: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignBendingResult'>
   :param Vsdred_Min: <class 'ctypes.c_double'>
   :param Vsdred_Max: <class 'ctypes.c_double'>
   :param Ved_Vrd: <class 'ctypes.c_double'>
   :param S: <class 'ctypes.c_double'>
   :param sv: <class 'ctypes.c_double'>
   :param smax: <class 'ctypes.c_double'>
   :param VErrorMessage: <class 'ctypes.c_long'>
   :param Tsd: <class 'ctypes.c_double'>
   :param Ted_Trd: <class 'ctypes.c_double'>
   :param st: <class 'ctypes.c_double'>
   :param Astor: <class 'ctypes.c_double'>
   :param x: <class 'ctypes.c_double'>
   :param VRdc: <class 'ctypes.c_double'>
   :param VRds: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnCheckingParameters

   :param CalcEccIncy: <class 'ctypes.c_long'>
   :param CalcEccIncz: <class 'ctypes.c_long'>
   :param CalcEcc2Y: <class 'ctypes.c_long'>
   :param CalcEcc2Z: <class 'ctypes.c_long'>
   :param Ky: <class 'ctypes.c_double'>
   :param Kz: <class 'ctypes.c_double'>
   :param IsCustomLength: <class 'ctypes.c_long'>
   :param ColumnLength: <class 'ctypes.c_double'>
   :param fieff_EC_ITA: <class 'ctypes.c_double'>
   :param SwayImp: <class 'ctypes.c_long'>
   :param BucklingModeY: <class 'ctypes.c_long'>
   :param BucklingModeZ: <class 'ctypes.c_long'>
   :param ShrinkCreepEpsSIA: <class 'ctypes.c_double'>
   :param ApproximateCurvatureSIA: <class 'ctypes.c_long'>
   :param Sum2ndEccentricites: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadLineDistributed

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param qx1: <class 'ctypes.c_double'>
   :param qy1: <class 'ctypes.c_double'>
   :param qz1: <class 'ctypes.c_double'>
   :param mx1: <class 'ctypes.c_double'>
   :param my1: <class 'ctypes.c_double'>
   :param mz1: <class 'ctypes.c_double'>
   :param qx2: <class 'ctypes.c_double'>
   :param qy2: <class 'ctypes.c_double'>
   :param qz2: <class 'ctypes.c_double'>
   :param mx2: <class 'ctypes.c_double'>
   :param my2: <class 'ctypes.c_double'>
   :param mz2: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param Position1: <class 'ctypes.c_double'>
   :param Position2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Trapezoid: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadRibConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Fgx: <class 'ctypes.c_double'>
   :param Fgy: <class 'ctypes.c_double'>
   :param Fgz: <class 'ctypes.c_double'>
   :param Mgx: <class 'ctypes.c_double'>
   :param Mgy: <class 'ctypes.c_double'>
   :param Mgz: <class 'ctypes.c_double'>
   :param Position: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadRibThermal

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Tref: <class 'ctypes.c_double'>
   :param Ttop: <class 'ctypes.c_double'>
   :param Tbot: <class 'ctypes.c_double'>
   :param Axis: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadTrussFault

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param DL: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadTrussThermal

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>
   :param Tref: <class 'ctypes.c_double'>
   :param T0: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceEdge

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param SurfaceId: <class 'ctypes.c_long'>
   :param qx1: <class 'ctypes.c_double'>
   :param qx2: <class 'ctypes.c_double'>
   :param qx3: <class 'ctypes.c_double'>
   :param qx4: <class 'ctypes.c_double'>
   :param qy1: <class 'ctypes.c_double'>
   :param qy2: <class 'ctypes.c_double'>
   :param qy3: <class 'ctypes.c_double'>
   :param qy4: <class 'ctypes.c_double'>
   :param qz1: <class 'ctypes.c_double'>
   :param qz2: <class 'ctypes.c_double'>
   :param qz3: <class 'ctypes.c_double'>
   :param qz4: <class 'ctypes.c_double'>
   :param System1: <class 'ctypes.c_long'>
   :param System2: <class 'ctypes.c_long'>
   :param System3: <class 'ctypes.c_long'>
   :param System4: <class 'ctypes.c_long'>
   :param EdgeLoaded1: <class 'ctypes.c_long'>
   :param EdgeLoaded2: <class 'ctypes.c_long'>
   :param EdgeLoaded3: <class 'ctypes.c_long'>
   :param EdgeLoaded4: <class 'ctypes.c_long'>
   :param DistributionType1: <class 'ctypes.c_long'>
   :param DistributionType2: <class 'ctypes.c_long'>
   :param DistributionType3: <class 'ctypes.c_long'>
   :param DistributionType4: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param SurfaceId: <class 'ctypes.c_long'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param x: <class 'ctypes.c_double'>
   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>
   :param ReferenceId: <class 'ctypes.c_long'>
   :param SystemGLR: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainPolyLine

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Nx: <class 'ctypes.c_double'>
   :param Ny: <class 'ctypes.c_double'>
   :param Nz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadDomainPolyAssoc

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Nx: <class 'ctypes.c_double'>
   :param Ny: <class 'ctypes.c_double'>
   :param Nz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceToBeam

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Px: <class 'ctypes.c_double'>
   :param Py: <class 'ctypes.c_double'>
   :param Pz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadDomainFluid

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param Direction: <class 'ctypes.c_long'>
   :param Coord1: <class 'ctypes.c_double'>
   :param Coord2: <class 'ctypes.c_double'>
   :param P1: <class 'ctypes.c_double'>
   :param P2: <class 'ctypes.c_double'>
   :param DomainId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceFluid

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param Direction: <class 'ctypes.c_long'>
   :param Coord1: <class 'ctypes.c_double'>
   :param Coord2: <class 'ctypes.c_double'>
   :param P1: <class 'ctypes.c_double'>
   :param P2: <class 'ctypes.c_double'>
   :param SurfaceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainLinear

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param LoadDistributionType: <class 'ctypes.c_long'>
   :param Component: <class 'ctypes.c_long'>
   :param P1: <class 'ctypes.c_double'>
   :param P2: <class 'ctypes.c_double'>
   :param P3: <class 'ctypes.c_double'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param x3: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param y3: <class 'ctypes.c_double'>
   :param z1: <class 'ctypes.c_double'>
   :param z2: <class 'ctypes.c_double'>
   :param z3: <class 'ctypes.c_double'>
   :param WindowLoad: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDynamic

   :param DynamicLoadType: <class 'ctypes.c_long'>
   :param LoadCaseId: <class 'ctypes.c_long'>
   :param NodeId: <class 'ctypes.c_long'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>
   :param ReferenceId: <class 'ctypes.c_long'>
   :param FxFunctionId: <class 'ctypes.c_long'>
   :param FyFunctionId: <class 'ctypes.c_long'>
   :param FzFunctionId: <class 'ctypes.c_long'>
   :param MxFunctionId: <class 'ctypes.c_long'>
   :param MyFunctionId: <class 'ctypes.c_long'>
   :param MzFunctionId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadBeamMemberConcentrated

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param Fgx: <class 'ctypes.c_double'>
   :param Fgy: <class 'ctypes.c_double'>
   :param Fgz: <class 'ctypes.c_double'>
   :param Mgx: <class 'ctypes.c_double'>
   :param Mgy: <class 'ctypes.c_double'>
   :param Mgz: <class 'ctypes.c_double'>
   :param Position: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadRibMemberDistributed

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param qx1: <class 'ctypes.c_double'>
   :param qy1: <class 'ctypes.c_double'>
   :param qz1: <class 'ctypes.c_double'>
   :param mx1: <class 'ctypes.c_double'>
   :param my1: <class 'ctypes.c_double'>
   :param mz1: <class 'ctypes.c_double'>
   :param qx2: <class 'ctypes.c_double'>
   :param qy2: <class 'ctypes.c_double'>
   :param qz2: <class 'ctypes.c_double'>
   :param mx2: <class 'ctypes.c_double'>
   :param my2: <class 'ctypes.c_double'>
   :param mz2: <class 'ctypes.c_double'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param Position1: <class 'ctypes.c_double'>
   :param Position2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Trapezoid: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainPolyLineItem

   :param StartPoint: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param EndPoint: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param LineGeomType: <class 'ctypes.c_long'>
   :param CircleArcGeomData: <class 'axisvm.com.core.tlb._16_100.RCircleArcGeomData'>
   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param ItemType: <class 'ctypes.c_long'>
   :param ElementId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadPanelLinear

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LoadPanelId: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param LoadDistributionType: <class 'ctypes.c_long'>
   :param Component: <class 'ctypes.c_long'>
   :param P1: <class 'ctypes.c_double'>
   :param P2: <class 'ctypes.c_double'>
   :param P3: <class 'ctypes.c_double'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param x3: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param y3: <class 'ctypes.c_double'>
   :param z1: <class 'ctypes.c_double'>
   :param z2: <class 'ctypes.c_double'>
   :param z3: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadPanelPolyArea

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param LoadDistributionType: <class 'ctypes.c_long'>
   :param Component: <class 'ctypes.c_long'>
   :param P1: <class 'ctypes.c_double'>
   :param P2: <class 'ctypes.c_double'>
   :param P3: <class 'ctypes.c_double'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param x3: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param y3: <class 'ctypes.c_double'>
   :param z1: <class 'ctypes.c_double'>
   :param z2: <class 'ctypes.c_double'>
   :param z3: <class 'ctypes.c_double'>
   :param WindowLoad: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadPanelPolyLine

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param Nx: <class 'ctypes.c_double'>
   :param Ny: <class 'ctypes.c_double'>
   :param Nz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadLineSelfWeigth

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param LineId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainConstant_V154

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>
   :param SystemGLR: <class 'ctypes.c_long'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>
   :param qz: <class 'ctypes.c_double'>
   :param WindowLoad: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadSurfaceSelfWeigth

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param SurfaceId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainSelfWeigth

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param DomainId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLoadDomainPolyAssoc_V161

   :param LoadCaseId: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param NormalVector: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>

.. py:class:: axisvm.com.tlb.RShowNumbering

   :param Node: <class 'ctypes.c_long'>
   :param Truss: <class 'ctypes.c_long'>
   :param Beam: <class 'ctypes.c_long'>
   :param Rib: <class 'ctypes.c_long'>
   :param Surface: <class 'ctypes.c_long'>
   :param Domain: <class 'ctypes.c_long'>
   :param Support: <class 'ctypes.c_long'>
   :param Links: <class 'ctypes.c_long'>
   :param Rigid: <class 'ctypes.c_long'>
   :param Diaphragm: <class 'ctypes.c_long'>
   :param Spring: <class 'ctypes.c_long'>
   :param Gap: <class 'ctypes.c_long'>
   :param Material: <class 'ctypes.c_long'>
   :param CrossSection: <class 'ctypes.c_long'>
   :param Reference: <class 'ctypes.c_long'>
   :param ARBO_CRETelems: <class 'ctypes.c_long'>
   :param DesignGroup: <class 'ctypes.c_long'>
   :param OptimisationGroup: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDisplacementValues

   :param ex: <class 'ctypes.c_double'>
   :param ey: <class 'ctypes.c_double'>
   :param ez: <class 'ctypes.c_double'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param eR: <class 'ctypes.c_double'>
   :param fR: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RCSOptimizationResultsPredefinedShapes

   :param OptimizationEfficiency: <class 'ctypes.c_double'>
   :param Efficiency: <class 'ctypes.c_double'>
   :param M: <class 'ctypes.c_double'>
   :param DeltaM: <class 'ctypes.c_double'>
   :param GroupCrossSection: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRibbedDomainParameters

   :param AutoExcentricityType: <class 'ctypes.c_long'>
   :param h: <class 'ctypes.c_double'>
   :param w: <class 'ctypes.c_double'>
   :param d: <class 'ctypes.c_double'>
   :param exc: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RConcentratedMovingLoadOnBeam

   :param SystemGL: <class 'ctypes.c_long'>
   :param Position: <class 'ctypes.c_double'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>
   :param Mx: <class 'ctypes.c_double'>
   :param My: <class 'ctypes.c_double'>
   :param Mz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLinearFootingCalced

   :param Calculated: <class 'ctypes.c_long'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param StepMeasureSource: <class 'ctypes.c_long'>
   :param dx1: <class 'ctypes.c_double'>
   :param dx2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSectionElementData

   :param SurfaceIndex: <class 'ctypes.c_long'>
   :param ContourLineId1: <class 'ctypes.c_long'>
   :param ContourLineRatio1: <class 'ctypes.c_double'>
   :param ContourLineId2: <class 'ctypes.c_long'>
   :param ContourLineRatio2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurfacePointIndexes

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Index: <class 'ctypes.c_long'>
   :param ContourPoint2Index: <class 'ctypes.c_long'>
   :param ContourPoint3Index: <class 'ctypes.c_long'>
   :param ContourPoint4Index: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RLinearFootingSpec

   :param FixedX1: <class 'ctypes.c_long'>
   :param FixedX2: <class 'ctypes.c_long'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param StepMeasureSource: <class 'ctypes.c_long'>
   :param dx1: <class 'ctypes.c_double'>
   :param dx2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RImperfectionParams_V153

   :param SwayDirection: <class 'ctypes.c_long'>
   :param SwayAngle: <class 'ctypes.c_double'>
   :param BaseHeightType: <class 'ctypes.c_long'>
   :param BaseHeight: <class 'ctypes.c_double'>
   :param StructureAutoHeight: <class 'ctypes.c_long'>
   :param StructureHeight: <class 'ctypes.c_double'>
   :param Def: <class 'ctypes.c_long'>
   :param MaterialType: <class 'ctypes.c_long'>
   :param ColumnsInvolved: <class 'ctypes.c_long'>
   :param Alpha_h: <class 'ctypes.c_double'>
   :param Alpha_m: <class 'ctypes.c_double'>
   :param Phi0: <class 'ctypes.c_double'>
   :param phi: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RNodeReinforcementValues

   :param Asbx: <class 'ctypes.c_double'>
   :param Asby: <class 'ctypes.c_double'>
   :param Astx: <class 'ctypes.c_double'>
   :param Asty: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLayerShapeAttributes

   :param LayerIndex: <class 'ctypes.c_long'>
   :param Colour: <class 'ctypes.c_long'>
   :param PenStyle: <class 'ctypes.c_long'>
   :param PenWidth: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLayerTextParams

   :param LayerIndex: <class 'ctypes.c_long'>
   :param Colour: <class 'ctypes.c_long'>
   :param PenStyle: <class 'ctypes.c_long'>
   :param PenWidth: <class 'ctypes.c_double'>
   :param FontSize: <class 'ctypes.c_double'>
   :param Angle: <class 'ctypes.c_double'>
   :param AlignmentPoint1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param AlignmentPoint2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param NormalVector: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param HorizontalAlignment: <class 'ctypes.c_long'>
   :param VerticalAlignment: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RShowSymbols

   :param ShowGraphicSymbols: <class 'axisvm.com.core.tlb._16_100.RShowGraphicSymbols'>
   :param ShowLocalSystems: <class 'axisvm.com.core.tlb._16_100.RShowLocalSystems'>
   :param ShowLoads: <class 'axisvm.com.core.tlb._16_100.RShowLoads'>
   :param ObjectContours3D: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRebarPos

   :param TopX: <class 'ctypes.c_double'>
   :param BottomX: <class 'ctypes.c_double'>
   :param TopY: <class 'ctypes.c_double'>
   :param BottomY: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RShowProperties

   :param MaterialName: <class 'ctypes.c_long'>
   :param CrossSectName: <class 'ctypes.c_long'>
   :param BoltedJoint: <class 'ctypes.c_long'>
   :param ColumnReinf: <class 'ctypes.c_long'>
   :param BeamLength: <class 'ctypes.c_long'>
   :param Thickness: <class 'ctypes.c_long'>
   :param DomainArea: <class 'ctypes.c_long'>
   :param COBIAXlabels: <class 'ctypes.c_long'>
   :param LoadValue: <class 'ctypes.c_long'>
   :param MassValue: <class 'ctypes.c_long'>
   :param Units: <class 'ctypes.c_long'>
   :param ConcentratedLoadValue: <class 'ctypes.c_long'>
   :param LineLoadValue: <class 'ctypes.c_long'>
   :param SurfaceLoadValue: <class 'ctypes.c_long'>
   :param TemperatureLoadValue: <class 'ctypes.c_long'>
   :param SelfWeightValue: <class 'ctypes.c_long'>
   :param OtherLoadValue: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RXLAMSurfaceStressValues

   :param xssvSxx_m_T: <class 'ctypes.c_double'>
   :param xssvSyy_m_T: <class 'ctypes.c_double'>
   :param xssvSxy_m_T: <class 'ctypes.c_double'>
   :param xssvSxx_m_B: <class 'ctypes.c_double'>
   :param xssvSyy_m_B: <class 'ctypes.c_double'>
   :param xssvSxy_m_B: <class 'ctypes.c_double'>
   :param xssvSxx_n: <class 'ctypes.c_double'>
   :param xssvSyy_n: <class 'ctypes.c_double'>
   :param xssvSxy_n: <class 'ctypes.c_double'>
   :param xssvSxz_max: <class 'ctypes.c_double'>
   :param xssvSyz_max: <class 'ctypes.c_double'>
   :param xssvSrx_max: <class 'ctypes.c_double'>
   :param xssvSry_max: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RExtendedDisplayParameters

   :param BasicDispParams: <class 'axisvm.com.core.tlb._16_100.RBasicDisplayParameters'>
   :param DisplayAnalysisType: <class 'ctypes.c_long'>
   :param ResultsType: <class 'ctypes.c_long'>
   :param MinMaxType: <class 'ctypes.c_long'>
   :param CriticalResCombinationType: <class 'ctypes.c_long'>
   :param SectPlaneContour: <class 'ctypes.c_long'>
   :param DisplayedEnvelopes: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RShowLabels

   :param ShowNumbering: <class 'axisvm.com.core.tlb._16_100.RShowNumbering'>
   :param ShowProperties: <class 'axisvm.com.core.tlb._16_100.RShowProperties'>
   :param ShowActualReinf: <class 'axisvm.com.core.tlb._16_100.RShowActualReinforcement'>
   :param UseFiniteElements: <class 'ctypes.c_long'>
   :param LabelsOnLines: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RWorldRectangle

   :param Left: <class 'ctypes.c_double'>
   :param Right: <class 'ctypes.c_double'>
   :param Top: <class 'ctypes.c_double'>
   :param Bottom: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RExtendedDisplayParameters_V153

   :param BasicDispParams: <class 'axisvm.com.core.tlb._16_100.RBasicDisplayParameters_V153'>
   :param DisplayAnalysisType: <class 'ctypes.c_long'>
   :param ResultsType: <class 'ctypes.c_long'>
   :param MinMaxType: <class 'ctypes.c_long'>
   :param CriticalResCombinationType: <class 'ctypes.c_long'>
   :param SectPlaneContour: <class 'ctypes.c_long'>
   :param DisplayedEnvelopes: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RCommonDisplayParameters_V161

   :param CriticalResSettings: <class 'axisvm.com.core.tlb._16_100.RCommonCriticalResultsSettings_V161'>
   :param CutMomentPeaks: <class 'ctypes.c_long'>
   :param DrawInPlane: <class 'ctypes.c_long'>
   :param MiscelSettings: <class 'axisvm.com.core.tlb._16_100.RMiscellaneousSettings'>

.. py:class:: axisvm.com.tlb.RPushOverParams

   :param x: <class 'axisvm.com.core.tlb._16_100.RPushOverDirectionParams'>
   :param y: <class 'axisvm.com.core.tlb._16_100.RPushOverDirectionParams'>

.. py:class:: axisvm.com.tlb.RWindLoadParams

   :param a: <class 'ctypes.c_double'>
   :param v_b0: <class 'ctypes.c_double'>
   :param c_season: <class 'ctypes.c_double'>
   :param c_o: <class 'ctypes.c_double'>
   :param TerrainCategoryDifferent: <class 'ctypes.c_long'>
   :param TerrainCat_Xp: <class 'ctypes.c_long'>
   :param TerrainCat_Xm: <class 'ctypes.c_long'>
   :param TerrainCat_Yp: <class 'ctypes.c_long'>
   :param TerrainCat_Ym: <class 'ctypes.c_long'>
   :param CustomDirectionalFactors: <class 'ctypes.c_long'>
   :param c_dir_xp: <class 'ctypes.c_double'>
   :param c_dir_xm: <class 'ctypes.c_double'>
   :param c_dir_yp: <class 'ctypes.c_double'>
   :param c_dir_ym: <class 'ctypes.c_double'>
   :param RoofType: <class 'ctypes.c_long'>
   :param FlatRoofEdgeType: <class 'ctypes.c_long'>
   :param FlatRoofEdgeParam: <class 'ctypes.c_double'>
   :param TorsionalEffect: <class 'ctypes.c_long'>
   :param u_xp: <class 'ctypes.c_double'>
   :param u_xm: <class 'ctypes.c_double'>
   :param u_yp: <class 'ctypes.c_double'>
   :param u_ym: <class 'ctypes.c_double'>
   :param Iw: <class 'ctypes.c_double'>
   :param Zone: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSeismicParams_V153

   :param VibrType: <class 'ctypes.c_long'>
   :param kg: <class 'ctypes.c_double'>
   :param ks: <class 'ctypes.c_double'>
   :param kt: <class 'ctypes.c_double'>
   :param psi: <class 'ctypes.c_double'>
   :param SeismicCombType: <class 'ctypes.c_long'>
   :param qd: <class 'ctypes.c_double'>
   :param ksiV: <class 'ctypes.c_double'>
   :param ModalCombType: <class 'ctypes.c_long'>
   :param Torsion: <class 'ctypes.c_long'>
   :param ExcCoeff: <class 'ctypes.c_double'>
   :param C: <class 'ctypes.c_double'>
   :param nu: <class 'ctypes.c_double'>
   :param LoadCaseLoadCombination: <class 'ctypes.c_long'>
   :param Eta: <class 'ctypes.c_double'>
   :param GroupID: <class 'ctypes.c_long'>
   :param qdy: <class 'ctypes.c_double'>
   :param SeismicLimitState: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RNonLinearAnalysis

   :param LoadCase: <class 'ctypes.c_long'>
   :param SolutionControl: <class 'ctypes.c_long'>
   :param NodeId: <class 'ctypes.c_long'>
   :param Direction: <class 'ctypes.c_long'>
   :param MaxDisplacement: <class 'ctypes.c_double'>
   :param Increments: <class 'ctypes.c_long'>
   :param Iterations: <class 'ctypes.c_long'>
   :param DisplacementConvergenceValue: <class 'ctypes.c_double'>
   :param ForceConvergenceValue: <class 'ctypes.c_double'>
   :param WorkConvergenceValue: <class 'ctypes.c_double'>
   :param EnableDisplacementConvergence: <class 'ctypes.c_long'>
   :param EnableForceConvergence: <class 'ctypes.c_long'>
   :param EnableWorkConvergence: <class 'ctypes.c_long'>
   :param GeometricNonLinearity: <class 'ctypes.c_long'>
   :param ReinforcementCalculation: <class 'ctypes.c_long'>
   :param StoreLastIncrementOnly: <class 'ctypes.c_long'>
   :param ReinforcementCalculationType: <class 'ctypes.c_long'>
   :param ContinueWithoutConvergence: <class 'ctypes.c_long'>
   :param IncrementFunctionId: <class 'ctypes.c_long'>
   :param MaterialNonLinearity: <class 'ctypes.c_long'>
   :param ConsiderCreep: <class 'ctypes.c_long'>
   :param ConsiderShrinkage: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RVibration

   :param LoadCase: <class 'ctypes.c_long'>
   :param Iterations: <class 'ctypes.c_long'>
   :param ModeShapes: <class 'ctypes.c_long'>
   :param EigenValueConvergence: <class 'ctypes.c_double'>
   :param EigenVectorConvergence: <class 'ctypes.c_double'>
   :param ConvertLoadsToMasses: <class 'ctypes.c_long'>
   :param ConcentratedMasses: <class 'ctypes.c_long'>
   :param ConvertConcentratedMassesToLoads: <class 'ctypes.c_long'>
   :param MassControl: <class 'ctypes.c_long'>
   :param ElementMasses: <class 'ctypes.c_long'>
   :param MassComponentX: <class 'ctypes.c_long'>
   :param MassComponentY: <class 'ctypes.c_long'>
   :param MassComponentZ: <class 'ctypes.c_long'>
   :param ConvertSlabsToDiaphragms: <class 'ctypes.c_long'>
   :param MassMatrixType: <class 'ctypes.c_long'>
   :param IncreasedSupportStiffness: <class 'ctypes.c_long'>
   :param MassesTakenIntoAccount: <class 'ctypes.c_long'>
   :param HeightZ: <class 'ctypes.c_double'>
   :param StoryID: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RBuckling

   :param LoadCase: <class 'ctypes.c_long'>
   :param Iterations: <class 'ctypes.c_long'>
   :param ModeShapes: <class 'ctypes.c_long'>
   :param EigenValueConvergence: <class 'ctypes.c_double'>
   :param EigenVectorConvergence: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDynamicAnalysis

   :param LoadCase: <class 'ctypes.c_long'>
   :param StaticLoadCase: <class 'ctypes.c_long'>
   :param LoadCombination: <class 'ctypes.c_long'>
   :param TimeIncrementFunctionId: <class 'ctypes.c_long'>
   :param TimeIncrement: <class 'ctypes.c_double'>
   :param NumberOfIncrements: <class 'ctypes.c_long'>
   :param a: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param MassMatrixType: <class 'ctypes.c_long'>
   :param ConvertLoadsToMasses: <class 'ctypes.c_long'>
   :param ConcentratedMasses: <class 'ctypes.c_long'>
   :param ConvertConcentratedMassesToLoads: <class 'ctypes.c_long'>
   :param MassControl: <class 'ctypes.c_long'>
   :param ElementMasses: <class 'ctypes.c_long'>
   :param MaterialNonLinearity: <class 'ctypes.c_long'>
   :param GeometricNonLinearity: <class 'ctypes.c_long'>
   :param PerformIterations: <class 'ctypes.c_long'>
   :param Iterations: <class 'ctypes.c_long'>
   :param DisplacementConvergenceValue: <class 'ctypes.c_double'>
   :param ForceConvergenceValue: <class 'ctypes.c_double'>
   :param WorkConvergenceValue: <class 'ctypes.c_double'>
   :param EnableDisplacementConvergence: <class 'ctypes.c_long'>
   :param EnableForceConvergence: <class 'ctypes.c_long'>
   :param EnableWorkConvergence: <class 'ctypes.c_long'>
   :param ContinueWithoutConvergence: <class 'ctypes.c_long'>
   :param SavingInterval: <class 'ctypes.c_double'>
   :param LoadsAndNodalMassesForDamping: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPushOverAnalysis

   :param LoadCase: <class 'ctypes.c_long'>
   :param ConstantLoadCase: <class 'ctypes.c_long'>
   :param NodeId: <class 'ctypes.c_long'>
   :param Direction: <class 'ctypes.c_long'>
   :param MaxDisplacement: <class 'ctypes.c_double'>
   :param Increments: <class 'ctypes.c_long'>
   :param Iterations: <class 'ctypes.c_long'>
   :param DisplacementConvergenceValue: <class 'ctypes.c_double'>
   :param ForceConvergenceValue: <class 'ctypes.c_double'>
   :param WorkConvergenceValue: <class 'ctypes.c_double'>
   :param EnableDisplacementConvergence: <class 'ctypes.c_long'>
   :param EnableForceConvergence: <class 'ctypes.c_long'>
   :param EnableWorkConvergence: <class 'ctypes.c_long'>
   :param GeometricNonLinearity: <class 'ctypes.c_long'>
   :param ContinueWithoutConvergence: <class 'ctypes.c_long'>
   :param MaterialNonLinearity: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RNonLinearAnalysisResultInfo

   :param Increments: <class 'ctypes.c_long'>
   :param Iterations: <class 'ctypes.c_long'>
   :param Lambda: <class 'ctypes.c_double'>
   :param ErrorP: <class 'ctypes.c_double'>
   :param ErrorU: <class 'ctypes.c_double'>
   :param ErrorE: <class 'ctypes.c_double'>
   :param ErrorEq: <class 'ctypes.c_double'>
   :param ControlVal: <class 'ctypes.c_double'>
   :param Convergence: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSeismicEq

   :param seEpsX: <class 'ctypes.c_double'>
   :param seEpsY: <class 'ctypes.c_double'>
   :param seEpsZ: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpectrumData

   :param SpectrumData_EC: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_EC'>
   :param SpectrumData_ITA: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_ITA'>
   :param SpectrumData_SIA: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_SIA'>
   :param SpectrumData_STAS: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_STAS'>
   :param SpectrumData_DIN: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_DIN'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignCrackResults

   :param Top: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignCrackResult'>
   :param Bottom: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignCrackResult'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignCrackResult

   :param Wk: <class 'ctypes.c_double'>
   :param I1: <class 'ctypes.c_double'>
   :param x1: <class 'ctypes.c_double'>
   :param I2: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param Mcr: <class 'ctypes.c_double'>
   :param Sr_max: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignReqReinfs

   :param Top: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignReqReinf'>
   :param Bottom: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignReqReinf'>
   :param Top_CC: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignReqReinf'>
   :param Bottom_CC: <class 'axisvm.com.core.tlb._16_100.RRCBeamDesignReqReinf'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignReqReinf

   :param N: <class 'ctypes.c_long'>
   :param Nf: <class 'ctypes.c_long'>
   :param NRow: <class 'ctypes.c_long'>
   :param u: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RWriteValuesTo

   :param Nodes: <class 'ctypes.c_long'>
   :param Lines: <class 'ctypes.c_long'>
   :param Surfaces: <class 'ctypes.c_long'>
   :param MinMaxOnly: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RBulkNodalSupportSpringParams

   :param SupportType: <class 'ctypes.c_long'>
   :param SpringParamIndexes: <class 'axisvm.com.core.tlb._16_100.RSpringParamIndexes'>
   :param IsolatorParamIndex: <class 'ctypes.c_long'>
   :param IsolatorD2: <class 'ctypes.c_double'>
   :param NodeId: <class 'ctypes.c_long'>
   :param MemberID: <class 'ctypes.c_long'>
   :param SurfaceId1: <class 'ctypes.c_long'>
   :param SurfaceId2: <class 'ctypes.c_long'>
   :param DomainId1: <class 'ctypes.c_long'>
   :param DomainId2: <class 'ctypes.c_long'>
   :param ReferenceId: <class 'ctypes.c_long'>
   :param ReferenceIdx: <class 'ctypes.c_long'>
   :param ReferenceIdz: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RBasicDisplayParameters

   :param ResultComponent: <class 'ctypes.c_long'>
   :param Scale: <class 'ctypes.c_double'>
   :param DisplayMode: <class 'ctypes.c_long'>
   :param DisplayShape: <class 'ctypes.c_long'>
   :param WriteValuesTo: <class 'axisvm.com.core.tlb._16_100.RWriteValuesTo'>

.. py:class:: axisvm.com.tlb.RVirtualBeamParams

   :param Name: <class 'comtypes.BSTR'>
   :param LocXVid: <class 'ctypes.c_long'>
   :param LocZVid: <class 'ctypes.c_long'>
   :param LocXV: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param LocZV: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param SectionI: <class 'ctypes.c_long'>
   :param SectionJ: <class 'ctypes.c_long'>
   :param DefinitionType: <class 'ctypes.c_long'>
   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param InnerDomains: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RSpectrumData_V153

   :param SpectrumData_EC: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_EC'>
   :param SpectrumData_ITA: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_ITA'>
   :param SpectrumData_SIA: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_SIA'>
   :param SpectrumData_STAS: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_STAS'>
   :param SpectrumData_DIN: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_DIN'>
   :param SpectrumData_ECHU: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_ECHU'>
   :param SpectrumData_ECNL: <class 'axisvm.com.core.tlb._16_100.RSpectrumData_ECNL'>

.. py:class:: axisvm.com.tlb.RNodeCrackWidthValues

   :param covBottom: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>
   :param covTop: <class 'axisvm.com.core.tlb._16_100.RCrackWidthValues'>

.. py:class:: axisvm.com.tlb.RBasicDisplayParameters_V153

   :param ResultComponent: <class 'ctypes.c_long'>
   :param Scale: <class 'ctypes.c_double'>
   :param DisplayMode: <class 'ctypes.c_long'>
   :param DisplayShape: <class 'ctypes.c_long'>
   :param WriteValuesTo: <class 'axisvm.com.core.tlb._16_100.RWriteValuesTo'>
   :param AutoScale: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPushOverDirectionParams

   :param Uniform: <class 'ctypes.c_long'>
   :param Modal: <class 'ctypes.c_long'>
   :param VibrationAnalysisType: <class 'ctypes.c_long'>
   :param VibrationLoadCase: <class 'ctypes.c_long'>
   :param VibrationMode: <class 'ctypes.c_long'>
   :param AutoDominantMode: <class 'ctypes.c_long'>
   :param AccidentalEcc: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RVirtualStripParams

   :param Name: <class 'comtypes.BSTR'>
   :param StartP: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param EndP: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param SectionI: <class 'ctypes.c_long'>
   :param SectionJ: <class 'ctypes.c_long'>
   :param NormV: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param L: <class 'ctypes.c_double'>
   :param R: <class 'ctypes.c_double'>
   :param DefinitionType: <class 'ctypes.c_long'>
   :param EccIY: <class 'ctypes.c_double'>
   :param EccIZ: <class 'ctypes.c_double'>
   :param EccJY: <class 'ctypes.c_double'>
   :param EccJZ: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RXLAMSurfaceStresses

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param xssvCenterPoint: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourPoint1: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourPoint2: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourPoint3: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourPoint4: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>
   :param xssvContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RXLAMSurfaceStressValues'>

.. py:class:: axisvm.com.tlb.RCircularFootingSpec

   :param FixedDiam: <class 'ctypes.c_long'>
   :param Diam: <class 'ctypes.c_double'>
   :param StepMeasureSource: <class 'ctypes.c_long'>
   :param DeltaR: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSurfaceStresses

   :param ContourPointCount: <class 'ctypes.c_long'>
   :param ContourPoint1Id: <class 'ctypes.c_long'>
   :param ContourPoint2Id: <class 'ctypes.c_long'>
   :param ContourPoint3Id: <class 'ctypes.c_long'>
   :param ContourPoint4Id: <class 'ctypes.c_long'>
   :param ContourLine1Id: <class 'ctypes.c_long'>
   :param ContourLine2Id: <class 'ctypes.c_long'>
   :param ContourLine3Id: <class 'ctypes.c_long'>
   :param ContourLine4Id: <class 'ctypes.c_long'>
   :param ssvtmbCenterPoint: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourPoint1: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourPoint2: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourPoint3: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourPoint4: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourLineMidPoint1: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourLineMidPoint2: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourLineMidPoint3: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>
   :param ssvtmbContourLineMidPoint4: <class 'axisvm.com.core.tlb._16_100.RSurfaceStressValuesTMB'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_STAS

   :param mbc: <class 'ctypes.c_double'>
   :param mbt: <class 'ctypes.c_double'>
   :param ksi0: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Npos: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Nneg: <class 'ctypes.c_double'>
   :param RebarPos: <class 'axisvm.com.core.tlb._16_100.RRebarPos'>
   :param fse: <class 'ctypes.c_double'>
   :param phi: <class 'ctypes.c_double'>
   :param nu: <class 'ctypes.c_double'>
   :param tau_a: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RStressPoint

   :param y: <class 'ctypes.c_double'>
   :param z: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RStressPointParams

   :param Tx_y: <class 'ctypes.c_double'>
   :param Tx_z: <class 'ctypes.c_double'>
   :param Vy_y: <class 'ctypes.c_double'>
   :param Vy_z: <class 'ctypes.c_double'>
   :param Vz_y: <class 'ctypes.c_double'>
   :param Vz_z: <class 'ctypes.c_double'>
   :param w: <class 'ctypes.c_double'>
   :param Tw_y: <class 'ctypes.c_double'>
   :param Tw_z: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRectangularFootingCalced

   :param Calculated: <class 'ctypes.c_long'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param dx1: <class 'ctypes.c_double'>
   :param dx2: <class 'ctypes.c_double'>
   :param dy1: <class 'ctypes.c_double'>
   :param dy2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDimensionLineParameters

   :param Orthogonal: <class 'ctypes.c_long'>
   :param Plane: <class 'ctypes.c_long'>
   :param OrthoDirection: <class 'ctypes.c_long'>
   :param NodeId1: <class 'ctypes.c_long'>
   :param NodeId2: <class 'ctypes.c_long'>
   :param LayerID: <class 'ctypes.c_long'>
   :param LabelDistance: <class 'ctypes.c_double'>
   :param LabelInside: <class 'ctypes.c_long'>
   :param LabelOrientation: <class 'ctypes.c_long'>
   :param TickMarkStyle: <class 'ctypes.c_long'>
   :param DisplayUnit: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RRectangularFootingSpec

   :param FixedX1: <class 'ctypes.c_long'>
   :param FixedX2: <class 'ctypes.c_long'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param FixedY1: <class 'ctypes.c_long'>
   :param FixedY2: <class 'ctypes.c_long'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param StepMeasureSource: <class 'ctypes.c_long'>
   :param dx1: <class 'ctypes.c_double'>
   :param dx2: <class 'ctypes.c_double'>
   :param dy1: <class 'ctypes.c_double'>
   :param dy2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_MSZ

   :param CrackWidthCheck: <class 'ctypes.c_long'>
   :param MaxCrackWidth_Top: <class 'ctypes.c_double'>
   :param MaxCrackWidth_Bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param AutoPsi: <class 'ctypes.c_long'>
   :param Deflection_Beam_L_div: <class 'ctypes.c_double'>
   :param Deflection_Cantilever_L_div: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpectrumData_EC

   :param SubsoilClass: <class 'ctypes.c_long'>
   :param agr: <class 'ctypes.c_double'>
   :param S: <class 'ctypes.c_double'>
   :param beta0: <class 'ctypes.c_double'>
   :param TB: <class 'ctypes.c_double'>
   :param TC: <class 'ctypes.c_double'>
   :param TD: <class 'ctypes.c_double'>
   :param gammaI: <class 'ctypes.c_double'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRelease

   :param ReleaseType: <class 'ctypes.c_long'>
   :param Init: <class 'ctypes.c_double'>
   :param Limit: <class 'ctypes.c_double'>
   :param FunctionId: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RPlaneTolerance

   :param ptType: <class 'ctypes.c_long'>
   :param Value: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RUnitParameters

   :param ConversionBaseID: <class 'ctypes.c_long'>
   :param UsedID: <class 'ctypes.c_long'>
   :param DecimalPlaces: <class 'ctypes.c_long'>
   :param Multiplier: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RMovingLoadOnDomainItem

   :param SystemGL: <class 'ctypes.c_long'>
   :param Position: <class 'ctypes.c_double'>
   :param a: <class 'ctypes.c_double'>
   :param b: <class 'ctypes.c_double'>
   :param u: <class 'ctypes.c_double'>
   :param Fx: <class 'ctypes.c_double'>
   :param Fy: <class 'ctypes.c_double'>
   :param Fz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RLoadDomainLine

   :param px1: <class 'ctypes.c_double'>
   :param px2: <class 'ctypes.c_double'>
   :param py1: <class 'ctypes.c_double'>
   :param py2: <class 'ctypes.c_double'>
   :param pz1: <class 'ctypes.c_double'>
   :param pz2: <class 'ctypes.c_double'>
   :param pm1: <class 'ctypes.c_double'>
   :param pm2: <class 'ctypes.c_double'>
   :param DistributionType: <class 'ctypes.c_long'>
   :param SegmentId: <class 'ctypes.c_long'>
   :param GlbStartx: <class 'ctypes.c_double'>
   :param GlbStarty: <class 'ctypes.c_double'>
   :param GlbStartz: <class 'ctypes.c_double'>
   :param GlbEndx: <class 'ctypes.c_double'>
   :param GlbEndy: <class 'ctypes.c_double'>
   :param GlbEndz: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_STAS

   :param mbc: <class 'ctypes.c_double'>
   :param mbt: <class 'ctypes.c_double'>
   :param ksi0: <class 'ctypes.c_double'>
   :param SeismicZone: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param PlasticHinges: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHinges'>

.. py:class:: axisvm.com.tlb.RRectanularFootingCalced

   :param Calculated: <class 'ctypes.c_long'>
   :param x1: <class 'ctypes.c_double'>
   :param x2: <class 'ctypes.c_double'>
   :param y1: <class 'ctypes.c_double'>
   :param y2: <class 'ctypes.c_double'>
   :param StepMeasureSource: <class 'ctypes.c_long'>
   :param dx1: <class 'ctypes.c_double'>
   :param dx2: <class 'ctypes.c_double'>
   :param dy1: <class 'ctypes.c_double'>
   :param dy2: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReleases

   :param x: <class 'axisvm.com.core.tlb._16_100.RRelease'>
   :param y: <class 'axisvm.com.core.tlb._16_100.RRelease'>
   :param z: <class 'axisvm.com.core.tlb._16_100.RRelease'>
   :param xx: <class 'axisvm.com.core.tlb._16_100.RRelease'>
   :param yy: <class 'axisvm.com.core.tlb._16_100.RRelease'>
   :param zz: <class 'axisvm.com.core.tlb._16_100.RRelease'>

.. py:class:: axisvm.com.tlb.RSpectrumData_ECHU

   :param SubsoilClass: <class 'ctypes.c_long'>
   :param agr: <class 'ctypes.c_double'>
   :param S: <class 'ctypes.c_double'>
   :param beta0: <class 'ctypes.c_double'>
   :param TB: <class 'ctypes.c_double'>
   :param TC: <class 'ctypes.c_double'>
   :param TD: <class 'ctypes.c_double'>
   :param gammaI: <class 'ctypes.c_double'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>
   :param LocalSpectrum: <class 'ctypes.c_long'>
   :param F0: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RSpectrumData_ECNL

   :param agr: <class 'ctypes.c_double'>
   :param P: <class 'ctypes.c_double'>
   :param TB: <class 'ctypes.c_double'>
   :param TC: <class 'ctypes.c_double'>
   :param TD: <class 'ctypes.c_double'>
   :param gammaI: <class 'ctypes.c_double'>
   :param qx: <class 'ctypes.c_double'>
   :param qy: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDomainVariableThickness

   :param VariableThicknessType: <class 'ctypes.c_long'>
   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P3: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param t1: <class 'ctypes.c_double'>
   :param t2: <class 'ctypes.c_double'>
   :param t3: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RDomainExcentricity

   :param ExcentricityType: <class 'ctypes.c_long'>
   :param P1: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P2: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param P3: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param exc1: <class 'ctypes.c_double'>
   :param exc2: <class 'ctypes.c_double'>
   :param exc3: <class 'ctypes.c_double'>
   :param GroupID: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RDomainCompositeRib

   :param RibMaterial: <class 'ctypes.c_long'>
   :param CrossSection: <class 'ctypes.c_long'>
   :param Direction: <class 'ctypes.c_long'>
   :param Origin: <class 'axisvm.com.core.tlb._16_100.RPoint3d'>
   :param d: <class 'ctypes.c_double'>
   :param EccType: <class 'ctypes.c_long'>
   :param Eccentricity: <class 'ctypes.c_double'>
   :param HasCustomShear: <class 'ctypes.c_long'>
   :param CustomShear: <class 'ctypes.c_double'>
   :param ActualRibs: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RShowActualReinforcement

   :param Symbol_axb: <class 'ctypes.c_long'>
   :param Symbol_ayb: <class 'ctypes.c_long'>
   :param Symbol_axt: <class 'ctypes.c_long'>
   :param Symbol_ayt: <class 'ctypes.c_long'>
   :param Label_axb: <class 'ctypes.c_long'>
   :param Label_ayb: <class 'ctypes.c_long'>
   :param Label_axt: <class 'ctypes.c_long'>
   :param Label_ayt: <class 'ctypes.c_long'>
   :param ActReinfLabelType: <class 'ctypes.c_long'>
   :param AccordResComponent: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_DIN

   :param dxt: <class 'ctypes.c_double'>
   :param dxb: <class 'ctypes.c_double'>
   :param dyt: <class 'ctypes.c_double'>
   :param dyb: <class 'ctypes.c_double'>
   :param SlabLoadTransfer: <class 'ctypes.c_long'>
   :param SlabLoadTransferDirection: <class 'ctypes.c_long'>
   :param MainDirectionTop: <class 'ctypes.c_long'>
   :param MainDirectionBottom: <class 'ctypes.c_long'>
   :param ct: <class 'ctypes.c_double'>
   :param cb: <class 'ctypes.c_double'>
   :param AggregateSize: <class 'ctypes.c_double'>
   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param EnvClass_T: <class 'ctypes.c_long'>
   :param EnvClass_B: <class 'ctypes.c_long'>
   :param ShearReinforcementAngle: <class 'ctypes.c_double'>
   :param ShearCrackAngle: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnStirrupSpacing

   :param ss_bottom: <class 'ctypes.c_double'>
   :param ss_middle: <class 'ctypes.c_double'>
   :param ss_top: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_MSZ

   :param UnfavorableEccentricity_Npos: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Nneg: <class 'ctypes.c_double'>
   :param AutoPsi: <class 'ctypes.c_long'>
   :param RebarPos: <class 'axisvm.com.core.tlb._16_100.RRebarPos'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_DIN

   :param EnvironmentClass: <class 'ctypes.c_long'>
   :param Deflection_Beam_L_div: <class 'ctypes.c_double'>
   :param Deflection_Cantilever_L_div: <class 'ctypes.c_double'>
   :param VariableAngleTrussMethod: <class 'ctypes.c_long'>
   :param Theta: <class 'ctypes.c_double'>
   :param CrackWidthCheck: <class 'ctypes.c_long'>
   :param MaxCrackWidth_Top: <class 'ctypes.c_double'>
   :param MaxCrackWidth_Bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RColumnStirrupDiameters

   :param sd_bottom: <class 'ctypes.c_double'>
   :param sd_middle: <class 'ctypes.c_double'>
   :param sd_top: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_EC

   :param dxt: <class 'ctypes.c_double'>
   :param dxb: <class 'ctypes.c_double'>
   :param dyt: <class 'ctypes.c_double'>
   :param dyb: <class 'ctypes.c_double'>
   :param SlabLoadTransfer: <class 'ctypes.c_long'>
   :param SlabLoadTransferDirection: <class 'ctypes.c_long'>
   :param MainDirectionTop: <class 'ctypes.c_long'>
   :param MainDirectionBottom: <class 'ctypes.c_long'>
   :param ct: <class 'ctypes.c_double'>
   :param cb: <class 'ctypes.c_double'>
   :param AggregateSize: <class 'ctypes.c_double'>
   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param StructClass: <class 'ctypes.c_long'>
   :param EnvClass_T: <class 'ctypes.c_long'>
   :param EnvClass_B: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Npos: <class 'ctypes.c_double'>
   :param UnfavorableEccentricity_Nneg: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param ShortTerm: <class 'ctypes.c_long'>
   :param ShearReinforcementAngle: <class 'ctypes.c_double'>
   :param ShearCrackAngle: <class 'ctypes.c_double'>
   :param TakeConcTensileStrengthNL: <class 'ctypes.c_long'>
   :param UseFctmfl: <class 'ctypes.c_long'>
   :param ShrinkageEps: <class 'ctypes.c_double'>
   :param RCNonlinearSurfType: <class 'ctypes.c_long'>
   :param ReinforcementType: <class 'ctypes.c_long'>
   :param AlphaAngle: <class 'ctypes.c_double'>
   :param BetaAngle: <class 'ctypes.c_double'>
   :param CalcFromLimitingCrackWidth: <class 'ctypes.c_long'>
   :param wk_b: <class 'ctypes.c_double'>
   :param wk2_b: <class 'ctypes.c_double'>
   :param wk_t: <class 'ctypes.c_double'>
   :param wk2_t: <class 'ctypes.c_double'>
   :param ApproximateLevelArm: <class 'ctypes.c_long'>
   :param SeelhoferMartiEquation: <class 'ctypes.c_long'>
   :param TrapSheetOnlyFormWork: <class 'ctypes.c_long'>
   :param TrapSheetOneLayerReinf: <class 'ctypes.c_long'>
   :param TrapSheetConsidered: <class 'ctypes.c_long'>

.. py:class:: axisvm.com.tlb.RReinforcementParameters_NEN

   :param AggregateSize: <class 'ctypes.c_double'>
   :param EnvClass_T: <class 'ctypes.c_long'>
   :param SurfaceCheck_T: <class 'ctypes.c_long'>
   :param ReductionOf5mm_T: <class 'ctypes.c_long'>
   :param CrackControl_T: <class 'ctypes.c_long'>
   :param EnvClass_B: <class 'ctypes.c_long'>
   :param SurfaceCheck_B: <class 'ctypes.c_long'>
   :param ReductionOf5mm_B: <class 'ctypes.c_long'>
   :param CrackControl_B: <class 'ctypes.c_long'>
   :param MainDirectionTop: <class 'ctypes.c_long'>
   :param MainDirectionBottom: <class 'ctypes.c_long'>
   :param ct: <class 'ctypes.c_double'>
   :param cb: <class 'ctypes.c_double'>
   :param ApplyMinimumCover: <class 'ctypes.c_long'>
   :param dxt: <class 'ctypes.c_double'>
   :param dxb: <class 'ctypes.c_double'>
   :param dyt: <class 'ctypes.c_double'>
   :param dyb: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RRCBeamDesignParameters_EC_RO

   :param Ksi0_RO: <class 'ctypes.c_double'>
   :param SeismicZone: <class 'ctypes.c_long'>
   :param fse: <class 'ctypes.c_double'>
   :param VariableAngleTrussMethod: <class 'ctypes.c_long'>
   :param Theta: <class 'ctypes.c_double'>
   :param Deflection_Beam_L_div: <class 'ctypes.c_double'>
   :param Deflection_Cantilever_L_div: <class 'ctypes.c_double'>
   :param CrackWidthCheck: <class 'ctypes.c_long'>
   :param MaxCrackWidth_Top: <class 'ctypes.c_double'>
   :param MaxCrackWidth_Bottom: <class 'ctypes.c_double'>
   :param TakeConcTensileStrength: <class 'ctypes.c_long'>
   :param ShortTerm: <class 'ctypes.c_long'>
   :param PlasticHinges: <class 'axisvm.com.core.tlb._16_100.RRCBeamPlasticHinges'>

.. py:class:: axisvm.com.tlb.RRCColumnCapacityDesignParams

   :param PlasticHinges: <class 'ctypes.c_long'>
   :param DuctilityClass: <class 'ctypes.c_long'>
   :param PlasticHingeYY_Top: <class 'ctypes.c_long'>
   :param PlasticHingeYY_Bottom: <class 'ctypes.c_long'>
   :param PlasticHingeZZ_Top: <class 'ctypes.c_long'>
   :param PlasticHingeZZ_Bottom: <class 'ctypes.c_long'>
   :param MRdB_MRdC_RatioYY_Top: <class 'ctypes.c_double'>
   :param MRdB_MRdC_RatioYY_Bottom: <class 'ctypes.c_double'>
   :param MRdB_MRdC_RatioZZ_Top: <class 'ctypes.c_double'>
   :param MRdB_MRdC_RatioZZ_Bottom: <class 'ctypes.c_double'>
   :param RelativeClearLengthYY: <class 'ctypes.c_double'>
   :param RelativeClearLengthZZ: <class 'ctypes.c_double'>
   :param GammaRd: <class 'ctypes.c_double'>

.. py:class:: axisvm.com.tlb.RColumnStirrupZones

   :param sz_bottom: <class 'ctypes.c_double'>
   :param sz_middle: <class 'ctypes.c_double'>

