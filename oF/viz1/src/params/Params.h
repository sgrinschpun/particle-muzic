#ifndef _Params //
#define _Params //
#include "ofMain.h"
#include "ParticleData.h"
#include "Colors.h"

class Params {

  public:
    virtual ofColor getColor() = 0;
    ~Params() {};

};
#endif
