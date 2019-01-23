#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

}

//--------------------------------------------------------------
void ofApp::update(){
  for(int i=0; i<groupOfParticles.size(); i++){
    groupOfParticles[i].update();
}

}

//--------------------------------------------------------------
void ofApp::draw(){
  for(int i=0; i<groupOfParticles.size(); i++){
    groupOfParticles[i].draw();
}
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
  groupOfParticles.push_back(Particle(x, y, ofRandom(10,40)));

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
  for (int i =0; i < groupOfParticles.size(); i++) {
  float distance = ofDist(x,y, groupOfParticles[i].x, groupOfParticles[i].y);
  if (distance < groupOfParticles[i].dim) {
      groupOfParticles.erase(groupOfParticles.begin()+i);
  }
}

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
