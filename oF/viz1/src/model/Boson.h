#ifndef _Boson //
#define _Boson //
#include "ofMain.h"
#include "Model.h"

class Boson: public Model {
  private:

  public:
    void addShapes();
    void draw();

    Boson(ParticleData* _particleData);

};
#endif
