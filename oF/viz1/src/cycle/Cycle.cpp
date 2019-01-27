#include "Cycle.h"

Cycle::Cycle(int _framesPerCicle):framesPerCicle(_framesPerCicle){
  frameRate = ofGetTargetFrameRate(); // or ofGetFrameRate()
  hz = frameRate/framesPerCicle;
  progressRatioMax = (float) (framesPerCicle-1)/framesPerCicle;
}

void Cycle::update(){
  int frameNum = ofGetFrameNum();
  currentCycle = (float) frameNum/(float) framesPerCicle;
  currentFrame = frameNum%framesPerCicle;
  progressRatio = (float) currentFrame/(float) framesPerCicle;
  QuadEaseInRatio = pow(progressRatio,2);
  QuadEaseOutRatio = 1-pow(progressRatio-1,2)+1;
  QuartEaseInRatio = pow(progressRatio,4);
  QuartEaseOutRatio = 1-pow(progressRatio-1,4)+1;
  SextEaseInRatio = pow(progressRatio,6);
  SextEaseOutRatio = 1-pow(progressRatio-1,6)+1;
}

float Cycle::getEase(){
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = 1-QuadEaseInRatio;}
  else {ease = 1-QuadEaseOutRatio;}
  return ease;
}

float Cycle::getEase2(){
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = QuadEaseOutRatio;}
  else {ease = 1-QuartEaseInRatio;}
  return ease;
}

void Cycle::newNoiseSeed(){
  if (progressRatio == progressRatioMax){
    return ofSeedRandom();
  }
}

bool Cycle::newLoop(){
  update();
  bool newcicle = false;
  if (progressRatio == progressRatioMax){
      newcicle = true;
  }
  return newcicle;
}

int Cycle::getCurrentFrame(){
  return currentFrame;
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
