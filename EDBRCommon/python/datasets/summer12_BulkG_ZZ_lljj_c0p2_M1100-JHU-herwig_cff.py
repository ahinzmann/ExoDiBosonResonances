
import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
      '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_10_1_oRH.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_11_1_LSF.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_2_6BB.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_E46.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_bvC.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_fJz.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_LE4.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_9jN.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_McU.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_6MR.root',
       '/store//cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_zz_20130729_Summer12MC_BulkGtoZZ_HERWIG_20130729_234201/bonato/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig/EDBR_PATtuple_edbr_zz_20130729/1b325ddfb984c14533be7920e22baeef/BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig__tomei-BulkG_ZZ_llnunu_c0p2_M1100-JHU-herwig-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_dBK.root'
      ])
