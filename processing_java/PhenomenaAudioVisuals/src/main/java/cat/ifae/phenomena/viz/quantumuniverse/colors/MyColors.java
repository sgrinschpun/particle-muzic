package cat.ifae.phenomena.viz.quantumuniverse.colors;

import processing.core.PApplet;

public class MyColors {

    PApplet p;

    public int r, g ,b, c, m, y, w, bl;
    public int[] matterColors;
    public int[] antiMatterColors;
    public int[] allColors;

    public int[] getMatterColors() {
        return matterColors;
    }

    public void setMatterColors() {
        this.matterColors = new int[] {r,g,b};
    }

    public int[] getAntiMatterColors() {
        return antiMatterColors;
    }

    public void setAntiMatterColors() {
        this.antiMatterColors = new int[] {c,m,y};
    }

    public int[] getAllColors() {
        return allColors;
    }

    public void setAllColors() {
        this.allColors = new int[] {r,g,b,c,m,y};
    }

    public MyColors(PApplet p) {
        this.p = p;

        this.r = p.color(255,0,0);
        this.g = p.color(0,255,0);
        this.b = p.color(0,0,255);
        setMatterColors();

        this.c = getComplement(r);
        this.m = getComplement(g);
        this.y = getComplement(b);
        setAntiMatterColors();

        setAllColors();

        this.w = r+g+b;
        this.bl = p.color(0);
        this.g = p.color(100);
    }

    private int getComplement (int original){
        float R = p.red(original);
        float G = p.green(original);
        float B = p.blue(original);
        float minRGB = p.min(R,p.min(G,B));
        float maxRGB = p.max(R,p.max(G,B));
        float minPlusMax = minRGB + maxRGB;
        int complement = p.color(minPlusMax-R, minPlusMax-G, minPlusMax-B);
        return complement;
    }

    private static int next(int item){
        if (item == 0){return 1;}
        else {if (item == 1){return 2;} else {return 0;}}
    }
}