import oscP5.*;
import netP5.*;

OscP5 oscP5;

int CANVAS_WIDTH  = 600;
int CANVAS_HEIGHT = 600;

void setup() {
  size(CANVAS_WIDTH, CANVAS_HEIGHT);
  loadData();
  oscP5 = new OscP5(this, localOSCAddress, localOSCPort);
}

void oscEvent(OscMessage theOscMessage) {
  print("### received an osc message.");
  print(" addrpattern: " + theOscMessage.addrPattern());
  println(" typetag: " + theOscMessage.typetag());
}
  
int rectX      = 10; 
int rectY      = 20;
int rectWidth  = 30;
int rectHeight = 50; 

void draw() {
  background(0);
  rectX      = rectX      + 10;    
  rectY      = rectY      + 10;
  rectWidth  = rectWidth  + 10;
  rectHeight = rectHeight + 10

  if ( rectX > width() ) {
    rectX      = 10; 
    rectY      = 20;
    rectWidth  = 30;
    rectHeight = 50; 
  }

  void drawRectangle(rectX , rectY, rectWidth, rectHeight);
}