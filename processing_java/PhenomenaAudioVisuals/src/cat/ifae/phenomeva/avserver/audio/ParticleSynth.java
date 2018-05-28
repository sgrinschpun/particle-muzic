package cat.ifae.phenomeva.avserver.audio;

import beads.*;

class ParticleSynth {
	int id;
	WavePlayer wp0 = null;
	WavePlayer wp1 = null;
	WavePlayer wp2 = null;
	WavePlayer wp3 = null;
	Envelope e = null;
	Envelope filterCutoffEnvelope;
	LPRezFilter lowPassFilter;
	Gain g = null;
	Gain gOsc0 = null;
	Gain gOsc1 = null;
	Gain gOsc2 = null;
	Gain gOsc3 = null;
	int pitch = -1;
	int decay = 500;

	public ParticleSynth(AudioContext ac, int id, int midiPitch, Gain synthGain) {
		this.id = id;
		pitch = midiPitch;
		float freq = midiToFreq(midiPitch);
		System.out.println("-MIDIPITCH: " + midiPitch + "\t-Freq at midi to freq: " + freq);
		wp0 = new WavePlayer(ac, freq / 2, Buffer.SINE);
		wp1 = new WavePlayer(ac, freq, Buffer.SINE);
		wp2 = new WavePlayer(ac, freq / 2, Buffer.TRIANGLE);
		wp3 = new WavePlayer(ac, freq, Buffer.TRIANGLE);
		e = new Envelope(ac);
		lowPassFilter = new LPRezFilter(ac);
		filterCutoffEnvelope = new Envelope(ac);
		gOsc0 = new Gain(ac, 1);
		gOsc1 = new Gain(ac, 1);
		gOsc2 = new Gain(ac, 1);
		gOsc3 = new Gain(ac, 1);
		g = new Gain(ac, 1, e);
		gOsc0.addInput(wp0);
		gOsc1.addInput(wp1);
		gOsc2.addInput(wp2);
		gOsc3.addInput(wp3);
		lowPassFilter.addInput(gOsc0);
		lowPassFilter.addInput(gOsc1);
		lowPassFilter.addInput(gOsc2);
		lowPassFilter.addInput(gOsc3);
		g.addInput(lowPassFilter);
		synthGain.addInput(g);
		e.addSegment((float) 0.4, 5);
		filterCutoffEnvelope.addSegment((float) 0.05, 50);
		lowPassFilter.setFrequency(200);
		lowPassFilter.setRes((float) 0.4);
		g.setGain((float) 0.05);
		gOsc1.setGain((float) 0.05);
		gOsc1.setGain((float) 0.05);
		gOsc2.setGain((float) 0.05);
		gOsc3.setGain((float) 0.05);
	}
	
	public void setDecay(int decay){
		this.decay = decay;
	}
	
	public void setFilter(float cutoff, float resonance){
		lowPassFilter.setFrequency(cutoff);
		lowPassFilter.setRes(resonance);
	}

	public void kill() {
		e.addSegment(0, decay, new KillTrigger(g));
		filterCutoffEnvelope.addSegment(0, decay, new KillTrigger(g));
	}

	// destroy the component beads so that they can be cleaned
	// up by the java virtual machine
	public void destroy() {
		wp0.kill();
		wp1.kill();
		wp2.kill();
		wp3.kill();
		e.kill();
		g.kill();
		gOsc0.kill();
		gOsc1.kill();
		gOsc2.kill();
		gOsc3.kill();
		lowPassFilter.kill();
		wp0 = null;
		wp1 = null;
		wp2 = null;
		wp3 = null;
		e = null;
		g = null;
		gOsc0 = null;
		gOsc1 = null;
		gOsc2 = null;
		gOsc3 = null;
		lowPassFilter = null;
	}

	public int getId() {
		return this.id;
	}

	private float midiToFreq(int midiPitch) {
		return (float) (Math.pow(2.0, ((float) midiPitch - 59.0 + 48) / 12.0) * 440);
	}
}
