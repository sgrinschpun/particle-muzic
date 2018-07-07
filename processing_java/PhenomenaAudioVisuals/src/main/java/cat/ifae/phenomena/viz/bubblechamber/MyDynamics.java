package cat.ifae.phenomena.viz.bubblechamber;

import cat.ifae.phenomena.viz.MyParticleData;
import processing.core.PVector;

public class MyDynamics {

    protected MyParticleData particleData;
    protected PVector velocity;
    protected float m, q;
    protected final static  PVector B = MyFields.B;
    protected final static PVector E = MyFields.E;

    public MyDynamics(MyParticleData particleData){

        this.particleData = particleData;
        this.m = (float) particleData.getMass();
        this.q = (float) particleData.getCharge();

    }

    private PVector Bforce (PVector v){

        return B.cross(v).mult(q/m);
    }

    private PVector Eforce (){

        return E.mult(q);
    }

    protected PVector applyForce(PVector force){
        float mass = 1f;
        PVector acceleration = PVector.div(force,mass);
        return acceleration;
    }

    protected PVector Kloss(PVector velocity){
        PVector drag = velocity.copy();
        drag.normalize();
        drag.mult(-0.01f);

        return drag;
    }

    public PVector getAcceleration(PVector velocity) {
        PVector acceleration = new PVector (0, 0);
        acceleration.add(applyForce(Bforce(velocity)));
        acceleration.add(applyForce(Eforce()));
        acceleration.add(applyForce(Kloss(velocity)));

        return acceleration;
    }

}
