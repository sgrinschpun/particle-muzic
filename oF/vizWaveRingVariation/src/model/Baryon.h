#ifndef _Baryon //
#define _Baryon //
#include "ofMain.h"
#include "Model.h"

class Baryon: public Model {
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
    Baryon(shared_ptr<ParticleData>& _particleData);

};
#endif
