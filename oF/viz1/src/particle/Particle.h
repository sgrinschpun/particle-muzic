#ifndef _Particle //
#define _Particle //
#include "ofMain.h"
#include "ParticleData.h"
#include "Model.h"
#include "Lepton.h"
#include "Boson.h"

class Particle {
  private:
  ParticleData *particleData;
  Model *model;

  void buildModel();

  public:
  void setup();
  void update();
  void draw();

  //constructor
  Particle(ParticleData* _particleData);

};
#endif
