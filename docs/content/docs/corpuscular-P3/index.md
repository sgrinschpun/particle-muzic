+++
title = "P3: Corpuscular View"
subtitle = "Painting Particles"
description = "P3 classes designed to give particles a localized visualization. Leptons, Bosons, Quarks, Mesons, Baryons,...their properties are mapped visually. Similarities and differences are emphasized."
date = "2018-04-13"
weight = 2
+++

##### Introduction
- **General Ideas:**
  - Input parameters are: Mass, charge, particle type, quark composition
  - Mass cannot be mapped to the size of the particle. It can be mapped to the rugosity - deformity of the particle
  - Charged or not. Positive and negative?
  - Quarks are displayed
  - Particle type determine the visual composition
- **Leptons:**
  - No color charge -> white
  - Shape: Deformed ring
- **Bosons:**
    - No color charge -> white
    - Shape: Deformed ring

- **Bosons:**

{{<mermaid align="left">}}
graph LR;
    MyParticle --> MyLepton
    MyParticle --> MyBoson
    MyParticle --> MyMeson
    MyParticle --> MyBaryon
    MyLepton --> myWaveRing
    MyMeson --> myWaveRing
    MyMeson --> myWaveCircle
    MyBaryon --> myWaveRing
    MyBaryon --> myWaveCircle
    MyBoson --> myWaveCircle
{{< /mermaid >}}



### myShapes
##### myWaveRing:
- Input Parameters:
  - _x: x position
  - _y: y position
  - _currentCicle: object of the currentCicle class that calculates cicle parameters, initialized with speed
  - speed: speed of the beat
  - _r0: radius of the ring
  - _weight: weight of the ring stroke
  - _noiseScale: 0.008 - 0.01 needs to be balanced by ampFactor
  - _ampFactor: more rugosity
  - _myColors = object of the myColors class paramsWaveRing['colors']
  - _noiseSeed = a random number in [0,99] in every cicle to avoid repetition of perlin noise

- Uses:
  - Quark:
    - Stroke color in rgb or cmy (matter or antimatter) changing in every cicle
    - Stroke weight :
    - Original radius:
    - Max Radius:
    -


  - Lepton
