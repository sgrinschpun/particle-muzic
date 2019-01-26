#ifndef _Colors //
#define _Colors //
#include "ofMain.h"

class Colors {
  private:
    ofColor red, green, blue, cyan, magenta, yellow, white, black;
    vector <ofColor> matterColors = {red,green,blue};
    vector <ofColor> antiMatterColors = {cyan,magenta,yellow};
    vector <ofColor> allColors = {red,green,blue,cyan,magenta,yellow};

  public:
    vector <ofColor> getMatterColors(){return matterColors;};
    vector <ofColor> getAntiMatterColors(){return antiMatterColors;};
    vector <ofColor> getAllColors(){return antiMatterColors;};
    ofColor getWhite(){return white;};
    ofColor getBlack(){return black;};

    Colors();
    ~Colors() {}

};
#endif
