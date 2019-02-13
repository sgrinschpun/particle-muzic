#ifndef _WaveRing //
#define _WaveRing //
#include "ofMain.h"
#include "Cycle.h"

class WaveRing {

  private:

    //shape
    ofMesh wigglyMeshRing;
    int segments;
    float width;
    float noiseStep;
    float noiseAmount;
    float noiseCursor;
    //variation
    float radius;
    ofPoint pos;
    ofVec3f rotate;
    float speed;
    float speed_noise;
    float speed_amp;
    ofVec3f pos_noise;
    ofVec3f pos_amp;
    ofVec3f rot_noise;
    ofVec3f rot_amp;
    int col;
    float col_speed;
    bool col_mode;

    void setupCircleMeshRing();
    void updateWigglyMeshRing();

  public:
    shared_ptr<Cycle> cycle;

    void setup();
    void draw();
    void update();

    //shape
    void setNoiseStep(float _noiseStep);
    void setNoiseAmount(float _noiseAmount);
    void setWidth(float _width);
    void setCycle(int _framesPerCycle);
    void setSegments(int _segments);
    //variation
    void setRadius(float radius);
    void setPosAmp(ofVec3f pos_amp);
    void setRotAmp(ofVec3f rot_amp);
    void setSpeedAmp(float speed_amp);
    void setColorMode(bool col_mode);

    WaveRing(shared_ptr<Cycle>& cycle);

};
#endif
