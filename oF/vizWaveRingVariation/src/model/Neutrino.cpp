#include "Neutrino.h"
s
Neutrino::Neutrino(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Neutrino::buildParameters(){
  shapes_num;
  after_img;
  radius;
  pos_amp;
  rot_amp;
  speed_amp;
  col_mode;
  noiseStep;
  noiseAmount;
  width;
  framesPerCycle;
  segments;
  getColorMode();
}

bool Neutrino::getColorMode(){
  bool color = 0;
  switch(data.name){
    case "nu_e":
    case "nu_mu":
    case "nu_tau":
      color = 0;
      break;
      case "nu_ebar":
      case "nu_mubar":
      case "nu_taubar":
      color = 1;
      break;
    default:
      color = 0;
      break;
  }
  return color;
}
