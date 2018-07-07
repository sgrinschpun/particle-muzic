package cat.ifae.phenomena.viz.bubblechamber;

import cat.ifae.phenomena.viz.MyParticle;
import cat.ifae.phenomena.viz.MyParticleData;

import processing.core.PApplet;
import processing.core.PVector;

public class MyParticleBC extends MyParticle {

    protected MyDynamics myDinamics;
    protected static float topVelocity = 20f;

    protected PVector acceleration;

    public MyParticleBC(PApplet p, PVector location, float theta, float beta, MyParticleData particleData) {
        super(p ,location,theta,beta,particleData);

        myDinamics = new MyDynamics(particleData);

    }

    public MyParticleBC(PApplet p, float theta, float beta, MyParticleData particleData) {
        super(p, theta,beta,particleData);
        this.location = new PVector((float) p.width / 2, (float) p.height / 2);

        myDinamics = new MyDynamics(particleData);
    }

    protected PVector setAcceleration(){
        return myDinamics.getAcceleration(velocity);
    }

    protected void update() {
        acceleration = setAcceleration();
        velocity.add(acceleration);
        PApplet.println(particleData.getName() + " Vel "+velocity);
        velocity.limit(topVelocity);
        location.add(velocity);
        PApplet.println(particleData.getName() + " Loc "+location);
    }

    protected void draw() {
        p.stroke(0);
        p.point(location.x,location.y);
    }

    public void display(){
        update();
        draw();
    }

    @Override
    public PVector getLocation() {
        return location;

    }
}
