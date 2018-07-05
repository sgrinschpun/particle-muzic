package cat.ifae.phenomena.viz.quantumuniverse.shapes;

import cat.ifae.phenomena.viz.quantumuniverse.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.quantumuniverse.params.MyFamilyParams;

import processing.core.PApplet;

import java.util.concurrent.ThreadLocalRandom;

import static processing.core.PConstants.CLOSE;
import static processing.core.PConstants.TWO_PI;

public class MyWaveRing extends MyShape {


    private float noiseAmount;
    private CurrentCicle currentCicle;
    private float r0, weight, ampFactor, noiseScale, r;
    private int color, noiseSeed;

    private static int N = 100;

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
        setVertex1(r);
        p.endShape(CLOSE);

        /*p.beginShape();
        p.strokeWeight(30);
        p.stroke(p.random(255), p.random(255), p.random(255), 40);
        setVertex2(r);
        p.endShape();*/

        // if charged particle, alpha and weight depending on charge
        if (myParams.getCharge() != 0) {
            p.stroke(p.random(255), p.random(255), p.random(255), 40);
            p.strokeWeight(20);
            p.beginShape();
            p.noiseSeed(noiseSeed);
            setNoiseAmount();
            setVertex1(r);
            p.endShape();
        }

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

    private void setVertex1(float r){
        for (Integer i =0; i<N+1;i++) {
            float x1 = (float) (location.x + r * Math.cos(TWO_PI * i / N));
            float y1 = (float) (location.y + r * Math.sin(TWO_PI * i / N));

            x1 += p.map(p.noise(noiseScale*x1,noiseScale*y1),0,1,-noiseAmount,noiseAmount);
            y1 += p.map(p.noise(noiseScale*x1,noiseScale*y1),0,1,-noiseAmount,noiseAmount);
            p.vertex(x1,y1);

        }
    }

    private void setVertex2(float r){
        for (Integer i =0; i<N+1;i++) {

            float x2 = (float) (location.x + r * Math.cos(TWO_PI * i / N));
            float y2 = (float) (location.y + r * Math.sin(TWO_PI * i / N));;

            x2 += p.noise(location.x * 0.2f, location.x* 0.2f) * 10 + 5;
            y2 += p.noise(location.y * 0.2f, location.y* 0.2f) * 10 + 5;
            p.vertex(x2,y2);
        }
    }

}

