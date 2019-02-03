#include "Model.h"

Model::Model(shared_ptr<ParticleData>& _data): data(_data){
  buildShape();
}

void Model::buildShape(){


    shape = make_shared<WaveRingVariation>(ZZZZZZZZ);
}



void Model::setup(){
    shape->setup();
}

void Model::draw(){
    shape->draw();
}

void Model::update(){
    shape->update();
}
