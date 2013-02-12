import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//Photon_Run2012A_recover/cmgTuple_0.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//Photon_Run2012A_recover/cmgTuple_1.root',
]);