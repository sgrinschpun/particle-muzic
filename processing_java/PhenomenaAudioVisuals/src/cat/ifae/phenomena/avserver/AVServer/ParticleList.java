package cat.ifae.phenomena.avserver.AVServer;

import java.util.ArrayList;

import cat.ifae.phenomena.avserver.json.PARAMS;

public class ParticleList {
	private ArrayList<PARAMS> list;

	public ParticleList() {
		list = new ArrayList<PARAMS>();
	}

	public void addNewParticle(PARAMS newParticle) {
		list.add(newParticle);
		System.out.println("Adding particle to list!");
	}

	public boolean seekAndDestroy(PARAMS particle) {
		int index = find(particle);
		if (index == -1) {
			System.out.println("Not found, not erasing!");
			return false;
		}

		else {
			list.remove(index);
			System.out.println("Found, erasing!");
			return true;
		}
	}

	public ArrayList<PARAMS> getList() {
		return list;
	}

	private int find(PARAMS particle) {
		for (int i = 0; i < list.size(); i++) {
			if (list.get(i).getId() == particle.getId()) {
				return i;
			}
		}
		return -1;
	}
}