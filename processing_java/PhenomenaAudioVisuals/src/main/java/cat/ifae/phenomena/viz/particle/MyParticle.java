package cat.ifae.phenomena.viz.particle;

import cat.ifae.phenomena.viz.data.MyParticleData;

import processing.core.PApplet;

public class MyParticle {

    PApplet p;
    private float x;
    private float y;
    private MyParticleData particleData;
    private MyParticleFamily particle;

    public MyParticle(PApplet p,float x, float y, MyParticleData particleData){
        this.p = p;
        this.x = x;
        this.y = y;
        this.particleData = particleData;

        buildParticle();
    }

    private void buildParticle(){
        switch(particleData.getType()){
            case "lepton":
                this.particle = new MyLepton(p,x,y,particleData);
                break;
            case "meson":
                this.particle = new MyMeson(p,x,y,particleData);
                break;
            case "baryon":
                this.particle = new MyBaryon(p, x,y,particleData);
                break;
            case "boson":
                this.particle = new MyBoson(p, x,y,particleData);
                break;
        }
    }

    public void display(){
        particle.display();
    }

    public void move(){
        particle.move();
    }
}








