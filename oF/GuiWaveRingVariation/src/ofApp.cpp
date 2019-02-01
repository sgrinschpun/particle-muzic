#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
  ofBackground(0);
  ofSetFrameRate(60);
  ofSetBackgroundAuto(false);
  ofSetCircleResolution(60);

  gui.setup();
  //variations
  gui.add(shapes_num.set("number of shapes", 1, 1, 500));

  gui.add(pos.set("pos",
                  ofVec3f(0),
                  ofVec3f(0),
                  ofVec3f(ofGetWidth()/2, ofGetHeight()/2, 1000)));
  gui.add(rot.set("rot",
                  ofVec3f(0),
                  ofVec3f(0),
                  ofVec3f(720, 720, 720)));
  gui.add(speed.set("speed", 0, 0, 0.1));
  gui.add(color_mode.set("color mode", 0));
  gui.add(after_img.set("after image", 0, 0, 255));

  imgcount = 0;
  guidraw = true;

  //WaveRing
  gui.add(radius.set("radius", ofGetHeight()/4, 1, ofGetHeight()/2));
  gui.add(framesPerCycle.set("framesPerCycle", 50, 1, 500));
  //gui.add(radius.set("radius", 100, 1, 500));
  gui.add(segments.set("segments", 100, 1, 500));
  gui.add(width.set("width", 2, 0, 5));
  gui.add(noiseStep.set("noiseStep", 0.0,0, 1));
  gui.add(noiseAmount.set("noiseAmount", 0.40, 0.0, 100));

  WaveRingVariation particle;
  shapes.push_back(particle);

}

//--------------------------------------------------------------
void ofApp::update(){

  for (int i = 0; i < shapes.size(); i++) {
    shapes[i].update();

    shapes[i].setShapeNum(shapes_num);
    //shapes[i].setRadius(radius);
    shapes[i].setPosAmp(pos);
    shapes[i].setRotAmp(rot);
    shapes[i].setSpeedAmp(speed);
    shapes[i].setColorMode(color_mode);

    vector<WaveRing> waverings = shapes[i].getWaveRings();

    for (int j = 0; j < waverings.size(); j++) {

      waverings[j].setNoiseStep(noiseStep);
      waverings[j].setNoiseAmount(noiseAmount);
      waverings[j].setWidth(width);
      waverings[j].setCycle(framesPerCycle);
      waverings[j].setRadius(radius);
      waverings[j].setSegments(segments);

    }


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
//   if(key == 's'){
//
//     img.grabScreen(0,0,ofGetWidth(),ofGetHeight());
//     img.save("pic" + ofToString(imgcount) + ".png", OF_IMAGE_QUALITY_BEST);
//     imgcount++;
// }
//
// if (key == 'g') {
//     guidraw = false;
// }

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
