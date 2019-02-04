#ifndef _Kinematics
#define _Kinematics
#include "ofMain.h"

class Kinematics {
  private:
    ofPoint position;
    ofVec3f velocity;
    ofVec3f acceleration;

  public:
    void updateLocation();
    void getLocation();

    Kinematics();
    ~Kinematics();

};
#endif
