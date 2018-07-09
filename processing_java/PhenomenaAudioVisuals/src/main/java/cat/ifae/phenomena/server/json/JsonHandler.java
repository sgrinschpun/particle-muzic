package cat.ifae.phenomena.server.json;

import com.google.gson.Gson;

public class JsonHandler {

	public JsonHandler() {
	}

	public PhenomenaCMD parse(String clientString) {
		System.out.println(clientString);
		Gson gson = new Gson();
		return gson.fromJson(clientString, PhenomenaCMD.class);
	}
}