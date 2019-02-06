#ifdef DEBUG
#define DEBUG_MSG(str) do { std::cout << str << std::endl; } while( false )
#else
#define DEBUG_MSG(str) do { } while ( false )
#endif
#include "Boson.h"

Boson::Boson(shared_ptr<ParticleData>& _particleData):Model(_particleData){
  buildParameters();
  DEBUG_MSG("Boson Parameters done");
  setShape();
}

void Boson::buildParameters(){
  string name = data -> getName();
  shapes_num = 33;
  segments = 100;
  radius = 200;
  col_mode = 0;
  if (name == "gamma"){
      after_img = 16;
      pos_amp.set(radius, radius, 2*radius);
      rot_amp.set(2*radius, radius, radius);
      speed_amp = 0.01;
      noiseStep = 0;
      noiseAmount = 0;
      width = 0;
      framesPerCycle = 100;
  }
  else if (name == "Z0"){
      after_img = 145;
      pos_amp.set(radius/2, radius/2, 2*radius);
      rot_amp.set(2*radius, radius/2, radius/2);
      speed_amp = 0.01;
      noiseStep = 0;
      noiseAmount = 0;
      width = 8;
      framesPerCycle = 100;
  }
  else if (name == "W+"){
      after_img = 91;
      pos_amp.set(radius, radius, 2*radius);
      rot_amp.set(radius, radius/2, radius/2);
      speed_amp = 0.009;
      noiseStep = 0.9;
      noiseAmount = 85;
      width = 8;
      framesPerCycle = 40;
      DEBUG_MSG("W+");
  }
  else if (name == "h0(H_1)"){
      after_img = 43;
      pos_amp.set(radius/2, radius/2, radius);
      rot_amp.set(2*radius, radius/2, radius/2);
      speed_amp = 0.05;
      noiseStep = 0;
      noiseAmount = 0;
      width = 8;
      framesPerCycle = 100;
  }

}

void Boson::setColorMode(){
    col_mode = 0;
}
