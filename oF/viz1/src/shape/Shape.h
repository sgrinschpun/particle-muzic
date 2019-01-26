#ifndef _Shape //
#define _Shape //
#include "ofMain.h"
#include "Params.h"

class Shape {

  public:
    virtual void setup() = 0;
    virtual void draw() = 0;
    virtual void update() = 0;
    
    ~Shape() {}

};
#endif
