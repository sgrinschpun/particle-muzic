package cat.ifae.phenomena.viz.particle;


import cat.ifae.phenomena.viz.params.MyParams;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.data.MyParticleData;

import cat.ifae.phenomena.viz.shapes.MyWaveLines;
import cat.ifae.phenomena.viz.shapes.MyWaveDisc;
import processing.core.PApplet;
import beads.AudioContext;

import java.util.ArrayList;

public class MyBoson extends MyParticleFamily{


    public MyBoson(PApplet p, AudioContext ac, float x, float y, MyParticleData particleData){
        super(p, ac, x, y, particleData);
        this.myParams= new MyParams(p, particleData);
        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        shapes = new ArrayList<MyShape>();
        shapes.add(new MyWaveDisc(p,x,y,myParams.boson));
        //shapes.add(new MyWaveLines(p,x,y,myParams.boson));

    }

    @Override
    public void display(){
        for (MyShape shape: shapes){
            shape.display();
        }
    }

    @Override
    public void move(){
        for (MyShape shape: shapes){
            shape.move();
        }
    }
}
