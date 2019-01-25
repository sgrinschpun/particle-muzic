#ifndef _BosonParams //
#define _BosonParams //
#include "ofMain.h"
#include "Params.h"

class BosonParams: public Params {

  private:
  ParticleData *particleData;
  Colors colors;

  public:
    BosonParams(ParticleData* _particleData);
    ofColor getColor() {return colors.getWhite();};

};
#endif
