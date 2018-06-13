package cat.ifae.phenomena.viz.shapes;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.params.MyFamilyParams;

import processing.core.PApplet;
import processing.core.PVector;

import java.util.concurrent.ThreadLocalRandom;
import static processing.core.PConstants.TWO_PI;

public class MyWaveRing extends MyShape {


    private float noiseAmount;
    private CurrentCicle currentCicle;
    private float r0, weight, ampFactor, noiseScale, r;
    private int color, noiseSeed;

    private static int N = 300;

    public MyWaveRing(PApplet p, CurrentCicle currentCicle, MyFamilyParams myParams){
        super(p,myParams);
        this.currentCicle = currentCicle;
        this.r0 = (float) myParams.getSize();
        this.weight = myParams.getWeight();
        this.ampFactor = myParams.getAmpFactor();
        this.noiseScale = (float) myParams.getNoiseScale();
        this.color = myParams.getColor();
        this.noiseSeed = ThreadLocalRandom.current().nextInt(1, 100);
    }

    public void display(){
        draw();
    }

    private void draw(){
        p.noFill();
        currentCicle.update();
        updateColor();
        setR();
        p.stroke(color);
        p.strokeWeight(weight);
        p.beginShape();
        p.noiseSeed(noiseSeed);
        setNoiseAmount();
        setVertex();
        p.endShape();
    }


    private void updateColor(){
        if (currentCicle.getProgressRatio() == currentCicle.getProgressRatioMax()){
            color = myParams.updateColor();
        }
    }


    private void setR(){
       /* if (currentCicle.number == 0){
            r= (float) (r0*currentCicle.SextEaseOutRatio);
        }else r = r0;*/
       r = r0;
    }

    private void setNoiseAmount(){

        currentCicle.update();

        if (currentCicle.getProgressRatio() <= 0.5){
            noiseAmount = (float) (currentCicle.getQuadEaseOutRatio()*ampFactor);
        }else{
            if (currentCicle.getProgressRatio() > 0.5){
                noiseAmount = (float) ((1-currentCicle.getQuadEaseInRatio())*ampFactor);
            }
        }
        if (currentCicle.getProgressRatio() == currentCicle.getProgressRatioMax()){
            noiseSeed = ThreadLocalRandom.current().nextInt(1, 100);
        }
    }

    private void setVertex(){
        for (Integer i =0; i<N+1;i++) {
            float x1 = (float) (location.x + r * Math.cos(TWO_PI * i / N));
            float y1 = (float) (location.y + r * Math.sin(TWO_PI * i / N));
            x1 += p.map(p.noise(noiseScale*x1,noiseScale*y1),0,1,-noiseAmount,noiseAmount);
            y1 += p.map(p.noise(noiseScale*x1,noiseScale*y1),0,1,-noiseAmount,noiseAmount);
            p.vertex(x1,y1);
        }
    }

}

