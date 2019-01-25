#ifndef _Model //
#define _Model //
#include "ofMain.h"
#include "Shape.h"
#include "ParticleData.h"


class Model {
  protected:
    vector<Shape*> shapes;
    ParticleData *particleData;

  public:
    virtual void addShapes() = 0;
    virtual void draw() = 0;

    Model(ParticleData* _particleData);
    virtual ~Model() {}

};
#endif
