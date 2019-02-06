#include "Quark.h"
s
Quark::Quark(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Quark::buildParameters(){
  shapes_num =1;
  after_img = 10;
  radius = 200
  pos_amp.set(0,0,0);
  rot_amp.set(0,0,720);
  speed_amp =0.07
  noiseStep = 0.275;
  noiseAmount = 100;
  width = 40;
  framesPerCycle= 280;
  segments = 100;
  getColorMode();
}

bool Quark::getColorMode(){
  bool color = 0;
  switch(data.name){
    case "u":
    case "d":
    case "c":
    case "s":
    case "b":
    case "t":
      color = 0;
      break;
    case "ubar":
    case "dbar":
    case "cbar":
    case "sbar":
    case "bbar":
    case "tbar":
      color = 1;
      break;
    default:
      color = 0;
      break;
  }
  col_mode = color;
}
