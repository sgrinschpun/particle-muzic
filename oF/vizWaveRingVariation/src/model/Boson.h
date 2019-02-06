#ifndef _Boson //
#define _Boson //
#include "ofMain.h"
#include "Model.h"

class Boson: public Model {
  private:
    void buildParameters();
    void setColorMode();

  public:
    Boson(shared_ptr<ParticleData>& _particleData);

};
#endif
