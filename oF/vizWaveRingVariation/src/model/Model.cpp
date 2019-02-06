#include "Model.h"

Model::Model(shared_ptr<ParticleData>& _data): data(_data){
  buildParameters();
  setShape();
}

void Model::setShape(){
    shape = make_shared<WaveRingVariation>();
    shape -> setShapeNum(shapes_num);
    shape -> setAfterImg(after_img);
    shape -> setRadius(radius);
    shape -> setPosAmp(pos_amp);
    shape -> setRotAmp(rot_amp);
    shape -> setSpeedAmp(speed_amp);
    shape -> setColorMode(col_mode);
    shape -> setNoiseStep(noiseStep);
    shape -> setNoiseAmount(noiseAmount);
    shape -> setWidth(width);
    shape -> setCycle(framesPerCycle);
    shape -> setSegments(segments);
}

void Model::draw(){
    shape->draw();
}

void Model::update(){
    shape->update();
}

void Model::setPosition(ofPoint _position){
  shape->setPosition(_position);
}
