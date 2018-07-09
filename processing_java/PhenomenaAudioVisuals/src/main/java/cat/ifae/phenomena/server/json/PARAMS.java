package cat.ifae.phenomena.server.json;

public class PARAMS {
	private int id;
	public int parent;
	private String name;
	private float mass;
	private float charge;
	private float decay_time;
	private String[] composition;
	private String type;
	private float p;
	private float beta;
	private float theta;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public float getMass() {
		return this.mass;
	}

	public void setMass(float mass) {
		this.mass = mass;
	}
	
	public String getType() {
		return this.type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public float getDecayTime() {
		return decay_time;
	}

	public void setDecayTime(float decayTime) {
		this.decay_time = decayTime;
	}

	public float getCharge() {
		return charge;
	}

	public void setCharge(float charge) {
		this.charge = charge;
	}

	public String getName() {
		return this.name;
	}

	public String[] getComposition() {
		return this.composition;
	}

	public void setComposition(String[] composition) {
		this.composition = composition;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public void setParent(int parent) {
		this.parent = parent;
	}
	
	public int getParent() {
		return parent;
	}

	public void setp(int p) {
		this.p = p;
	}

	public float getp() {
		return p;
	}

	public void setBeta(int beta) {
		this.beta = beta;
	}

	public float getBeta() {
		return beta;
	}

	public void setTheta(int theta) {
		this.theta = theta;
	}

	public float getTheta() {
		return theta;
	}

	@Override
	public String toString() {
		return "PhenomenaCMD [type = " + type + " parent = "+ parent + " mass = " + mass + ", id = " + id + ", decayTime = " + decay_time + ", charge = " + charge
				+ ", name = " + name + ", composition = " + composition + ", p = " + p + ", beta = " + beta + ", theta = " + theta + "]";
	}

	public boolean equals(PARAMS p) {
		return this.getId() == p.getId();
	}
}
