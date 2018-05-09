package cat.ifae.phenomeva.avserver.audio;

import beads.*;

class ParticleSynth {
	private int id;
	private WavePlayer wp0 = null;
	private WavePlayer wp1 = null;
	private WavePlayer wp2 = null;
	private WavePlayer wp3 = null;
	private Envelope e = null;
	private Envelope filterCutoffEnvelope;
	private LPRezFilter lowPassFilter;
	private Gain g = null;
	private Gain gOsc0 = null;
	private Gain gOsc1 = null;
	private Gain gOsc2 = null;
	private Gain gOsc3 = null;
	private int pitch = -1;

	// the constructor for our sine wave synthesizer
	public ParticleSynth(AudioContext ac, int id, int midiPitch, Gain synthGain) {
		this.id = id;
		pitch = midiPitch;
		// set up the new WavePlayer, convert the MidiPitch to a
		// frequency

		float freq = midiToFreq(midiPitch);
		System.out.println("-MIDIPITCH: " + midiPitch + "\t-Freq at midi to freq: " + freq);
		wp0 = new WavePlayer(ac, freq, Buffer.SINE);
		wp1 = new WavePlayer(ac, freq, Buffer.SINE);
		wp2 = new WavePlayer(ac, freq, Buffer.TRIANGLE);
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
		filterCutoffEnvelope.addSegment((float) 0.05, 5);
		lowPassFilter.setFrequency(200);
		lowPassFilter.setRes((float) 0.4);
		g.setGain((float) 0.05);
		gOsc1.setGain((float) 0.05);
		gOsc1.setGain((float) 0.05);
		gOsc2.setGain((float) 0.05);
		gOsc3.setGain((float) 0.05);
	}

	// when this note is killed, ramp the amplitude down to 0
	// over 300ms
	public void kill() {
		e.addSegment(0, 500, new KillTrigger(g));
		filterCutoffEnvelope.addSegment(0, 500, new KillTrigger(g));
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
