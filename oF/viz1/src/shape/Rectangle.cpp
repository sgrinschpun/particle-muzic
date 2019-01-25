#include "Rectangle.h"

Rectangle::Rectangle(Params* _params):params(_params){
  color.set(ofRandom(255),ofRandom(255),ofRandom(255));
  height = 100;
  width = 100;
}

void Rectangle::draw(){
    ofSetColor(color);
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      ofDrawRectangle(0, 0, width, height);
    ofPopMatrix();
}
