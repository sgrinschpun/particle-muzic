import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.particle.MyParticle;
import processing.core.PApplet;
import java.util.ArrayList;

public class Sketch extends PApplet{

    public ArrayList<MyParticle> allParticles;

    MyParticleData electronData = TestParticles.eminus;
    MyParticleData pionData = TestParticles.pion;
    MyParticleData neutronData = TestParticles.neutron;
    MyParticleData ZData = TestParticles.Z0;
    MyParticleData N1700Data = TestParticles.N1700;
    MyParticleData muplusData = TestParticles.muplus;


    MyParticle testParticle, testParticle2;



    public void settings(){
        fullScreen();
        size(1280,720);
        smooth();
    }

    public void setup(){
        allParticles = new ArrayList<MyParticle>();
        allParticles.add(new MyParticle(this,200, 200, ZData));
        allParticles.add(new MyParticle(this,500, 200, electronData));
        allParticles.add(new MyParticle(this,800, 200, pionData));
        allParticles.add(new MyParticle(this,200, 400, neutronData));
        allParticles.add(new MyParticle(this,500, 400, N1700Data));
        allParticles.add(new MyParticle(this,800, 400, muplusData));




        //testParticle = new MyParticle(this,640, 360, ZData);
        //testParticle2 = new MyParticle(this,300, 300, neutronData);
     }

    public void draw(){
        background(0);
        for (MyParticle particle: allParticles){
            particle.display();
        }
    }
}

