package cat.ifae.phenomena.viz;

import processing.core.PApplet;
import processing.core.PVector;

public abstract class MyParticle {

    public PApplet p;
    public MyParticleData particleData;
    public PVector location, velocity;
    public float px,py, beta;


    public MyParticle(PApplet p, PVector location, float px, float py, float beta, MyParticleData particleData) {
        this.p = p;
        this.location = location.copy();
        this.px = px;
        this.py = py;
        this.beta = beta;
        this.velocity = setVelocity(px,py, beta);
        this.particleData = particleData;

    }

    public MyParticle(PApplet p, float px, float py, float beta, MyParticleData particleData) {
        this.p = p;
        this.px = px;
        this.py = py;
        this.beta = beta;
        this.velocity = setVelocity(px,py, beta);
        this.particleData = particleData;

        //this.location = new PVector((float) p.width / 2, (float) p.height / 2);
    }

    // non-abstract methods it has default implementation
    protected PVector setVelocity(float px, float py, float beta){
        velocity = new PVector(px,py);
        velocity.normalize().mult(3*beta);
        return velocity;
    }

    // abstract methods which will be implemented by its subclass(es)
    abstract public void display();
    abstract public PVector getLocation();


}
