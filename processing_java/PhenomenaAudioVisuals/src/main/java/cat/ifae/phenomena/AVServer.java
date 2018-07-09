package cat.ifae.phenomena;

import cat.ifae.phenomena.server.json.JsonHandler;
import cat.ifae.phenomena.server.ListManager;
import cat.ifae.phenomena.viz.MyViz;
import processing.core.PApplet;
import processing.net.Client;
import processing.net.Server;

public class AVServer extends PApplet {
	int port = 1234;
	Server server;
	JsonHandler handleJson;
	ListManager manageList;
	MyViz myViz;


	public static void main(String[] args) {
		PApplet.main("cat.ifae.phenomena.AVServer");
	}

	public void settings() {
		//size(1920, 1200, P3D);
		fullScreen(P3D);
	}

	public void setup() {
		frameRate(24);
		smooth();

		server = new Server(this, port);
		handleJson = new JsonHandler();

		//define your visualization
		//myViz = new MyViz(this, "quantumuniverse");
		myViz = new MyViz(this, "bubblechamber");

        background(myViz.getBackgroundColor());


		manageList = new ListManager( this, myViz);
	}

	public void draw() {

	    myViz.refresh();

        Client thisClient = server.available();
		if (thisClient != null) {
			try {
				String receivedString = thisClient.readString();
				manageList.updateList(handleJson.parse(receivedString));
			} catch (Exception ex) {
				System.out.println("Failed loading particle!");
				ex.printStackTrace();
			}
		}
		manageList.visualize();
	}

	public void keyPressed() {

	}
}
