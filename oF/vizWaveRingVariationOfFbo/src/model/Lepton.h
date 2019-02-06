#ifndef _Lepton //
#define _Lepton //
#include "ofMain.h"
#include "Model.h"

class Lepton: public Model {
  private:
  void setColorMode();
  void buildParameters();

  public:
    Lepton(shared_ptr<ParticleData>& _particleData);

};
#endif
