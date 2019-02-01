#ifndef _WaveRingVariation //
#define _WaveRingVariation //
#include "ofMain.h"
#include "Cycle.h"
#include "WaveRing.h"

class WaveRingVariation {

  private:

    vector<WaveRing> waverings;

    int shapes_num;

    //float radius;
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


  public:
    void setup();
    void draw();
    void update();

    vector<WaveRing> getWaveRings();

    void setShapeNum(int shapes_num);
    //void setRadius(float radius);
    void setPosAmp(ofVec3f pos_amp);
    void setRotAmp(ofVec3f rot_amp);
    void setSpeedAmp(float speed_amp);
    void setColorMode(bool col_mode);

    WaveRingVariation();

};
#endif
