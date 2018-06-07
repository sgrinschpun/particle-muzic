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
    MyParticleData ubarData = TestParticles.ubar;

    AudioContext ac;

    public void settings(){
        fullScreen();
        //size(5000,5000, P2D);
        smooth(4);
    }

    public void setup(){
        frameRate(30);
        ac = new AudioContext();
        allParticles = new ArrayList<MyParticle>();
        allParticles.add(new MyParticle(this, ZData));
        allParticles.add(new MyParticle(this, electronData));
        allParticles.add(new MyParticle(this, pionData));
        //allParticles.add(new MyParticle(this, neutronData));
        //allParticles.add(new MyParticle(this, ubarData));
        //allParticles.add(new MyParticle(this, N1700Data));
        //allParticles.add(new MyParticle(this, muplusData));


        //for (MyParticle particle: allParticles){
        //    particle.sound();
        //}

        //MySynth mysynth = new MySynth(ac,400);

        //mysynth.ac.start();

     }

    public void draw(){
        background(0);
        for (MyParticle particle: allParticles){
            particle.display();
        }
        // saveFrame("test/boson-######.png");

    }
}

