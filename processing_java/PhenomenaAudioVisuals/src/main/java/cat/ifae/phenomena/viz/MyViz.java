package cat.ifae.phenomena.viz;

import processing.core.PApplet;
import processing.core.PVector;

import cat.ifae.phenomena.viz.quantumuniverse.MyParticleQU;
import cat.ifae.phenomena.viz.bubblechamber.MyParticleBC;

public class MyViz {
    private PApplet p;
    private String vizName;
    public MyParticle particle;


    public MyViz (PApplet p, String vizName ) {
        this.p = p;
        this.vizName = vizName;
    }

    public MyParticle particle(PVector location, float theta, float beta, MyParticleData particleData) {
        switch (vizName) {
            case "quantumuniverse" :
                particle = new MyParticleQU(this.p, location, theta, beta, particleData);
                break;
            case "bubblechamber" :
                particle = new MyParticleBC(this.p, location, theta, beta, particleData);
                break;
        }
        return particle;
    }

    public MyParticle particle(float theta, float beta, MyParticleData particleData) {
        switch (vizName) {
            case "quantumuniverse" :
                particle = new MyParticleQU(this.p, theta, beta, particleData);
                break;
            case "bubblechamber" :
                particle = new MyParticleBC(this.p, theta, beta, particleData);
                break;
        }
        return particle;
    }








}
