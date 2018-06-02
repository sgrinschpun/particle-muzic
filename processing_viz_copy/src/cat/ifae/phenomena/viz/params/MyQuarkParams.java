package cat.ifae.phenomena.viz.params;

import cat.ifae.phenomena.viz.data.MyParticleData;
import processing.core.PApplet;


import java.util.HashMap;
import java.util.Map;

public class MyQuarkParams extends MyFamilyParams{

    private int initial;
    private String quark;

    private static Map<String, Quark> quarkParams = new HashMap<>();
    private static Map<String, Map> quarkParamsValues = new HashMap<>();
    private static Map<Integer, Integer> wgt = new HashMap<>();
    private static Map<Integer, Integer> amp = new HashMap<>();
    private static Map<Integer, Integer> speed = new HashMap<>();
    private static Map<Integer, int[]> colorSet = new HashMap<>();

    public MyQuarkParams(PApplet p, MyParticleData particleData, String q, int i){
        super(p, particleData);

        this.initial = i;
        this.quark = q;
        buildQuarkParams();

        buildQuarkParamsValues();
        this.myColorSet = setColorSet(quark);
        this.myColor = setColor(quark, initial);
    }


    private static void buildQuarkParams(){
        quarkParams.put("u", new Quark(0, 1, 2, 0.022));
        quarkParams.put("d", new Quark(0, 1, -1, 0.0047));
        quarkParams.put("c", new Quark(0, 2, 2, 1.27));
        quarkParams.put("s", new Quark(0, 2, -1, 0.096));
        quarkParams.put("t", new Quark(0, 3, 2, 173.21));
        quarkParams.put("b", new Quark(0, 3, -1, 4.18));
        quarkParams.put("ubar", new Quark(1, 1, -2, 0.022));
        quarkParams.put("dbar", new Quark(1, 1, 1, 0.0047));
        quarkParams.put("cbar", new Quark(1, 2, -2, 1.27));
        quarkParams.put("sbar", new Quark(1, 2, 1, 0.096));
        quarkParams.put("tbar", new Quark(1, 3, -2, 173.21));
        quarkParams.put("bbar", new Quark(1, 3, 1, 4.18));
    }

    private void buildQuarkParamsValues(){
        wgt.put(2,6);
        wgt.put(1,4);
        wgt.put(-1,4);
        wgt.put(-2,6);
        quarkParamsValues.put("wgt", wgt);
        amp.put(1,40);
        amp.put(2,60);
        amp.put(3,80);
        quarkParamsValues.put("amp", amp);
        speed.put(1,50);
        speed.put(2,30);
        speed.put(3,100);
        quarkParamsValues.put("speed", speed);
        colorSet.put(0,colors.getMatterColors());
        colorSet.put(1,colors.getAntiMatterColors());
        quarkParamsValues.put("colorSet", colorSet);
    }

    public static int getType(String quark){
        return quarkParams.get(quark).getType();
    }

    public static int getGen(String quark){
        return quarkParams.get(quark).getGen();
    }

    public static int getQ3(String quark){
        return quarkParams.get(quark).getQ3();
    }

    public static double getMass(String quark){
        return quarkParams.get(quark).getMass();
    }

    protected int setColor(String q, int i){
        int j = getType(q);
        int[] set = (int[]) quarkParamsValues.get("colorSet").get(j);
        return set[i];
    }

    private static int[] setColorSet(String q){
        int i = getType(q);
        return (int[]) quarkParamsValues.get("colorSet").get(i);
    }

    @Override
    public float getAmpFactor(){
        int i = getGen(quark);
        return (float) (int) quarkParamsValues.get("amp").get(i);
    }

    @Override
    public double getSize(){
        //return massRenorm(mass);
        return 70;
    }

    @Override
    public int getSpeed(){
        int i = getGen(quark);
        return (int) quarkParamsValues.get("speed").get(i);
    }

    @Override
    public int updateColor(){
        int index = getIndex(myColorSet, myColor);
        int next = getNext(myColorSet, index);
        myColor = myColorSet[next];
        return myColor;
    }

    @Override
    public float getWeight(){
        int i = getQ3(quark);
        return (float) (int) quarkParamsValues.get("wgt").get(i);
    }
}

class Quark{
    private int type;
    private int gen;
    private int q3;
    private double mass;

    public Quark(int type, int gen, int q3, double mass){
        this.type = type;
        this.gen = gen;
        this.q3 = q3;
        this.mass = mass;
    }

    public int getType(){
        return type;
    }

    public int getGen(){
        return gen;
    }

    public int getQ3(){
        return q3;
    }

    public double getMass(){
        return mass;
    }

    @Override
    public String toString() {
        return "cat.ifae.phenomena.viz.params.Quark{" +
                "type='" + type + '\'' +
                ", gen='" + gen + '\'' +
                ", q3='" + Float.toString(gen) + '\'' +
                ", mass='" + Double.toString(mass) + '\'' +
                '}';
    }
}
