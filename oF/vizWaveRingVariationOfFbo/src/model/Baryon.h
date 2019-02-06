#ifndef _Baryon //
#define _Baryon //
#include "ofMain.h"
#include "Model.h"

class Baryon: public Model {
  private:
    void buildParameters();
    void setColorMode();

  public:
    Baryon(shared_ptr<ParticleData>& _particleData);

};
#endif
