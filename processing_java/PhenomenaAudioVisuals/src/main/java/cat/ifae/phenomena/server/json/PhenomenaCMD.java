package cat.ifae.phenomena.server.json;

public class PhenomenaCMD {
	private String CMD;

	private PARAMS PARAMS;

	public String getCMD() {
		return CMD;
	}

	public void setCMD(String CMD) {
		this.CMD = CMD;
	}

	public PARAMS getPARAMS() {
		return PARAMS;
	}

	public void setPARAMS(PARAMS PARAMS) {
		this.PARAMS = PARAMS;
	}

	@Override
	public String toString() {
		return "PhenomenaCMD [CMD = " + CMD + ", PARAMS = " + PARAMS + "]";
	}
}