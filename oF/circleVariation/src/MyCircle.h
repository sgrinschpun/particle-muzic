#pragma once
#include "ofMain.h"

class MyCircle {

  private:
    float radius;
    //ofPath path;


  public:
    MyCircle();
    void draw();
    void setup();

    void setRadius(float radius);
};
