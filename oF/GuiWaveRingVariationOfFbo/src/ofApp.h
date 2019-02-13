#pragma once

#include "ofMain.h"
#include "ofxGui.h"
#include "WaveRingVariation.h"

class ofApp : public ofBaseApp{

public:
    void setup();
    void update();
    void draw();

    void keyPressed(int key);
    void keyReleased(int key);
    void mouseMoved(int x, int y );
    void mouseDragged(int x, int y, int button);
    void mousePressed(int x, int y, int button);
    void mouseReleased(int x, int y, int button);
    void mouseEntered(int x, int y);
    void mouseExited(int x, int y);
    void windowResized(int w, int h);
    void dragEvent(ofDragInfo dragInfo);
    void gotMessage(ofMessage msg);

    ofxPanel gui;

    //WaveRing panel parameters
    ofParameter<float> noiseStep;
    ofParameter<float> noiseAmount;
    ofParameter<int> framesPerCycle;
    ofParameter<int> segments;
    ofParameter<float> width;
    //Variations panel parameters
    ofParameter<int> shapes_num;
    ofParameter<int> fadeAmnt;
    ofParameter<float> radius;
    ofParameter<ofVec3f> pos;
    ofParameter<ofVec3f> rot;
    ofParameter<float> speed;
    ofParameter<bool> color_mode;


    vector<WaveRingVariation> shapes;

    ofFbo image;
    bool guidraw;
    ofImage img;
    int imgcount;
};
