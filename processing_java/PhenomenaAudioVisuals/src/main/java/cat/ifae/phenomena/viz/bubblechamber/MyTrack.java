package cat.ifae.phenomena.viz.bubblechamber;

import cat.ifae.phenomena.viz.MyParticleData;
import processing.core.PVector;

public class MyTrack {

    protected MyParticleData particleData;

    public MyTrack (MyParticleData particleDataData){

        this.particleData = particleData;


    }

    public float getWidth(PVector velocity){
        return 1f;

    }

    public int getColor(){
        return 1;
    }





}
