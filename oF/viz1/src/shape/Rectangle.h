#ifndef _Rectangle
#define _Rectangle
#include "ofMain.h"
#include "Shape.h"

class Rectangle: public Shape {
  private:
    ofColor color;
    int height;
    int width;

  public:
    void draw();
    Rectangle();

};
#endif
