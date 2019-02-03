#ifndef _ParticleData //
#define _ParticleData //
#include "ofMain.h"

class ParticleData {
  private:
    int id;
    int parentId;
    string name;
    string type;
    vector<string> composition;
    double mass;
    double charge;
    vector<string> decay;

  public:
    int getId();
    int getParentId();
    string getName();
    string getType();
    vector<string> getComposition();
    double getMass();
    double getCharge();
    vector<string> getDecay();
    Boolean isStable();
    Boolean isFundamental();

    //constructor
    ParticleData(int _id, int _parentId, string _name, string _type);
    ParticleData(int _id, int _parentId, string _name, string _type, vector<string> _composition, double _mass, double _charge, vector<string> _decay);

    ~ParticleData() {}

};
#endif
