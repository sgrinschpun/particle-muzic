#ifndef _Meson //
#define _Meson //
#include "ofMain.h"
#include "Model.h"

class Meson: public Model {
  private:
    int getShapesNum();
    int getFramesPerCycle();
    int getAfterImg();
    float getRadius();
    ofVec3f getPos();
    ofVec3f getRot();
    float getSpeed();
    bool getColorMode();
    float getNoiseStep();
    float getNoiseAmount();
    int getSegments();
    int getWidth();

  public:
    Meson(shared_ptr<ParticleData>& _particleData);

};
#endif
