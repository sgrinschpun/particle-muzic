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
    PVector acceleration;
    float topSpeed;

    protected MyFamilyParams myParams;

    public MyShape(PApplet p, PVector location, PVector velocity, PVector acceleration, MyFamilyParams myParams) {
        this.p = p;
        this.location = location;
        this.velocity = velocity;
        this.topSpeed = 10;
        this.acceleration = acceleration;
        this.myParams = myParams;

    }

    public void display(){}

    public void move(){
        update();
        checkEdges();
    }

    private void update() {

        velocity.add(acceleration);
        velocity.limit(topSpeed);
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