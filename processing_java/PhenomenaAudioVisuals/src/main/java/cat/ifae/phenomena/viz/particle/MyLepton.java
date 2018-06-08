package cat.ifae.phenomena.viz.particle;


import cat.ifae.phenomena.viz.sound.MySynth;
import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;
import processing.core.PApplet;
import beads.AudioContext;
import processing.core.PVector;

class MyLepton extends MyParticleFamily{

    public MyLepton(PApplet p, PVector location, MyParticleData particleData){
        super(p, location, particleData);
        this.myParams= new MyParams(p, particleData);
        this.currentCicle = new CurrentCicle(p, myParams.lepton.getSpeed());

        addMyShapes();
        //addMySounds();
    }

    @Override
    public void addMyShapes(){
        shapes.add(new MyWaveRing(p,location, velocity, acceleration,currentCicle,myParams.lepton));
    }

    //@Override
    //public void addMySounds(){
    //    sounds.add(new MySynth(ac, currentCicle, 440.0f));
    //}

    @Override
    public void display(){
        p.text(particleData.getName(), x, y);
        for (MyShape shape: shapes){
            shape.display();
        }
    }

  /*  @Override
    public void sound(){
        for (MySynth sound: sounds){
            sound.ac.start();
        }
    }*/

}
