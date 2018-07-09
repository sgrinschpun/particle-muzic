package cat.ifae.phenomena.viz.quantumuniverse.params;

import cat.ifae.phenomena.viz.MyParticleData;
import processing.core.PApplet;

public class MyGluonParams extends MyFamilyParams{

    public MyGluonParams(PApplet p, MyParticleData particleData){
        super(p, particleData);

        this.myColorSet = setColorSet();
        this.myColor = setColor();
    }

    @Override
    protected  int[] setColorSet(){
        return colors.getAllColors();
    }

    @Override
    protected int setColor(){
        return getRandom(myColorSet);
    }

    @Override
    public int getColor(){
        return setColor();
    }

    @Override
    public float getWeight(){
        float value = p.map((float) massRenorm(mass),0,1,1,25);
        return value;
    }

    @Override
    public int getN(){return 4;}

    @Override
    public float getdeltayoff(){
        float value = p.map((float) massRenorm(mass),0,1, (float) 0,(float)0.1);
        return value;
    }

    @Override
    public float getdeltaxoff() {
        float value = p.map((float) massRenorm(mass), 0, 1, 1, 0);
        return value;
    }
}
