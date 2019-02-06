#include "Meson.h"
s
Meson::Meson(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

int Meson::getShapesNum(){
  int shapeNum = 0;
  switch(data.name){
    case "gamma":
      shapeNum = 33;
      break;
    case "Z0":
      shapeNum = 45;
      break;
    default:
      shapeNum = 45;
      break;
  }
  return shapeNum;
}

}
int Meson::getFramesPerCycle(){

}
int Meson::getAfterImg(){

}
float Meson::getRadius(){

}
ofVec3f Meson::getPos(){

}
ofVec3f Meson::getRot(){

}
float Meson::getSpeed(){

}
bool Meson::getColorMode(){

}
float Meson::getNoiseStep(){

}
float Meson::getNoiseAmount(){

}
int Meson::getSegments(){

}
int Meson::getWidth(){

}
