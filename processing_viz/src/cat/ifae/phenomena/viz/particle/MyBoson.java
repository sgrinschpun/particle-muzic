package cat.ifae.phenomena.viz.particle;


import cat.ifae.phenomena.viz.params.MyParams;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.data.MyParticleData;

import cat.ifae.phenomena.viz.shapes.MyWaveLines;
import cat.ifae.phenomena.viz.shapes.MyWaveDisc;
import processing.core.PApplet;
import beads.AudioContext;
import processing.core.PVector;

import java.util.ArrayList;

public class MyBoson extends MyParticleFamily{


    public MyBoson(PApplet p, PVector location, PVector acceleration, MyParticleData particleData){
        super(p, location, acceleration, particleData);
        this.myParams= new MyParams(p, particleData);
        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        shapes = new ArrayList<MyShape>();
        shapes.add(new MyWaveDisc(p,location,acceleration,myParams.boson));
        //shapes.add(new MyWaveLines(p,x,y,myParams.boson));

    }

    @Override
    public void display(){
        for (MyShape shape: shapes){
            shape.display();
        }
    }

}
