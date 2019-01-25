#ifndef _Shape //
#define _Shape //
#include "ofMain.h"
#include "Params.h"

class Shape {
  protected:

  public:
    virtual void draw() = 0;
    virtual ~Shape() {}

};
#endif
