#ifndef _Cycle//
#define _Cycle //
#include "ofMain.h"

class Cycle {
  private:
    int framesPerCicle;  //a full cycle lasts this number of frames
    int frameRate;  //number of frames per second
    float hz; // freqüency of a cycle
    int currentCycle; //How many cycles have passed since instantiatiation
    int currentFrame; //How many frames have passed since beginning of cycle
    float progressRatio; //How far away are we in this cycle
    float QuadEaseInRatio, QuadEaseOutRatio, QuartEaseInRatio, QuartEaseOutRatio, SextEaseInRatio, SextEaseOutRatio; //Easing methods

  public:
    void update();
    float getEase();
    float getEase2();

    float getQuadIn();
    float getQuadOut();
    float getQuartIn();
    float getQuartOut();
    float getSextIn();
    float getSextOut();

    Cycle(int _framesPerCicle);
    ~Cycle() {}

};
#endif
