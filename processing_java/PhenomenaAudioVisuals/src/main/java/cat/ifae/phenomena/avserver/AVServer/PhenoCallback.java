package cat.ifae.phenomena.avserver.AVServer;

import cat.ifae.phenomena.avserver.json.PhenomenaCMD;

public interface PhenoCallback {
	void callback(PhenomenaCMD cmd);
}