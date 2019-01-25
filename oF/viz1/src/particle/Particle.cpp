#include "Particle.h"
Particle::Particle(ParticleData* _particleData): particleData(_particleData){
  buildModel();
}

void Particle::buildModel(){
    string type = particleData->getType();
    if (type == "lepton") {model = new Lepton(particleData);}
    else if (type == "boson") {model = new Boson(particleData);}
  }


void Particle::update(){

}

void Particle::draw(){
  model->draw();
}
