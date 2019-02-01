#ifndef _WaveRing //
#define _WaveRing //
#include "ofMain.h"
#include "Cycle.h"

class WaveRing {

  private:
    shared_ptr<Cycle> cycle;
    //Cycle *cycle;
    int framesPerCycle;

    ofMesh wigglyMeshRing;
    int segments;
    float radius;
    int width;

    float noiseStep;
    float noiseAmount;
    float noiseCursor;

    float centerX;
    float centerY;

    void setupCircleMeshRing();
    void updateWigglyMeshRing();

  public:
    void setup();
    void draw();
    void update();

    void setNoiseStep(float _noiseStep);
    void setNoiseAmount(float _noiseAmount);
    void setWidth(int _width);
    void setCycle(int _framesPerCycle);
    void setRadius(float _radius);
    void setSegments(int _segments);

    WaveRing();
};
#endif
