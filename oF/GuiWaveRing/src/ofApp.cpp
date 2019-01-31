#include "ofApp.h"
#include "WaveRing.h"

//--------------------------------------------------------------
void ofApp::setup(){


  gui.setup();
  gui.add(framesPerCycle.set("framesPerCycle", 50, 1, 500));
  gui.add(radius.set("radius", 100, 1, 500));
  gui.add(segments.set("segments", 100, 1, 500));
  gui.add(width.set("width", 2, 0, 5));
  gui.add(noiseStep.set("noiseStep", 0.0,0, 1));
  gui.add(noiseAmount.set("noiseAmount", 0.40, 0.0, 100));

  WaveRing wavering;
  shapes.push_back(wavering);

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
    shapes[i].setNoiseStep(noiseStep);
    shapes[i].setNoiseAmount(noiseAmount);
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
