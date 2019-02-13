#include "WaveRing.h"

WaveRing::WaveRing(shared_ptr<Cycle>& cycle):cycle(cycle){

  segments = 100;
  radius =ofGetHeight()/4;
  width = 2;
  noiseStep = 0.0;
  noiseAmount = 0.40;

  pos.set(0, 0, 0); //
  rotate.set(0, 0, 0); //

  speed = 0.001; //
  speed_noise = ofRandom(10);
  speed_amp = ofRandom(10)/10000;
  pos_noise.set(ofRandom(10), ofRandom(10), ofRandom(10));
  pos_amp.set(0, 0, 0);
  rot_noise.set(ofRandom(10), ofRandom(10), ofRandom(10));
  rot_amp.set(0, 0, 0);

  col = ofRandom(255);
  col_speed = 1;
  col_mode = 0;  //

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
  ofSetLineWidth(width);
  ofNoFill();
  ofPushMatrix();
    ofTranslate(pos);
    ofRotateX(rotate.x);
    ofRotateY(rotate.y);
    ofRotateZ(rotate.z);
    if (col_mode)ofSetColor(col, 100);
    else ofSetColor(ofColor::fromHsb(col, 100, 255, 100));
    wigglyMeshRing.draw();
  ofPopMatrix();
}

void WaveRing::update(){
  if (cycle -> newLoop()==true){
     noiseCursor+= 0.1;
  }
  updateWigglyMeshRing();

  speed = ofNoise(speed_noise)*speed_amp;

  pos.set((ofNoise(pos_noise.x)*2-1)*pos_amp.x,
          (ofNoise(pos_noise.y)*2-1)*pos_amp.y,
          (ofNoise(pos_noise.z)*2-1)*pos_amp.z);

  rotate.set((ofNoise(rot_noise.x)*2-1)*rot_amp.x,
             (ofNoise(rot_noise.y)*2-1)*rot_amp.y,
             (ofNoise(rot_noise.z)*2-1)*rot_amp.z);

  speed_noise += 0.01;

  pos_noise.x += speed;
  pos_noise.y += speed;
  pos_noise.z += speed;

  rot_noise.x += speed;
  rot_noise.y += speed;
  rot_noise.z += speed;

  col += col_speed;
  if(col >= 255 || col <= 0) col_speed *= -1;
}

void WaveRing::setNoiseStep(float _noiseStep){
  noiseStep=_noiseStep;
}

void WaveRing::setNoiseAmount(float _noiseAmount){
  noiseAmount=_noiseAmount;
}

void WaveRing::setWidth(float _width){
  width = _width;
}

void WaveRing::setRadius(float _radius){
  radius = _radius;
}

void WaveRing::setSegments(int _segments){
  segments = _segments;
}

void WaveRing::setPosAmp(ofVec3f _pos_amp) {
    pos_amp = _pos_amp;
}

void WaveRing::setRotAmp(ofVec3f _rot_amp) {
    rot_amp = _rot_amp;
}

void WaveRing::setSpeedAmp(float _speed_amp) {
    speed_amp = _speed_amp;
}

void WaveRing::setColorMode(bool _col_mode) {
    col_mode = _col_mode;
}
