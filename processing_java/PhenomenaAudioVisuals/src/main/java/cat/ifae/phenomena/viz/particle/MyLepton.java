package cat.ifae.phenomena.viz.particle;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;
import processing.core.PApplet;
import processing.core.PVector;

class MyLepton extends MyParticleFamily{

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
