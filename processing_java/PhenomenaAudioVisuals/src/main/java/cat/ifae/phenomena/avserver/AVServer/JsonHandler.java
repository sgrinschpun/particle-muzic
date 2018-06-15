package cat.ifae.phenomena.avserver.AVServer;

import processing.data.JSONObject;
import com.google.gson.Gson;
import processing.core.PApplet;
import cat.ifae.phenomena.avserver.json.*;

public class JsonHandler {
	JSONObject json;

	public JsonHandler() {
	}

	public String[] parsetoString(String clientString) {
		PhenomenaCMD phenoCMD = parse(clientString);
		return new String[] { "-CMD: " + phenoCMD.getCMD(), "-ID: " + phenoCMD.getPARAMS().getId(),
				"-parent: " + phenoCMD.getPARAMS().getParent(), "-name: " + phenoCMD.getPARAMS().getName(), 
				"-type: " + phenoCMD.getPARAMS().getType(),  "-mass: " + phenoCMD.getPARAMS().getMass(),
				"-charge: " + phenoCMD.getPARAMS().getCharge(), "-decayTime: " + phenoCMD.getPARAMS().getDecayTime(),
				"-composition: " + phenoCMD.getPARAMS().getComposition().toString() };
	}

	public PhenomenaCMD parse(String clientString) {
		System.out.println(clientString);
		Gson gson = new Gson();
		return gson.fromJson(clientString, PhenomenaCMD.class);
	}
}