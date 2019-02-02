#pragma once
#include "ofMain.h"
#include "WaveRing.h"

class WaveRingVariation {

public:
    WaveRingVariation();
    void update();
    void draw();
    void setup();

    void setShapeNum(int shapes_num);
    void setAfterImg(int after_img);
    //Variations
    void setRadius(float radius);
    void setPosAmp(ofVec3f pos_amp);
    void setRotAmp(ofVec3f rot_amp);
    void setSpeedAmp(float speed_amp);
    void setColorMode(bool col_mode);
    //shape
    void setNoiseStep(float noiseStep);
    void setNoiseAmount(float noiseAmount);
    void setWidth(int width);
    void setCycle(int framesPerCycle);
    void setSegments(int segments);


private:
    vector<WaveRing> waverings;
    int shapes_num;
    int after_img;

};
