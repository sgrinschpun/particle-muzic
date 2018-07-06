package cat.ifae.phenomena.server;

import cat.ifae.phenomena.audio.MidiOutputGenerator;
import cat.ifae.phenomena.audio.ParticleNote;
import cat.ifae.phenomena.server.json.PhenomenaCMD;
import processing.core.PApplet;

import java.util.ArrayList;

//import java.util.ArrayList;
//import beads.*;

public class AudioManager implements PhenoCallback {
	private PApplet parent;
	private MidiOutputGenerator midiGen;
	private ArrayList<ParticleNote> particleNotesList;

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
		particleNotesList = new ArrayList<ParticleNote>();
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
			System.out.println("Adding " +cmd.getPARAMS().getName() +" to list!"); // (int) (
																	// cmd.getPARAMS().getMass()
																	// * 440 +
																	// 440)
			int type = 0;
			ParticleNote particleNote = new ParticleNote(midiGen, cmd.getPARAMS().getId(), cmd.getPARAMS().getType(),
					cmd.getPARAMS().getName(), cmd.getPARAMS().getMass());
			particleNotesList.add(particleNote);
			break;
			
		/*
		 * ParticleSynth partSynth = new ParticleSynth(ac, cmd.getPARAMS().getId(), 
		 * 			(int) (cmd.getPARAMS().getMass() * 12), synthGain); 
		 * System.out.println("What's sent to getMass: " + (cmd.getPARAMS().getMass() * 12) ); 
		 * list.add(partSynth);
		 */

		case "REMOVE":
			for (int i = 0; i < particleNotesList.size(); i++) {
				if (particleNotesList.get(i).getId() == cmd.getPARAMS().getId()) {
					particleNotesList.get(i).killNote();
					particleNotesList.remove(i);
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
