#ifndef _Disc
#define _Disc
#include "ofMain.h"
#include "Shape.h"

class Disc: public Shape {
  private:
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
