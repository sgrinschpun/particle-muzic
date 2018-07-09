package cat.ifae.phenomena.viz.quantumuniverse.particle;

import cat.ifae.phenomena.viz.MyParticleData;
import cat.ifae.phenomena.viz.quantumuniverse.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.quantumuniverse.shapes.MyShape;
import cat.ifae.phenomena.viz.quantumuniverse.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.quantumuniverse.params.MyParams;
import processing.core.PApplet;
import processing.core.PVector;

public class MyLepton extends MyParticleFamily{

    public MyLepton(PApplet p, PVector location, PVector velocity, MyParticleData particleData){
        super(p, location, velocity, particleData);
        this.myParams= new MyParams(p, particleData);
        this.currentCicle = new CurrentCicle(p, myParams.lepton.getSpeed());
        addMyShapes();
    }


    @Override
    public void addMyShapes(){
        shapes.add(new MyWaveRing(p,currentCicle,myParams.lepton));
    }


    @Override
    public void display(){
        update();
        p.text(particleData.getName(), location.x, location.y);
        for (MyShape shape: shapes){
            shape.setLocation(location);
            shape.display();
        }
    }

}
