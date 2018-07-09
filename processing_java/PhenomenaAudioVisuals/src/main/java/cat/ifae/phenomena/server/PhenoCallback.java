package cat.ifae.phenomena.server;

import cat.ifae.phenomena.server.json.PhenomenaCMD;

public interface PhenoCallback {
	void callback(PhenomenaCMD cmd);
}