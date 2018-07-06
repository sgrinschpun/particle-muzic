package cat.ifae.phenomena.audio;

class Scales {
	 int[][] toneStep = {
	    {0, 2, 4, 5, 7, 9, 11, 12}, //0-Ionian
	    {0, 2, 3, 5, 7, 9, 10, 12}, //1-Dorian
	    {0, 1, 3, 5, 7, 8, 10, 12}, //2-Phrygian
	    {0, 2, 4, 6, 7, 9, 11, 12}, //3-Phrygian
	    {0, 2, 4, 5, 7, 9, 10, 12}, //4-Mixolydian
	    {0, 2, 3, 5, 7, 8, 10, 12}, //5-Aeolian
	    {0, 1, 3, 5, 6, 8, 10, 12}, //6-Locrian
	    {0, 2, 3, 5, 7, 8, 11, 12}, //7-Harmonic Minor
	    {0, 1, 4, 5, 7, 8, 10, 12}, //8-Spanish Gipsy
	    {0, 2, 3, 5, 7, 9, 11, 12}, //9-Hawaian
	    {0, 3, 5, 6, 7, 10, 12,15}, //10-Blues
	    {0, 1, 5, 7, 8, 12, 13,17} //11-Japanese   
	  };
	  int _tonality;
	  int _step;
	  int _numberScales;

	  public Scales() {
	    _tonality = 0;
	    _step = 0;
	    _numberScales = 12;
	  }
	  
	  public void setTonality(int tonality) {
	    _tonality = tonality;
	  }
	  
	  public int getTonality() {
	    return _tonality;
	  }
	  public int getScaleStep(int stepScale) {
	    return toneStep[_tonality][stepScale];
	  }
}