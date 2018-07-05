package cat.ifae.phenomena.viz.quantumuniverse.particle;

import cat.ifae.phenomena.viz.MyParticleData;
import cat.ifae.phenomena.viz.quantumuniverse.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.quantumuniverse.shapes.MyShape;
import cat.ifae.phenomena.viz.quantumuniverse.shapes.MyWaveDisc;
import cat.ifae.phenomena.viz.quantumuniverse.shapes.MyWaveRing;

import cat.ifae.phenomena.viz.quantumuniverse.params.*;

import processing.core.PApplet;
import processing.core.PVector;

import java.util.ArrayList;

public class MyBaryon extends MyParticleFamily{


    public MyBaryon(PApplet p, PVector location, PVector velocity, MyParticleData particleData){
        super(p, location, velocity, particleData);
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
