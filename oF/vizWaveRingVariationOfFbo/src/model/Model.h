#ifndef _Model //
#define _Model //
#include "ofMain.h"
#include "WaveRingVariation.h"
#include "ParticleData.h"

class Model {
  public:
    shared_ptr<WaveRingVariation> shape;
    shared_ptr<ParticleData> data;

    int shapes_num;
    float radius;
    ofVec3f pos_amp;
    ofVec3f rot_amp;
    float speed_amp;
    bool col_mode;
    float noiseStep;
    float noiseAmount;
    float width;
    int framesPerCycle;
    int segments;

    int fadeAmnt;

    void buildParameters();
    void setShape();

    void draw();
    void update();

    void setPosition(ofPoint _position);

    Model(shared_ptr<ParticleData>& _particleData);

};
#endif
