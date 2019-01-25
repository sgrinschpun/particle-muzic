#include "Lepton.h"
#include "Disc.h"
#include "Rectangle.h"
#include "Politest1.h"

void Lepton::addShapes(){
  shapes.push_back(new Politest1(params));
}

void Lepton::draw(){
  for(int i=0; i<shapes.size(); i++){
    shapes[i]->draw();
  }
}

Lepton::Lepton(ParticleData* _particleData):Model(_particleData){
  addShapes();
};
