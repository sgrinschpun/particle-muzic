#include "NewWaveRing.h"

NewWaveRing::NewWaveRing(){
  cycle = new Cycle(120);
  segments =100;

  centerY = ofGetHeight()/2;
  centerX = ofGetWidth()/2;
}

void NewWaveRing::setup(){
  setupSignedNoise();

}

void NewWaveRing::testDraw2(){
  ofBackgroundGradient( ofColor(255), ofColor(180), OF_GRADIENT_CIRCULAR);

	ofPushMatrix();
	ofTranslate(centerX,centerY,0);
	ofEnableAlphaBlending();
	ofEnableSmoothing();
	ofNoFill();
  ofSetLineWidth(width);


	ofMesh wigglyMeshLine; // yes, technically, it's a "mesh"
	wigglyMeshLine.setMode(OF_PRIMITIVE_LINE_STRIP);
  ofPoint p;

  float max = (cycle -> getEaseQuart2());
  float wigglyRadius = radius;
  for(int i=0; i<=nSignedNoiseData; i++){
		wigglyRadius +=  radius * signedNoiseData[i]*max;
    p.x =  (radius * cos(TWO_PI * i / nSignedNoiseData));
    p.y =  (radius * sin(TWO_PI * i / nSignedNoiseData));
    wigglyMeshLine.addVertex(p);
  }

  if (cycle -> newLoop()==true){
    nSignedNoiseData = segments;
  	signedNoiseData = new float[nSignedNoiseData];
  	for (int i=0; i<nSignedNoiseData; i++){
      ofPoint vertex = wigglyMeshLine.getVertex(i);
  		signedNoiseData[i] =  ofSignedNoise( noiseStep*vertex.x, noiseStep*vertex.y);
      vertex += signedNoiseData[i]*noiseAmount*max;
      wigglyMeshLine.setVertex(i, vertex);
  	}
  }

  ofEnableSmoothing();
  wigglyMeshLine.draw();
  ofPopMatrix();
}

void NewWaveRing::testDraw(){
  ofBackgroundGradient( ofColor(255), ofColor(180), OF_GRADIENT_CIRCULAR);

	ofPushMatrix();
	ofTranslate(centerX,centerY,0);
	ofEnableAlphaBlending();
	ofEnableSmoothing();
	ofNoFill();
  ofSetLineWidth(width);


	ofMesh wigglyMeshLine; // yes, technically, it's a "mesh"
	wigglyMeshLine.setMode(OF_PRIMITIVE_LINE_STRIP);
  ofPoint p;

  float max = (cycle -> getEaseQuart2());
  float wigglyRadius = radius;
  for(int i=0; i<=nSignedNoiseData/2; i++){
		wigglyRadius +=  radius * signedNoiseData[i]*max;
    p.x =  (wigglyRadius * cos(TWO_PI * i / nSignedNoiseData));
    p.y =  (wigglyRadius * sin(TWO_PI * i / nSignedNoiseData));
    wigglyMeshLine.addVertex(p);
  }
  for(int i=nSignedNoiseData/2-1; i==0; i--){
    wigglyRadius +=  radius * signedNoiseData[i]*max;
    p.x =  (wigglyRadius * cos(TWO_PI * i / nSignedNoiseData));
    p.y =  (wigglyRadius * sin(TWO_PI * i / nSignedNoiseData));
    wigglyMeshLine.addVertex(p);
  }
  ofEnableSmoothing();
  wigglyMeshLine.draw();
  ofPopMatrix();
}


void NewWaveRing::draw(){
  testDraw2();

}

void NewWaveRing::update(){
  //updateSignedNoise();
  if (cycle -> newLoop()==true){
    updateSignedNoise();
  }

}

void NewWaveRing::setNoiseStep(float _noiseStep){
  noiseStep=_noiseStep;
}

void NewWaveRing::setNoiseAmount(float _noiseAmount){
  noiseAmount=_noiseAmount;
}

void NewWaveRing::setWidth(int _width){
  width = _width;
}

void NewWaveRing::setCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
  cycle -> setFramesPerCycle(_framesPerCycle);
}

void NewWaveRing::setRadius(float _radius){
  radius = _radius;
}

void NewWaveRing::setSegments(int _segments){
  segments = _segments;
}

void NewWaveRing::setupSignedNoise(){

  radialNoiseCursor = 0.0;
  nSignedNoiseData = segments;
	signedNoiseData = new float[nSignedNoiseData];
	for (int i=0; i<nSignedNoiseData; i++){
		signedNoiseData[i] = noiseAmount * ofSignedNoise( radialNoiseCursor );
    radialNoiseCursor += noiseStep;;
	}

}

void NewWaveRing::updateSignedNoise(){
  nSignedNoiseData = segments;
  for (int i=0; i<nSignedNoiseData; i++){
    signedNoiseData[i] = noiseAmount * ofSignedNoise( radialNoiseCursor );
    radialNoiseCursor += noiseStep;;
  }

  // Shift all of the old data forward through the array
  //for (int i=(nSignedNoiseData-1); i>0; i--){
  //  signedNoiseData[i] = signedNoiseData[i-1];
  //}

  // Compute the latest data, and insert it at the head of the array.
	// Here is where ofSignedNoise is requested.
  //signedNoiseData[0] = noiseAmount * ofSignedNoise( radialNoiseCursor );
  //radialNoiseCursor += noiseStep;

}
