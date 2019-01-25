#include "Politest1.h"

Politest1::Politest1(Params* _params):params(_params){
  color = params->getColor();
  width = params->getWidth();
}

void Politest1::draw(){
    ofSetColor(color);
    ofSetLineWidth(width);
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      ofPoint point1(0,0);
      polyline1.arc(point1,100,100,0,360);
      ofSetColor(color);
      polyline1.draw();
    ofPopMatrix();
}
