#ifndef _Particle //
#define _Particle //
#include "ofMain.h"
#include "ParticleData.h"

class Particle {
  public:

  //methods
  void setup();
  void update();
  void draw();

  //variables
  float x;
  float y;
  float speedY;
  float speedX;
  int dim;
  ofColor color;

  //constructor
  Particle(float _x, float _y, int _dim);

  private:
    ofVec3f location;
    ofVec3f velocity;


};
#endif
