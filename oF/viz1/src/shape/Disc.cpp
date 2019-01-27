#include "Disc.h"

Disc::Disc(Params* _params):params(_params){
  cycle = new Cycle(120);
  color = params->getColor();
  dim = 100;
}

void Disc::setup(){
  ofSetColor(color);
  ofSetCircleResolution(100);

}

void Disc::draw(){
    float rad = (cycle -> getEaseQuad2())*dim;
    string rads = to_string(rad);
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      ofSetColor(0);
      ofDrawCircle(0, 0, rad);
      ofSetColor(color);
      ofDrawBitmapString(rads, 0, 0);

    ofPopMatrix();
}

void Disc::update(){
}
