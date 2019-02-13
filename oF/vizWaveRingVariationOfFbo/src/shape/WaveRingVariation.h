#ifndef _WaveRingVariation
#define _WaveRingVariation
#include "ofMain.h"
#include "WaveRing.h"
#include "Cycle.h"

class WaveRingVariation {

public:
    WaveRingVariation();
    void update();
    void draw();
    void setPosition(ofPoint _position);

    void setShapeNum(int shapes_num);
    void setFadeAmount(int fadeAmnt);
    //Variations
    void setRadius(float radius);
    void setPosAmp(ofVec3f pos_amp);
    void setRotAmp(ofVec3f rot_amp);
    void setSpeedAmp(float speed_amp);
    void setColorMode(bool col_mode);
    //shape
    void setNoiseStep(float noiseStep);
    void setNoiseAmount(float noiseAmount);
    void setWidth(float width);
    void setCycle(int framesPerCycle);
    void setSegments(int segments);

    shared_ptr<Cycle> cycle;

private:
    vector<WaveRing> waverings;
    ofPoint position;
    float radius;
    int shapes_num;
    int framesPerCycle;

    ofFbo rgbaFbo;
    int fadeAmnt;
    void drawFbo();

};
#endif
