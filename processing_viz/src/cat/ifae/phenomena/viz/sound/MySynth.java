package cat.ifae.phenomena.viz.sound;

import cat.ifae.phenomena.viz.cicle.CurrentCicle;

import java.util.ArrayList;
import beads.*;

public class MySynth {

    public AudioContext ac;
    public CurrentCicle currentCicle;
    public double hz;
    private WavePlayer square, saw, lfo, square2;
    private BiquadFilter hpf;
    private LPRezFilter lpf;
    private Envelope envelope;
    private Gain vca;
    private ArrayList<WavePlayer> waves;
    private Envelope gainEnvelope;

    private Gain g;
    private Glide gainGlide;

    public MySynth(AudioContext ac, CurrentCicle currentCicle, float freq){
        this.ac = ac;
        this.currentCicle = currentCicle;
        this.hz = currentCicle.gethz();


        envelope = new Envelope(ac, 0.0f);
        envelope.addSegment(0.5f, 0.5f);

        lfo = new WavePlayer(ac, (float) hz, Buffer.SINE);

        Function frequencyModulation = new Function(lfo){
            @Override
            public float calculate()
            {
                // x[0] = modulator
                // 20.0f = modulation width
                // 440.0f = modulation center (carrier frequency)
                return (x[0] * 20.0f) + 440.0f;
            }
        };

        this.square = new WavePlayer(ac, frequencyModulation, Buffer.SQUARE);
        this.square2 = new WavePlayer(ac, 220.0f, Buffer.SQUARE);
        this.saw = new WavePlayer(ac, frequencyModulation, Buffer.SAW);

        // set up a custom function to convert the envelope to frequency range
        Function filterEnvelope = new Function(envelope)
        {
            @Override
            public float calculate()
            {
                // x[0] = envelope
                // 5000.0f = maximum frequency
                // 20.0f = minimum frequency
                return (x[0] * 5000.0f) + 20.0f;
            }
        };

        hpf = new BiquadFilter(ac, BiquadFilter.BESSEL_HP, 100.0f, 1.0f);
        lpf = new LPRezFilter(ac, filterEnvelope, 0.95f);
        hpf.addInput(square);
        hpf.addInput(square2);
        hpf.addInput(saw);
        lpf.addInput(hpf);
        vca = new Gain(ac, 1, envelope);
        vca.addInput(lpf);
        ac.out.addInput(vca);

    }

    public void addWaves(WavePlayer wp1, WavePlayer wp2){
        waves.add(wp1);
        waves.add(wp2);
    }

    public void buildEnvelope(){
        gainEnvelope.addSegment(0.9f, 5000.0f);
        gainEnvelope.addSegment(0.0f, 5000.0f);
    }

    public void connect(ArrayList<WavePlayer> waves, Gain g){
        for (WavePlayer wave: waves){
            g.addInput(wave);
        }
        ac.out.addInput(g);
    }

}
