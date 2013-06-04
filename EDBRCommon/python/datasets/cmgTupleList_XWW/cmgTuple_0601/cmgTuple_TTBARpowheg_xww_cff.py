import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_0.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_1.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_10.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_100.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_101.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_102.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_103.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_104.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_105.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_106.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_107.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_108.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_109.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_11.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_110.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_111.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_112.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_113.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_114.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_115.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_116.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_117.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_118.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_119.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_12.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_120.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_121.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_122.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_123.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_124.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_125.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_126.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_127.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_128.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_129.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_13.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_130.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_131.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_132.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_133.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_134.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_135.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_136.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_137.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_138.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_139.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_14.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_140.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_141.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_142.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_143.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_144.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_145.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_146.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_147.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_148.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_149.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_15.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_150.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_151.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_152.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_153.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_155.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_156.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_157.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_158.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_159.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_16.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_160.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_161.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_162.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_163.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_164.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_165.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_166.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_167.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_168.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_169.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_17.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_170.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_171.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_172.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_173.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_174.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_175.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_176.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_177.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_178.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_179.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_18.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_180.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_181.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_182.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_183.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_184.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_185.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_186.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_187.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_188.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_189.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_19.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_190.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_191.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_192.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_193.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_194.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_195.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_196.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_197.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_198.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_199.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_2.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_20.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_200.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_21.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_22.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_23.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_24.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_25.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_26.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_27.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_28.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_29.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_3.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_30.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_31.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_32.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_33.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_34.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_35.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_36.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_37.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_38.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_39.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_4.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_40.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_41.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_42.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_43.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_44.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_45.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_46.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_47.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_48.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_49.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_5.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_51.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_52.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_53.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_54.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_55.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_56.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_57.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_58.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_59.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_6.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_60.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_61.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_62.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_63.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_64.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_65.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_66.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_67.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_69.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_7.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_70.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_71.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_72.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_73.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_74.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_75.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_76.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_77.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_78.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_79.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_8.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_80.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_81.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_82.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_83.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_84.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_85.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_86.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_87.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_88.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_89.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_9.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_90.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_91.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_92.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_93.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_94.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_95.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_96.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_97.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_98.root',
    '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0601/Summer12/CA8//TTBARpowheg_xww/cmgTuple_99.root',
    ])