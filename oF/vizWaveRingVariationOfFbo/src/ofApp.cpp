#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
  ofSetWindowTitle("Univers Quàntic @ cccB");
  ofBackground(0);
  ofSetFrameRate(60);
  ofSetVerticalSync(true);
	ofSetCircleResolution(256);

  groupOfParticleData.push_back(make_shared<ParticleData>(1,-1,"W+", "boson"));
  groupOfParticleData.push_back(make_shared<ParticleData>(1,-1,"tau-", "lepton"));
  //groupOfParticleData.push_back(make_shared<ParticleData>(1,-1,"nu_e", "lepton"));
  groupOfParticleData.push_back(make_shared<ParticleData>(1,-1,"pi0", "meson"));
  ofVec3f velocity1;
  velocity1.set(1,0,0);
  ofVec3f velocity2;
  velocity2.set(0,1,0);
  ofVec3f velocity3;
  velocity3.set(0,-1,0);
  ofPoint position;
  position.set(ofGetWidth()/2, ofGetHeight()/2,0);
  groupOfParticles.push_back(make_shared<Particle>(groupOfParticleData[0], position, velocity1));
  //groupOfParticles.push_back(make_shared<Particle>(groupOfParticleData[1],position, velocity2));
  //groupOfParticles.push_back(make_shared<Particle>(groupOfParticleData[2],position, velocity3));


}

//--------------------------------------------------------------
void ofApp::update(){
  for(int i=0; i<groupOfParticles.size(); i++){
    groupOfParticles[i]->update();
  }
}

//--------------------------------------------------------------
void ofApp::draw(){
  for(int i=0; i<groupOfParticles.size(); i++){
    groupOfParticles[i]->draw();
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
