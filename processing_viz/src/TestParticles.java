import cat.ifae.phenomena.viz.data.MyParticleData;

public class TestParticles {

    public static MyParticleData electron = new MyParticleData("e-","lepton",new String[0] ,0.0005109989461,-1.0,0,new String[0]);
    public static MyParticleData pion = new MyParticleData("pi+","meson",new String[]{"d", "ubar"},0.13957018,-1.0,6.745569150965853, new String[]{"mu-", "nubar_mu"});
    public static MyParticleData neutron = new MyParticleData("n0","baryon",new String[]{"u","d", "d"},0.939565413, 0.0,1.333699306732677, new String[]{"nubar_e", "e-", "p+"});

}
