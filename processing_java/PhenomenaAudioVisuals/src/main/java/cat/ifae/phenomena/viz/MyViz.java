package cat.ifae.phenomena.viz;

public class MyViz {

    private String vizName;
    public MyParticleViz particle;


    public MyViz (String vizName ) {
        this.vizName = vizName;

    }


    public void MyParticleViz (){
        switch (vizName) {
            case "quantumuniverse" : return cat.ifae.phenomena.viz.quantumuniverse.MyParticle,
            case "bubblechamber" : this.particle = cat.ifae.phenomena.viz.bubblechamber.MyParticle
        }



    }







}
