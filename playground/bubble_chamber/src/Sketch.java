import processing.core.PApplet;
import java.util.ArrayList;
import cat.ifae.phenomena.bubbleChamber.data.MyParticleData;
import cat.ifae.phenomena.bubbleChamber.particle.MyParticle;



public class Sketch extends PApplet{

    public ArrayList<MyParticle> allParticles;

    MyParticleData electronData = TestParticles.eminus;
    MyParticleData muonData = TestParticles.muplus;



    public void settings(){
        fullScreen();
        //size(1280,720);
        smooth();

    }

    public void setup() {
        frameRate(30);
        allParticles = new ArrayList<MyParticle>();
        allParticles.add(new MyParticle(this,0, 0.9f, electronData));
        allParticles.add(new MyParticle(this,0, 0.1f, muonData));
        this.background(220);
    }


    public void draw(){
        for (MyParticle particle: allParticles){
            particle.display();
        }


    }
}

