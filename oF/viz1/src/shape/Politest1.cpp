#include "Politest1.h"

Politest1::Politest1(Params* _params):params(_params){
  color = params->getColor();
  width = params->getWidth();
}

void Politest1::setup(){
  ofSetColor(color);
  ofSetLineWidth(width);

  int resolution = 20;
  float endAngle = 360.0 - 360.0/resolution;
  originalPolyline.arc(0, 0, 100, 100, 0, endAngle, resolution);
  originalPolyline.setClosed(true);

  modifiedPolyline = originalPolyline; // Creates a copy

}

void Politest1::draw(){
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      modifiedPolyline.draw();
    ofPopMatrix();
}

void Politest1::update(){
  float startAngle = ofGetElapsedTimef() * TWO_PI/2.0; // angle = time (in seconds) * speed (in radians/second)
  for (int i=0; i<originalPolyline.size(); i++) {
      float angleOffset = float(i)/originalPolyline.size() * (4.0*TWO_PI);
      float angle = startAngle + angleOffset;
      float scale = sin(angle*2.0) * 10.0;
      modifiedPolyline[i].x = originalPolyline[i].x + scale * cos(angle);
      modifiedPolyline[i].y = originalPolyline[i].y + scale * sin(angle);
  }
}
