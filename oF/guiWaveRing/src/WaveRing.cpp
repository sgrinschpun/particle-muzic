#include "WaveRing.h"
#include <math.h>

WaveRing::WaveRing(){
  cycle = new Cycle(120);
  color.set(255, 0, 0);
}

void WaveRing::setup(){
  ofSetColor(color);
}

void WaveRing::draw(){
  ofPushMatrix();
    ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
    polyline.draw();
  ofPopMatrix();
}

void WaveRing::update(){
  ofPoint p ;
  float max = (cycle -> getEaseQuart2())*amplitude;

  if (cycle -> newLoop()){ofSeedRandom();}
  else{}

  polyline.clear() ;

  ofSetLineWidth(width);

  for(int i=0; i<segments; i++){
    p.x =  (0 + radius * cos(2*M_PI * i / segments));
    p.y =  (0 + radius * sin(2*M_PI * i / segments));

    p.x += ofMap(ofSignedNoise(noiseScale*p.x, noiseScale*p.y),-1,1,-max,max);
    p.y += ofMap(ofSignedNoise(noiseScale*p.x ,noiseScale*p.y),-1,1,-max,max);

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
