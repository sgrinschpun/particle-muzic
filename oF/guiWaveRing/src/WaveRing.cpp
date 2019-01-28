#include "WaveRing.h"
#include <math.h>

WaveRing::WaveRing(){
  cycle = new Cycle(120);
  color.set(255, 0, 0);
  noiseRate = 0.02 + ofNoise(ofGetElapsedTimef() * 0.02, 100.0) * 0.015;
  segments =100;

}

void WaveRing::setup(){
  ofSetColor(color);

  for(int i=0; i<segments; i++){
    offsets.push_back(ofVec2f(ofRandom(0,100000), ofRandom(0,100000)));
  }
}

void WaveRing::draw(){
  ofPushMatrix();
    ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
    polyline.draw();
    ofDrawBitmapString(noiseRate, 0, 0);
    ofDrawBitmapString(cycle -> getCurrentCycle(), 0, 20);
    ofDrawBitmapString(cycle -> getCurrentFrame(), 0, 40);
    ofDrawBitmapString(cycle -> getProgressRatio(), 0, 60);
    ofDrawBitmapString(cycle -> newLoop(), 0, 80);
    ofDrawBitmapString(cycle -> getSeed(), 0, 100);
  ofPopMatrix();
}

void WaveRing::update(){
  ofPoint p ;
  float max = (cycle -> getEaseQuart2())*amplitude;

  if (cycle -> newLoop()==true){
    noiseRate = 0.02 + ofNoise(ofGetElapsedTimef() * 0.02, 100.0) * 0.15;
  }

  polyline.clear() ;

  ofSetLineWidth(width);
  for(int i=0; i<segments; i++){

    p.x =  (0 + radius * cos(2*M_PI * i / segments));
    p.y =  (0 + radius * sin(2*M_PI * i / segments));

    //p.x += ofMap(ofSignedNoise(noiseScale*p.x, noiseScale*p.y),-1,1,-max,max);
    //p.y += ofMap(ofSignedNoise(noiseScale*p.x ,noiseScale*p.y),-1,1,-max,max);

    float time = ofGetElapsedTimef();
    float timeScale = 5.0;
    ofVec3f timeOffsets = offsets[i];

    p.x += (ofSignedNoise(noiseRate*noiseScale+timeOffsets.x)) * max;
    p.y += (ofSignedNoise(noiseRate*noiseScale+timeOffsets.y)) * max;

    polyline.addVertex(p);
  }
  polyline.setClosed(true);

}


void WaveRing::setCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
  cycle -> setFramesPerCycle(_framesPerCycle);
}

void WaveRing::setRadius(float _radius){
  radius = _radius;
}

void WaveRing::setAmplitude(float _amplitude){
  amplitude = _amplitude;
}

void WaveRing::setNoiseScale(float _noiseScale){
  noiseScale = _noiseScale;
}

void WaveRing::setSegments(int _segments){
  segments = _segments;
}

void WaveRing::setWidth(int _width){
  width = _width;
}
