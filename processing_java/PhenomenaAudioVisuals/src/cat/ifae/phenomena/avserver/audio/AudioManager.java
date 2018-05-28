package cat.ifae.phenomena.avserver.audio;

import java.util.ArrayList;
import beads.*;
import cat.ifae.phenomena.avserver.AVServer.PhenoCallback;
import cat.ifae.phenomena.avserver.json.PhenomenaCMD;

public class AudioManager implements PhenoCallback {
	private AudioContext ac;
	private Reverb reverb;
	private Gain synthGain;
	private Gain reverbGain;
	private ArrayList<ParticleSynth> list;

	public AudioManager() {
		list = new ArrayList<ParticleSynth>();
		ac = new AudioContext();
		synthGain = new Gain(ac, 1);
		reverb = new Reverb(ac, 1);
		reverbGain = new Gain(ac, 1);
		reverb.setSize((float) 1.0);
		reverb.setDamping((float) 0.6);
		reverb.setEarlyReflectionsLevel((float) 0.2);
		reverb.setLateReverbLevel((float) 0.6);
		reverbGain.addInput(synthGain);
		reverb.addInput(reverbGain);
		ac.out.addInput(synthGain);
		ac.out.addInput(reverb);
		ac.start();
	}

	@Override
	public void callback(PhenomenaCMD cmd) {
		switch (cmd.getCMD()) {
		case "ADD":
			System.out.println("Adding particle-pic to list!"); // (int) (
																// cmd.getPARAMS().getMass()
																// * 440 + 440)
			ParticleSynth partSynth = new ParticleSynth(ac, cmd.getPARAMS().getId(),
					(int) (cmd.getPARAMS().getMass() * 12), synthGain);
			System.out.println("What's sent to getMass: " + (cmd.getPARAMS().getMass() * 12) );
			list.add(partSynth);
			break;
		case "REMOVE":
			for (int i = 0; i < list.size(); i++) {
				if (list.get(i).getId() == cmd.getPARAMS().getId()) {
					list.get(i).kill();
					list.get(i).destroy();
					list.remove(i);
					System.out.println("Removing particle-synth from list!");
					break;
				}
			}
			break;
		}
	}
}
