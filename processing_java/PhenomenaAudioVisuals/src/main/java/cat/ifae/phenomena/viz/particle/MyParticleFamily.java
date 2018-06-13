package cat.ifae.phenomena.viz.particle;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;

import processing.core.PApplet;
import processing.core.PVector;

import java.util.ArrayList;

public
class MyParticleFamily {

    PApplet p;
    public float x;
    public float y;
    public MyParticleData particleData;
    public MyParams myParams;
    public CurrentCicle currentCicle;

    protected int i;
    protected String q;

    protected PVector location, acceleration, velocity;

    public ArrayList<MyShape> shapes;

    protected float topSpeed;

    public MyParticleFamily(PApplet p, PVector location, MyParticleData particleData){
        this.p = p;

        this.location = location.copy();
        this.acceleration = setAcceleration();
        this.acceleration.mult(p.random(2f));
        this.velocity = setVelocity();
        this.topSpeed = 10f;

        this.particleData = particleData;

        this.shapes = new ArrayList<MyShape>();


    }

    protected PVector setAcceleration(){
        return PVector.random2D(p);
    }

    protected PVector setVelocity(){
        return new PVector(0f,0f);
    }

    protected void addMyShapes(){}

    public void display(){}

    protected void update() {
        checkEdges();
        velocity.add(acceleration);
        velocity.limit(topSpeed);
        location.add(velocity);
    }

    protected void checkEdges() {
        if ((location.x > p.width) || (location.x < 0)) {
            velocity.x = velocity.x * -1;
            acceleration.x = acceleration.x * -1;
        }
        if ((location.y > p.height) || (location.y < 0)) {
            velocity.y = velocity.y * -1;
            acceleration.y = acceleration.y * -1;
        }
    }


}
