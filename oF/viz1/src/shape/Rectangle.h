#ifndef _Rectangle
#define _Rectangle
#include "ofMain.h"
#include "Shape.h"

class Rectangle: public Shape {
  private:
    Params *params;
    ofColor color;
    int height;
    int width;

  public:
    void setup();
    void draw();
    void update();

    Rectangle(Params* _params);

};
#endif
