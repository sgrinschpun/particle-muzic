#include "WaveRingVariation.h"

WaveRingVariation::WaveRingVariation() {
    shapes_num = 1;
    fadeAmnt = 50;
    framesPerCycle = 50;
    cycle = make_shared<Cycle>(framesPerCycle);

    //FBO
    ofFboSettings s;
    s.width = 1024;
    s.height = 768;
    s.internalformat = GL_RGBA;
    s.useDepth = true;
    rgbaFbo.allocate(s);

    rgbaFbo.begin();
    ofClear(255,255,255, 0);
    rgbaFbo.end();

}

void WaveRingVariation::update() {

  while (waverings.size() != shapes_num){
      if (waverings.size() < shapes_num) {
          WaveRing wr = WaveRing(cycle);
          waverings.push_back(wr);
      } else if (waverings.size() > shapes_num) {
          waverings.pop_back();
      }
  }

  for(int i=0; i<waverings.size(); i++){
    waverings[i].update();
  }

  ofEnableAlphaBlending();
  rgbaFbo.begin();
  drawFbo();
  rgbaFbo.end();
}

void WaveRingVariation::drawFbo(){
  
  ofEnableBlendMode(OF_BLENDMODE_ADD);
  ofPushMatrix();
  ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
  for(int i=0; i<waverings.size(); i++){
    waverings[i].draw();
  }
  ofPopMatrix();

  ofEnableBlendMode(OF_BLENDMODE_SUBTRACT);
  ofFill();
  ofSetColor(255,255,255, fadeAmnt);
  ofDrawRectangle(0,0,1024,768);
}

void WaveRingVariation::draw() {
  rgbaFbo.draw(0,0);
}

void WaveRingVariation::setShapeNum(int _shapes_num) {
    shapes_num = _shapes_num;
}

void WaveRingVariation::setFadeAmnt(int _fadeAmnt){
    fadeAmnt = _fadeAmnt;
}

void WaveRingVariation::setCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
  cycle -> setFramesPerCycle(_framesPerCycle);
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

void WaveRingVariation::setSegments(int _segments){
  for(int i=0; i<waverings.size(); i++){
    waverings[i].setSegments(_segments);
  }
}
