package cat.ifae.phenomena.viz.shapes;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.params.MyFamilyParams;

import processing.core.PApplet;

public class MyShape {
    PApplet p;
    protected float x;
    protected float y;

    protected MyFamilyParams myParams;

    public MyShape(PApplet p, float x, float y, MyFamilyParams myParams) {

        this.p = p;
        this.x = x;
        this.y = y;
        this.myParams = myParams;
    }

    public void display(){}

    public void move(){}
}