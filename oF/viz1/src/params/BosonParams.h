#ifndef _BosonParams //
#define _BosonParams //
#include "ofMain.h"
#include "Params.h"

class BosonParams: public Params {
  private:
    ParticleData *particleData;

  public:
    BosonParams(ParticleData* _particleData);

};
#endif
