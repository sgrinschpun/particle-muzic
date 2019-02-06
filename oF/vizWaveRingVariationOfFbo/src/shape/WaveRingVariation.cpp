#ifdef DEBUG
#define DEBUG_MSG(str) do { std::cout << str << std::endl; } while( false )
#else
#define DEBUG_MSG(str) do { } while ( false )
#endif
#include "WaveRingVariation.h"

WaveRingVariation::WaveRingVariation() {

  ofFboSettings s;
  s.width = ofGetWidth();
  s.height = ofGetHeight();
  s.internalformat = GL_RGBA;
  s.useDepth = true;
  rgbaFbo.allocate(s);

  rgbaFbo.begin();
  ofClear(255,255,255, 0);
  rgbaFbo.end();

}

void WaveRingVariation::setPosition(ofPoint _position){
  position = _position;
}

void WaveRingVariation::update() {
  for(int i=0; i<waverings.size(); i++){
    waverings[i].update();
  }

  ofEnableAlphaBlending();
  rgbaFbo.begin();
  drawFbo();
  rgbaFbo.end();
}

void WaveRingVariation::drawFbo(){
  if( ofGetKeyPressed('c') ){
    ofClear(255,255,255, 0);
  }

  ofEnableBlendMode(OF_BLENDMODE_ADD);
  ofPushMatrix();
  ofTranslate(position.x, position.y);
  for(int i=0; i<waverings.size(); i++){
    waverings[i].draw();
  }
  ofPopMatrix();

  ofEnableBlendMode(OF_BLENDMODE_SUBTRACT);
  ofFill();
  ofSetColor(255,255,255, fadeAmnt);
  ofDrawRectangle(0,0,ofGetWidth(),ofGetHeight());


}

void WaveRingVariation::draw() {
rgbaFbo.draw(0,0);
}

void WaveRingVariation::setShapeNum(int _shapes_num) {
    shapes_num = _shapes_num;
    for(int i=0; i<shapes_num; i++){
      WaveRing wr = WaveRing(cycle);
      waverings.push_back(wr);
    }

}

void WaveRingVariation::setFadeAmount(int _fadeAmnt){
  fadeAmnt = _fadeAmnt;
}

void WaveRingVariation::setCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
  DEBUG_MSG("framesPerCycle: " + to_string(framesPerCycle));
  cycle = make_shared<Cycle>(framesPerCycle);
}

void WaveRingVariation::setRadius(float _radius) {
  radius=_radius;
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
