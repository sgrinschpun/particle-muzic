#include "WaveRingVariation.h"

WaveRingVariation::WaveRingVariation() {
    shapes_num = 1;  //
    after_img = 50; //
}

void WaveRingVariation::update() {

  while (waverings.size() != shapes_num){
      if (waverings.size() < shapes_num) {
          WaveRing wv;
          waverings.push_back(wv);
      } else if (waverings.size() > shapes_num) {
          waverings.pop_back();
      }
  }

  for(int i=0; i<waverings.size(); i++){
    waverings[i].update();
  }
}


void WaveRingVariation::draw() {

  ofEnableBlendMode(OF_BLENDMODE_ADD);
  for(int i=0; i<waverings.size(); i++){
    waverings[i].draw();
  }

  ofEnableBlendMode(OF_BLENDMODE_ALPHA);
  ofFill();
  ofSetColor(0, after_img);
  ofDrawRectangle(-ofGetWidth()/2, -ofGetHeight()/2, ofGetWidth(), ofGetHeight());
  ofPopMatrix();


}

void WaveRingVariation::setShapeNum(int _shapes_num) {
    shapes_num = _shapes_num;
}

void WaveRingVariation::setAfterImg(int _after_img) {
    after_img = _after_img;
}

void WaveRingVariation::setRadius(float _radius) {
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setRadius(_radius);
  }
}

void WaveRingVariation::setPosAmp(ofVec3f _pos_amp) {
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setPosAmp(_pos_amp);
  }
}

void WaveRingVariation::setRotAmp(ofVec3f _rot_amp) {
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setRotAmp(_rot_amp);
  }
}

void WaveRingVariation::setSpeedAmp(float _speed_amp) {
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setSpeedAmp(_speed_amp);
  }
}

void WaveRingVariation::setColorMode(bool _col_mode) {
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setColorMode(_col_mode);
  }
}

void WaveRingVariation::setNoiseStep(float _noiseStep){
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setNoiseStep(_noiseStep);
  }
}

void WaveRingVariation::setNoiseAmount(float _noiseAmount){
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setNoiseAmount(_noiseAmount);
  }
}

void WaveRingVariation::setWidth(int _width){
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setWidth(_width);
  }
}

void WaveRingVariation::setCycle(int _framesPerCycle){
  for(int i=0; i<waverings.size(); i++){
    waverings[i].cycle->setFramesPerCycle(_framesPerCycle);
  }
}


void WaveRingVariation::setSegments(int _segments){
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setSegments(_segments);
  }
}
