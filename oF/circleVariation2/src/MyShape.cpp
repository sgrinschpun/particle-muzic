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

  for(int i=0; i<circles.size(); i++){
    circles[i].update();
  }
}


void MyShape::draw() {
  ofEnableBlendMode(OF_BLENDMODE_ADD);

  for(int i=0; i<circles.size(); i++){
    circles[i].draw();
    }

  ofEnableBlendMode(OF_BLENDMODE_ALPHA);
  ofFill();
  ofSetColor(0, after_img);
  ofDrawRectangle(-ofGetWidth()/2, -ofGetHeight()/2, ofGetWidth(), ofGetHeight());
  ofPopMatrix();


}

void MyShape::setShapeNum(int _shapes_num) {
    shapes_num = _shapes_num;
}

void MyShape::setAfterImg(int _after_img) {
    after_img = _after_img;
}

void MyShape::setRadius(float _radius) {
  for(int i=0; i<circles.size(); i++){
    circles[i].setRadius(_radius);
  }
}

void MyShape::setPosAmp(ofVec3f _pos_amp) {
  for(int i=0; i<circles.size(); i++){
    circles[i].setPosAmp(_pos_amp);
  }
}

void MyShape::setRotAmp(ofVec3f _rot_amp) {
  for(int i=0; i<circles.size(); i++){
    circles[i].setRotAmp(_rot_amp);
  }
}

void MyShape::setSpeedAmp(float _speed_amp) {
  for(int i=0; i<circles.size(); i++){
    circles[i].setSpeedAmp(_speed_amp);
  }
}

void MyShape::setColorMode(bool _col_mode) {
  for(int i=0; i<circles.size(); i++){
    circles[i].setColorMode(_col_mode);
  }
}
