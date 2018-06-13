package cat.ifae.phenomena.viz.shapes;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.params.MyFamilyParams;

import processing.core.PApplet;
import processing.core.PVector;
import java.util.Random;

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