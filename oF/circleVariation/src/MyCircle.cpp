#include "MyCircle.h"

MyCircle::MyCircle(){
  radius = ofGetHeight()/4;
}

void MyCircle::setup(){

}



void MyCircle::draw(){
  //ofDrawCircle(0, 0, 0, radius);
  ofCircle(0, 0, 0, radius);
  //path.setCircleResolution(80);
  //path.circle(0,0,radius);
  //path.draw();
}


void MyCircle::setRadius(float _radius){
  radius = _radius;
}
