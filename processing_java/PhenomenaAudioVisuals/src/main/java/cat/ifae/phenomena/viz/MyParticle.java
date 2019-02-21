package cat.ifae.phenomena.viz;

import processing.core.PApplet;
import processing.core.PVector;

public abstract class MyParticle {

    public PApplet p;
    public MyParticleData particleData;
    public PVector location, velocity;
    public float vx,vy, beta;


    public MyParticle(PApplet p, PVector location, float vx, float vy, MyParticleData particleData) {
        this.p = p;
        this.location = location.copy();
        this.vx = vx;
        this.vy = vy;
        this.velocity = new PVector(vx,vy);
        this.velocity.mult(3);
        this.particleData = particleData;

    }

    public MyParticle(PApplet p, float vx, float vy, MyParticleData particleData) {
        this.p = p;
        this.vx = vx;
        this.vy = vy;
        this.velocity = new PVector(vx,vy);
        this.velocity.mult(3);
        this.particleData = particleData;

        //this.location = new PVector((float) p.width / 2, (float) p.height / 2);
    }

    // abstract methods which will be implemented by its subclass(es)
    abstract public void display();
    abstract public PVector getLocation();


}
