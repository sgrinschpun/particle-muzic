#ifndef _Model //
#define _Model //
#include "ofMain.h"
#include "WaveRingVariation.h"
#include "ParticleData.h"
#include "Params.h"
#include "LeptonParams.h"
#include "BosonParams.h"


class Model {
  protected:
    shared_ptr<WaveRingVariation> shape;
    shared_ptr<ParticleData> data;

    void buildShape();

    virtual int getShapesNum() = 0;
    virtual int getFramesPerCycle() = 0;
    virtual int getAfterImg() = 0;

  public:

    void setup();
    void draw();
    void update();

    Model(shared_ptr<ParticleData>& _particleData);
    ~Model() {}

};
#endif
