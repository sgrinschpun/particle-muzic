import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.particle.MyParticle;
import processing.core.PApplet;

public class Sketch extends PApplet{

    MyParticleData electronData = TestParticles.electron;
    MyParticleData pionData = TestParticles.pion;
    MyParticleData neutronData = TestParticles.neutron;

    MyParticle testParticle;



    public void settings(){
        fullScreen();
        size(1280,720);
        smooth();
    }

    public void setup(){
        testParticle = new MyParticle(this,640, 360, neutronData);
     }

    public void draw(){
        background(0);
        testParticle.display();

    }
}

