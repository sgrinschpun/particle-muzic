package cat.ifae.phenomena.viz.cicle;

import processing.core.PApplet;

public class CurrentCicle {

    PApplet p;

    double frameCountPerCicle, hz;

    public double getFrameCount() {
        return FrameCount;
    }

    public double gethz() {
        return hz;
    }

    public double getProgressRatioMax() {
        return ProgressRatioMax;
    }

    public double getNumber() {
        return number;
    }

    public double getProgressRatio() {
        return ProgressRatio;
    }

    public double getQuadEaseInRatio() {
        return QuadEaseInRatio;
    }

    public double getQuadEaseOutRatio() {
        return QuadEaseOutRatio;
    }

    public double getQuartEaseInRatio() {
        return QuartEaseInRatio;
    }

    public double getQuartEaseOutRatio() {
        return QuartEaseOutRatio;
    }

    public double getSextEaseInRatio() {
        return SextEaseInRatio;
    }

    public double getSextEaseOutRatio() {
        return SextEaseOutRatio;
    }

    double FrameCount, myFrameRate;
    double ProgressRatioMax, number, ProgressRatio, QuadEaseInRatio, QuadEaseOutRatio, QuartEaseInRatio, QuartEaseOutRatio, SextEaseInRatio, SextEaseOutRatio;


    public CurrentCicle(PApplet p, int frameCountPerCicle) {
        this.p = p;
        this.frameCountPerCicle = frameCountPerCicle;
        this.ProgressRatioMax = (double) (frameCountPerCicle-1)/frameCountPerCicle;
        this.myFrameRate = p.frameRate;
        this.hz = myFrameRate/frameCountPerCicle;
    }

    public void update(){
        number = p.frameCount/frameCountPerCicle;
        FrameCount = p.frameCount%frameCountPerCicle;
        ProgressRatio = FrameCount/frameCountPerCicle;
        QuadEaseInRatio = Math.pow(ProgressRatio,2);
        QuadEaseOutRatio = -Math.pow(ProgressRatio-1,2)+1;
        QuartEaseInRatio = Math.pow(ProgressRatio,4);
        QuartEaseOutRatio = -Math.pow(ProgressRatio-1,4)+1;
        SextEaseInRatio = Math.pow(ProgressRatio,6);
        SextEaseOutRatio = -Math.pow(ProgressRatio-1,6)+1;
    }


}
