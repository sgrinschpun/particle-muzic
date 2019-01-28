#include "NewWaveRingExample.h"

NewWaveRingExample::NewWaveRingExample(){

}

void NewWaveRingExample::setup(){
  setupSignedNoise();

}

void NewWaveRingExample::draw(){
  ofBackgroundGradient( ofColor(255), ofColor(180), OF_GRADIENT_CIRCULAR);

	float centerX = radialNoiseDemoX;
	float centerY = radialNoiseDemoY;

	// Render the Signed Noise demo, using
	// the noise as radial displacements to a circle.
	ofPushMatrix();
	ofTranslate(centerX + radialNoiseDemoR,centerY,0);
	ofEnableAlphaBlending();
	ofEnableSmoothing();
	ofNoFill();

	// Draw a faint plain circle, so that we can better understand
	// the radial displacements caused by the signed noise later on.
	// ofSetColor(0,0,0, 64);
	// ofSetCircleResolution(256);
	// ofDrawEllipse(0,0, radialNoiseDemoR*2,radialNoiseDemoR*2);

	// Let's use the signed noise as a radial displacement to a circle.
	// We render out the points stored in the X and Y arrays.
	ofMesh wigglyMeshLine; // yes, technically, it's a "mesh"
	wigglyMeshLine.setMode(OF_PRIMITIVE_LINE_STRIP);
	float px = 0, py = 0;
	for (int i=(nSignedNoiseData-1); i>=0; i--){

		// From the 'i' iterator, use ofMap to compute both
		// an angle (around a circle) and an alpha value.
		float angle   = ofMap(i, 0,nSignedNoiseData-1, 0,-TWO_PI) - HALF_PI;
		float alph    = ofMap(i, 0,nSignedNoiseData-1, 1,0     );
		//wigglyMeshLine.addColor(ofFloatColor(0,0,255, alph));
    wigglyMeshLine.addColor(ofFloatColor(0,0,255));


		// Cpmpute the displaced radius
		float wigglyRadius = radialNoiseDemoR;
		wigglyRadius +=  radialNoiseDemoR * signedNoiseData[i];

		// Good old-fashioned trigonometry: y = cos(t), x = sin(t)
		px = wigglyRadius * cos( angle );
		py = wigglyRadius * sin( angle );
        wigglyMeshLine.addVertex({px,py,0});
	}

	// draw the "mesh" (line)
	ofEnableSmoothing();
	wigglyMeshLine.draw();

	// draw a little ball at the end
	// ofFill();
	// ofSetColor(0,0,0, 160);
	// ofDrawEllipse(px,py, 7,7);

	ofPopMatrix();

}

void NewWaveRingExample::update(){
  updateSignedNoise();

}

void NewWaveRingExample::setNoiseStep(float _noiseStep){
  noiseStep=_noiseStep;
}

void NewWaveRingExample::setNoiseAmount(float _noiseAmount){
  noiseAmount=_noiseAmount;
}

void NewWaveRingExample::setupSignedNoise(){

  radialNoiseDemoY = 200;
	radialNoiseDemoR = 100;
	radialNoiseDemoX = ofGetWidth()/2 - radialNoiseDemoR;

  nSignedNoiseData = 400;
	signedNoiseData = new float[nSignedNoiseData];
	for (int i=0; i<nSignedNoiseData; i++){
		signedNoiseData[i] = 0;
	}
  radialNoiseCursor = 0.0;
}

void NewWaveRingExample::updateSignedNoise(){

  // Shift all of the old data forward through the array
  for (int i=(nSignedNoiseData-1); i>0; i--){
    signedNoiseData[i] = signedNoiseData[i-1];
  }

  // Compute the latest data, and insert it at the head of the array.
	// Here is where ofSignedNoise is requested.
  signedNoiseData[0] = noiseAmount * ofSignedNoise( radialNoiseCursor );
  radialNoiseCursor += noiseStep;

}
