#include "Model.h"

Model::Model(ParticleData* _particleData){
  buildParams(_particleData);

}

void Model::buildParams(ParticleData* _particleData){
  string type = _particleData->getType();
  if (type == "lepton") {params = new LeptonParams(_particleData);}
  else if (type == "boson") {params = new BosonParams(_particleData);}
}

void Model::setup(){
  for(int i=0; i<shapes.size(); i++){
    shapes[i]->setup();
  }
}

void Model::draw(){
  for(int i=0; i<shapes.size(); i++){
    shapes[i]->draw();
  }
}

void Model::update(){
  for(int i=0; i<shapes.size(); i++){
    shapes[i]->update();
  }
}
