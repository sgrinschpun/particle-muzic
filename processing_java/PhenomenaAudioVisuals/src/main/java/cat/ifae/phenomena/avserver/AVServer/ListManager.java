package cat.ifae.phenomena.avserver.AVServer;

import java.util.ArrayList;
import cat.ifae.phenomena.avserver.json.PARAMS;
import cat.ifae.phenomena.avserver.json.PhenomenaCMD;
import cat.ifae.phenomena.avserver.visuals.VisualManager;
import cat.ifae.phenomena.avserver.audio.AudioManager;
import processing.core.PApplet;

public class ListManager {
	private PApplet parent;
	private ParticleList particleList;
	private VisualManager vManager;
	private AudioManager aManager;

	public ListManager(PApplet p) {
		parent = p;
		particleList = new ParticleList();
		vManager = new VisualManager(parent);
		aManager = new AudioManager();
	}

	public void updateList(PhenomenaCMD phenom) {
		vManager.callback(phenom);
		aManager.callback(phenom);
		/*switch (phenom.getCMD()) {
		case "ADD":
			particleList.addNewParticle(phenom.getPARAMS());
			break;
		case "REMOVE":
			particleList.seekAndDestroy(phenom.getPARAMS());
			break;
		}*/
	}

	public void visualize() {
		vManager.moveParticles();
		vManager.displayParticles();
	}

	public ArrayList<PARAMS> getList() {
		return particleList.getList();
	}
}