#ifdef DEBUG
#define DEBUG_MSG(str) do { std::cout << str << std::endl; } while( false )
#else
#define DEBUG_MSG(str) do { } while ( false )
#endif
#include "Model.h"

Model::Model(shared_ptr<ParticleData>& _data): data(_data){

}

void Model::setShape(){
    shape = make_shared<WaveRingVariation>();

    shape -> setCycle(framesPerCycle);
    shape -> setShapeNum(shapes_num);
    shape -> setRadius(radius);
    shape -> setFadeAmount(fadeAmnt);
    shape -> setPosAmp(pos_amp);
    shape -> setRotAmp(rot_amp);
    shape -> setSpeedAmp(speed_amp);
    shape -> setColorMode(col_mode);
    shape -> setNoiseStep(noiseStep);
    shape -> setNoiseAmount(noiseAmount);
    shape -> setWidth(width);
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
