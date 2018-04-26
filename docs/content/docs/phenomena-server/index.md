+++
title = "Phenomena Server"
subtitle = "Particle I/O management"
description = "Particle instantiation & life-cycle is managed by the Phenomena server. It also provides communication with the visualization & sonorization modules."
date = "2018-04-13"
weight = 2
+++

##### Introduction
-

{{<mermaid align="left">}}
graph LR
    A --> B
    B --> C
    C --> D
    D --> A
    subgraph Accumulator
    D
    G[Particle Decay]
    end
    subgraph Video Node
    C
    C1[Particle add/remove]
    C2[Particle parameters]
    C3[Video Mapping]
    end
    subgraph Audio Node
    B
    B1[Particle add/remove]
    B2[Particle parameters]
    B3[Audio Mapping]
    end
    subgraph Particle Entry
    A
    H[Particle Instantiation]
    end
{{< /mermaid >}}
