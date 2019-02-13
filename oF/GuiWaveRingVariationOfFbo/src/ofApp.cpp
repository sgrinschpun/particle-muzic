#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    ofSetWindowTitle("GuiWaveRing test");
    ofBackground(0);
    ofSetFrameRate(60);
    //ofSetBackgroundAuto(false);
    ofSetCircleResolution(256);
    ofSetVerticalSync(true);

    gui.setup();
    gui.add(shapes_num.set("number of shapes", 1, 1, 100));
    gui.add(radius.set("radius", ofGetHeight()/4, 1, ofGetHeight()/2));
    gui.add(pos.set("pos",
                    ofVec3f(0),
                    ofVec3f(0),
                    ofVec3f(720, 720, 720)));
    gui.add(rot.set("rot",
                    ofVec3f(0),
                    ofVec3f(0),
                    ofVec3f(720, 720, 720)));
    gui.add(speed.set("speed", 0, 0, 0.1));
    gui.add(color_mode.set("color mode", 0));
    gui.add(fadeAmnt.set("Fade Amount", 50, 0, 255));

    //WaveRing
    gui.add(framesPerCycle.set("framesPerCycle", 50, 1, 500));
    gui.add(segments.set("segments", 100, 1, 500));
    gui.add(width.set("width", 2, 0, 40));
    gui.add(noiseStep.set("noiseStep", 0.0,0, 1));
    gui.add(noiseAmount.set("noiseAmount", 0.40, 0.0, 100));

    imgcount = 0;
    guidraw = true;

    WaveRingVariation wrv;
    shapes.push_back(wrv);

}

//--------------------------------------------------------------
void ofApp::update(){

    for (int i = 0; i < shapes.size(); i++) {
        shapes[i].update();

        shapes[i].setShapeNum(shapes_num);
        shapes[i].setRadius(radius);
        shapes[i].setPosAmp(pos);
        shapes[i].setRotAmp(rot);
        shapes[i].setSpeedAmp(speed);
        shapes[i].setColorMode(color_mode);
        shapes[i].setFadeAmnt(fadeAmnt);
        shapes[i].setNoiseStep(noiseStep);
        shapes[i].setNoiseAmount(noiseAmount);
        shapes[i].setWidth(width);
        shapes[i].setCycle(framesPerCycle);
        shapes[i].setRadius(radius);
        shapes[i].setSegments(segments);
    }
}

//--------------------------------------------------------------
void ofApp::draw(){
    for (int i = 0; i < shapes.size(); i++) {
        shapes[i].draw();
    }



    if(guidraw) {
        gui.draw();
    }
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if(key == 's'){

        img.grabScreen(0,0,ofGetWidth(),ofGetHeight());
        img.save("pic" + ofToString(imgcount) + ".png", OF_IMAGE_QUALITY_BEST);
        imgcount++;
    }

    if (key == 'g') {
        guidraw = false;
    }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){

}
