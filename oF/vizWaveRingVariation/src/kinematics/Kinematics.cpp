#include "Kinematics.h"

Kinematics::Kinematics(ofPoint _position, ofVec3f _velocity): position(_position), velocity(_velocity){
  setAcceleration();
  topSpeed = 4;
}

void Kinematics::setAcceleration(){
  acceleration.set(0,0,0);
}

void Kinematics::checkEdges(){
  if (location.x > ofGetWidth()) {
      location.x = 0;
  }
  if (location.x < 0) {
      location.x = ofGetWidth();
  }
  if (location.y > ofGetHeight()) {
      location.y = 0;
  }
  if (location.y < 0) {
      location.y = pofGetHeight();
  }
}

ofPoint Kinematics::getLocation(){
  return location;
}

float Kinematics::getDistance(){
  ofVec3f center(3, 4, 2);
  return location.distance(center);
}

void Kinematics::update(){
  checkEdges();
  velocity+=acceleration;
  velocity.limit(topSpeed);
  location+=velocity;

}
