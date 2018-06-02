import cat.ifae.phenomena.viz.data.MyParticleData;

public class TestParticles {

    public static MyParticleData eminus = new MyParticleData("e-","lepton",new String[0] ,0.0005109989461,-1.0,0,new String[0]);
    public static MyParticleData muplus = new MyParticleData("mu+","lepton",new String[0],0.1056583745, 1.0,7.6809856755910735, new String[]{"nu_e", "e+", "nubar_mu"});
    public static MyParticleData eplus = new MyParticleData("e+","lepton",new String[0] ,0.0005109989461,1.0,0,new String[0]);
    public static MyParticleData muminus = new MyParticleData("mu-","lepton",new String[0],0.1056583745, -1.0,7.6809856755910735, new String[]{"nubar_e", "e-", "nu_mu"});

    public static MyParticleData pion = new MyParticleData("pi+","meson",new String[]{"d", "ubar"},0.13957018,-1.0,6.745569150965853, new String[]{"mu-", "nubar_mu"});
    public static MyParticleData neutron = new MyParticleData("n0","baryon",new String[]{"u","d", "d"},0.939565413, 0.0,1.333699306732677, new String[]{"nubar_e", "e-", "p+"});
    public static MyParticleData Z0 = new MyParticleData("Z0","boson",new String[0],91.1876, 0.0,0.01893509882150804, new String[]{"e-", "e+"});
    public static MyParticleData N1700 = new MyParticleData("N1700","baryon",new String[]{"u","d", "d"},1.7, 0.0,0.01893509882150804, new String[]{"mu-", "nubar_mu"});

}
