#include "Baryon.h"

Baryon::Baryon(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Baryon::buildParameters(){
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
}

bool Baryon::getColorMode(){

}
