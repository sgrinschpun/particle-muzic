package cat.ifae.phenomena.viz.params;

import cat.ifae.phenomena.viz.data.MyParticleData;
import processing.core.PApplet;


public class MyBosonParams extends MyFamilyParams{

    public MyBosonParams(PApplet p, MyParticleData particleData){
        super(p,particleData);

        this.myColorSet = setColorSet();
        this.myColor = setColor();
    }
    @Override
    protected  int[] setColorSet(){
        return colors.allColors;
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
        float value = p.map((float) massRenorm(mass),0,1,1,5);
        return value;
    }

    @Override
    public int getN(){return 100;}

    @Override
    public float getdeltayoff(){
        float value = p.map((float) massRenorm(mass),0,1, 0f,0.1f);
        return value;
    }

    @Override
    public float getdeltaxoff() {
        float value = p.map((float) massRenorm(mass), 0, 1, 0.01f, 0f);
        return value;
    }
}
