package cat.ifae.phenomena.avserver.audio;

import processing.core.PApplet;
import themidibus.MidiBus;

public class MidiOutputGenerator {
	private MidiBus midiBus;
	private PApplet parent;
	
	public MidiOutputGenerator(PApplet p){
		MidiBus.list();
		parent = p;
		midiBus = new MidiBus(parent, "Bus IAC 1", "Bus IAC 1");
	}

	public void sendNoteOn(int channel, int note, int velocity){
		midiBus.sendNoteOn(channel, note, velocity);
	}
	 public void sendNoteOff(int channel, int note){
		 midiBus.sendNoteOff(channel,  note, 0);
	 }
}
