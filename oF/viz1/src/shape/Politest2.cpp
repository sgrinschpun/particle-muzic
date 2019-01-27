#include "Politest2.h"
#include <math.h>

Politest2::Politest2(Params* _params):params(_params){
  cycle = new Cycle(120);
  color = params->getColor();
  width = params->getWidth();
}


void Politest2::setup(){
  ofSetColor(color);
  ofSetLineWidth(2);

}

void Politest2::draw(){
    ofPushMatrix();
      ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
      polyline.draw();
      ofDrawBitmapString(to_string(cycle -> getCurrentFrame()), 0, 0);
    ofPopMatrix();

}

void Politest2::update(){

  ofPoint p ;
  int num = 100;
  float max = (cycle -> getEase2())*20;

  if (cycle -> newLoop()){ofSeedRandom();}
  else{}


  polyline.clear() ;

  for(int i=0; i<num; i++){
    p.x =  (0 + width * cos(2*M_PI * i / num));
    p.y =  (0 + width * sin(2*M_PI * i / num));


    p.x += ofMap(ofSignedNoise(0.01*p.x, 0.01*p.y),-1,1,-max,max);
    p.y += ofMap(ofSignedNoise(0.01*p.x ,0.01*p.y),-1,1,-max,max);

    polyline.addVertex(p);
  }
  polyline.setClosed(true);

}
