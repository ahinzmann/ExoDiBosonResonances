#include "DataFormats/Common/interface/Wrapper.h"

#include "AnalysisDataFormats/ExoDiBosonResonances/interface/CompoundTypesHZZLL.h"

#include <vector>

namespace {
  struct HiggsAna_DataFormats {

    cmg::DiGenParticle dgg_;
    std::vector<cmg::DiGenParticle> dggv;
    edm::Wrapper<cmg::DiGenParticle> edgg;
    edm::Wrapper<std::vector<cmg::DiGenParticle> > edggv;

    cmg::DiMuonDiJet dz_;
    std::vector<cmg::DiMuonDiJet> dzv;
    edm::Wrapper<cmg::DiMuonDiJet> edz;
    edm::Wrapper<std::vector<cmg::DiMuonDiJet> > edzv;

    cmg::DiElectronDiJet dze_;
    std::vector<cmg::DiElectronDiJet> dzev;
    edm::Wrapper<cmg::DiElectronDiJet> edez;
    edm::Wrapper<std::vector<cmg::DiElectronDiJet> > edzev;

    cmg::DiGenParticleDiGenParticle dzgg_;
    std::vector<cmg::DiGenParticleDiGenParticle> dzggv;
    edm::Wrapper<cmg::DiGenParticleDiGenParticle> edzgg;
    edm::Wrapper<std::vector<cmg::DiGenParticleDiGenParticle> > edzggv;

    cmg::GenParticlePtr gpptr_;

    edm::Ptr<cmg::DiObject<cmg::BaseJet,cmg::BaseJet> > vbtfptr_;
    edm::Ptr<cmg::DiObject<cmg::PFJet,cmg::PFJet> > vbtfptr2_;

  };
  

}