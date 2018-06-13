package cat.ifae.phenomena.viz.particle;

import beads.AudioContext;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.shapes.MyWaveDisc;
import cat.ifae.phenomena.viz.params.MyParams;

import processing.core.PApplet;
import processing.core.PVector;

import java.util.ArrayList;

public class MyBaryon extends MyParticleFamily{


    public MyBaryon(PApplet p, PVector location, MyParticleData particleData){
        super(p, location, particleData);
        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        shapes = new ArrayList<MyShape>();
        int j = 0;
        for (String q: particleData.getComposition()) {
            myParams = new MyParams(p, particleData,q,j);
            currentCicle = new CurrentCicle(p, myParams.quark.getSpeed());
            shapes.add(new MyWaveRing(p,currentCicle,myParams.quark));
            j++;
        }
       shapes.add(new MyWaveDisc(p,myParams.gluon));
    }

    @Override
    public void display(){
        p.text(particleData.getName(), location.x, location.y);
        update();
        p.blendMode(PApplet.ADD);
        for (MyShape shape: shapes){
            shape.setLocation(location);
            shape.display();
        }
    }

}
