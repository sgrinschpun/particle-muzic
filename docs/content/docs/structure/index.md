+++
title = "Structure"
description = ""
date = "2018-04-13"
+++

{{<mermaid align="left">}}
graph LR;
    A[touchOSC] -->|OSC| B[OSC Sever]
    H[MIDI keyboard] -->|OSC| B[OSC Sever]
    I[OpenCV App] -->|OSC| B[OSC Sever]
    B -->|Sockets| C{Phenomena Server}
    K[baked simulation] --> J[simulation.py]
    J -->|Sockets| C{Phenomena Server}
    C -->|Sockets| D[Processing Audio]
    C -->|Sockets| E[Processing Video]
    D --> F[Sound]
    D --> L[MIDI Synth]
    E --> G[Image]
{{< /mermaid >}}

##### Phenomena Server

{{<mermaid align="left">}}
graph LR
    A --> B
    B --> C
    C --> D
    D --> A
    subgraph accumulator
    D
    G[Particle Decay]
    end
    subgraph node video
    C
    C1[Particle add/remove]
    C2[Video Mapping]
    end
    subgraph node audio
    B
    B1[Particle add/remove]
    B2[Audio Mapping]
    end
    subgraph particle entry
    A
    H[Particle Instantiation]
    end
{{< /mermaid >}}
