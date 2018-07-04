package cat.ifae.phenomena.bubbleChamber.particle;


import cat.ifae.phenomena.bubbleChamber.data.MyParticleData;
import processing.core.PApplet;
import processing.core.PVector;


public class MyParticle {

    PApplet p;
    private MyParticleData particleData;

    public float theta, beta, topVelocity, q, m;

    public String name;

    protected PVector location, velocity, acceleration;

    private final static PVector B = new PVector(0, 0,  0.005f );


    public MyParticle(PApplet p, PVector location, float theta, float beta, MyParticleData particleData){
        this.p = p;

        this.location = location;

        this.theta = theta;
        this.beta = beta;
        this.velocity = setVelocity(theta, beta);
        this.topVelocity = 2f;

        this.particleData = particleData;
        this.q = (float) particleData.getCharge();
        this.m = (float) particleData.getMass();


        this.acceleration = setAcceleration();
    }

    public MyParticle(PApplet p, float theta, float beta, MyParticleData particleData){
        this.p = p;

        this.name = particleData.getName();

        this.location = setLocation();

        this.theta = theta;
        this.beta = beta;
        this.velocity = setVelocity(theta, beta);
        this.topVelocity = 200000f;

        this.particleData = particleData;
        this.q = (float) particleData.getCharge();
        this.m = (float) particleData.getMass();

    }

    protected PVector setLocation(){
        return new PVector((float) p.width / 2, (float) p.height / 2, 0);
    }


    protected PVector setVelocity(float theta, float beta){
        velocity = PVector.fromAngle(theta);
        velocity.set(velocity.x,velocity.y,0);
        velocity.mult(2*beta);
        PApplet.println("Vel "+velocity);
        return velocity;
    }

    protected void setBending() {
        PVector bending = velocity.cross(B);
        bending.mult(q);
        applyForce(bending);
    }

    protected void setDrag(){
        float speed = velocity.mag();
        float dragMagnitude = speed*speed/500;
        PVector drag = velocity.copy();
        drag.normalize();
        drag.mult(-1);
        drag.mult(dragMagnitude);

        applyForce(drag);

    }


    protected PVector setAcceleration(){

        acceleration = new PVector (0, 0);

        setDrag();
        setBending();
        return acceleration;
    }

    protected void applyForce(PVector force){
        float mass = 1;
        PVector f = PVector.div(force,mass);
        acceleration.add(f);
    }

    public void display(){
        update();
        draw();
    }

    protected void update() {
        acceleration = setAcceleration();
        PApplet.println(name + " Acc "+acceleration);
        velocity.add(acceleration);
        PApplet.println(name + " Vel "+velocity);
        velocity.limit(topVelocity);
        location.add(velocity);
        PApplet.println(name + " Loc "+location);
    }

    protected void draw(){
        p.stroke(0);
        p.point(location.x,location.y);
    }

}








