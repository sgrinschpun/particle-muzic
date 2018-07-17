package cat.ifae.phenomena.viz.bubblechamber.display;

import cat.ifae.phenomena.viz.MyParticleData;
import processing.core.PApplet;
import processing.core.PVector;

public class MyTrack {

    protected MyParticleData particleData;
    public PApplet p;

    public MyTrack (PApplet p, MyParticleData particleDataData){

        this.p = p;
        this.particleData = particleData;

    }

    public float getWidth(PVector velocity){
        float speed = velocity.mag();
        p.println(speed);
        float width = p.map(speed,0,3,5f,1);
        return width;

    }

    public int getColor(){
        return 1;
    }

    public void drawDotTrack(PVector location){
        p.stroke(255);
        p.point(location.x,location.y);
    }

    public void drawCircleTrack(PVector location, PVector velocity){
        p.noStroke();
        p.fill(255);
        float width = getWidth(velocity);
        p.ellipse(location.x,location.y,width,width);
    }

}
