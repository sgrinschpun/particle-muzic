import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.particle.MyParticle;
import processing.core.PApplet;
import java.util.ArrayList;

import beads.*;

public class Sketch extends PApplet{

    public ArrayList<MyParticle> allParticles;

    MyParticleData electronData = TestParticles.eminus;
    MyParticleData pionData = TestParticles.pion;
    MyParticleData neutronData = TestParticles.neutron;
    MyParticleData ZData = TestParticles.Z0;
    MyParticleData N1700Data = TestParticles.N1700;
    MyParticleData muplusData = TestParticles.muplus;

    AudioContext ac;

    public void settings(){
        fullScreen();
        size(1280,720);
        smooth();
    }

    public void setup(){
        frameRate(30);
        ac = new AudioContext();
        allParticles = new ArrayList<MyParticle>();
        allParticles.add(new MyParticle(this,ac,200, 200, ZData));
        allParticles.add(new MyParticle(this,ac,500, 200, electronData));
        //allParticles.add(new MyParticle(this,ac,800, 200, pionData));
        //allParticles.add(new MyParticle(this,ac,200, 400, neutronData));
        //allParticles.add(new MyParticle(this,ac,500, 400, N1700Data));
        //allParticles.add(new MyParticle(this,ac,800, 400, muplusData));


        for (MyParticle particle: allParticles){
            particle.sound();
        }

        //MySynth mysynth = new MySynth(ac,400);

        //mysynth.ac.start();

     }

    public void draw(){
        background(0);
        for (MyParticle particle: allParticles){
            particle.display();
        }
    }
}

