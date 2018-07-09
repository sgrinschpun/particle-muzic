package cat.ifae.phenomena.server;

import cat.ifae.phenomena.server.json.PhenomenaCMD;
import cat.ifae.phenomena.viz.MyViz;
import processing.core.PApplet;

public class ListManager {
	private PApplet p;
	private VisualManager vManager;
	private AudioManager aManager;

	public ListManager(PApplet p, MyViz myViz) {
		this.p = p;
		this.vManager = new VisualManager(this.p, myViz);
		this.aManager = new AudioManager(this.p);
	}

	public void updateList(PhenomenaCMD phenom) {
		vManager.callback(phenom);
		aManager.callback(phenom);

	}

	public void visualize() {
		vManager.displayParticles();
	}

}