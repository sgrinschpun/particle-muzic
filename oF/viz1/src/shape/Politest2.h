#ifndef _Politest2
#define _Politest2
#include "ofMain.h"
#include "Shape.h"
#include "Cycle.h"

class Politest2: public Shape {
  private:
    Cycle *cycle;
    Params *params;
    ofColor color;
    float width;
    ofPolyline polyline;


  public:
    void setup();
    void draw();
    void update();

    Politest2(Params* _params);

};
#endif
