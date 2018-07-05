package cat.ifae.phenomena.viz;

import processing.core.PApplet;
import processing.core.PVector;

public class MyParticleViz {

    PApplet p;
    private MyParticleData particleData;
    public PVector location, velocity;
    protected float theta, beta;


    public MyParticle(PApplet p, PVector location, float theta, float beta, MyParticleData particleData) {
        this.p = p;
        this.location = location;
        this.theta = theta;
        this.beta = beta;
        this.velocity = setVelocity(theta, beta);
        this.particleData = particleData;

    }

    public MyParticle(PApplet p, float theta, float beta, MyParticleData particleData) {
        this.p = p;
        this.theta = theta;
        this.beta = beta;
        this.velocity = setVelocity(theta, beta);
        this.particleData = particleData;

        //this.location = new PVector((float) p.width / 2, (float) p.height / 2);

    }




    protected PVector setVelocity(float theta, float beta){

        velocity = PVector.fromAngle(theta);
        velocity.mult(3*beta);
        return velocity;

    }



    public void display() {
    }


    public PVector getLocation() {
        return this.location;
    }


}
