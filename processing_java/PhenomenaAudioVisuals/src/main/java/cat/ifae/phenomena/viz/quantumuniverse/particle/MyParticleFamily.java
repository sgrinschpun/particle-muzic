package cat.ifae.phenomena.viz.quantumuniverse.particle;

import cat.ifae.phenomena.viz.MyParticleData;
import cat.ifae.phenomena.viz.quantumuniverse.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.quantumuniverse.params.MyParams;
import cat.ifae.phenomena.viz.quantumuniverse.shapes.MyShape;

import processing.core.PApplet;
import processing.core.PVector;

import java.util.ArrayList;

public class MyParticleFamily {

    PApplet p;

    public MyParticleData particleData;
    public MyParams myParams;
    public CurrentCicle currentCicle;

    protected int i;
    protected String q;

    public PVector location;
    protected PVector acceleration;
    protected PVector velocity;

    public ArrayList<MyShape> shapes;

    protected float topSpeed;

    public MyParticleFamily(PApplet p, PVector location, PVector velocity, MyParticleData particleData){
        this.p = p;

        this.location = location;
        this.velocity = velocity;


        this.acceleration = setAcceleration();
        //this.acceleration.mult(p.random(0.5f));

        this.topSpeed = 2f;

        this.particleData = particleData;


        this.shapes = new ArrayList<MyShape>();


    }

    protected PVector setAcceleration(){

        return new PVector(0f,0f);
        //return PVector.random2D(p);
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
