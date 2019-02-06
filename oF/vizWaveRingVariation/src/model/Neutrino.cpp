#include "Neutrino.h"

Neutrino::Neutrino(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Neutrino::buildParameters(){
  shapes_num = 3;
  after_img = 60;
  radius = 20;
  pos_amp.set(radius*4,radius*4,radius*10);
  rot_amp.set(radius*4,radius*4,0);
  speed_amp = 0.03;
  noiseStep = 0;
  noiseAmount = 0;
  width = 3;
  framesPerCycle = 100;
  segments= 100;
  setColorMode();
}

bool Neutrino::setColorMode(){
    col_mode = 0;
}
