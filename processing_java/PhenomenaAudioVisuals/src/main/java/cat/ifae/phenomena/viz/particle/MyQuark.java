package cat.ifae.phenomena.viz.particle;


import beads.AudioContext;
import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveDisc;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import processing.core.PApplet;

class MyQuark extends MyParticleFamily{

    public MyQuark(PApplet p, AudioContext ac, float x, float y, MyParticleData particleData){
        super(p, ac, x, y, particleData);

        addMyShapes();
    }

    public MyQuark(PApplet p, float x, float y, MyParticleData particleData){
        super(p, x, y, particleData);

        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        myParams = new MyParams(p, particleData,particleData.getName(),0);
        currentCicle = new CurrentCicle(p, myParams.quark.getSpeed());
        shapes.add(new MyWaveRing(p,x,y,currentCicle,myParams.quark));
    }

    @Override
    public void display(){
        p.text(particleData.getName(), x, y);
        p.blendMode(PApplet.ADD);
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
