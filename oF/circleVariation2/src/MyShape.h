#pragma once
#include "ofMain.h"
#include "MyCircle.h"

class MyShape {

public:
    MyShape();
    void update();
    void draw();

    void setShapeNum(int shapes_num);
    void setRadius(float radius);
    void setPosAmp(ofVec3f pos_amp);
    void setRotAmp(ofVec3f rot_amp);
    void setSpeedAmp(float speed_amp);

    void setColorMode(bool col_mode);

    void setAfterImg(int after_img);


private:
    vector<MyCircle> circles;
    int shapes_num;

    int after_img;

};
