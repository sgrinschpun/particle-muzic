#include "Model.h"

Model::Model(ParticleData* _particleData){
  buildParams(_particleData);
}

void Model::buildParams(ParticleData* _particleData){
  string type = _particleData->getType();
  if (type == "lepton") {params = new LeptonParams(_particleData);}
  else if (type == "boson") {params = new BosonParams(_particleData);}
}
