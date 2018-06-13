package cat.ifae.phenomena.viz.params;

import cat.ifae.phenomena.viz.data.MyParticleData;
import processing.core.PApplet;

import java.util.HashMap;
import java.util.Map;

public class MyLeptonParams extends MyFamilyParams{
    private static Map<String, Lepton> leptonParams = new HashMap<>();
    private static Map<String, Map> leptonParamsValues = new HashMap<>();
    private static Map<Integer, Integer> wgt = new HashMap<>();
    private static Map<Integer, Integer> amp = new HashMap<>();
    private static Map<Integer, Integer> speed = new HashMap<>();
    private static Map<Integer, Integer> color = new HashMap<>();

    private String lepton;
    private Double charge;


    public MyLeptonParams(PApplet p, MyParticleData particleData){
        super(p,particleData);

        this.lepton = particleData.getName();
        this.charge = particleData.getCharge();

        buildLeptonParams();
        buildLeptonParamsValues();

        this.myColor = setColor();

    }

    private  void buildLeptonParams() {
        leptonParams.put("e-", new Lepton(0, 1));
        leptonParams.put("mu-", new Lepton(0, 2));
        leptonParams.put("tau-", new Lepton(0, 3));
        leptonParams.put("e+", new Lepton(1, 1));
        leptonParams.put("mu+", new Lepton(1, 2));
        leptonParams.put("tau+", new Lepton(1, 3));
        leptonParams.put("nu_e", new Lepton(0, 1));
        leptonParams.put("nu_mu", new Lepton(0, 2));
        leptonParams.put("nu_tau", new Lepton(0, 3));
        leptonParams.put("nubar_e", new Lepton(1, 1));
        leptonParams.put("nubar_mu", new Lepton(1, 2));
        leptonParams.put("nubar_tau", new Lepton(1, 3));

    }

    private void buildLeptonParamsValues(){
        wgt.put(1,3);
        wgt.put(2,2);
        wgt.put(3,1);
        leptonParamsValues.put("wgt", wgt);
        amp.put(1,40);
        amp.put(2,10);
        amp.put(3,10);
        leptonParamsValues.put("amp", amp);
        speed.put(1,100);
        speed.put(2,30);
        speed.put(3,100);
        leptonParamsValues.put("speed", speed);
        color.put(0,colors.w);
        color.put(1,colors.g);
        leptonParamsValues.put("color", color);
    }

    private int getType(String lepton){
        return leptonParams.get(lepton).getType();
    }

    private int getGen(String lepton){
        return leptonParams.get(lepton).getGen();
    }

    @Override
    protected int setColor(){
        int i = getType(lepton);
        return (int) leptonParamsValues.get("color").get(i);
    }

    @Override
    public float getAmpFactor(){
        int i = getGen(lepton);
        return (float) (int) leptonParamsValues.get("amp").get(i);
    }

    @Override
    public double getSize(){
        return  50 + 10*massRenorm(mass);
    }

    @Override
    public int getSpeed(){
        int i = getGen(lepton);
        return (int) leptonParamsValues.get("speed").get(i);
    }

    @Override
    public float getWeight(){
        int i = getGen(lepton);
        return (float) (int) leptonParamsValues.get("wgt").get(i);
    }

    @Override
    public int updateColor(){ return myColor; }

}

class Lepton{
    private Integer type;
    private Integer gen;

    public Lepton(Integer type, Integer gen){
        this.type = type;
        this.gen = gen;
    }

    public Integer getType(){
        return type;
    }

    public Integer getGen(){
        return gen;
    }

    @Override
    public String toString() {
        return "cat.ifae.phenomena.viz.params.Lepton{" +
                "type='" + type + '\'' +
                ", gen='" + gen + '\'' +
                '}';
    }
}