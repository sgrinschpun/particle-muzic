#ifndef _Disc
#define _Disc
#include "ofMain.h"
#include "Shape.h"
#include "Cycle.h"

class Disc: public Shape {
  private:
    Cycle *cycle;
    Params *params;
    ofColor color;
    int dim;

  public:
    void setup();
    void draw();
    void update();

    Disc(Params* _params);

};
#endif
