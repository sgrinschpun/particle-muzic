package cat.ifae.phenomena.viz.particle;

import beads.AudioContext;
import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;
import cat.ifae.phenomena.viz.sound.MySynth;

import processing.core.PApplet;
import processing.core.PVector;

import java.util.ArrayList;

public
class MyParticleFamily {

    PApplet p;
    public AudioContext ac;
    public float x;
    public float y;
    public MyParticleData particleData;
    public MyParams myParams;
    public CurrentCicle currentCicle;

    protected int i;
    protected String q;

    public PVector location, acceleration;

    public ArrayList<MyShape> shapes;
    public ArrayList<MySynth> sounds;

    public MyParticleFamily(PApplet p, PVector location, PVector acceleration, MyParticleData particleData){
        this.p = p;
        this.location = location;
        this.acceleration = acceleration;
        this.particleData = particleData;
        this.shapes = new ArrayList<MyShape>();
        this.sounds = new ArrayList<MySynth>();

    }

    protected void addMyShapes(){}

    protected void addMySounds(){}

    public void display(){}

    public void sound(){
        for (MySynth sound: sounds){
            sound.ac.start();
        }
    }

}
