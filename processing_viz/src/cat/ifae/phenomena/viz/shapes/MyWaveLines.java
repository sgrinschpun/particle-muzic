package cat.ifae.phenomena.viz.shapes;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.params.MyFamilyParams;

import processing.core.PApplet;
import static processing.core.PConstants.TWO_PI;


public class MyWaveLines extends MyShape  {
    private int color, N;
    private float r0, weight, xoff, yoff, deltaxoff, deltayoff, magnitude;
    private CurrentCicle currentCicle;
    public  float[][][] myLimits;


    public MyWaveLines(PApplet p, float x, float y, MyFamilyParams myParams){
        super(p,x,y,myParams);
        this.myParams = myParams;
        this.color = myParams.getColor();

        //this.weight = myParams.getWeight();
        this.weight = 8;
        //this.N = myParams.getN();
        this.N= 100;
        this.xoff = (float) 0;
        this.yoff = (float) 1000;
        //this.deltaxoff = myParams.getdeltaxoff();
        //this.deltayoff = myParams.getdeltayoff();
        this.deltaxoff = 0.01f;
        this.deltayoff = 0.01f;
        this.r0 = 2000;
        //this.magnitude = 1;

        this.myLimits = build_shape();
    }

    private float[][][] build_shape(){
        float limits[][][] = new float[N+1][2][2];
        for(int i=0;i<N+1;i++){
            limits[i][0][0] = (float) (y + r0*Math.sin(TWO_PI*i/N));
            limits[i][1][0] = (float) (x - r0*Math.cos(TWO_PI*i/N));
            limits[i][1][1] = (float) (x + r0*Math.cos(TWO_PI*i/N));
        }
        return limits;
    }

    float u(float n) {
        return p.width/100 * n;
    }

    private void setLine(int i, float y1){
        for(float x1 = p.width*0.1f; x < (float) p.width*0.9f; x++){
            float ypos=p.map(p.noise(x1/100 + xoff, y1/100 + yoff), 0, 1, -100, 100);
            float magnitude = x < p.width*0.5 ? p.map(x, p.width*0.1f, p.width*0.5f,0f, 1f) : p.map(x, p.width*0.5f, p.width*0.9f, 1f, 0f) ;
            ypos *= magnitude;
            if(ypos > 0) ypos = 0;
            p.vertex(x1, ypos);
        }
    }

    private void setLines() {
        for(float y = p.height*0.1f; y < p.height*0.9f; y += u(1.5f)) {
            p.strokeWeight(weight);
            color = myParams.getColor();
            p.stroke(color);
            p.pushMatrix();
            p.translate(0, y);
            p.noFill();
            p.beginShape();
            for(float x = p.width*0.1f; x < p.width*0.9f; x++) {
                float ypos = p.map(p.noise(x/100 + xoff, y/100 + yoff), 0, 1, -100, 100);
                float magnitude = x < p.width*0.5 ? p.map(x, p.width*0.1f, p.width*0.5f, 0, 1) : p.map(x, p.width*0.5f, p.width*0.9f, 1, 0) ;
                ypos *= magnitude;
                if(ypos > 0) ypos = 0;
                p.vertex(x, ypos);
            }
            p.endShape();
            p.popMatrix();
        }
    }

    public void display(){
        setLines();
        xoff += 0.01;
        yoff += -0.01;
    }

    public void move(){

    }


}

