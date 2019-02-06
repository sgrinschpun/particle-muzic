#include "Cycle.h"
#include <math.h>


Cycle::Cycle(int _framesPerCycle):framesPerCycle(_framesPerCycle){
  frameRate = ofGetTargetFrameRate(); // or ofGetFrameRate()
  hz = frameRate/framesPerCycle;
  progressRatioMax = (float) (framesPerCycle-1)/framesPerCycle;

  update();
}

void Cycle::update(){
  int frameNum = ofGetFrameNum();
  currentCycle = (float) frameNum/(float) framesPerCycle;
  currentFrame = frameNum%framesPerCycle;
  progressRatio = (float) currentFrame/(float) framesPerCycle;
  QuadEaseInRatio = pow(progressRatio,2);
  QuadEaseOutRatio = 1-pow(progressRatio-1,2);
  QuartEaseInRatio = pow(progressRatio,4);
  QuartEaseOutRatio = 1-pow(progressRatio-1,4);
  SextEaseInRatio = pow(progressRatio,6);
  SextEaseOutRatio = 1-pow(progressRatio-1,6);
}


int Cycle::getCurrentCycle(){
  return currentCycle;
}

int Cycle:: getCurrentFrame(){
  return currentFrame;
}

float Cycle:: getProgressRatio(){
  return progressRatio;
}

float Cycle::getEaseQuad1(){ // slow-> fast
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = QuadEaseInRatio;}
  else {ease = 1-QuadEaseOutRatio;}
  return ease;
}

float Cycle::getEaseQuad2(){ //fast -> slow
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = QuadEaseOutRatio;}
  else {ease = 1-QuadEaseInRatio;}
  return ease;
}

float Cycle::getEaseQuart1(){ // slow-> fast
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = QuartEaseInRatio;}
  else {ease = 1-QuartEaseOutRatio;}
  return ease;
}

float Cycle::getEaseQuart2(){ //fast -> slow
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = QuartEaseOutRatio;}
  else {ease = 1-QuartEaseInRatio;}
  return ease;
}


bool Cycle::newLoop(){
  update();
  if (currentFrame == 0){
      return true;
  }
  else{ return false;}
}

int Cycle::getSeed(){
  return randomSeeds[currentFrame];
}


float Cycle::getQuadIn(){
  return QuadEaseInRatio;
}

float Cycle::getQuadOut(){
  return QuadEaseOutRatio;
}

float Cycle::getQuartIn(){
  return QuartEaseInRatio;
}

float Cycle::getQuartOut(){
  return QuartEaseOutRatio;
}

float Cycle::getSextIn(){
  return SextEaseInRatio;
}

float Cycle::getSextOut(){
  return SextEaseOutRatio;
}

void Cycle::setFramesPerCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
}
