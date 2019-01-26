#ifndef _Boson //
#define _Boson //
#include "ofMain.h"
#include "Model.h"

class Boson: public Model {
  private:

  public:
    void addShapes();

    Boson(ParticleData* _particleData);

};
#endif
