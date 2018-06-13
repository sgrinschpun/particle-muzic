package cat.ifae.phenomena.viz.params;

import cat.ifae.phenomena.viz.data.MyParticleData;

import processing.core.PApplet;


public class MyParams {
    PApplet p;
    private int i;
    private String q;
    private MyParticleData particleData;

    public MyQuarkParams quark;
    public MyGluonParams gluon;
    public MyLeptonParams lepton;
    public MyBosonParams boson;

    //baryons and mesons
    public MyParams(PApplet p, MyParticleData particleData, String q, int i){
        this.p = p;
        this.q = q;
        this.i = i;
        this.particleData = particleData;

        buildParticle();
    }

    //gluons, bosons, leptons
    public MyParams(PApplet p, MyParticleData particleData){
        this.p = p;
        this.particleData = particleData;
        buildParticle();
    }

    private void buildParticle(){
        switch(particleData.getType()){
            case "lepton":
                this.lepton = new MyLeptonParams(p,particleData);
                break;
            case "meson":
            case "baryon":
                this.quark = new MyQuarkParams(p, particleData, q, i);
                this.gluon = new MyGluonParams(p, particleData);
                break;
            case "quark":
                this.quark = new MyQuarkParams(p, particleData, q, i);
                break;
            case "boson":
                this.boson = new MyBosonParams(p, particleData);
                break;
        }
    }
}





