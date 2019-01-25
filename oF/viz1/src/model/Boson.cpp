#include "Boson.h"
#include "Rectangle.h"

void Boson::addShapes(){
  shapes.push_back(new Rectangle(params));
}

void Boson::draw(){
  for(int i=0; i<shapes.size(); i++){
    shapes[i] -> draw();
  }
}

Boson::Boson(ParticleData* _particleData):Model(_particleData){
  addShapes();
};
