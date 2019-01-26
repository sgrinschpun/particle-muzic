#include "Lepton.h"
#include "Disc.h"
#include "Rectangle.h"
#include "Politest1.h"

void Lepton::addShapes(){
  shapes.push_back(new Disc(params));
}

Lepton::Lepton(ParticleData* _particleData):Model(_particleData){
  addShapes();
};
