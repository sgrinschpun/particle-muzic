#ifndef _NewWaveRing //
#define _NewWaveRing //
#include "ofMain.h"
#include "Cycle.h"

class NewWaveRing {

  private:
    Cycle *cycle;
    int framesPerCycle;

    ofMesh wigglyMeshLine;
    int segments;
    float radius;
    int width;

    float noiseStep;
    float noiseAmount;
    float *signedNoiseData;
    int nSignedNoiseData;
    float radialNoiseCursor;

    float centerX;
    float centerY;

    void setupCircleMeshLine();
    void updateWigglyMeshLine();
    void setupSignedNoise();
    void updateSignedNoise();


  public:
    void setup();
    void draw();
    void update();

    void exampleDraw();
    void testDraw();
    void testDraw2();

    void setNoiseStep(float _noiseStep);
    void setNoiseAmount(float _noiseAmount);
    void setWidth(int _width);
    void setCycle(int _framesPerCycle);
    void setRadius(float _radius);
    void setSegments(int _segments);

    NewWaveRing();

};
#endif
