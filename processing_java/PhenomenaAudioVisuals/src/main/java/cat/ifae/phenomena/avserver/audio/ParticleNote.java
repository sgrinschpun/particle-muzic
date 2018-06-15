package cat.ifae.phenomena.avserver.audio;

import processing.core.PApplet;

public class ParticleNote {
	int id;
	int channel = 0;
	int pitch = -1;
	int velocity = 80;
	MidiOutputGenerator midiGen;
	int FIRST_SYNTH_CHANNEL = 0;
	int SECOND_SYNTH_CHANNEL = 1;
	int THIRD_SYNTH_CHANNEL = 2;
	int FOURTH_SYNTH_CHANNEL = 3;
	int FIFTH_SYNTH_CHANNEL = 4;
	int SUBBASS_CHANNEL = 5;
	private float nMass;

	public ParticleNote(MidiOutputGenerator mGen, int id, String type, String name, float mass) {
		midiGen = mGen;
		System.out.println("Mass is:" + mass);
		nMass = normaliseMass(mass);
		this.id = id;
		typeToChannel(type);
		this.pitch = Math.round(mass * 24) + 45;
		if (mass == 0.0 || name.equals("nu_e") || name.equals("nu_mu") || name.equals("nu_tau")
				|| name.equals("nubar_e") || name.equals("nubar_mu") || name.equals("nubar_tau")) {
			System.out.println("This will be a SUBBASS note!");
			this.channel = SUBBASS_CHANNEL;
			this.pitch = 33;
		}
		System.out.println("-MIDIPITCH: " + pitch);
		midiGen.sendNoteOn(this.channel, this.pitch, this.velocity);
	}

	private float normaliseMass(float mass) {
		return PApplet.map(PApplet.constrain((float) Math.log10(1.0 + mass), 0f, 11f), 0f, 11f, 0f, 1f);
	}

	public int getChannel() {
		return this.channel;
	}

	public int getNote() {
		return this.pitch;
	}

	public int getVelocity() {
		return this.velocity;
	}

	public int getId() {
		return this.id;
	}

	public void killNote() {
		midiGen.sendNoteOff(this.channel, this.pitch);
	}

	private void typeToChannel(String type) {
		switch (type) {
		case "lepton": // Soft Canada, is okay!
			this.channel = FIRST_SYNTH_CHANNEL;
			break;
		case "meson": // 2 Circles w Signal Scope Inside
			this.channel = SECOND_SYNTH_CHANNEL;
			break;
		case "baryon": // 3 Circles w Signal Scope inside
			this.channel = THIRD_SYNTH_CHANNEL;
			break;
		case "quark": // Organic Coloured Fuzzy Bubble!
			this.channel = FOURTH_SYNTH_CHANNEL;
			break;
		case "boson": // Unknows Coloured Pleasures!
			this.channel = FIFTH_SYNTH_CHANNEL;
			break;
		}
	}

	/*
	 * private float midiToFreq(int midiPitch) { return (float) (Math.pow(2.0,
	 * ((float) midiPitch - 59.0 + 48) / 12.0) * 440); }
	 */
}
