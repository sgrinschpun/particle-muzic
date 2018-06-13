package cat.ifae.phenomena.avserver.audio;

import processing.core.PApplet;

public class ParticleNote {
	PApplet parent;
	int id;
	int channel = 0;
	int pitch = -1;
	int velocity = 80;
	MidiOutputGenerator midiGen;

	public ParticleNote(MidiOutputGenerator mGen, int id, String type, int midiPitch) {
		midiGen = mGen;
		this.id = id;
		typeToChannel(type);
		pitch = midiPitch + 52;
		System.out.println("-MIDIPITCH: " + pitch);
		midiGen.sendNoteOn(this.channel, this.pitch, this.velocity);
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
	
	public void killNote(){
		midiGen.sendNoteOff(this.channel, this.pitch);
	}
	
    private void typeToChannel(String type){
        switch(type){
            case "lepton":
                this.channel = 0;
                break;
            case "meson":
            	this.channel = 1;
                break;
            case "baryon":
            	this.channel = 2;
                break;
            case "quark":
            	this.channel = 0;
                break;
            case "boson":
            	this.channel = 1;
                break;
        }
    }

	/*
	 * private float midiToFreq(int midiPitch) { return (float) (Math.pow(2.0,
	 * ((float) midiPitch - 59.0 + 48) / 12.0) * 440); }
	 */
}
