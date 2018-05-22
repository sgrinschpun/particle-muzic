package cat.ifae.phenomena.avserver.visuals;

import processing.core.PApplet;

public class ParticlePic {
	PApplet parent;
	private int id;
	private int size;
	private float posX;
	private float posY;
	private int color;
	private int speedX;
	private int speedY;
	float noiseOff;

	public ParticlePic(PApplet parent, int id, float size, float speed, float color) {
		this.parent = parent;
		this.id = id;
		this.size = (int) (size * parent.width / 10.0);
		this.posX = parent.random(0, parent.width);
		this.posY = parent.random(0, parent.height);
		this.color = (int) (color * 360.0);
		this.speedX = (int) (1 - speed * 10);// (int) parent.random(-1,1);
		this.speedY = (int) (1 - speed * 10);// (int) parent.random(-1,1);
		this.noiseOff = 0;
	}

	public int getId() {
		return this.id;
	}

	public void move() {
		this.posX += this.speedX;
		this.posY += this.speedY;
		if (this.posX + this.size / 2 > parent.width || this.posX - this.size / 2 < 0)
			this.speedX *= -1;
		if (this.posY + this.size / 2 > parent.height || this.posY - this.size / 2 < 0)
			this.speedY *= -1;
	}

	public void display() {
		parent.fill(color, 100, 100);
		float noisedSize = (float) (this.size + 50.0 * parent.noise(noiseOff));
		parent.ellipse(this.posX, this.posY, noisedSize, noisedSize);
		noiseOff += 0.05;
	}
}
