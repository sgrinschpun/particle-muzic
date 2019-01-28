#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
  ofSetWindowTitle("WaveRing GUI");
  ofSetVerticalSync(true);
  ofSetCircleResolution(256);
  //ofBackground(0);
  ofSetFrameRate(60);
  //ofSetBackgroundAuto(false);
  ofSetCircleResolution(60);
  ofEnableAntiAliasing();

  //ofSeedRandom();


  gui.setup();
  gui.add(framesPerCycle.set("framesPerCycle", 50, 1, 500));
  gui.add(radius.set("radius", 100, 1, 500));
  gui.add(amplitude.set("amplitude", 20, 1, 80));
  gui.add(noiseScale.set("noiseScale", 0.01, 0.0, 5));
  gui.add(segments.set("segments", 100, 1, 100));
  gui.add(width.set("width", 2, 1, 10));

  WaveRing wavering1;
  shapes.push_back(wavering1);
  //WaveRing wavering2;
  //shapes.push_back(wavering2);


  for(int i=0; i<shapes.size(); i++){
    shapes[i].setup();
  }
}

//--------------------------------------------------------------
void ofApp::update(){

  for(int i=0; i<shapes.size(); i++){
    shapes[i].update();

    shapes[i].setCycle(framesPerCycle);
    shapes[i].setRadius(radius);
    shapes[i].setAmplitude(amplitude);
    shapes[i].setNoiseScale(noiseScale);
    shapes[i].setSegments(segments);
    shapes[i].setWidth(width);

  }
}

//--------------------------------------------------------------
void ofApp::draw(){

  for(int i=0; i<shapes.size(); i++){
    shapes[i].draw();
  }

  ofFill();
  ofSetColor(0, 255);
  gui.draw();

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

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
