package cat.ifae.phenomena.viz.shapes;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.params.MyFamilyParams;

import processing.core.PApplet;
import processing.core.PVector;

import static processing.core.PConstants.TWO_PI;


public class MyWaveDisc extends MyShape  {
    private int color, N;
    private float r0, weight, xoff, yoff, deltaxoff, deltayoff, magnitude;
    private CurrentCicle currentCicle;
    public  float[][][] myLimits;


    public MyWaveDisc(PApplet p, MyFamilyParams myParams){
        super(p ,myParams);
        this.myParams = myParams;
        this.color = myParams.getColor();
        this.weight = myParams.getWeight();
        this.N = myParams.getN();
        this.xoff = (float) 0;
        this.yoff = (float) 1;
        this.deltaxoff = myParams.getdeltaxoff();
        this.deltayoff = myParams.getdeltayoff();
        this.r0 = 70;
        this.magnitude = 1;
    }

    private float[][][] build_shape(){
        float limits[][][] = new float[N+1][2][2];
        for(int i=0;i<N+1;i++){
            limits[i][0][0] = (float) (location.y + r0*Math.sin(TWO_PI*i/N));
            limits[i][1][0] = (float) (location.x - r0*Math.cos(TWO_PI*i/N));
            limits[i][1][1] = (float) (location.x + r0*Math.cos(TWO_PI*i/N));
        }
        return limits;
    }

    private void setLine(int i, float y1){

        for (float x1=myLimits[i][1][0]; x1<myLimits[i][1][1]; x1++){
            float ypos=p.map(p.noise(x1/100 + xoff, y1/100 + yoff), 0, 1, -100, 100);
            p.vertex(x1, ypos);
        }
    }

    private void setLines() {
        myLimits = build_shape();
        for (Integer i=0; i<N+1; i++) {
            float y1= myLimits[i][0][0];
            p.strokeWeight(weight);
            color = myParams.getColor();
            p.stroke(color);
            p.pushMatrix();
            p.translate(0, y1);
            p.noFill();
            p.beginShape();
            setLine(i,y1);
            p.endShape();
            p.popMatrix();
        }
    }

    public void display(){
        checkEdges();
        draw();
    }


    private void draw(){
        setLines();
        xoff += deltaxoff;
        yoff += deltayoff;
    }




}

