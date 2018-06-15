package cat.ifae.phenomena.viz.params;

import cat.ifae.phenomena.viz.colors.MyColors;
import cat.ifae.phenomena.viz.data.MyParticleData;
import processing.core.PApplet;
import java.util.Random;

public class MyFamilyParams {

    public PApplet p;

    public MyParticleData particleData;
    public MyColors colors;

    protected int myColor;
    protected int[] myColorSet;
    public Double mass, charge;

    public MyFamilyParams(PApplet p, MyParticleData particleData){
        this.p = p;
        this.colors = new MyColors(p);
        this.particleData = particleData;
        this.mass = particleData.getMass();
        this.charge = particleData.getCharge();

    }

    protected int setColor(){return 40;}
    protected int[] setColorSet(){return new int[] {};}

    protected int getIndex(int[] colorSet, int color){
        int index = -1;
        for (int i = 0; (i < colorSet.length) && (index == -1); i++) {
            if (colorSet[i] == color) {
                index = i;
            }
        }
        return index;
    }

    protected int getNext(int[] colorSet, int i){
        int next = i + 1;
        if (next > (colorSet.length-1)){ next = 0;}
        return next;
    }

    public double getCharge(){
        return charge;
    }

    public float getAmpFactor(){return 40;}
    public int getColor(){
        return myColor;
    }
    public double getNoiseScale(){return 0.01;}
    public double getSize(){return 40;}
    public int getSpeed(){return 40;}
    public int updateColor(){return 40;}
    public float getWeight(){return 40;}
    public int getN() {return 4;};
    public float getdeltayoff(){ return (float) 0.01;}
    public float getdeltaxoff(){ return (float) 0.01;}


    protected float massRenorm(double mass){
        double step = 0.22;
        int factor = 10;
        float value = 0;
        double logmass =  Math.log10(1+mass);
        //double[] bins = [0.0, 0.22, 0.44, 0.66, 0.88, 1.1 , 1.32, 1.54, 1.76, 1.98, 2.2 ];
        for (Integer i = 0; i < 10; i++ ) {
            if (i*step<=logmass && logmass<step*(i+1)) {
                value = (float) (i+1)/10;
            }
        }
        return value;
    }

    public static int getRandom(int[] array) {
        int rnd = new Random().nextInt(array.length);
        return array[rnd];
    }


}
