package cat.ifae.phenomena.viz;

import processing.core.PApplet;
import processing.core.PVector;

public abstract class MyParticle {

    public PApplet p;
    public MyParticleData particleData;
    public PVector location, velocity;
    public float theta, beta;


    public MyParticle(PApplet p, PVector location, float theta, float beta, MyParticleData particleData) {
        this.p = p;
        this.location = location.copy();
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

    // non-abstract methods it has default implementation
    protected PVector setVelocity(float theta, float beta){
        velocity = PVector.fromAngle(theta);
        velocity.mult(3*beta);
        return velocity;
    }

    // abstract methods which will be implemented by its subclass(es)
    abstract public void display();
    abstract public PVector getLocation();


}
