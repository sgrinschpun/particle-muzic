#include "Disc.h"

Disc::Disc(Params* _params):params(_params){
  color = params->getColor();
  dim = 10;
}

void Disc::setup(){
  ofSetColor(color);
}

void Disc::draw(){
    ofSetColor(color);
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      ofDrawCircle(0, 0, dim);
    ofPopMatrix();
}

void Disc::update(){
}
