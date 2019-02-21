package cat.ifae.phenomena.viz.quantumuniverse;


import cat.ifae.phenomena.viz.MyParticle;
import cat.ifae.phenomena.viz.MyParticleData;
import cat.ifae.phenomena.viz.quantumuniverse.particle.*;
import processing.core.PApplet;
import processing.core.PVector;

public class MyParticleQU extends MyParticle {

    private MyParticleFamily particle;

    public MyParticleQU(PApplet p, PVector location, float vx,float vy, MyParticleData particleData) {
        super(p ,location, vx,vy,particleData);
        buildParticle();
    }

    public MyParticleQU(PApplet p, float vx,float vy, MyParticleData particleData) {
        super(p, vx,vy,particleData);
        this.location = new PVector((float) p.width / 2, (float) p.height / 2);
        buildParticle();
    }


    public void buildParticle() {
        switch (this.particleData.getType()) {
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

    @Override
    public void display() {
        particle.display();
    }


    @Override
    public PVector getLocation() {
        return particle.location;

    }

}
