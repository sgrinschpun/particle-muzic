#include "ParticleData.h"

ParticleData::ParticleData(int _id, int _parentId, string _name, string _type): id(_id), parentId(_parentId), name(_name), type(_type){
}

ParticleData::ParticleData(int _id, int _parentId, string _name, string _type, vector<string> _composition, double _mass, double _charge, vector<string> _decay): id(_id), parentId(_parentId), name(_name), type(_type), composition(_composition), mass(_mass), charge(_charge), decay(_decay){
}

int ParticleData::getId(void){
  return id;
}

int ParticleData::getParentId(void){
  return parentId;
}

string ParticleData::getName(void){
  return name;
}

string ParticleData::getType(void){
  return type;
}

vector<string> ParticleData::getComposition(void){
  return composition;
}

Boolean ParticleData::isFundamental(void){
  return composition.empty();
}

double ParticleData::getMass(void){
  return mass;
}

double ParticleData::getCharge(void){
  return charge;
}

vector<string> ParticleData::getDecay(void){
  return decay;
}

Boolean ParticleData::isStable(void){
  return decay.empty();
}
