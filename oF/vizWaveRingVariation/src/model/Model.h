#ifndef _Model //
#define _Model //
#include "ofMain.h"
#include "WaveRingVariation.h"
#include "ParticleData.h"
#include "Params.h"
#include "LeptonParams.h"
#include "BosonParams.h"


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

    void buildParameters();
    void setShape();

    virtual int getShapesNum() = 0;
    virtual int getFramesPerCycle() = 0;
    virtual int getAfterImg() = 0;
    virtual float getRadius() = 0;
    virtual ofVec3f getPos() = 0;
    virtual ofVec3f getRot() = 0;
    virtual float getSpeed() = 0;
    virtual bool getColorMode() = 0;
    virtual float getNoiseStep()=0;
    virtual float getNoiseAmount()=0;
    virtual int getSegments()=0;
    virtual int getWidth()=0;

  public:

    void draw();
    void update();

    Model(shared_ptr<ParticleData>& _particleData);
    ~Model() {}

};
#endif
