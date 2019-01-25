#include "Colors.h"

Colors::Colors(){

  red.set(255, 0, 0);
  green.set(0, 255, 0);
  blue.set(0, 0, 255);
  cyan = red.invert();
  magenta = green.invert();
  yellow = blue.invert();
  white.set(255,255,255);
  black.set(0,0,0);

}
