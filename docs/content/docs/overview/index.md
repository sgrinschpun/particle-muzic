+++
title = "Overview"
subtitle = "Structure of Phenomena"
description = "Phenomena is composed of several modules and processes to manage interactivity, simulations, audio & video outputs,... They are described here."
date = "2018-04-13"
weight = 1
+++

##### Introduction
- The **OSC server** allows interactive particle instantiation. It uses sockets to communicate with the Phenomena server.
- **Simulation.py** allows for prebuild simulations to be used in Phenomena. It uses sockets to communicate with the Phenomena server.
- The **Phenomena server** manages particle instantiation & life-cycle and output to audio & video. It is composed of several nodes. It uses sockets to communicate with the audio & video modules.
- The **Audio module** builds visulization with Processing libraries.

{{<mermaid align="left">}}
graph LR;
    A[touchOSC] -->|OSC| B[OSC Sever]
    H[MIDI keyboard] -->|OSC| B[OSC Sever]
    I[OpenCV App] -->|OSC| B[OSC Sever]
    B -->|Sockets| C{Phenomena Server}
    K[baked simulation] --> J[simulation.py]
    J -->|Sockets| C{Phenomena Server}
    C -->|Sockets| D[P3 Audio]
    C -->|Sockets| E[P3 Video]
    D --> F[Sound System]
    D --> L[MIDI Synth]
    L --> F
    E --> G[Screen]
{{< /mermaid >}}

##### Example of how to run
