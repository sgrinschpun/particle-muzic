#ifndef _LeptonParams //
#define _LeptonParams //
#include "ofMain.h"
#include "Params.h"

class LeptonParams: public Params {
  private:
    ParticleData *particleData;

  public:
    LeptonParams(ParticleData* _particleData);

};
#endif
