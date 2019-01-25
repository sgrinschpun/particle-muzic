#ifndef _Shape //
#define _Shape //
#include "ofMain.h"
#include "Params.h"

class Shape {

  public:
    virtual void draw() = 0;
    ~Shape() {}

};
#endif
