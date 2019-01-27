#ifndef _LeptonParams //
#define _LeptonParams //
#include "ofMain.h"
#include "Params.h"

class LeptonParams: public Params {

  private:
  ParticleData *particleData;
  Colors colors;

  public:
    LeptonParams(ParticleData* _particleData);

    ofColor getColor() {return colors.getWhite();};
    float getWidth() {return 100;};

};
#endif
