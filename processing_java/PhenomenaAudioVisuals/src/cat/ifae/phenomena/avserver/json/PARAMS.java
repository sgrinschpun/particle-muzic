package cat.ifae.phenomena.avserver.json;

public class PARAMS {
	private int id;
	private String name;
	private float mass;
	private float charge;
	private float decayTime;
	private String[] composition;

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

	public float getDecayTime() {
		return decayTime;
	}

	public void setDecayTime(float decayTime) {
		this.decayTime = decayTime;
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

	@Override
	public String toString() {
		return "PhenomenaCMD [mass = " + mass + ", id = " + id + ", decayTime = " + decayTime + ", charge = " + charge
				+ ", name = " + name + ", composition = " + composition + "]";
	}

	public boolean equals(PARAMS p) {
		return this.getId() == p.getId();
	}
}
