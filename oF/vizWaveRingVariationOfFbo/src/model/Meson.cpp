#include "Meson.h"

Meson::Meson(shared_ptr<ParticleData>& _particleData):Model(_particleData){
  buildParameters();
  setShape();
}

void Meson::buildParameters(){
  shapes_num = 2;
  fadeAmnt = 50;
  radius = 50;
  pos_amp.set(0,0,0);
  rot_amp.set(radius*4,radius*4,0);
  speed_amp = 0.007;
  col_mode = 0;
  noiseStep = 0;
  noiseAmount = 0;
  width = 30;
  framesPerCycle = 200;
  segments = 100;
}


void Meson::setColorMode(){
    col_mode = 0;
}
