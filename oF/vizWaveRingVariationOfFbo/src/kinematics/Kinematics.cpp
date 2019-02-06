#include "Kinematics.h"

Kinematics::Kinematics(ofPoint _position, ofVec3f _velocity): position(_position), velocity(_velocity){
  setAcceleration();
  topSpeed = 4;
}

void Kinematics::setAcceleration(){
  acceleration.set(0,0,0);
}

void Kinematics::checkEdges(){
  if (position.x > ofGetWidth()) {
      position.x = 0;
  }
  if (position.x < 0) {
      position.x = ofGetWidth();
  }
  if (position.y > ofGetHeight()) {
      position.y = 0;
  }
  if (position.y < 0) {
      position.y = ofGetHeight();
  }
}

ofPoint Kinematics::getPosition(){
  return position;
}

float Kinematics::getDistance(){
  ofVec3f center(3, 4, 2);
  return position.distance(center);
}

void Kinematics::update(){
  checkEdges();
  velocity+=acceleration;
  velocity.limit(topSpeed);
  position+=velocity;

}
