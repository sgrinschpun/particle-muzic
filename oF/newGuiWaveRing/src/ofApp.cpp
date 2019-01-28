#include "ofApp.h"
#include "NewWaveRing.h"

//--------------------------------------------------------------
void ofApp::setup(){


  gui.setup();
  gui.add(noiseStep.set("noiseStep", 0.01, 0.01, 0.15));
  gui.add(noiseAmount.set("noiseAmount", 0.40, 0.0, 1));

  NewWaveRing wavering;
  shapes.push_back(wavering);

  for(int i=0; i<shapes.size(); i++){
    shapes[i].setup();
  }

}

//--------------------------------------------------------------
void ofApp::update(){

  for(int i=0; i<shapes.size(); i++){
    shapes[i].update();

    shapes[i].setNoiseStep(noiseStep);
    shapes[i].setNoiseAmount(noiseAmount);

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
