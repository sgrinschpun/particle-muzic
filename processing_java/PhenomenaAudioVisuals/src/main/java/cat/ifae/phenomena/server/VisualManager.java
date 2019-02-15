package cat.ifae.phenomena.server;

import cat.ifae.phenomena.server.json.PARAMS;
import cat.ifae.phenomena.server.json.PhenomenaCMD;
import cat.ifae.phenomena.viz.MyParticle;
import cat.ifae.phenomena.viz.MyParticleData;
import cat.ifae.phenomena.viz.MyViz;
import processing.core.PApplet;
import processing.core.PVector;

import java.util.HashMap;
import java.util.Map;

public class VisualManager implements PhenoCallback {
	private Map<Integer, MyParticle> list = new HashMap<Integer, MyParticle>();
	private PApplet p;

	private MyViz myViz;

	public VisualManager(PApplet p, MyViz myViz) {

		this.p = p;
		this.myViz = myViz;
	}

	public void displayParticles() {
		for (MyParticle particle : this.list.values()) {
			particle.display();
		}
	}

	@Override
	public void callback(PhenomenaCMD cmd) {
		switch (cmd.getCMD()) {
		case "ADD":
			MyParticle particle;
			PARAMS params = cmd.getPARAMS();
			String message = String.format("Adding particle-pic to list!: ID: %d - Parent: %d type: %s", 
				params.getId(),
				params.getParent(),
				params.getType()
				);
			System.out.println(message);
			String sent[] = {};
			MyParticleData particle_data = new MyParticleData(params.getName(),
														params.getType(),
														params.getComposition(),
														(double) params.getMass(), 
														(double) params.getCharge(),
														(double) params.getDecayTime(),
														sent);
			if (params.getParent() == -1) {
				particle = myViz.particle(params.getPy(), params.getPz(),params.getBeta(), particle_data);
			}
			else {
				MyParticle parentParticle = list.get(params.getParent());
				PVector location = parentParticle.getLocation();
                particle = myViz.particle(location, params.getPy(), params.getPz(), params.getBeta(), particle_data);

            }
			this.list.put(cmd.getPARAMS().getId(), particle);
			break;
		case "REMOVE":
			for (int i = 0; i < list.size(); i++) {
				if(list.containsKey(cmd.getPARAMS().getId())) {
					list.remove(cmd.getPARAMS().getId());
					System.out.println("Removing particle-pic from list!");
					break;
				}
			}
			break;
		}
	}
}
