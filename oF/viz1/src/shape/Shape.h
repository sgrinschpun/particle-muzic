#ifndef _Shape //
#define _Shape //
#include "ofMain.h"

class Shape {
  private:

  public:
    virtual void draw() = 0;
    virtual ~Shape() {}

};
#endif
