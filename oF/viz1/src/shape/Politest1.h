#ifndef _Politest1
#define _Politest1
#include "ofMain.h"
#include "Shape.h"

class Politest1: public Shape {
  private:
    Params *params;
    ofColor color;
    float width;
    ofPolyline polyline1, polyline2;


  public:
    void setup();
    void draw();
    void update();

    Politest1(Params* _params);

};
#endif
