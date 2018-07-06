package cat.ifae.phenomena.viz.bubblechamber;

import cat.ifae.phenomena.viz.MyParticle;
import cat.ifae.phenomena.viz.MyParticleData;

import processing.core.PApplet;
import processing.core.PVector;

public class MyParticleBC extends MyParticle {


    public MyParticleBC(PApplet p, PVector location, float theta, float beta, MyParticleData particleData) {
        super(p ,location, theta,beta,particleData);
    }

    public MyParticleBC(PApplet p, float theta, float beta, MyParticleData particleData) {
        super(p, theta,beta,particleData);
        this.location = new PVector((float) p.width / 2, (float) p.height / 2);
    }

    @Override
    public void display() {

    }

    @Override
    public PVector getLocation() {
        return location;

    }





}
