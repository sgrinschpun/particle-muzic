#ifndef _Cycle//
#define _Cycle //
#include "ofMain.h"

class Cycle {
  private:
    int framesPerCycle;  //a full cycle lasts this number of frames
    int frameRate;  //number of frames per second
    float hz; // freqüency of a cycle
    int currentCycle; //How many cycles have passed since instantiatiation
    int currentFrame; //How many frames have passed since beginning of cycle
    float progressRatio; //How far away are we in this cycle
    float progressRatioMax;
    float QuadEaseInRatio, QuadEaseOutRatio, QuartEaseInRatio, QuartEaseOutRatio, SextEaseInRatio, SextEaseOutRatio; //Easing methods

    //int randomSeed;
    int randomSeeds[100];

    void buildRandomSeeds();

  public:
    void update();

    float getEaseQuad1();
    float getEaseQuad2();
    float getEaseQuart1();
    float getEaseQuart2();

    bool newLoop();
    int getSeed();

    float getQuadIn();
    float getQuadOut();
    float getQuartIn();
    float getQuartOut();
    float getSextIn();
    float getSextOut();

    int getCurrentFrame();
    int getCurrentCycle();
    float getProgressRatio();

    void setFramesPerCycle(int _framesPerCycle);

    Cycle(int _framesPerCycle);
    ~Cycle() {}

};
#endif
