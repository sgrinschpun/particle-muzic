package cat.ifae.phenomena.viz.bubblechamber.dynamics;

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
        int mass = 1;
        return B.cross(v).mult(q/mass);
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
        float speed = velocity.mag();
        float dragMagnitude = speed*speed/500;
        PVector drag = velocity.copy();
        drag.normalize();
        drag.mult(-1);
        drag.mult(dragMagnitude);

        return drag;
    }

    public PVector getAcceleration(PVector velocity) {
        PVector acceleration = new PVector (0, 0);
        acceleration.add(applyForce(Bforce(velocity)));
        //acceleration.add(applyForce(Eforce()));
        acceleration.add(applyForce(Kloss(velocity)));

        return acceleration;
    }

}
