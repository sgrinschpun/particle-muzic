#ifndef _Lepton //
#define _Lepton //
#include "ofMain.h"
#include "Model.h"

class Lepton: public Model {
  private:

  public:
    void addShapes();
    void draw();

    Lepton(ParticleData* _particleData);

};
#endif
