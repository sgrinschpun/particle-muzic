#ifndef _Kinematics
#define _Kinematics
#include "ofMain.h"

class Kinematics {
  private:
    ofPoint position;
    ofVec3f velocity;
    ofVec3f acceleration;

    float topSpeed;

    void setAcceleration();
    void checkEdges();

  public:
    void update();
    ofPoint getPosition();
    float getDistance();

    Kinematics(ofPoint _position, ofVec3f _velocity);

};
#endif
