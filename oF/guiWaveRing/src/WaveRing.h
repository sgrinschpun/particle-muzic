#ifndef _WaveRing //
#define _WaveRing //
#include "ofMain.h"
#include "Cycle.h"

class WaveRing {
  private:
    Cycle *cycle;
    ofColor color;
    ofPolyline polyline;

    int framesPerCycle;
    float radius;
    float amplitude;
    float noiseScale;
    int segments;

  public:
    void setup();
    void draw();
    void update();

    void setCycle(int _framesPerCycle);
    void setRadius(float _radius);
    void setAmplitude(float _amplitude);
    void setNoiseScale(float _noiseScale);
    void setSegments(int _segments);

    WaveRing();
    //~WaveRing();
};
#endif
