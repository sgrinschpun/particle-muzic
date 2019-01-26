#ifndef _Model //
#define _Model //
#include "ofMain.h"
#include "Shape.h"
#include "ParticleData.h"
#include "Params.h"
#include "LeptonParams.h"
#include "BosonParams.h"


class Model {
  protected:
    vector<Shape*> shapes;
    Params *params;

    void buildParams(ParticleData* _particleData);

  public:
    virtual void addShapes() = 0;

    void setup();
    void draw();
    void update();

    Model(ParticleData* _particleData);
    ~Model() {}

};
#endif
