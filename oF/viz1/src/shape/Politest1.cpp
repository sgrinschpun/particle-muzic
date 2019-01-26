#include "Politest1.h"

Politest1::Politest1(Params* _params):params(_params){
  color = params->getColor();
  width = params->getWidth();
}

void Politest1::setup(){
  ofSetColor(color);
  ofSetLineWidth(width);

}

void Politest1::draw(){
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      polyline1.arc(0,0,100,100,0,360);
      polyline1.draw();
    ofPopMatrix();
}

void Politest1::update(){

}
