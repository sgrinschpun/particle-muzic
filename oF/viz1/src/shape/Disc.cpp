#include "Disc.h"

Disc::Disc(){
  color.set(ofRandom(255),ofRandom(255),ofRandom(255));
  dim = 10;
}

void Disc::draw(){
    ofSetColor(color);
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      ofDrawCircle(0, 0, dim);
    ofPopMatrix();
}
