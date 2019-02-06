#ifndef _Quark //
#define _Quark //
#include "ofMain.h"
#include "Model.h"

class Quark: public Model {
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
    Quark(shared_ptr<ParticleData>& _particleData);

};
#endif
