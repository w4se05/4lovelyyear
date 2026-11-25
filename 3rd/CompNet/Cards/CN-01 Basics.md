---
course: Computer Networks
source: "[[01-Basics]]"
---
#flashcards/cn/01-basics

# CN-01 Basics — Cards (script 02)

> [!info] How to use
> The exam asks you to explain in your own words, so the ✍️ cards matter most here. Fill them from memory, then check in [[01-Basics|CN-01]]. Plan: [[00 CompNet Plan]]

## Components and terms

Three components every computer network needs?::At least 2 hosts with network services, a transmission medium, network protocols.

Server vs. client vs. peer?::Server: provides a network service. Client: uses (consumes) a network service. Peer: is server and client at the same time (P2P).

Do server/client describe hardware?::No — they describe roles of network services; almost any computer can act as both.

What is a protocol?::The set of all agreements made beforehand between communication partners (message formats, rules, behavior).

Guided vs. unguided transmission media?::Guided: copper cable (electrical impulses), fiber-optic cable (light impulses). Unguided: electromagnetic waves (radio, infrared, ...).

Network classes by dimension, small to large?::PAN/BAN (few meters) < LAN (building/campus) < MAN (city) < WAN (country/continent) < GAN (global).

Why is fiber used in MANs?::Lower attenuation and higher data rates over long distances.

## Communication

Unicast / broadcast / multicast / anycast?::Unicast: one-to-one. Broadcast: one-to-all. Multicast: one-to-group (all members). Anycast: one-to-one-of-a-group (e.g. the nearest member).

Which cast schemes need the notion of a group?::Multicast and anycast.

Connection-oriented vs. connectionless?::Connection-oriented: 3 phases (establishment, transfer, release), stateful — e.g. TCP. Connectionless: just send, stateless — e.g. UDP.

Simplex / half-duplex / full-duplex?::Simplex: only one direction. Half-duplex: both directions, but not at the same time. Full-duplex: both directions simultaneously.

## Performance

Bandwidth vs. throughput vs. goodput?::Bandwidth: bits per time the network can transmit. Throughput: bits actually transmitted per time. Goodput: useful payload actually delivered (without overhead/retransmissions). Bandwidth ≥ throughput ≥ goodput.

Latency formula?::t_lat = t_prop + t_trans + t_wait, with propagation delay t_prop = d / (c · v_f) and transmission delay t_trans = message size / bandwidth.

Velocity factors: vacuum, twisted pair, optical fiber?::1, about 0.6, about 0.67.

Link volume (bits "inside" the line)?::V = R · t_prop (bandwidth × propagation delay).

## Topologies

Bus topology?::All devices on one shared medium, no active components; easy to extend; collisions; a cable break splits the network.

Ring topology?::Node to node, data passed on until the destination; disruption of one node or link can break the ring.

Star topology?::All nodes connected to a central component (switch); the central component is a single point of failure; standard for wired LANs today.

Mesh topology?::Nodes connected to one or more others; redundant paths; fully connected mesh with n nodes needs n(n−1)/2 links.

## Reference models

Layers of the TCP/IP reference model?::Link (network access), Internet, Transport, Application.

The 7 OSI layers from bottom to top?::Physical, Data Link, Network, Transport, Session, Presentation, Application.

Data unit per layer (L1–L4)?::L1 bits/signals, L2 frames, L3 packets, L4 segments.

Addressing per layer (L2–L4)?::L2 MAC addresses, L3 IP addresses, L4 port numbers.

Devices per layer?::L1 repeater, hub; L2 bridge, switch; L3 router; above: gateways.

Encapsulation?::Each layer adds its own header (some also a trailer, e.g. Ethernet) to the data of the layer above.

Services / interfaces / protocols in OSI?::Service: what a layer does. Interface: how the layer above accesses it. Protocol: how peers on the same layer communicate.

## Understanding — write your own answers ✍️

✍️ Prussian semaphore (sheet 1): 6 arms with 4 positions, new setting every 10 s, 62 stations, 1 min forwarding per station. Data rate? End-to-end delay? Time for 24 bits and for 512 bits?
?
✍️ your answer (show the steps) — then check [[01-Basics|CN-01]] §6 and exercise session 02

✍️ Explain the difference between bandwidth, throughput and latency with the tube analogy. (self-check question)
?
✍️ your answer — then check [[01-Basics|CN-01]] §6

✍️ What is a reference model, and why are layers useful? (self-check question)
?
✍️ your answer — then check [[01-Basics|CN-01]] §8

✍️ Why are the Session and Presentation layers hardly used? (sheet 2)
?
✍️ your answer — then check [[01-Basics|CN-01]] §9

✍️ What is a computer network, and what are its objectives? (self-check question)
?
✍️ your answer — then check [[01-Basics|CN-01]] §1–2
