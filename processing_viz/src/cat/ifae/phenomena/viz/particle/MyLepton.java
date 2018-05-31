package cat.ifae.phenomena.viz.particle;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;
import processing.core.PApplet;

class MyLepton extends MyParticleFamily{

    private int i = 0;
    private String q= "";

    public MyLepton(PApplet p, float x, float y, MyParticleData particleData){
        super(p, x,y, particleData);
        this.myParams= new MyParams(p, particleData,q,i);
        this.currentCicle = new CurrentCicle(p, myParams.lepton.getSpeed());

        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        shapes.add(new MyWaveRing(p,x,y,currentCicle,myParams.lepton));
    }

    @Override
    public void display(){
        p.text(particleData.getName(), x, y);
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
