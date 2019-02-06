#ifndef _Meson //
#define _Meson //
#include "ofMain.h"
#include "Model.h"

class Meson: public Model {
  private:
    void buildParameters();
    bool getColorMode();

  public:
    Meson(shared_ptr<ParticleData>& _particleData);

};
#endif
