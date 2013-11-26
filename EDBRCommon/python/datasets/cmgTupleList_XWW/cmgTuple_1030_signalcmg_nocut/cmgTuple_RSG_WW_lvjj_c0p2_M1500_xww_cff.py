import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_0.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_1.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_10.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_11.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_12.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_13.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_14.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_15.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_16.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_17.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_18.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_19.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_2.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_20.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_21.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_22.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_23.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_24.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_25.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_26.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_27.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_28.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_29.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_3.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_30.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_31.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_32.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_33.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_34.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_35.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_36.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_37.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_38.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_39.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_4.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_40.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_41.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_42.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_43.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_44.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_45.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_46.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_47.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_48.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_49.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_5.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_50.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_6.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_7.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_8.root',
    '/store/cmst3/group/exovv/CMGtuple/shuai/production1113/Summer12/CA8//RSG_WW_lvjj_c0p2_M1500_xww/cmgTuple_9.root',
    ])
