#pragma once
#include "ofMain.h"
#include "WaveRing.h"
#include "Cycle.h"

class WaveRingVariation {

public:
    WaveRingVariation();
    void update();
    void draw();
    void setup();

    void setShapeNum(int shapes_num);
    void setFadeAmnt(int fadeAmnt);
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
    int shapes_num;
    int framesPerCycle;

    ofFbo rgbaFbo;
    int fadeAmnt;
    void drawFbo();


};
