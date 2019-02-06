#ifndef _Quark //
#define _Quark //
#include "ofMain.h"
#include "Model.h"

class Quark: public Model {
  private:
    void buildParameters();
    bool getColorMode();

  public:
    Quark(shared_ptr<ParticleData>& _particleData);

};
#endif
