#ifndef _Model //
#define _Model //
#include "ofMain.h"
#include "WaveRingVariation.h"
#include "ParticleData.h"

class Model {
  private:
    shared_ptr<WaveRingVariation> shape;
    shared_ptr<ParticleData> data;

    int shapes_num;
    int after_img;
    float radius;
    ofVec3f pos_amp;
    ofVec3f rot_amp;
    float speed_amp;
    bool col_mode;
    float noiseStep;
    float noiseAmount;
    int width;
    int framesPerCycle;
    int segments;

    virtual void buildParameters()=0;
    void setShape();

  public:

    void draw();
    void update();

    void setLocation(ofPoint _position);

    Model(shared_ptr<ParticleData>& _particleData);
    ~Model() {}

};
#endif
