package cat.ifae.phenomena.avserver.audio;

import java.util.ArrayList;

//import java.util.ArrayList;
//import beads.*;
import cat.ifae.phenomena.avserver.AVServer.PhenoCallback;
import cat.ifae.phenomena.avserver.json.PhenomenaCMD;
import processing.core.PApplet;
import themidibus.MidiBus;

public class AudioManager implements PhenoCallback {
	private PApplet parent;
	private MidiOutputGenerator midiGen;
	private ArrayList<ParticleNote> list;

	/*
	 * private AudioContext ac; 
	 * private Reverb reverb; 
	 * private Gain synthGain;
	 * private Gain reverbGain;
	 */
	// private ArrayList<ParticleSynth> list;

	public AudioManager(PApplet p) {
		parent = p;
		midiGen = new MidiOutputGenerator(parent);
		list = new ArrayList<ParticleNote>();
		// list = new ArrayList<ParticleSynth>();
		/*
		 * ac = new AudioContext(); synthGain = new Gain(ac, 1); reverb = new
		 * Reverb(ac, 1); reverbGain = new Gain(ac, 1); reverb.setSize((float)
		 * 1.0); reverb.setDamping((float) 0.6);
		 * reverb.setEarlyReflectionsLevel((float) 0.2);
		 * reverb.setLateReverbLevel((float) 0.6);
		 * reverbGain.addInput(synthGain); reverb.addInput(reverbGain);
		 * ac.out.addInput(synthGain); ac.out.addInput(reverb); ac.start();
		 */

	}

	@Override
	public void callback(PhenomenaCMD cmd) {
		switch (cmd.getCMD()) {
		case "ADD":
			System.out.println("Adding particle-note to list!"); // (int) (
																	// cmd.getPARAMS().getMass()
																	// * 440 +
																	// 440)
			int type = 0;
			ParticleNote partNote = new ParticleNote(midiGen, cmd.getPARAMS().getId(), type,
					(int) (cmd.getPARAMS().getMass() * 12));
			System.out.println("What's sent to getMass: " + (cmd.getPARAMS().getMass() * 12));
			list.add(partNote);
			break;
		/*
		 * ParticleSynth partSynth = new ParticleSynth(ac,
		 * cmd.getPARAMS().getId(), (int) (cmd.getPARAMS().getMass() * 12),
		 * synthGain); System.out.println("What's sent to getMass: " +
		 * (cmd.getPARAMS().getMass() * 12) ); list.add(partSynth);
		 */

		case "REMOVE":
			for (int i = 0; i < list.size(); i++) {
				if (list.get(i).getId() == cmd.getPARAMS().getId()) {
					list.get(i).killNote();
					list.remove(i);
					System.out.println("Removing particle-note from list!");
					break;
					// list.get(i).kill();
					// list.get(i).destroy();
				}
			}

			break;
		}
	}
}
