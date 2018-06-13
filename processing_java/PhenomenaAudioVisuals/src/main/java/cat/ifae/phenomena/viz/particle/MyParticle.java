package cat.ifae.phenomena.viz.particle;


import cat.ifae.phenomena.viz.data.MyParticleData;

import processing.core.PApplet;
import processing.core.PVector;

public class MyParticle {

    PApplet p;
    private MyParticleData particleData;
    private MyParticleFamily particle;
    public PVector location;


    public MyParticle(PApplet p, PVector location, MyParticleData particleData) {
        this.p = p;
        this.location = location;
        this.particleData = particleData;
        buildParticle();
    }


    public MyParticle(PApplet p, MyParticleData particleData) {
        this.p = p;
        this.location = new PVector((float) p.width / 2, (float) p.height / 2);
        this.particleData = particleData;
        buildParticle();
    }


    private void buildParticle() {
        switch (particleData.getType()) {
            case "lepton":
                this.particle = new MyLepton(p, location, particleData);
                break;
            case "meson":
                this.particle = new MyMeson(p, location, particleData);
                break;
            case "baryon":
                this.particle = new MyBaryon(p, location, particleData);
                break;
            case "quark":
                this.particle = new MyQuark(p, location, particleData);
                break;
            case "boson":
                this.particle = new MyBoson(p, location, particleData);
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