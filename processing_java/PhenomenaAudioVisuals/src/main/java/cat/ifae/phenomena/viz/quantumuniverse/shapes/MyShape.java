package cat.ifae.phenomena.viz.quantumuniverse.shapes;

import cat.ifae.phenomena.viz.quantumuniverse.params.*;

import processing.core.PApplet;
import processing.core.PVector;

public class MyShape {
    PApplet p;

    public PVector location;

    protected MyFamilyParams myParams;

    public MyShape(PApplet p, MyFamilyParams myParams) {
        this.p = p;
        this.myParams = myParams;
    }

    public void setLocation(PVector location){
        this.location = location;
    }

    public void display(){}

}