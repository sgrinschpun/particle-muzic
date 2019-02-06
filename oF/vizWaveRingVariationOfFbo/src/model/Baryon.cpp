#include "Baryon.h"

Baryon::Baryon(shared_ptr<ParticleData>& _particleData):Model(_particleData){
  buildParameters();
  setShape();
}

void Baryon::buildParameters(){
  shapes_num = 3;
  fadeAmnt = 5;
  radius = 200;
  pos_amp.set(radius, radius,0);
  rot_amp.set(radius, radius,0);
  speed_amp = 0.007;
  col_mode = 0;
  noiseStep =0;
  noiseAmount = 0;
  width = 32;
  framesPerCycle = 100;
  segments = 100;
}

void Baryon::setColorMode(){
    col_mode = 0;
}
