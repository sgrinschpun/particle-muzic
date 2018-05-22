package cat.ifae.phenomena.avserver.visuals;

import java.util.ArrayList;

import cat.ifae.phenomena.avserver.AVServer.PhenoCallback;
import cat.ifae.phenomena.avserver.json.PhenomenaCMD;
import processing.core.PApplet;

public class VisualManager implements PhenoCallback {
	private ArrayList<ParticlePic> list;
	private PApplet parent;

	public VisualManager(PApplet p) {
		parent = p;
		list = new ArrayList<ParticlePic>();
	}

	public void moveParticles() {
		for (int i = 0; i < list.size(); i++) {
			list.get(i).move();
		}
	}

	public void displayParticles() {
		for (int i = 0; i < list.size(); i++) {
			list.get(i).display();
		}
	}

	@Override
	public void callback(PhenomenaCMD cmd) {
		switch (cmd.getCMD()) {
		case "ADD":
			System.out.println("Adding particle-pic to list!");
			ParticlePic partPic = new ParticlePic(parent, cmd.getPARAMS().getId(), cmd.getPARAMS().getMass(),
					cmd.getPARAMS().getDecayTime(), cmd.getPARAMS().getCharge());
			list.add(partPic);
			break;
		case "REMOVE":
			for (int i = 0; i < list.size(); i++) {
				if (list.get(i).getId() == cmd.getPARAMS().getId()) {
					list.remove(i);
					System.out.println("Removing particle-pic from list!");
					break;
				}
			}
			break;
		}
	}

}