//
//  MyShape.cpp
//  ofGenerativePractice
//
//  Created by Miyashita Keita on 2017/05/15.
//
//

#include "MyShape.h"

MyShape::MyShape() {
    shapes_num = 1;  //
    //radius = ofGetHeight()/4;
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

    after_img = 0; //
}

void MyShape::update() {

  while (circles.size() != shapes_num){
      if (circles.size() < shapes_num) {
          MyCircle c;
          circles.push_back(c);
      } else if (circles.size() > shapes_num) {
          circles.pop_back();
      }
  }

}

void MyShape::addNoise() {
  speed_noise += 0.01;

  pos_noise.x += speed;
  pos_noise.y += speed;
  pos_noise.z += speed;

  rot_noise.x += speed;
  rot_noise.y += speed;
  rot_noise.z += speed;

  col += col_speed;
  if(col >= 255 || col <= 0) col_speed *= -1;

  speed = ofNoise(speed_noise)*speed_amp;

  pos.set((ofNoise(pos_noise.x)*2-1)*pos_amp.x,
          (ofNoise(pos_noise.y)*2-1)*pos_amp.y,
          (ofNoise(pos_noise.z)*2-1)*pos_amp.z);

  rotate.set((ofNoise(rot_noise.x)*2-1)*rot_amp.x,
             (ofNoise(rot_noise.y)*2-1)*rot_amp.y,
             (ofNoise(rot_noise.z)*2-1)*rot_amp.z);
}

void MyShape::resetNoise() {
  speed_noise = ofRandom(10);
  speed_amp = ofRandom(10)/10000;
  pos_noise.set(ofRandom(10), ofRandom(10), ofRandom(10));
  pos_amp.set(0, 0, 0);
  rot_noise.set(ofRandom(10), ofRandom(10), ofRandom(10));
  rot_amp.set(0, 0, 0);

  col = ofRandom(255);
  col_speed = 1;
}



void MyShape::draw() {
  ofEnableBlendMode(OF_BLENDMODE_ADD);
  ofNoFill();
  ofPushMatrix();

  for(int i=0; i<circles.size(); i++){
    addNoise();
    ofTranslate(pos);
    ofRotateX(rotate.x);
    ofRotateY(rotate.y);
    ofRotateZ(rotate.z);
    if (col_mode)ofSetColor(col, 100);
    else ofSetColor(ofColor::fromHsb(col, 100, 255, 100));
    circles[i].draw();
    }

  ofEnableBlendMode(OF_BLENDMODE_ALPHA);
  ofFill();
  ofSetColor(0, after_img);
  ofDrawRectangle(-ofGetWidth()/2, -ofGetHeight()/2, ofGetWidth(), ofGetHeight());
  ofPopMatrix();


}

void MyShape::setRadius(float _radius) {
  for(int i=0; i<circles.size(); i++){
    circles[i].setRadius(_radius);
  }
}

void MyShape::setPosAmp(ofVec3f _pos_amp) {
    pos_amp = _pos_amp;
}

void MyShape::setRotAmp(ofVec3f _rot_amp) {
    rot_amp = _rot_amp;
}

void MyShape::setSpeedAmp(float _speed_amp) {
    speed_amp = _speed_amp;
}

void MyShape::setColorMode(bool _col_mode) {
    col_mode = _col_mode;
}

void MyShape::setShapeNum(int _shapes_num) {
    shapes_num = _shapes_num;
}

void MyShape::setAfterImg(int _after_img) {
    after_img = _after_img;
}
