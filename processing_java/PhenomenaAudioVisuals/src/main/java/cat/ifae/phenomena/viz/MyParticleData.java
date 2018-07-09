package cat.ifae.phenomena.viz;

import java.util.HashMap;

public class MyParticleData {
    private String name;
    private String type;
    private String[] composition;
    private double mass;
    private double charge;
    private double time_to_decay;
    private String[] decay;
    private int parent_particle;

    private HashMap<String,Object> myParticleHash = new HashMap<String,Object>();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String[] getComposition() {
        return composition;
    }

    public void setComposition(String[] composition) {
        this.composition = composition;
    }

    public double getMass() {
        return mass;
    }

    public void setMass(double mass) {
        this.mass = mass;
    }

    public double getCharge() {
        return charge;
    }

    public void setCharge(double charge) {
        this.charge = charge;
    }

    public double getTime_to_decay() {
        return time_to_decay;
    }

    public void setTime_to_decay(double time_to_decay) {
        this.time_to_decay = time_to_decay;
    }

    public String[] getDecay() {
        return decay;
    }

    public void setDecay(String[] decay) {
        this.decay = decay;
    }

    public MyParticleData(String name, String type, String[] composition, double mass, double charge, double time_to_decay, String[] decay) {
        this.name = name;
        this.type = type;
        this.composition = composition;
        this.mass = mass;
        this.charge = charge;
        this.time_to_decay = time_to_decay;
        this.decay = decay;


        setMyParticleHash();
    }

    public HashMap<String, Object> getMyParticleHash() {
        return myParticleHash;
    }

    private void setMyParticleHash() {
        myParticleHash.put("name",name);
        myParticleHash.put("type",type);
        myParticleHash.put("composition",composition);
        myParticleHash.put("mass",mass);
        myParticleHash.put("charge",charge);
        myParticleHash.put("time_to_decay",time_to_decay);
        myParticleHash.put("decay",decay); }
}


