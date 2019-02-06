#ifdef DEBUG
#define DEBUG_MSG(str) do { std::cout << str << std::endl; } while( false )
#else
#define DEBUG_MSG(str) do { } while ( false )
#endif
#include "Particle.h"

Particle::Particle(shared_ptr<ParticleData>& _data): data(_data){
  ofPoint position;
  position.set(ofGetWidth()/2, ofGetHeight()/2,0);
  ofVec3f velocity;
  velocity.set(0,0,0);
  kinematics = make_shared<Kinematics>(position, velocity);
  DEBUG_MSG("Kinematics up");
  buildModel();
}

Particle::Particle(shared_ptr<ParticleData>& _data, ofPoint _position, ofVec3f _velocity): data(_data){
  kinematics = make_shared<Kinematics>(_position, _velocity);
  buildModel();
}


void Particle::buildModel(){
    string type = data->getType();
    string name = data->getName();
    const string neutrinos[] = {"nu_e", "nu_mu", "nu_tau", "nu_ebar","nu_mubar","nu_taubar"};

    if (type == "lepton"){
      auto it = find(begin(neutrinos), end(neutrinos), name);
      if (it != end(neutrinos)) {model = make_shared<Neutrino>(data);}
      else {model = make_shared<Lepton>(data);}
      //model = make_shared<Lepton>(data);
    }
    else if (type == "boson") {
      model = make_shared<Boson>(data);
      DEBUG_MSG("Boson Model Up");
    }
    else if (type == "meson") {model = make_shared<Meson>(data);}
    else if (type == "baryon"){model = make_shared<Baryon>(data);}
    else if (type == "quark") {model = make_shared<Quark>(data);}
  }


void Particle::draw(){
  model->draw();
}

void Particle::update(){
  kinematics->update();
  model->setPosition(kinematics->getPosition());
  model->update();
}
