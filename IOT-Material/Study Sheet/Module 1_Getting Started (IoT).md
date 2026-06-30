	## 1. MODULE OVERVIEW

This module answers the question: *"What is IoT and how does a physical device talk to the Internet?"* It starts by defining IoT and the hardware that makes it possible (Lesson 1), then zooms into how those devices actually work inside — CPU, memory, I/O, and the Arduino/Raspberry Pi programming models (Lesson 2). Lesson 3 covers the two physical-world interfaces — sensors (gathering data) and actuators (making things happen). Lesson 4 ties it all together by introducing MQTT, the protocol that lets a device send sensor readings to the cloud and receive commands back. By the end, the student conceptually understands the full chain: physical world → sensor → device → Internet → cloud processing → command → actuator → real-world action.

---

## 2. KEY CONCEPTS

### 2.1 The Internet of Things (IoT)

- **Plain-language definition:** Connecting everyday physical objects to the Internet so they can send data about their surroundings and/or receive instructions to do something in the real world.
- **Why it matters:** Before IoT, computers only interacted with people (keyboard, screen). IoT lets computers sense and act on the physical world automatically, at massive scale.
- **Example from the material:** A smart thermostat senses room temperature (sensor), sends it to a cloud service, and receives a command to turn heating on/off (actuator). The user can also check the temperature from a phone app anywhere in the world.

### 2.2 Sensors

- **Plain-language definition:** A piece of hardware that measures something about the physical world (temperature, light, movement, sound) and turns that measurement into an electrical signal that a computer can read.
- **Why it matters:** Sensors are the *eyes and ears* of an IoT device. Without them, the device is blind to what's happening around it.
- **Example from the material:** A light sensor in the nightlight project returns an integer value (0–1023) representing how bright or dark the room is.

### 2.3 Actuators

- **Plain-language definition:** A piece of hardware that takes an electrical signal from a computer and turns it into a physical action — like turning on a light, making a sound, or moving a motor.
- **Why it matters:** Actuators are the *hands and voice* of an IoT device. They let the device change the physical world, not just observe it.
- **Example from the material:** An LED (light-emitting diode) turns on when it receives a digital "1" signal and off on a digital "0" signal. In the nightlight, the LED lights up automatically when the room is dark.

### 2.4 Microcontroller (MCU)

- **Plain-language definition:** A tiny, cheap computer on a single chip with a CPU, memory, and pins to connect sensors/actuators. It runs one specific program forever and uses very little power.
- **Why it matters:** Microcontrollers are the "brains" inside most mass-produced IoT products (smart plugs, fitness trackers, microwave ovens). They cost as little as a few cents and can run for years on a small battery.
- **Example from the material:** The Wio Terminal (used in the Arduino track) is a microcontroller developer kit costing ~US$30, with a 120 MHz CPU and 192 KB of RAM.

### 2.5 Single-Board Computer (SBC)

- **Plain-language definition:** A complete, general-purpose computer (CPU, memory, graphics, USB ports, SD card slot) squeezed onto a single small circuit board, running a full operating system like Linux.
- **Why it matters:** SBCs let you use familiar tools (Python, a desktop OS, a web browser) to build IoT prototypes and even professional products. They trade low power/cost for flexibility and ease of programming.
- **Example from the material:** The Raspberry Pi 4B has a 1.5 GHz quad-core CPU, up to 8 GB RAM, and 40 GPIO pins, running Raspberry Pi OS (Debian Linux), starting at US$35.

### 2.6 Microcontroller vs. Single-Board Computer (Conceptual Comparison)

This comparison appears across Lessons 1–2. See section 4 below for a full tradeoff table. The core ideas are: microcontrollers are specialized and minimalist; SBCs are general-purpose and full-featured.

### 2.7 Analog vs. Digital (for Sensors and Actuators)

- **Analog:** A continuously varying electrical signal (like a dimmer switch — any brightness level between off and full). Analog sensors return a voltage proportional to what they measure. Analog actuators respond proportionally to the voltage they receive.
- **Digital:** A signal with only two states — on (1, HIGH) or off (0, LOW). Digital sensors return either 0 or 1, or have a built-in converter to send a stream of bits. Digital actuators are either on or off (or use built-in converters for more nuance).
- **Why it matters:** Computers are digital — they only understand 0s and 1s. So an analog signal from a sensor must be converted to digital before the computer can process it (ADC). Likewise, if you want to control an analog actuator from a digital device, you need a DAC or PWM.
- **Example from the material:** The nightlight's light sensor is analog (returns 0–1023). The LED is digital (on/off). The threshold of 300 is a digital decision made from an analog reading.

### 2.8 Analog-to-Digital Converter (ADC)

- **Plain-language definition:** A circuit (often built into the IoT device or on a connector board) that takes a smoothly varying analog voltage and converts it into a binary number the computer can work with.
- **Why it matters:** Without ADC, a microcontroller or SBC cannot make sense of most sensors, since the physical world is analog and computers are digital.
- **Example from the material:** A light sensor sending 1V when powered by 3.3V gets converted by the Grove hat ADC to the digital value 300 (out of 1023). From code, you simply read this as the number 300.

### 2.9 Pulse-Width Modulation (PWM)

- **Plain-language definition:** A trick to *simulate* an analog signal using only digital on/off pulses — you turn the signal on and off very quickly, and the *percentage* of time it stays on (the duty cycle) determines the effective output.
- **Why it matters:** Many IoT devices don't have a true DAC. PWM lets them approximate analog control (dimming an LED, controlling motor speed) using only digital pins.
- **Example from the material:** To run a motor at half speed (75 RPM instead of 150 RPM), you pulse 5V for 0.01s on, then 0V for 0.03s off in each 0.04s cycle — a 25% duty cycle.

### 2.10 The Arduino Sketch Model (setup/loop)

- **Plain-language definition:** A programming pattern where you write two functions: `setup()` (runs *once* when the device powers on — configure things) and `loop()` (runs *over and over forever* — read sensors, send data, control actuators). This is called an **event loop** or **message loop**.
- **Why it matters:** This is the fundamental programming architecture for Arduino and many embedded systems. It reflects the reality that an IoT device's job is to repeatedly sense, decide, and act, forever.
- **Example from the material:** In the Arduino sketch, `setup()` initializes WiFi and pins; `loop()` reads a sensor, maybe sends telemetry, and calls `delay(10000)` to sleep for 10 seconds before the next cycle.

### 2.11 IoT on the Edge

- **Plain-language definition:** Processing sensor data on the device itself (or a nearby local hub) instead of sending everything to a distant cloud server. "Edge" means the edge of the network — close to where data is created.
- **Why it matters:** Edge processing is faster (no network lag), works offline, and keeps sensitive data private.
- **Example from the material:** Smart speakers (Amazon Echo, Google Home) run AI speech recognition locally and only send audio to the cloud *after* detecting the wake word. Everything else stays on the device. **Air-gapping** is the extreme case — a network completely isolated from the Internet.

### 2.12 MQTT (Message Queuing Telemetry Transport)

- **Plain-language definition:** A very lightweight messaging system designed for small, low-power devices. All devices connect to a central **broker**. One device **publishes** a message to a named **topic**; the broker forwards it to every device that **subscribed** to that topic. This is called **publish/subscribe** (pub/sub).
- **Why it matters:** MQTT is the most popular protocol for IoT communication. It's designed to be minimal so it can run on microcontrollers with tiny amounts of memory and over unreliable connections.
- **Example from the material:** The nightlight device publishes `{"light": 143}` to the topic `id/telemetry` every 5 seconds. The server subscribes to that topic, receives the message, decides the light is too dim, and publishes `{"led_on": true}` to `id/commands`. The device, subscribed to `id/commands`, receives this and calls `led.on()`.

### 2.13 Telemetry

- **Plain-language definition:** Data about the physical world gathered by sensors and sent from the device to the cloud. The word means "measuring from afar."
- **Why it matters:** Telemetry is the "upload lane" of IoT — it's how the cloud knows what's happening at every device.
- **Example from the material:** The nightlight sends light-level values as JSON telemetry to the MQTT broker.

### 2.14 Commands

- **Plain-language definition:** Messages sent from the cloud *to* a device instructing it to do something — turn on a light, open a valve, reboot.
- **Why it matters:** Commands are the "download lane" of IoT — they close the loop, enabling automatic responses to telemetry.
- **Example from the material:** The server sends `{"led_on": true}` as a command; the device receives it and turns the LED on.

### 2.15 Quality of Service (QoS) in MQTT

- **Plain-language definition:** A setting for each MQTT message that tells the broker how hard to try to deliver it:
  - **QoS 0:** Send once, don't check if it arrived (fire and forget).
  - **QoS 1:** Keep re-sending until the receiver acknowledges it (at least once).
  - **QoS 2:** A two-step handshake to guarantee the message is delivered exactly once, no duplicates (assured delivery).
- **Why it matters:** Different IoT data has different reliability needs. A lost temperature reading from a thermostat may not matter; a missed "emergency shutdown" command in a factory could be catastrophic.
- **Example from the material:** The lesson contrasts thermostat telemetry (current value is what matters, data loss is okay) with factory machinery telemetry (every data point matters for anomaly detection, must be queued if offline).

---

## 3. KEY TERMS

| Term | One-line plain-language definition |
|------|------------------------------------|
| **IoT (Internet of Things)** | Connecting physical objects to the Internet so they can send sensor data and/or receive commands to act on the real world. |
| **Kevin Ashton** | The person who coined the term "Internet of Things" in 1999. |
| **Sensor** | Hardware that measures a physical property (light, temperature, motion) and converts it into an electrical signal a computer can read. |
| **Actuator** | Hardware that converts an electrical signal from a computer into a physical action (light, sound, movement). |
| **Edge device** | A device that processes sensor data locally rather than sending it to the cloud; can operate offline. |
| **Air-gapping** | Running a network completely isolated from the Internet for maximum privacy and security. |
| **Microcontroller (MCU)** | A tiny, cheap, single-purpose computer on a chip with CPU, memory, and I/O pins; runs one program on bare metal. |
| **Single-Board Computer (SBC)** | A full computer on one board, running an OS like Linux, with GPIO pins for sensors/actuators (e.g., Raspberry Pi). |
| **Developer kit** | A general-purpose IoT board designed for prototyping, with extra pins and features not found in final products. |
| **GPIO (General-Purpose Input/Output)** | Pins on an IoT device that can be set by software to either read a value (input) or send one (output). |
| **CPU (Central Processing Unit)** | The "brain" that executes program instructions; its speed is measured in Hertz (cycles per second). |
| **Clock cycle** | One tick of the CPU's internal clock; each tick, the CPU can execute one instruction. |
| **Hertz (Hz)** | Unit of CPU speed; 1 Hz = 1 cycle per second. 1 MHz = 1 million Hz, 1 GHz = 1 billion Hz. |
| **Fetch-decode-execute cycle** | The three-step loop a CPU repeats every clock tick: grab an instruction from memory, figure out what it means, then do it. |
| **Program memory** | Non-volatile storage on a microcontroller that holds your code; survives power-off. |
| **RAM (Random-Access Memory)** | Volatile, fast memory used while a program runs; all contents are lost when power is removed. |
| **RTOS (Real-Time Operating System)** | A lightweight OS for microcontrollers that supports multitasking, networking, and GUIs. |
| **Arduino** | The most popular open-source microcontroller framework; programs are written in C/C++. |
| **Sketch** | An Arduino program consisting of a `setup()` function (runs once) and a `loop()` function (runs forever). |
| **Event loop / Message loop** | A program structure where a main loop repeatedly checks for new input (events) and responds to them. |
| **Raspberry Pi** | The most popular single-board computer; made by a UK charity, runs Linux, starts at US$5 (Zero) to US$35 (Pi 4). |
| **Raspberry Pi OS** | A version of Debian Linux that runs on all Raspberry Pi models; available with or without a desktop. |
| **ARM processor** | The type of CPU used in Raspberry Pi, most smartphones, and Apple Silicon Macs — different from Intel/AMD x86 CPUs. |
| **Hat (Raspberry Pi)** | An add-on board that plugs into the Pi's 40 GPIO pins, adding extra capabilities like screens or sensor adapters. |
| **Analog sensor** | A sensor that returns a continuously varying voltage proportional to what it measures. |
| **Digital sensor** | A sensor that returns either 0/1 (two states) or a binary number via a built-in ADC. |
| **Analog-to-digital converter (ADC)** | Hardware that converts a smoothly varying voltage into a binary number a computer can process. |
| **Digital-to-analog converter (DAC)** | Hardware that converts a binary number into a smoothly varying voltage for controlling analog actuators. |
| **Voltage** | A measure of how strongly electricity is being "pushed" through a circuit. |
| **Potentiometer** | A rotating dial sensor; the returned voltage depends on the dial's position. |
| **Thermistor** | A resistor whose resistance changes with temperature; used in analog temperature sensors. |
| **Photodiode** | A component that converts light into an electrical signal; used in light sensors. |
| **Pulse-Width Modulation (PWM)** | A technique that simulates an analog signal by rapidly pulsing a digital signal on and off. |
| **Duty cycle** | The percentage of time a PWM signal stays on during one on-off cycle. |
| **LED (Light-Emitting Diode)** | A simple digital actuator that lights up when it receives a digital "1" (HIGH) signal. |
| **Relay** | A switch actuator that lets a small voltage from an IoT device control a much larger voltage (like a mains-powered appliance). |
| **Stepper motor** | An actuator that rotates in precise, fixed-angle steps based on electrical pulses. |
| **Consumer IoT** | IoT products people buy for personal use at home (smart speakers, fitness trackers, smart thermostats). |
| **Commercial IoT** | IoT used in workplaces (office occupancy sensors, retail stock monitoring, vehicle tracking). |
| **Industrial IoT (IIoT)** | IoT used to control and monitor factory machinery at large scale, including predictive maintenance. |
| **Infrastructure IoT** | IoT used to manage public systems — smart cities (air quality monitoring) and smart power grids. |
| **Smart City** | An urban area that uses IoT sensors to collect data and improve city operations (traffic, pollution, energy). |
| **Smart power grid** | A power grid that gathers usage data at the individual-house level to optimize energy production and distribution. |
| **Digital agriculture** | Using IoT sensors, drones, satellites, and AI in farming to monitor crops, soil, and automate watering. |
| **Stuxnet** | A computer worm that destroyed centrifuges by manipulating their valves — the go-to example of why IoT security matters. |
| **Cloud service** | Software running on Internet servers that processes IoT data, runs AI models, and sends commands back to devices. |
| **MQTT (Message Queuing Telemetry Transport)** | The most popular IoT messaging protocol; uses a central broker and publish/subscribe topics. |
| **Broker** | The central server in MQTT that receives all messages and routes them to subscribers based on topics. |
| **Topic** | A named channel in MQTT (like a label) used to route messages between publishers and subscribers. |
| **Publish** | To send a message to a specific MQTT topic. |
| **Subscribe** | To tell the MQTT broker you want to receive all messages sent to a particular topic. |
| **Publish/Subscribe (pub/sub)** | A messaging pattern where senders and receivers are decoupled — they communicate only through named topics on a broker. |
| **QoS (Quality of Service)** | An MQTT guarantee level for message delivery: 0 (at most once), 1 (at least once), 2 (exactly once). |
| **Retained flag** | An MQTT setting that makes the broker store the last message on a topic and send it immediately to any new subscriber. |
| **Keep alive** | An MQTT feature that periodically checks if the connection to the broker is still alive during quiet periods. |
| **Telemetry** | Sensor data sent from an IoT device to the cloud (derived from Greek for "measure remotely"). |
| **Command** | A message sent from the cloud to an IoT device telling it to perform an action. |
| **JSON (JavaScript Object Notation)** | A simple text format for structured data using key/value pairs (e.g., `{"light": 143}`), used to encode telemetry and commands. |
| **Eclipse Mosquitto** | A free, open-source MQTT broker; also provides the public test broker at `test.mosquitto.org`. |
| **paho-mqtt** | A Python library (`pip install paho-mqtt`) for connecting to and using MQTT. |
| **Virtual environment (Python)** | An isolated copy of Python in its own folder so installed packages don't conflict across projects. |
| **CounterFit** | A software tool that simulates IoT sensors and actuators on your PC so you can write and test device code without buying hardware. |

---

## 4. COMPARISONS & TRADEOFFS

### 4.1 Microcontroller (MCU) vs. Single-Board Computer (SBC)

| Aspect | Microcontroller (e.g., Arduino/Wio Terminal) | Single-Board Computer (e.g., Raspberry Pi) |
|--------|----------------------------------------------|--------------------------------------------|
| **What it is** | A single-purpose chip with CPU, tiny memory, and I/O pins. No OS. | A full computer on one board, running a desktop OS. |
| **Cost** | As low as US$0.03; dev kits US$4–$30 | US$5 (Pi Zero) to US$35+ (Pi 4B) |
| **Power use** | Extremely low — can run months/years on small batteries | Higher — needs a proper power supply |
| **Speed / Memory** | Wio Terminal: 120 MHz, 192 KB RAM, 4 MB storage | Pi 4B: 1.5 GHz quad-core, 2–8 GB RAM, SD card storage |
| **Operating System** | No desktop OS; may use an RTOS | Full Linux OS (Raspberry Pi OS) |
| **Programming** | Typically C/C++; Arduino uses setup/loop | Typically Python; wide language support |
| **Best for** | Mass-produced single-purpose devices, battery-powered, cost-sensitive | Prototyping, education, projects needing an OS |
| **Physical size** | Tiny — smallest MCU is 1.6×2×1 mm | Larger — Pi 4B is 88×58×19.5 mm |

**When to use which:** Use a microcontroller when you need low cost, low power, and one specific job (e.g., a smart light switch). Use a single-board computer when you need a full OS, ease of programming, or complex local processing (e.g., a home automation hub running Python scripts and a web dashboard).

### 4.2 Edge Processing vs. Cloud Processing

| Aspect | Edge Processing | Cloud Processing |
|--------|-----------------|------------------|
| **What it is** | Processing sensor data on the device itself or on a local hub. | Sending all data to remote servers for processing. |
| **Speed** | Instant — no network delay. | Slower — depends on Internet speed and latency. |
| **Offline capability** | Works without Internet. | Fails without Internet. |
| **Privacy** | Data stays local. | Data leaves the local network. |
| **Computing power** | Limited (small device). | Massive (data centers with AI/ML). |
| **Best for** | Time-sensitive actions, privacy-critical data, remote locations. | Complex analytics, AI model training, cross-device coordination. |

### 4.3 Analog vs. Digital Sensors

| Aspect | Analog Sensor | Digital Sensor |
|--------|---------------|----------------|
| **What it returns** | A continuously varying voltage. | Either 0/1, or a binary number (via built-in ADC). |
| **Conversion needed** | Needs an external ADC between sensor and device. | May handle conversion internally. |
| **Granularity** | Can measure a full range of values. | Simple digital: only detects on/off; advanced: fine-grained via internal ADC. |
| **Example from material** | Light sensor returning 0–1023 via Grove hat ADC. | A button returning 0 (not pressed) or 1 (pressed). |

### 4.4 PWM vs. True Analog (DAC)

| Aspect | PWM (Pulse-Width Modulation) | True Analog (DAC) |
|--------|------------------------------|-------------------|
| **What it does** | Simulates analog with rapid on/off pulses. | Produces a genuine smooth varying voltage. |
| **Hardware needed** | Uses a standard digital pin. | Needs a dedicated DAC circuit. |
| **Output** | A square wave whose average power varies with duty cycle. | A smooth, continuous voltage level. |
| **Example** | Controlling motor speed with PWM (75–150 RPM). | A dimmable light whose brightness follows the exact voltage. |

### 4.5 MQTT QoS Levels

| QoS | Name | Guarantee | Use when |
|-----|------|-----------|----------|
| **0** | At most once | Sent once, no acknowledgement. | Routine telemetry where occasional loss is acceptable. |
| **1** | At least once | Re-sent until acknowledged; duplicates possible. | Important data where missing a message is worse than duplicates. |
| **2** | Exactly once | Two-step handshake; no duplicates, no loss. | Critical commands where duplicates cause problems (e.g., an emergency shutdown that must happen exactly once). |

---

## 5. LIKELY EXAM ANGLES

1. **"Which of the following is NOT a category of IoT applications?"** — Expect a multiple-choice question listing Consumer, Commercial, Industrial (IIoT), Infrastructure plus one distractor. Know the four categories and one example from each.

2. **"Compare a microcontroller and a single-board computer. When would a product designer choose one over the other?"** — Short-answer question covering cost, power, memory, OS, programming language, and use cases. Be ready to cite specific numbers: e.g., Wio Terminal: 120 MHz, 192 KB RAM; Raspberry Pi 4B: 1.5 GHz, up to 8 GB RAM.

3. **"Explain what ADC and PWM are and why they are necessary in IoT."** — A combined concept question. Expected answer: computers are digital, but the physical world is analog; ADC converts analog sensor readings to digital for processing; PWM simulates analog control using digital pins because many devices lack a true DAC.

4. **"Describe the sequence of events in an MQTT-based IoT system, from sensor reading to actuator response."** — Walk through: device reads sensor → publishes JSON telemetry to a topic → broker routes to subscribed server → server processes, decides an action → publishes command JSON to another topic → broker routes to device → device calls actuator. Include the terms: publish, subscribe, broker, topic, telemetry, command.

5. **"Why is IoT security important? Give an example of a real-world consequence of poor IoT security."** — Stuxnet (manipulated centrifuge valves); hackers accessing baby monitors/security cameras. Key phrase: "the S in IoT stands for Security" (there is no S — it's a joke about IoT's reputation for being insecure). Also: air-gapping as a mitigation.

---

## 6. GAPS / AMBIGUITIES

- **Mesh networking mentioned but not explained.** Lesson 2 mentions that devices can use "mesh networking (e.g. Bluetooth) to talk to each other, connecting via a hub device that has an Internet connection," but no definition or mechanism is given. A student seeing "mesh networking" on an exam would need outside knowledge.

- **AMQP and HTTP/HTTPS name-dropped without context.** Lesson 4 states MQTT is the most popular protocol, and that others include "AMQP and HTTP/HTTPS," but never explains what they are or how they differ from MQTT. These could appear as distractors in an MCQ.

- **RTOS examples listed but not differentiated.** Azure RTOS, FreeRTOS, and Zephyr are named in Lesson 2 but with zero explanation of any. A question like "Which of these is an RTOS?" would be fair game based on the key terms, but no distinction is provided.

- **Serial.begin(9600) and baud rate not defined.** The Arduino code in Lesson 2 uses `Serial.begin(9600)` with no explanation of what baud rate means. The term appears in the walkthrough but never in the key terms or concepts. The concept (bits per second for serial communication) is implied but never stated.

- **GUID / unique ID generation is a click-path instruction with no conceptual anchoring.** The lesson says "Replace `<ID>` with a unique ID (e.g., a GUID from guidgen.com)" but never explains *why* uniqueness matters in a pub/sub system (to prevent multiple students' device/server pairs from interfering on the public broker because they'd share topic names). This is a conceptual point (topic namespace isolation) presented as a menu click.

- **JSON is described as "key/value pairs" but the exam may expect recognition of JSON syntax.** Students who have never seen JSON before might not immediately connect `{'light': 143}` to the term "key/value pair." The Python examples use single quotes, which is Python dict syntax, not strictly valid JSON (JSON requires double quotes). This distinction is not discussed.

- **"No standard unit like lux" for the light sensor is flagged but not resolved.** The CounterFit light sensor returns a unitless integer (0–1023). A student might wonder: is this the same on real hardware? The lesson doesn't explain what units real light sensors use or how the 0–1023 range maps to real-world brightness.