#include "Boson.h"
#include "Rectangle.h"

void Boson::addShapes(){
  shapes.push_back(new Rectangle(params));
}

Boson::Boson(ParticleData* _particleData):Model(_particleData){
  addShapes();
};
