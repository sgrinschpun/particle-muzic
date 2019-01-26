#include "Particle.h"

Particle::Particle(ParticleData* _particleData): particleData(_particleData){
  buildModel();
}

void Particle::buildModel(){
    string type = particleData->getType();
    if (type == "lepton") {model = new Lepton(particleData);}
    else if (type == "boson") {model = new Boson(particleData);}
  }

void Particle::setup(){
  model->setup();
}

void Particle::draw(){
  model->draw();
}

void Particle::update(){
  model->update();
}
