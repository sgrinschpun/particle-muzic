package cat.ifae.phenomena.viz.particle;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;

import processing.core.PApplet;

import java.util.ArrayList;

public
class MyParticleFamily {

    PApplet p;
    public float x;
    public float y;
    public MyParticleData particleData;
    public MyParams myParams;
    public CurrentCicle currentCicle;

    protected int i;
    protected String q;

    public ArrayList<MyShape> shapes;

    public MyParticleFamily(PApplet p, float x, float y, MyParticleData particleData){
        this.p = p;
        this.x = x;
        this.y = y;
        this.particleData = particleData;
        this.shapes = new ArrayList<MyShape>();

    }

    protected void addMyShapes(){}

    public void display(){}

    public void move(){}


}
