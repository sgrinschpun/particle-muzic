package cat.ifae.phenomena.viz.shapes;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.params.MyFamilyParams;

import processing.core.PApplet;
import processing.core.PVector;
import java.util.Random;

public class MyShape {
    PApplet p;
    protected float x;
    protected float y;

    PVector location;
    PVector velocity;



    protected MyFamilyParams myParams;

    public MyShape(PApplet p, float x, float y, MyFamilyParams myParams) {

        this.p = p;
        this.x = x;
        this.y = y;
        this.location = new PVector(x, y);
        this.velocity = new PVector(p.random(-2,2),p.random(-2,2));
        this.myParams = myParams;
    }

    public void display(){}

    public void move(){
        update();
        checkEdges();
    }

    private void update() {
        location.add(velocity);
    }

    private void checkEdges() {

        if (location.x > p.width) {
            location.x = 0;
        } else if (location.x < 0) {
            location.x = p.width;
        }

        if (location.y > p.height) {
            location.y = 0;
        } else if (location.y < 0) {
            location.y = p.height;
        }

    }
}