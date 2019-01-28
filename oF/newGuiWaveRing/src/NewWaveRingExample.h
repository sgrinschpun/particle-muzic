#ifndef _NewWaveRingExample //
#define _NewWaveRingExample //
#include "ofMain.h"

class NewWaveRingExample {

  private:
    float noiseStep;
    float noiseAmount;
    float *signedNoiseData;
    int nSignedNoiseData;
    float radialNoiseCursor;
    float radialNoiseDemoX;
    float radialNoiseDemoY;
    float radialNoiseDemoR; // radius

    void setupSignedNoise();
    void updateSignedNoise();


  public:
    void setup();
    void draw();
    void update();

    void setNoiseStep(float _noiseStep);
    void setNoiseAmount(float _noiseAmount);

    NewWaveRingExample();

};
#endif
