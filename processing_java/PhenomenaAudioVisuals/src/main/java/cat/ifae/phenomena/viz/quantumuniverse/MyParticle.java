package cat.ifae.phenomena.viz.quantumuniverse;


import cat.ifae.phenomena.viz.MyParticleData;
import cat.ifae.phenomena.viz.quantumuniverse.particle.*;
import processing.core.PApplet;
import processing.core.PVector;

public class MyParticle {

    PApplet p;
    private MyParticleData particleData;
    private MyParticleFamily particle;
    public PVector location, velocity;

    protected float theta, beta;


    public MyParticle(PApplet p, PVector location, float theta, float beta, MyParticleData particleData) {
        this.p = p;
        this.location = location;
        this.theta = theta;
        this.beta = beta;
        this.velocity = setVelocity(theta, beta);

        this.particleData = particleData;

        buildParticle();
    }

    public MyParticle(PApplet p, float theta, float beta, MyParticleData particleData) {
        this.p = p;
        this.location = new PVector((float) p.width / 2, (float) p.height / 2);
        this.theta = theta;
        this.beta = beta;
        this.velocity = setVelocity(theta, beta);
        this.particleData = particleData;
        buildParticle();
    }

    protected PVector setVelocity(float theta, float beta){

        velocity = PVector.fromAngle(theta);
        velocity.mult(3*beta);
        return velocity;

        //return new PVector(0f,0f);
    }


    private void buildParticle() {
        switch (particleData.getType()) {
            case "lepton":
                this.particle = new MyLepton(p, location, velocity, particleData);
                break;
            case "meson":
                this.particle = new MyMeson(p, location, velocity, particleData);
                break;
            case "baryon":
                this.particle = new MyBaryon(p, location, velocity, particleData);
                break;
            case "quark":
                this.particle = new MyQuark(p, location, velocity, particleData);
                break;
            case "boson":
                this.particle = new MyBoson(p, location, velocity, particleData);
                break;
        }
    }

    public void display() {
        particle.display();
    }


    public PVector getLocation() {
        return particle.location;

    }

}