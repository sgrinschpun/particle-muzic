#include "Lepton.h"

Lepton::Lepton(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Lepton::buildParameters(){
  shapes_num = 1;
  after_img = 8;
  segments = 100;
  radius = 200;
  pos_amp.set(radius/4,radius/4,radius);
  rot_amp.set(0,0,0);
  switch(data.name){
    case "e-":
    case "e+":
      speed_amp = 0.05;
      noiseStep = 0;
      noiseAmount = 0;
      width = 0;
      framesPerCycle = 80;
      break;
    case "mu-":
    case "mu+":
      speed_amp = 0.02;
      noiseStep = 0.04;
      noiseAmount = 17;
      width = 14;
      framesPerCycle = 128;
      break;
    case "tau-":
    case "tau+":
      speed_amp = 0.01;
      noiseStep = 0.3;
      noiseAmount = 74;
      width = 14;
      framesPerCycle = 198;
      break;
  }
  getColorMode();
}


bool Lepton::getColorMode(){
  bool color = 0;
  switch(data.name){
    case "e-":
    case "mu-":
    case "tau-":
      color = 0;
      break;
    case "e+":
    case "mu+":
    case "tau+":
      color = 1;
      break;
    default:
      color = 0;
      break;
  }
  return color;

}
