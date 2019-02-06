#include "Boson.h"
s
Boson::Boson(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Boson::buildParameters(){
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
  switch(data.name){
    case "gamma":
      break;
    case "Z0":
      break;
    case "W+":
    case "W+":
      break;
    case "h0(H_1)":
      break;
}
