#include "WaveRing.h"

WaveRing::WaveRing(){
  cycle = make_shared<Cycle>(120);
  segments =100;
  radius =100;

  centerY = ofGetHeight()/2;
  centerX = ofGetWidth()/2;
}

void WaveRing::setup(){
  setupCircleMeshRing();
}

void WaveRing::setupCircleMeshRing(){
  wigglyMeshRing.setMode(OF_PRIMITIVE_LINE_STRIP);
  ofPoint p;
  for(int i=0; i<=segments; i++){
    p.x =  (radius * cos(TWO_PI * i / segments));
    p.y =  (radius * sin(TWO_PI * i / segments));
    wigglyMeshRing.addVertex(p);
  }
  noiseCursor = 0.1;
}

void WaveRing::updateWigglyMeshRing(){
  float max = noiseAmount*(cycle -> getEaseQuart2());
  ofPoint p;
  wigglyMeshRing.clear();

  for(int i=0; i<=segments; i++){
    p.x =  radius*cos(TWO_PI * i / segments);
    p.y =  radius*sin(TWO_PI * i / segments);

    p.x += ofSignedNoise(noiseCursor+noiseStep*p.x/radius, noiseCursor+noiseStep*p.y/radius)*max;
    p.y += ofSignedNoise(noiseCursor+noiseStep*p.x/radius, noiseCursor+noiseStep*p.y/radius)*max;
    wigglyMeshRing.addVertex(p);
  }
}


void WaveRing::draw(){
  ofBackgroundGradient( ofColor(255), ofColor(180), OF_GRADIENT_CIRCULAR);
  ofEnableAlphaBlending();
  ofEnableSmoothing();
  ofNoFill();
  ofSetLineWidth(width);
  ofEnableSmoothing();
  ofPushMatrix();
    ofTranslate(centerX,centerY,0);
    wigglyMeshRing.draw();
    ofDrawBitmapString(cycle -> getCurrentCycle(), 0, -40);
    ofDrawBitmapString(cycle -> getCurrentFrame(), 0, -20);
    ofDrawBitmapString(cycle -> getProgressRatio(), 0, 0);
    ofDrawBitmapString(cycle -> newLoop(), 0, 20);
    ofDrawBitmapString(cycle -> getEaseQuart2(),0,40);
  ofPopMatrix();
}

void WaveRing::update(){
  if (cycle -> newLoop()==true){
     noiseCursor+= 0.1;
  }
  updateWigglyMeshRing();
}

void WaveRing::setNoiseStep(float _noiseStep){
  noiseStep=_noiseStep;
}

void WaveRing::setNoiseAmount(float _noiseAmount){
  noiseAmount=_noiseAmount;
}

void WaveRing::setWidth(int _width){
  width = _width;
}

void WaveRing::setCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
  cycle -> setFramesPerCycle(_framesPerCycle);
}

void WaveRing::setRadius(float _radius){
  radius = _radius;
}

void WaveRing::setSegments(int _segments){
  segments = _segments;
}
