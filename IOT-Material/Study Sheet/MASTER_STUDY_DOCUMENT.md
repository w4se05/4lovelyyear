# MASTER IoT STUDY DOCUMENT -- Closed-Book Exam Preparation

> **How to use this document:** Start with Section 1 (Big Picture) to build the mental model. Study Section 2 (Recurring Core Concepts) thoroughly -- these are the highest-probability exam topics. Use Section 3 as a quick module-by-module refresher. Drill Section 4 (Glossary) for multiple-choice questions. Review Section 5 (Comparison Tables) for writing questions. Test yourself with Section 6 (Predicted Exam Questions). Section 7 flags anything the source material did not explain well.

---

## 1. BIG PICTURE: What IoT Is and the One Pattern That Runs Through Everything

### 1.1 What Is IoT?

**In plain language:** IoT (Internet of Things) means connecting everyday physical objects to the Internet so they can send data about their surroundings and/or receive instructions to do something in the real world.

Before IoT, computers only interacted with people (keyboard, screen). IoT lets computers sense and act on the physical world automatically, at massive scale.

### 1.2 The Universal IoT Pattern

Every IoT system in this course follows the same four-stage pipeline. If you internalize this pattern, you can reason about *any* IoT scenario on the exam -- even one you have never seen before.

```
SENSOR / DEVICE  ->  CONNECTIVITY  ->  CLOUD / PROCESSING  ->  ACTION / OUTPUT
(physical world)    (send data)      (analyze & decide)      (do something)
```

**Stage 1 -- Sensor / Device (the "Thing"):** A physical object equipped with sensors (eyes & ears) and sometimes actuators (hands & voice). Examples: a soil moisture probe, a GPS receiver, a camera, a microphone.

**Stage 2 -- Connectivity (the "Internet"):** The data travels from the device to a central system. Could be MQTT over WiFi, LoRaWAN across a field, cellular from a moving truck, or wired protocols (I2C, SPI, UART) within the device itself.

**Stage 3 -- Cloud / Processing (the "Insights"):** The data reaches a cloud service (or an edge device) where it is processed -- stored, analyzed, fed into an AI model, compared against thresholds. This is where raw numbers become actionable information.

**Stage 4 -- Action / Output (the "Actions"):** The system does something with the insight. Sends a command back to turn on a pump, lights an LED, displays a map, speaks an alert, or triggers a restock notification.

This four-stage pattern is formally called the **Things -> Insights -> Actions** reference architecture (introduced in Module 4), but it is the same idea described in Module 1 as "physical world -> sensor -> device -> Internet -> cloud processing -> command -> actuator -> real-world action."

### 1.3 How Each Module Instantiates the Same Pattern

| Module | Thing (Sensor/Device) | Connectivity | Insights (Processing) | Action (Output) |
|--------|----------------------|--------------|----------------------|-----------------|
| **1. Getting Started** | Light sensor on Wio Terminal / Raspberry Pi | MQTT to broker | Cloud server checks light level against threshold | Command turns LED on |
| **2. Farm** | Soil moisture sensor, temperature sensor | MQTT -> Azure IoT Hub | Serverless function checks moisture; GDD calculated from temp CSV | Relay activates water pump |
| **3. Transport** | GPS receiver on vehicle | IoT Hub (over cellular) | Geofence API checks location; blob storage saves coordinates | Map visualization; geofence alert |
| **4. Manufacturing** | Camera + proximity sensor on conveyer belt | IoT Hub -> edge device (Docker container) | Edge AI classifier decides ripe/unripe; cloud function orchestrates | C2D command triggers LED alert (or pneumatic sorter in production) |
| **5. Retail** | Camera pointed at store shelf | REST API to cloud AI | Custom Vision object detector counts items; code filters duplicates | Restock notification sent to staff |
| **6. Consumer** | MEMS microphone + button on smart timer | HTTP trigger -> Azure Functions -> LUIS -> Translator | Speech->text (STT); NLU extracts intent + duration; TTS synthesizes reply | Spoken confirmation; timer alert |

Every module is the same pattern with different sensors, different processing, and different actions -- but the skeleton is identical. If an exam question describes an unfamiliar IoT scenario (e.g., "a hospital wants to monitor refrigerator temperatures for vaccine storage"), you can answer by mapping it onto these four stages.

### 1.4 The Course's Implicit Journey

The modules also tell a progression story:

1. **Module 1:** Learn the basic building blocks (sensors, actuators, MQTT, microcontrollers, Raspberry Pi).
2. **Module 2:** Apply them to a real problem (smart farming), then **professionalize** -- migrate from a public test broker to Azure IoT Hub, add serverless cloud functions, add encryption and device authentication.
3. **Module 3:** Add location data (GPS) and learn to store/visualize it, introducing the hot/warm/cold data path model.
4. **Module 4:** Introduce AI (image classification) and **edge computing** -- moving AI from the cloud onto a local device for speed and privacy.
5. **Module 5:** Level up the AI to object detection (not just "what is this?" but "how many and where?"), adding the real-world challenge of filtering bad predictions.
6. **Module 6:** Switch sensor modality entirely -- from physical measurements to human speech -- tying together speech recognition, language understanding, and speech synthesis into a complete voice interface, then adding translation to make it multilingual.

The exam may test you on concepts from any point in this progression -- but the recurring ideas (Section 2) are the ones the course keeps coming back to.

---

## 2. RECURRING CORE CONCEPTS (Highest-Probability Exam Topics)

These concepts appear across multiple modules. For each one, assume a writing question could ask you to define it, explain it, compare it to an alternative, or map it onto a new scenario.

---

### 2.1 Cloud Processing vs. Edge Processing

**Appears in:** Module 1 (introduced), Module 4 (full implementation), Module 6 (TinyML / wake words)

#### What Each One Is

- **Cloud processing:** Sensor data travels over the Internet to a distant data center (owned by Microsoft, Amazon, Google). All the analysis, AI, and decision-making happens there. Results are sent back to the device or shown on a dashboard.

- **Edge processing:** A powerful computer sits on the same local network as the IoT devices (the "edge" of the network -- close to where data is created). Data is processed locally. The cloud is still used for long-term storage, management, and analytics -- but real-time decisions happen on the edge.

#### Why This Matters

This is arguably the single most important architectural decision in any IoT system. Choosing wrong means wasting money, compromising privacy, or creating a system that fails every time the Internet goes down.

#### How It Appears Differently in Each Module

- **Module 1:** Introduced conceptually. Smart speakers run AI locally to detect the wake word ("Alexa," "Hey Siri") -- this is edge processing. Only *after* the wake word is detected does audio go to the cloud. **Air-gapping** (a network completely disconnected from the Internet) is presented as the extreme edge case for maximum privacy.

- **Module 4:** This is where edge computing is fully implemented. The trained fruit classifier model is exported from Custom Vision, packaged as a **Docker container**, and deployed to an **Azure IoT Edge** device on the factory floor. The camera sends images to `http://<edge_device_ip>/image` instead of the cloud API. Benefits: no Internet lag, works offline, lower cloud compute costs, images never leave the building.

- **Module 6:** **Wake words** implement edge processing on microcontrollers. **TinyML** compresses machine learning models to fit on devices with tiny memory and battery. The wake word model runs entirely on-device -- no audio leaves the device before activation. The course uses a physical button to avoid TinyML complexity, but the concept is the same: local, private, always-on processing.

#### Complete Tradeoff Table

| Aspect | Edge Processing | Cloud Processing |
|--------|-----------------|------------------|
| **What it is** | Processing on a local device or nearby hub, close to where data is created | Processing on remote servers in a data center |
| **Speed / Latency** | Instant -- no network round-trip | Depends on Internet speed; transatlantic latency is ~28ms+ |
| **Offline capability** | Works without Internet | Fails without Internet |
| **Privacy** | Data stays on local network | Data leaves your control |
| **Computing power** | Limited by local hardware | Massive -- data centers with GPUs, AI/ML clusters |
| **Cost per operation** | Hardware purchase + maintenance | Pay-per-use (often fractions of a cent) |
| **Scalability** | Limited -- must buy more hardware | Auto-scales instantly |
| **Software updates** | Must update each device | Update once in the cloud |
| **Best for** | Real-time decisions, privacy-critical data, remote/offline locations, high-bandwidth data like video | Complex analytics, AI model training, cross-device coordination, long-term storage |

#### The Exam Answer: When to Choose Edge

Choose **edge** when any of these apply:
1. **Latency matters** -- you need a response in under 100ms (factory sorting, autonomous vehicles)
2. **Internet is unreliable or absent** -- remote farm, underground mine, at sea
3. **Data is private** -- factory trade secrets, medical images, home audio
4. **Bandwidth is expensive** -- streaming video from hundreds of cameras to the cloud costs a fortune; process locally and send only results
5. **You need a gateway** -- bridging incompatible or insecure devices onto a secure network

Choose **cloud** when:
1. You need to aggregate data from thousands of geographically distributed devices
2. You are training AI models (requires massive compute)
3. You want zero hardware maintenance
4. Long-term historical analysis across years of data

**Real systems blend both** -- edge for real-time, cloud for long-term storage and management. Module 4 explicitly recommends this hybrid approach.

---

### 2.2 Sensors (the "Eyes and Ears" of IoT)

**Appears in:** Every module (they are the starting point of every IoT pipeline)

#### What a Sensor Is

A sensor is hardware that measures a physical property (light, temperature, moisture, location, sound, distance) and converts it into an electrical signal a computer can read. Without sensors, an IoT device is blind.

#### The Cross-Module Sensor Catalog

| Physical Property | Sensor Type | Which Module | How It Works |
|-------------------|-------------|--------------|--------------|
| **Light** | Photodiode / light sensor | Module 1 | Converts light to voltage; returns 0-1023 via ADC |
| **Temperature** | Thermistor / DHT11 | Modules 1, 2 | Resistance changes with temperature; DHT11 is a digital combined temp+humidity sensor |
| **Soil moisture** | Resistive probe | Module 2 | Two metal probes; wet soil conducts more electricity -> lower resistance -> higher voltage |
| **Soil moisture** | Capacitive sensor | Module 2 | Measures electrical charge storage of soil; wetter soil -> lower voltage. More durable (no exposed metal). Used in CounterFit simulation. |
| **Location** | GPS receiver | Module 3 | Listens to satellite radio signals; triangulates position from 3+ satellites |
| **Images** | Camera (CMOS/APS) | Modules 4, 5 | Grid of millions of photodiodes; lens focuses light onto sensor; SPI protocol transfers large image data |
| **Distance** | Proximity sensor | Module 4 | Emits laser/IR/ultrasonic pulse; times the reflection (time-of-flight) |
| **Sound** | MEMS microphone | Module 6 | Etched onto silicon chip; same principle as condenser mic; tiny size, ideal for IoT |

#### The Big Idea: Analog World, Digital Computers

Nearly all physical properties are **analog** -- continuously varying. A room does not go from "dark" to "bright" in one step; the temperature does not jump from 20C to 21C instantaneously. But computers only understand **digital** -- discrete 0s and 1s.

This is why the **ADC (Analog-to-Digital Converter)** is such a foundational concept: it bridges the analog physical world and the digital computing world. Every sensor that produces an analog signal needs an ADC somewhere in the chain. The ADC is covered in depth in Module 1 and used throughout Modules 2 and 6.

**Key ADC numbers to know:**
- A 10-bit ADC (common on Arduino/Wio Terminal) divides the voltage range into 2^10 = 1,024 values (0-1,023)
- On a 3.3V board: 0V -> value 0, 3.3V -> value 1,023, 1.65V -> value ~511

#### Analog vs. Digital Sensors

| Aspect | Analog Sensor | Digital Sensor |
|--------|---------------|----------------|
| **Output** | Continuously varying voltage | Either 0/1, or a binary number (via built-in ADC) |
| **Conversion needed** | Needs external ADC | May handle conversion internally |
| **Granularity** | Full range of values | Simple digital: on/off only; advanced: fine-grained via internal ADC |
| **Example** | Light sensor (0-1023) via Grove hat ADC | Button (0 or 1); DHT11 (digital temp+humidity) |

#### Sensor Calibration (Module 2)

A sensor's raw output (e.g., "615") is meaningless by itself -- 615 what? **Calibration** is the process of mapping raw readings to real-world units by comparing against known reference samples. For soil moisture: take sensor readings from field soil, send samples to a lab for actual water content measurement, plot lab values vs. sensor values, and use the resulting line to convert future readings. The same moisture level produces different readings in sandy vs. clay soil, so calibration must be done per soil type.

---

### 2.3 Actuators (the "Hands and Voice" of IoT)

**Appears in:** Module 1 (LEDs, relays, stepper motors), Module 2 (relay -> water pump), Module 4 (LEDs as indicators, real actuators in production)

#### What an Actuator Is

An actuator takes an electrical signal from a computer and turns it into a physical action -- light, sound, movement. If sensors are input (world -> computer), actuators are output (computer -> world).

#### The Relay -- A Cross-Module Essential

The **relay** deserves special attention because it is the critical bridge between low-power IoT electronics and high-power real-world devices, appearing in both Modules 1 and 2.

**What it is:** An electrically-controlled mechanical switch. A tiny current from an IoT device (3.3V at under 1A) activates an internal electromagnet that physically pulls a metal lever, closing a separate high-power circuit.

**Why it is needed:** IoT devices output only 3.3V-5V at under 1 amp -- far too weak to directly power a water pump, a factory machine, or a mains appliance. The relay bridges this gap (the Grove relay handles up to 250V at 10A).

**How it works step by step:**
1. IoT device sends HIGH signal (3.3V/5V) to relay's **control circuit**
2. Current flows through a coil -> coil becomes an **electromagnet** -> pulls a lever -> lever touches switch contacts -> **output circuit** completes
3. Pump/motor/appliance (connected to output circuit) receives external power and runs
4. IoT device sends LOW signal -> electromagnet deactivates -> lever springs back -> output circuit opens -> pump stops
5. The relay makes an audible **click** when the lever moves

#### PWM -- Simulating Analog Control from Digital Pins

Many IoT devices lack a true DAC (Digital-to-Analog Converter). **PWM (Pulse-Width Modulation)** is the trick that simulates analog behavior using only digital on/off pulses: turn the signal on and off very fast, and the *percentage of time it stays on* (the **duty cycle**) determines the effective output. Used for dimming LEDs, controlling motor speed, and any scenario where you need graduated control from a digital-only pin.

---

### 2.4 Connectivity Protocols (How Devices Talk)

**Appears in:** Module 1 (MQTT), Module 2 (GPIO, I2C, UART, SPI, BLE, LoRaWAN, WiFi, Zigbee), Module 3 (IoT Hub transport), Module 6 (HTTP / REST)

IoT communication happens at two very different scales:
1. **Wired (board-level):** How a sensor chip talks to the microcontroller it is attached to (centimeters)
2. **Wireless (network-level):** How the device talks to the cloud or to other devices (meters to kilometers)

#### Wired Protocols (Board-Level)

**GPIO (General-Purpose Input/Output):** The most basic. A programmable metal pin on a board that you can set to read a voltage (input mode) or send a voltage (output mode). Limitation: only understands digital on/off (1/0). To read an analog sensor, you need an ADC.

**Analog Pins:** GPIO pins with a built-in ADC -- converts a continuous voltage range into a discrete digital number (e.g., 0-1,023 for 10-bit). Built into Arduino and Wio Terminal. The Raspberry Pi has NO native analog pins -- you need an external ADC board (like a Grove hat).

**I2C (Inter-Integrated Circuit):** One controller talks to multiple peripherals (sensors, displays) over just two shared wires -- SDA (data) and SCL (clock). Each peripheral has a hard-coded address; the controller sends a message starting with the target address so only the intended device responds. Speeds: Standard 100 Kbps, Fast 400 Kbps (Raspberry Pi max), High Speed 3.4 Mbps.

**UART (Universal Asynchronous Receiver-Transmitter):** A direct two-device connection. Tx (transmit) of device A connects to Rx (receive) of device B, and vice versa. Data sent one bit at a time. Both devices must agree on a **baud rate** (speed in bits per second; 9,600 is common). Each byte wrapped with a start bit and stop bit. No clock wire -- timing relies on agreed baud rate.

**SPI (Serial Peripheral Interface):** Controller-peripheral protocol using four wires: COPI (controller->peripheral), CIPO (peripheral->controller), SCLK (clock), and CS (chip select -- one per peripheral). Full-duplex (send and receive simultaneously). Very fast (multiple MB/s). Used for high-data-rate devices like cameras and flash memory.

#### The I2C vs. UART vs. SPI Comparison Table

| | I2C | UART | SPI |
|---|---|---|---|
| **Number of devices** | Multiple controllers + multiple peripherals | Exactly 2 devices | 1 controller + multiple peripherals |
| **Wires needed** | 2 shared (SDA + SCL) + power/ground | 2 (Tx<->Rx cross-connected) per pair | 4 (COPI, CIPO, SCLK, CS); +1 CS per extra peripheral |
| **Device identification** | Hard-coded address per peripheral | Only two devices -- no addressing needed | Chip Select (CS) wire wakes one peripheral at a time |
| **Speed** | Standard 100 Kbps; Fast 400 Kbps; High Speed 3.4 Mbps | Up to ~6.5 Mbps | No defined limit; often multiple MB/s |
| **Clock** | Yes (SCL from controller) | No -- relies on agreed baud rate | Yes (SCLK from controller) |
| **Framing** | Start/stop conditions on bus | Start bit + stop bit per byte | None needed (clock-synced) |
| **Full-duplex?** | No (half-duplex -- shared data wire) | Separate Tx/Rx but typically half-duplex | **Yes** (separate COPI and CIPO) |
| **Example use** | Multiple sensors/actuators on a board | GPS modules, serial consoles | Flash memory, cameras, displays, fast sensors |

#### Wireless / Network-Level Protocols

**MQTT (Message Queuing Telemetry Transport):** The most important IoT protocol in this course -- covered in Module 1 and used throughout Modules 2 and 3. A lightweight publish/subscribe messaging system.

- **Broker:** Central server that receives all messages and routes them
- **Topic:** A named channel (like a label) -- e.g., `device123/telemetry`
- **Publish:** Send a message to a topic
- **Subscribe:** Tell the broker you want to receive all messages on a topic
- **The beauty:** Publishers and subscribers do not know about each other -- they only know the topic name. This is called **decoupling.**
- **QoS (Quality of Service):** Three levels -- 0 (fire and forget, no guarantee), 1 (at least once, may duplicate), 2 (exactly once, assured delivery)
- **Example flow:** Device reads sensor -> publishes JSON to `device123/telemetry` -> broker routes to subscribed server -> server processes -> publishes command to `device123/commands` -> broker routes to device -> device acts

**Other wireless protocols (Module 2):**

| Protocol | Range | Power | Key Feature |
|----------|-------|-------|-------------|
| **BLE (Bluetooth Low Energy)** | Short (meters) | Very low | Fitness trackers, wearables |
| **LoRaWAN (Long Range, Low Power)** | Long (kilometers) | Very low | Commercial farm sensors; sends small data to a central hub |
| **WiFi** | Medium (tens of meters) | Higher | Standard home/office WiFi |
| **Zigbee** | Medium | Low | Mesh networking -- devices relay messages for each other to reach a coordinator |

#### HTTP / REST API

**Appears in:** Modules 4, 5, 6

Not a dedicated "IoT protocol" like MQTT, but used when IoT devices call cloud AI services directly (Custom Vision prediction API, LUIS, Translator). The device sends an HTTP POST request with data (image bytes, text) and receives a JSON response. Authentication is via API keys in HTTP headers (e.g., `Prediction-Key`, `Ocp-Apim-Subscription-Key`).

---

### 2.5 Security & Privacy in IoT

**Appears in:** Module 1 (Stuxnet, air-gapping), Module 2 (encryption, authentication, Mirai botnet), Module 6 (privacy via wake words, voice cloning risk)

#### Why IoT Security Matters

IoT devices are physically accessible, often mass-produced with minimal security, and connected to the Internet 24/7. A compromised IoT device becomes a doorway into networks, a spy in private spaces, or a soldier in a botnet army.

#### Real-World Failures Cited Across Modules

1. **Stuxnet (Module 1):** A computer worm that destroyed Iranian centrifuges by manipulating their valves -- the canonical example of why industrial IoT security matters. Physical destruction caused by digital attack.
2. **Mirai Botnet, 2016 (Module 2):** Malware scanned the Internet for IoT devices (DVRs, cameras) still using factory-default usernames/passwords. Enslaved hundreds of thousands of them and used them to launch a massive DDoS attack that took down large portions of the Internet. The vulnerability: **default passwords never changed.**
3. **Fish tank thermostat hack, 2018 (Module 2):** Attackers used an insecure WiFi-connected thermostat on a casino's fish tank as an entry point to steal data from the casino's corporate network. The vulnerability: **unsecured IoT device on the same network as critical systems.**
4. **CloudPets (Module 2):** A database of Internet-connected toy users (including children's voice recordings) was left publicly accessible. The vulnerability: **no access controls on stored data.**
5. **Voice cloning (Module 6):** Using transfer learning, a TTS model can be trained on a short audio sample to clone someone's voice -- meaning voice-based authentication is no longer reliable.

#### The Core Security Concepts

**Encryption** -- scrambling readable data into gibberish using a secret key, so only someone with the key can read it. Two types:

| | Symmetric Encryption | Asymmetric Encryption |
|---|---|---|
| **Keys** | One shared key for both encrypt and decrypt | Public key (encrypt only) + Private key (decrypt only) |
| **Key sharing risk** | Both parties must know the key -- sharing it is risky | Private key never shared; public key can be posted publicly |
| **Speed** | Faster | Slower (more complex math) |
| **Security** | Less secure -- key interception breaks everything | More secure -- private key never leaves owner |
| **IoT Hub usage** | SharedAccessKey -> SAS token authentication | X.509 certificate authentication |
| **Real-world pattern** | Used for bulk data after initial key exchange | Used to securely exchange the symmetric key first |

**Authentication** -- proving you are who you claim to be. Two methods in IoT Hub:

1. **Symmetric Key / SAS Token:** The device has a connection string containing a SharedAccessKey. On connection, the device creates a SAS token (URL + expiry time + encrypted signature). The key itself is never sent over the network. SAS tokens expire (preventing replay attacks), so the device must have an accurate clock (synced via NTP).

2. **X.509 Certificate:** The device presents a digital certificate signed by a trusted Certification Authority (CA). The certificate contains the device's public key. IoT Hub verifies the CA's signature. No clock dependency. One certificate can be shared across many devices; each device only needs its own private key.

**Privacy by Architecture:**
- **Air-gapping (Module 1):** Running a network completely isolated from the Internet -- the ultimate privacy measure but limits functionality.
- **Wake words (Module 6):** The device listens locally (TinyML on the edge) for a specific phrase. Only after detecting it does audio stream to the cloud. This means private conversations are never sent anywhere.
- **HTTP trigger wrapping (Module 6):** Instead of putting API keys on the device (where firmware extraction exposes them), put a serverless function in the cloud that holds the keys. The device calls your function; your function calls the AI service.

---

### 2.6 Data Storage & Management (Where All That Sensor Data Goes)

**Appears in:** Module 1 (telemetry concept), Module 2 (CSV files, IoT Hub storage), Module 3 (structured vs. unstructured, SQL vs. NoSQL, blob storage, hot/warm/cold paths)

#### Why Data Storage Is a Core Concern

An IoT system produces a continuous firehose of data -- GPS coordinates every few seconds from every vehicle, soil moisture from every field sensor, images from every shelf camera. That data needs to go somewhere, and choosing the wrong storage approach creates ongoing pain.

#### Structured vs. Unstructured Data

- **Structured data:** Fixed format, like an Excel spreadsheet. Every row has the same columns. Stored in SQL (relational) databases.
- **Unstructured data:** No fixed shape. One document has 3 fields; the next has 7 completely different fields. Stored in NoSQL databases or blob storage.

**Why IoT data is naturally unstructured:** A tractor sends GPS only. A delivery truck sends GPS + speed + driver ID. A refrigerated truck sends all of that + temperature. Forcing them all into one rigid SQL table means constantly altering the schema.

#### SQL vs. NoSQL

| | SQL (Relational Database) | NoSQL (Document Database) |
|---|---|---|
| **Data shape** | Fixed schema -- every row has the same columns | Schema-less -- each document can have different fields |
| **Adding new fields** | Requires ALTER TABLE; may cause downtime | Just start including the new field; zero database changes |
| **Query language** | SQL (standardized) | Varies by database; often JSON-based queries |
| **Best for** | Financial records, user accounts -- stable, uniform data | IoT telemetry from mixed fleets -- heterogeneous, evolving data |

**In the course:** GPS readings are stored as individual JSON blobs in **Azure Blob Storage** -- a form of unstructured storage where each blob is a tiny JSON file named with a UUID and organized in folders by device ID.

#### The Hot / Warm / Cold Data Path Model

Data is not equally urgent. This model classifies data by how quickly it needs to be processed:

| Path | Timing | What Happens | Example |
|------|--------|--------------|---------|
| **Hot** | Immediately (real-time) | Stream processing, instant alerts | Refrigerated truck temperature spike -> alert driver NOW |
| **Warm** | Shortly after receipt (minutes to hours) | Dashboards, reports, map generation | Yesterday's mileage report generated this morning |
| **Cold** | Long-term (months to years) | Stored in a data warehouse for historical batch analysis | 5 years of fuel costs analyzed to optimize next year's routes |

**Key insight:** You do not build the same infrastructure for all three. Hot path needs streaming processors and triggers. Cold path goes to a **data warehouse** -- a specialized database optimized for enormous historical datasets and complex analytical queries.

---

### 2.7 MQTT, IoT Hub, and the Evolution of Device-to-Cloud Communication

**Appears in:** Module 1 (MQTT fundamentals), Module 2 (migration to IoT Hub), Module 3 (consumer groups, Event Hub), Module 4 (C2D messages, device client)

#### The Journey from Simple to Professional

**Stage 1 -- Public MQTT Broker (Module 1):**
- Device publishes to `device123/telemetry`; server subscribes to that topic
- Server publishes to `device123/commands`; device subscribes to that topic
- Works for learning. Problems: no security (anyone can listen or inject), no reliability guarantees, no device management, cannot handle scale.

**Stage 2 -- Azure IoT Hub (Module 2):**
- A professionally managed replacement for the MQTT broker
- Only registered devices with valid keys/certificates can connect
- Built-in device registry -- knows all registered devices
- Handles millions of messages per day
- Four communication modes:

| Mode | Direction | Response Required? | Storage | Use |
|------|-----------|:---:|---------|-----|
| **D2C** (Device-to-Cloud) | Device -> Hub | No | Default 1 day | Sensor telemetry |
| **C2D** (Cloud-to-Device) | Hub -> Device | No | Configurable | App notifications, commands |
| **Direct Method** | Hub -> Device | **Yes** -- device must respond | Configurable | "Do this thing and confirm it worked" |
| **Device Twin** | Both ways | N/A (auto-synced) | **Permanent** | Device state and remote configuration |

**Stage 3 -- Consumer Groups (Module 3):**
- When multiple applications need to read the same IoT Hub messages independently, each needs its own **consumer group** -- an independent bookmark into the message stream
- Without separate consumer groups, two readers share one cursor and miss messages
- The `$Default` consumer group is created automatically; create additional ones (e.g., `geofence`) as needed
- Under the hood, IoT Hub exposes an **Event Hub compatible endpoint** -- Microsoft's message-streaming service

**Stage 4 -- The Full Palette (Module 4):**
- `IoTHubRegistryManager` -- cloud-side SDK class for sending C2D messages, invoking direct methods, managing device twins
- `IoTHubDeviceClient` -- device-side SDK class that handles connection, authentication, message send/receive
- `client.on_message_received` -- handler for incoming C2D messages on the device

#### The Device Twin -- A Deeper Look

**Appears in:** Module 2 (introduced), Module 4 (implemented for real)

A device twin is a JSON document in IoT Hub permanently paired with each device. It has two sides:
- **Desired properties:** What the cloud *wants* the device to do (e.g., "distance threshold = 10 cm")
- **Reported properties:** What the device says it *is* actually doing

The device automatically syncs when desired properties change. This solves the problem of **remote configuration**: change a threshold, update a setting, or reconfigure behavior without touching the physical device or updating firmware.

---

### 2.8 Azure Functions & Serverless Computing

**Appears in:** Module 2 (Event Hub trigger for soil moisture), Module 3 (multiple triggers with consumer groups), Module 4 (orchestration trigger for fruit detection), Module 6 (HTTP trigger for LUIS wrapper)

#### What "Serverless" Really Means

"Serverless" does not mean there are no servers. It means you write small chunks of code and upload them; the cloud provider handles all the servers -- running your code when triggered, scaling it automatically, and billing you only for the time your code actually executes. When no events arrive, you pay $0.

#### Why It Matters for IoT

A farm might have 10 sensors today and 10,000 next year. Serverless code automatically scales -- the provider runs your function in parallel for every incoming message, no matter how many. No server to provision, no capacity planning, no idle compute costs.

#### Trigger Types Used Across Modules

| Trigger Type | How It Fires | Used In | Example |
|--------------|-------------|---------|---------|
| **Event Hub trigger** | A new message arrives on IoT Hub's Event Hub endpoint | Modules 2, 3, 4 | Fires when soil moisture telemetry arrives; fires when GPS data arrives; fires when proximity sensor reports |
| **HTTP trigger** | An HTTP request (GET/POST) arrives at a URL | Module 6 | Device sends `{"text": "set a 3 minute timer"}` -> function calls LUIS -> returns `{"seconds": 180}` |

#### Key Technical Details for the Exam

- `function.json` -- configuration file defining trigger type, bindings, and settings
- `local.settings.json` -- local development settings (connection strings); never deployed, never committed to source control
- **Cardinality:** In `function.json`, must be changed from default `"many"` to `"one"` for IoT Hub triggers, and `eventHubName` set to `""` (empty) because the connection string already identifies the hub
- **Application Settings:** The cloud equivalent of `local.settings.json`; set via CLI and read by functions as environment variables

---

### 2.9 Transfer Learning (AI Without a Supercomputer)

**Appears in:** Module 4 (image classification via Custom Vision), Module 5 (object detection via Custom Vision / YOLO), Module 6 (custom speech models, voice cloning)

#### What Transfer Learning Is

Training an AI model from scratch requires millions of examples and enormous computing power (days on GPU clusters). **Transfer learning** shortcuts this: you start with a model already trained on a huge, general dataset. You then "fine-tune" only the final layer(s) using your small, specific dataset. It is like taking a person who already knows how to recognize shapes, edges, and textures and teaching them just the new labels you care about -- instead of teaching them what "vision" is from birth.

#### How It Manifests in Each Module

- **Module 4 (Image Classification):** Custom Vision's "Food" domain is a model pre-trained on food images. You upload ~30 photos of ripe bananas and ~30 of unripe bananas. Quick Training retrains only the final classification layer. Result: a classifier that works with as few as 15-30 images per category.

- **Module 5 (Object Detection):** Same principle but for drawing bounding boxes. The "Products on Shelves" domain is pre-trained on retail shelf images. You draw boxes around products in ~15-50 images. The model learns to detect and count your specific products. The lesson also references **YOLO (You Only Look Once)** -- a famous fast object detection model that can be retrained via transfer learning.

- **Module 6 (Speech & Voice):**
  - **Custom speech models:** Fine-tune a general speech-to-text model for your specific environment (noisy factory, medical vocabulary) by providing sample audio + correct transcriptions.
  - **Voice cloning:** Fine-tune a TTS model on a short audio sample of a person's voice to mimic how they speak. This is the security risk -- anyone with a few minutes of your recorded voice can impersonate you.

#### Why Transfer Learning Matters for IoT

It democratizes AI. A small team with limited data and no ML expertise can build a working classifier, object detector, or custom speech model in minutes using cloud services -- no GPU, no PhD, no million-image dataset.

---

### 2.10 Machine Learning Fundamentals: Training, Model, Prediction, and Evaluation

**Appears in:** Module 4 (image classification), Module 5 (object detection), Module 6 (speech recognition, NLU)

#### The Universal ML Pipeline

Every ML-based IoT feature follows the same three-step workflow:

1. **Training:** The algorithm studies labeled example data to learn patterns. Like studying flashcards before a test.
2. **Model:** The finished, trained "brain" -- a function that takes new input and produces output. Like the knowledge in your head after studying.
3. **Prediction:** The model's output for a new, never-before-seen input. Predictions are *probabilities* (e.g., "ripe: 99.7%"), not absolute yes/no answers -- this lets you gauge confidence and set custom thresholds.

#### Evaluating Model Quality: Precision, Recall, AP, mAP

These metrics appear in Modules 4 and 5 -- know the difference:

| Metric | Plain-Language Meaning | Appears In |
|--------|----------------------|------------|
| **Precision** | When the model says "this is X," how often is it actually right? | Modules 4, 5 |
| **Recall** | Out of all the real X in the data, how many did the model find? (Did it miss any?) | Modules 4, 5 |
| **AP (Average Precision)** | A single number summarizing overall quality for one class | Module 4 |
| **mAP (mean Average Precision)** | AP averaged across all object classes -- the summary score for object detection | Module 5 |
| **IoU (Intersection over Union)** | Measures how much two bounding boxes overlap (0-1) | Module 5 |

**Practical interpretation:**
- High precision + low recall = the model is too cautious; it misses a lot
- High recall + low precision = the model cries wolf; too many false alarms
- In food sorting, letting unripe fruit through (low precision on "ripe") is worse than occasionally re-checking a ripe one
- In stock counting, overcounting from duplicate boxes means shelves look fuller than they are -- you never restock

#### Traditional Programming vs. Machine Learning

| | Traditional Programming | Machine Learning |
|---|---|---|
| **How it works** | Human writes explicit rules ("if green -> unripe, if yellow -> ripe") | Model learns patterns from labeled examples |
| **Best for** | Simple, well-understood rules (geofence: inside vs. outside) | Visual/text complexity, subtle patterns (bruises, disease spots) |
| **Pros** | Predictable, explainable, no training data needed | Handles complexity; adapts via retraining |
| **Cons** | Cannot handle visual variation (lighting, angles, occlusion); breaks on edge cases | Needs labeled data; predictions are probabilistic; can learn spurious correlations |

---

### 2.11 Analog-to-Digital Conversion (ADC) and Digital-to-Analog Conversion

**Appears in:** Module 1 (full ADC/PWM coverage), Module 2 (ADC with soil moisture), Module 6 (PCM sampling = audio ADC)

#### The Foundational Problem

The physical world is **analog** (continuously varying). Computers are **digital** (discrete 0s and 1s). Every sensor reading, every sound wave, every light measurement must cross this divide.

#### ADC (Analog-to-Digital Converter)

A circuit that takes a smoothly varying voltage and converts it into a binary number. Key facts:
- A 10-bit ADC produces values from 0 to 1,023 (2^10 = 1,024 possible values)
- On a 3.3V board: 0V = 0, 3.3V = 1,023, 1.65V ~= 511
- Built into Arduino and Wio Terminal analog pins
- Raspberry Pi has NO native analog pins -- needs external ADC (like Grove hat)

#### PCM (Pulse Code Modulation) -- Audio's ADC

Module 6 introduces PCM as the audio equivalent of general ADC. A microphone produces an analog waveform; PCM measures (samples) the voltage at regular intervals and rounds each measurement to the nearest digital value.

**Critical numbers for the exam:**
- **Sample rate:** 16 kHz = 16,000 samples per second (adequate for speech)
- **Bit depth:** 16-bit = 65,536 possible values per sample
- **Data rate:** 16-bit x 16 kHz = 2 bytes x 16,000 = **32 KB per second**
- **Wio Terminal RAM:** 192 KB total -> fills in ~5 seconds -> cannot hold entire recording in memory -> must stream to external storage (SD card)

---

### 2.12 The Things -> Insights -> Actions Architecture

**Appears in:** Module 4 (formally introduced as a "reference architecture"), but it is the implicit structure of every module (see Section 1.3)

This is the most important *conceptual framework* in the course. When faced with an unfamiliar IoT scenario on the exam:

1. **Things:** What physical devices and sensors collect data?
2. **Insights:** Where and how is that data processed? What AI models, threshold checks, or analytics produce decisions?
3. **Actions:** What happens as a result? Commands back to devices? Alerts to humans? Dashboard updates?

If you can answer these three questions for any scenario, you understand IoT system design.

---

### 2.13 Microcontroller (MCU) vs. Single-Board Computer (SBC)

**Appears in:** Module 1 (full comparison), Module 6 (RAM limitation example)

This is the fundamental hardware choice in IoT device design. Know the full table below and be ready to recommend one over the other in a scenario question.

| Aspect | Microcontroller (Arduino/Wio Terminal) | Single-Board Computer (Raspberry Pi) |
|--------|----------------------------------------|--------------------------------------|
| **What it is** | Single-purpose chip: CPU + tiny memory + I/O pins. No OS. | Full computer on one board, running Linux. |
| **Cost** | As low as US$0.03; dev kits US$4-$30 | US$5 (Pi Zero) to US$35+ (Pi 4B) |
| **Power use** | Extremely low -- can run months/years on batteries | Higher -- needs proper power supply |
| **Speed / Memory** | Wio Terminal: 120 MHz, 192 KB RAM, 4 MB storage | Pi 4B: 1.5 GHz quad-core, 2-8 GB RAM, SD card |
| **Operating System** | No desktop OS; may use RTOS | Full Linux OS (Raspberry Pi OS) |
| **Programming** | Typically C/C++; Arduino uses setup/loop | Typically Python; wide language support |
| **Best for** | Mass-produced single-purpose devices, battery-powered, cost-sensitive | Prototyping, education, projects needing an OS or complex local processing |

---

## 3. MODULE-BY-MODULE QUICK REFERENCE

This section gives you a condensed version of each module's unique contributions -- the concepts that are *not* already covered in depth in Section 2. Use this for sequential review or to quickly orient yourself to a specific module.

---

### Module 1: Getting Started (IoT Fundamentals)

**The point:** Build the foundation -- what IoT is, what hardware it runs on, and how devices talk to the Internet.

**Unique concepts (not covered above):**

- **Kevin Ashton:** Coined "Internet of Things" in 1999.
- **Four IoT application categories:** Consumer (smart speakers, fitness trackers), Commercial (office sensors, vehicle tracking), Industrial/IIoT (factory machinery, predictive maintenance), Infrastructure (smart cities, smart power grids).
- **The Arduino Sketch Model:** `setup()` runs once at power-on (configure WiFi, pins); `loop()` runs forever (read sensor -> send data -> sleep -> repeat). This is called an **event loop** or **message loop**.
- **RTOS (Real-Time Operating System):** A lightweight OS for microcontrollers that supports multitasking, networking, and GUIs. Examples: Azure RTOS, FreeRTOS, Zephyr.
- **CounterFit:** A software tool that simulates IoT sensors and actuators on your PC so you can write and test device code without buying hardware.
- **JSON:** A text format for structured data using key/value pairs (e.g., `{"light": 143}`). Used to encode telemetry and commands. Note: JSON requires double quotes; Python dicts using single quotes are not strictly valid JSON.
- **Raspberry Pi Hat:** An add-on board that plugs into the Pi's 40 GPIO pins, adding extra capabilities like screens or sensor adapters.
- **ARM processor:** The CPU type used in Raspberry Pi, most smartphones, and Apple Silicon Macs -- different architecture from Intel/AMD x86.
- **Retained flag (MQTT):** Makes the broker store the last message on a topic and send it immediately to any new subscriber.
- **Keep alive (MQTT):** Periodically checks if the connection to the broker is still alive during quiet periods.

---

### Module 2: Farm (Digital Agriculture)

**The point:** Apply IoT to farming -- collect data, automate irrigation, then professionalize with cloud services and security.

**Unique concepts (not covered above):**

- **Growing Degree Days (GDD):** Formula: `GDD = ((T_max + T_min) / 2) - T_base`. Measures how much "heat credit" a plant earned today toward maturity. If the daily average is below the base temperature, the plant earns zero GDD (not negative).
- **Three plant temperature thresholds:** Base (minimum to grow), Optimum (fastest growth), Maximum (above this, plant stops growing).
- **Digital Agriculture / Agriculture 4.0 / Precision Agriculture:** Using sensors, AI, and cloud to make farming decisions at the individual-field level instead of relying on human observation across the whole farm.
- **Photosynthesis:** Plants use water, CO2, and light -> carbohydrates + oxygen.
- **Transpiration:** Water evaporating from leaves pulls nutrients up from roots and cools the plant (like sweating).
- **Sensor/Actuator Timing Problem:** Water takes ~20 seconds to soak through soil to reach the moisture sensor. Naive "keep pumping until sensor says wet" causes massive over-watering. Solution: the **watering cycle** -- 5s pump pulse -> 20s wait -> re-check -> repeat. Server unsubscribes from telemetry during the cycle to prevent overlapping commands.
- **Threading:** Running code in the background so the main program continues doing other things simultaneously. Used so the device can run the watering cycle while still responding to other events.
- **CSV (Comma-Separated Values):** A plain-text file format where each line is a row and commas separate values into columns. Used to store temperature readings for GDD calculation.
- **ISO 8601:** International standard date-time format (e.g., `2021-04-19T17:21:36-07:00`) that computers can reliably parse.
- **Steinhart-Hart Equation:** Mathematical formula converting electrical resistance to temperature in thermistor-based sensors. Named but never applied in the course -- likely exam-relevant only for name recognition.
- **Gravimetric vs. Volumetric Water Content:** Gravimetric = kg water per kg dry soil. Volumetric = m3 water per m3 dry soil.
- **Caesar Cipher / Vigenere Cipher / Substitution Cipher:** Historical encryption methods mentioned for context. Caesar shifts each letter by the same amount. Vigenere uses a keyword for varying shifts.
- **HSM (Hardware Security Module):** A physical chip that stores secret keys securely; code can use the keys but cannot extract the raw values.
- **Key rotation:** Switching from a compromised symmetric key to a backup while the compromised one is regenerated.
- **Self-signed certificate:** An X.509 certificate signed by its creator, not a trusted CA. OK for testing only.
- **Azurite:** A local emulator that mimics Azure Storage on your PC for testing Functions Apps without connecting to the cloud.
- **Cardinality bug fix:** Default Azure Functions template sets `cardinality: "many"`. For IoT Hub, must change to `"one"` and set `eventHubName: ""`.

---

### Module 3: Transport (GPS Tracking & Logistics)

**The point:** Track vehicles in a supply chain using GPS, store location data in the cloud, visualize it on maps, and trigger alerts with geofences.

**Unique concepts (not covered above):**

- **Supply Chain vs. Logistics:** Supply chain = entire journey from origin to customer. Logistics = the narrower job of physically moving goods.
- **Connected Vehicle:** Any vehicle with an onboard device sending location, speed, engine status, cargo temperature back to a central system over cellular networks. Enables six benefits at once: location tracking, route optimization, tax-by-mileage, driver safety, legal hours enforcement, cargo temperature surveillance.
- **Latitude and Longitude:** Latitude = north-south angle from equator (0 deg), range -90 to +90. Longitude = east-west angle from Prime Meridian (0 deg at Greenwich, England), range -180 to +180.
- **DMS vs. Decimal Degrees:** DMS = `2deg 17' 43"` (human-legible). Decimal = `2.295277 deg` (computer-ready). Conversion: `decimal = degrees + (minutes/60) + (seconds/3600)`. At the equator, 1 deg ~= 111.3 km, 1' ~= 1.855 km, 1" ~= 31 m.
- **GPS (Global Positioning System):** Network of satellites broadcasting position + precise time. Receiver triangulates its position from 3+ satellites. Fourth satellite provides altitude. Before 2000, civilian accuracy was degraded to ~5 m; after 2000, ~30 cm. Multiple constellations: USA's GPS, Russia's GLONASS, EU's Galileo, China's BeiDou, Japan's QZSS, India's NAVIC.
- **Atomic clocks** on GPS satellites must be corrected for Einstein's relativity -- time ticks 38 microseconds/day slower on the fast-moving satellites.
- **NMEA 0183:** Text-based standard for GPS sensor output. Messages are called *sentences* starting with `$`. `$GPGGA` = US GPS only; `$GNGGA` = multi-constellation. `pynmea2` library parses these into `.latitude` and `.longitude` decimal numbers.
- **NMEA coordinate format trap:** Coordinates use `(dd)dmm.mmmm` format -- the minutes portion includes decimal seconds. You MUST divide the mm.mmmm part by 60 to convert to decimal degrees. Example: `4738.538654,N` -> 47 + (38.538654 / 60) = 47.6423109 deg.
- **GeoJSON:** Standard JSON format for geographic data. **Critical trap:** coordinates are always `[longitude, latitude]` -- the opposite of spoken order. Swapping them places markers on the wrong side of the globe.
- **Azure Maps:** Microsoft's cloud mapping platform. `atlas.Map` creates a map in a webpage; `atlas.data.Point([lon, lat])` creates a point; `BubbleLayer` renders points as circles.
- **CORS (Cross-Origin Resource Sharing):** Browser security rule blocking web pages from reading data across different domains. Must be enabled on blob storage so the map webpage can fetch GPS data blobs.
- **Geofences:** Invisible digital boundaries. When a GPS-tracked device crosses one, the system triggers an action. Defined as GeoJSON Polygons (last coordinate = first to close the shape). Uploaded to Azure Maps -> returns a UDID. Each GPS reading is checked against it via the Geofence API.
- **Geofence distance values to memorize:** `999` = outside by >50 m; `0` to `50` (positive) = just outside, in the fuzzy search buffer; `-999` = inside by >50 m; `-50` to `0` (negative) = just inside, in the fuzzy zone. **Search buffer** (default 50 m) creates a fuzzy edge to handle GPS inaccuracy.
- **Consumer groups:** Independent read cursors into IoT Hub's message stream. Each application needs its own consumer group so they do not interfere. `$Default` is created automatically; create additional ones (e.g., `geofence`) as needed.
- **`enqueuedtime` vs. `datetime.now()`:** Use `event.iothub_metadata['enqueuedtime']` to timestamp GPS readings -- it records when IoT Hub received the message. Using `datetime.now()` records when the function processed it, which may be seconds/minutes later.
- **UUID:** Randomly generated unique string used as a blob filename so no two GPS readings overwrite each other.
- **`restype=container&comp=list`:** URL query parameters that tell Azure Blob Storage to return an XML list of all blobs in a container.

---

### Module 4: Manufacturing (AI-Powered Visual Inspection)

**The point:** Use cameras and AI to automatically inspect products (fruit) on a factory conveyer belt, culminating in an edge-deployed system.

**Unique concepts (not covered above):**

- **Traditional Programming vs. ML:** Traditional = human writes rules. ML = model learns patterns from labeled data.
- **Image Classifier:** An ML model that assigns a label to a whole image (e.g., "ripe banana" vs. "unripe banana"). It does not locate objects -- just classifies the entire picture.
- **Azure Custom Vision:** Cloud website + API for uploading images, tagging them, training image classifiers/object detectors, and publishing them -- no ML code required.
- **Training pipeline:** Upload labeled images -> pick a Domain (pre-trained base model) -> Quick Training uses transfer learning -> produces an Iteration (numbered model version) -> shows Precision, Recall, AP -> Publish to get a Prediction URL + Prediction-Key.
- **Domain (Custom Vision):** The base pre-trained model. `Food` for food images (cloud only). `Food (compact)` for export to edge devices.
- **Compact Model:** A smaller, exportable version that can run on an edge device (via Docker container). Standard models only run in the Custom Vision cloud.
- **Retraining:** Adding images the model got wrong (with corrected tags) and training again. The Predictions tab shows Quick Test results; re-tag incorrect ones and click Train again.
- **Camera Sensor (CMOS/APS):** A chip covered with millions of photodiodes (one per pixel). Lens focuses light onto the sensor. The most common type is CMOS -- inexpensive, low-power, ideal for IoT. High-speed protocols like SPI are needed for large image data.
- **Azure IoT Edge:** A service that deploys and manages containers on edge devices from the cloud. The device registers with `--edge-enabled` flag. You push a **deployment manifest** (JSON listing which containers to run). IoT Edge handles downloading, starting, monitoring, and updating containers.
- **Docker:** The tool for creating and managing containers. A **DockerFile** is a recipe (text file) of instructions for building a container image. A **container registry** (Azure Container Registry) stores and distributes images.
- **IoT Edge system modules:** `edgeAgent` manages lifecycle of all other modules. `edgeHub` routes messages between modules and to/from IoT Hub.
- **Decision on Device vs. Decision in Cloud:** Fundamental tradeoff. Device-side: fewer messages, lower cost, faster, but thresholds harder to change. Cloud-side: more messages, slower, but thresholds changeable instantly. **Device twin** mitigates by enabling remote threshold updates.
- **Proximity Sensor:** Measures distance via **time-of-flight** -- emits a pulse (laser, IR, ultrasonic), times the reflection. Detects when fruit arrives at the camera position.
- **Prototype vs. Production:** Prototype uses developer hardware (Pi, breadboard), hard-coded constants, direct internet, LED indicators. Production uses ruggedized hardware, device-twin configuration, internal network with edge gateway, real actuators (pneumatic pushers), and industrial protocols like OPC-UA.
- **OPC-UA:** Industrial machine-to-machine communication protocol for factory-floor device integration. Mentioned once; know it exists as an industrial IoT protocol.
- **Message schema:** The agreed structure of data fields in messages exchanged between devices and cloud services.

---

### Module 5: Retail (Object Detection for Stock Counting)

**The point:** Level up from image classification to object detection -- count items on a store shelf by drawing boxes around them and filtering out mistakes.

**Unique concepts (not covered above):**

- **Object Detection:** Finds, labels, and counts multiple individual objects in an image by drawing a **bounding box** around each one. Different from image classification, which gives one label for the whole image.
- **Bounding Box:** A rectangle described by four numbers as fractions of image dimensions: `top` (distance from top edge), `left` (distance from left edge), `height`, `width`. All between 0 and 1.
- **Normalized Coordinates (0-1):** Express bounding box positions as fractions so they work at any image resolution. `right edge = left + width`; `bottom edge = top + height`. Raw pixel coordinates change if the image is resized; normalized coordinates do not.
- **Overlapping Bounding Box Problem:** The detector sometimes draws two nearly identical boxes around the same object (one slightly inside the other) with different confidence percentages. The lower-confidence one is a **false positive** -- a duplicate that must be discarded. Without filtering, the system overcounts items and never triggers restock.
- **Overlap filtering (the 80% containment rule):** If box2's area is more than 80% inside box1, and box2 has lower confidence, discard box2.
- **IoU (Intersection over Union):** A number (0-1) measuring how much two bounding boxes overlap. The standard metric for deciding if two detections are really the same object.
- **Stock Counting Pipeline:** Take photo -> send to cloud AI -> receive list of detections -> apply probability threshold (discard < 0.5) -> remove overlapping duplicates for same tag -> count remaining items of target product -> compare to SHELF_CAPACITY -> alert if count is too low.
- **`/classify/` vs. `/detect/` API paths:** `/classify/` is the Custom Vision endpoint for image classification (returns tagName + probability). `/detect/` is the endpoint for object detection (returns tagName + probability + boundingBox).
- **Object Detector Retraining:** More labor-intensive than classifier retraining. Every predicted bounding box on every image must be manually reviewed -- confirm, resize, re-tag, or delete -- then re-run training.
- **Products on Shelves domain:** A Custom Vision domain pre-tuned for detecting products on store shelves.
- **Suggested Tags:** A Custom Vision feature where a partially-trained model auto-suggests bounding boxes on new images to speed up labeling.
- **SHELF_CAPACITY:** Known maximum items a shelf holds when fully stocked. **STOCK_TAG:** Specific product label to count.
- **Wrong stock detection:** Using object detection to find items on the wrong shelf.
- **YOLO (You Only Look Once):** A famous, very fast object detection model (20 general classes) that can be retrained via transfer learning.

---

### Module 6: Consumer (Voice-Controlled Smart Timer)

**The point:** Switch sensor modality entirely -- build a device you talk to -- by chaining speech recognition, language understanding, speech synthesis, and translation.

**Unique concepts (not covered above):**

**Microphones (the sensor for sound):**
- **Dynamic:** Magnet + coil; generates current when diaphragm moves. No external power. Reversible (can act as speaker). Live music.
- **Condenser:** Two charged plates; varying capacitance generates signal. Needs phantom power (48V). Best quality. Studio.
- **Ribbon:** Thin metal ribbon in magnetic field. Very sensitive. Vintage.
- **MEMS:** Condenser principle, but entire mic etched onto silicon chip <1 mm. Tiny, cheap. Used in phones and IoT devices.

**Digital Audio Concepts:**
- **PCM / Sampling:** Measuring analog audio voltage at regular intervals, rounding to digital numbers.
- **Sample rate:** 16 kHz adequate for speech; 48 kHz music standard; 96-192 kHz audiophile.
- **Bit depth:** 8-bit = 256 values (crunchy), 16-bit = 65,536 (speech sweet spot), 24-bit = ~16.7 million (studio).
- **Channels:** Mono = 1, Stereo = 2, 7.1 surround = 8.
- **WAV:** Uncompressed. 44-byte header + raw PCM data. Large, simple.
- **MP3:** Compressed. Smaller files. Lossy.

**Speech Recognition (STT):**
- Audio chopped into chunks -> fed into **RNN (Recurrent Neural Network)** -- remembers previous inputs to interpret the current one -> detects sound sequences -> validates as words.
- **Wake words / keyword spotting:** Local on-device TinyML listening for a specific phrase. Audio only sent to cloud after detection. Course uses button to simplify.
- **Custom speech models:** Transfer learning applied to STT -- fine-tune on your environment's audio.

**Natural Language Understanding (NLU):**
- **NLU vs. NLP:** NLP is the broad field. NLU extracts meaning and structured information from text.
- **LUIS:** Microsoft's cloud NLU service.
- **Intent:** The goal of a sentence (e.g., `set timer`).
- **Entity:** A specific piece of data extracted (e.g., `number: 3`, `time-unit: minute`).
- **Utterance:** An example sentence provided during training.
- **Prebuilt entity:** Provided out-of-the-box (e.g., `number`).
- **List entity:** Custom, with a **normalized value** (canonical form like `minute`) and **synonyms** (`minutes`, `mins`).
- **LUIS response:** Returns `topIntent`, all intents with scores, extracted entities in spoken order. Pair `number[i]` with `time-unit[i]` by index.

**Text to Speech (TTS):**
- Three-stage pipeline: Text Analysis (handle numbers, abbreviations, locale) -> Linguistic Analysis (break into phonemes, determine intonation) -> Wave-form Generation (produce audio).
- **Phoneme:** Smallest unit of sound. English has 44 phonemes from 26 letters.
- **Early TTS:** Stitched pre-recorded phoneme snippets -> robotic.
- **Neural TTS:** Deep learning generates audio from scratch -> near-human. Voice names with `Neural` suffix.
- **SSML (Speech Synthesis Markup Language):** XML-based markup controlling voice, language, speed, pitch, pauses.
- **Voice cloning risk:** Transfer learning on TTS + short audio sample -> impersonation.

**Translation:**
- **Why it is hard:** Different phrase structure, word order, proper nouns (should not translate), idioms, locale.
- **Translations are not symmetric:** English->Spanish->English may produce different sentence.
- **Machine Translation (MT):** Rule databases + statistical selection from corpora.
- **Neural Translation:** Deep learning trained end-to-end. Smaller model, whole-sentence context.
- **Intermediate language:** Pivot language when no direct pair exists. Errors accumulate.
- **Multi-language architecture:** LUIS stays English-only. Input speech translated to English before NLU; output translated from English before TTS.
- **Azure Speech Service translation:** `TranslationRecognizer` converts speech -> translated text in one step. SDK only.
- **Azure Translator Service:** Text->text via REST API. Profanity masking, custom glossaries.
- **Transliteration:** Converting word from one writing system to another by matching sounds.
- **Function key:** Security key required as `?code=` URL parameter for deployed HTTP-triggered Azure Function.
- **Daemon thread:** Background thread that auto-terminates when main program exits. Used for timer countdown.
## 4. MASTER GLOSSARY

Every term from all six modules, alphabetized, with one-line plain-language definitions. This is your multiple-choice quick-reference.

| Term | Plain-Language Definition |
|------|--------------------------|
| **Actions (architecture layer)** | What the system does with insights -- sending commands to devices, showing dashboards, triggering alerts. |
| **ADC (Analog-to-Digital Converter)** | Hardware that converts a smoothly varying (analog) voltage into a discrete digital number. |
| **Air-gapping** | Running a network completely isolated from the Internet for maximum privacy and security. |
| **Analog sensor** | A sensor that returns a continuously varying voltage proportional to what it measures. |
| **Analog signal** | A continuously varying signal, like a sound wave; opposite of a digital (discrete-step) signal. |
| **Annotations (IoT Hub)** | Extra properties automatically attached to messages (device ID, enqueue time, sequence number). |
| **Antimeridian (180th meridian)** | The line opposite the Prime Meridian on the far side of Earth; -180 deg and +180 deg are the same line. |
| **AP (Average Precision)** | A single-number metric summarizing overall model quality by averaging precision across different confidence thresholds. |
| **Application Settings** | The cloud equivalent of `local.settings.json` -- connection strings and config read by Azure Functions as environment variables. |
| **APS (Active-Pixel Sensor)** | A type of image sensor where each pixel has its own active electronic circuit. |
| **Arduino** | The most popular open-source microcontroller framework; programs are written in C/C++ using setup/loop. |
| **ARM processor** | The type of CPU used in Raspberry Pi, most smartphones, and Apple Silicon Macs -- different from Intel/AMD x86. |
| **Asymmetric encryption** | Encryption using a public key (encrypt only) and a private key (decrypt only); private key never leaves its owner. |
| **Atomic clock** | An extremely accurate clock (used inside GPS satellites) that must be corrected for relativistic time dilation. |
| **Azure Blob Storage** | Microsoft's cloud service for storing unstructured files (JSON, images, videos) organized into containers. |
| **Azure Container Registry (ACR)** | Microsoft's paid cloud service for storing Docker container images that IoT Edge devices pull from. |
| **Azure Custom Vision** | Microsoft's cloud-based tool for uploading images, tagging them, training image classifiers/object detectors, and publishing via API. |
| **Azure Functions** | Microsoft's serverless computing service -- code runs on demand without managing servers. |
| **Azure IoT Edge** | A service that deploys and manages container-based workloads on edge devices, orchestrated from IoT Hub. |
| **Azure IoT Hub** | Microsoft's managed cloud service for securely connecting, monitoring, and controlling millions of IoT devices. |
| **Azure Maps** | Microsoft's cloud platform providing maps, routing, traffic, and geofencing services. |
| **Azure Maps Web SDK** | A JavaScript library that embeds an interactive map into a web page and lets you add data layers. |
| **Azure Speech Service** | Microsoft cloud service providing speech-to-text, text-to-speech, and speech translation. |
| **Azure Translator Service** | Microsoft's cloud service for text translation via REST API; supports profanity masking and custom glossaries. |
| **Azurite** | A local emulator that mimics Azure Storage on your PC for testing Functions Apps without cloud connection. |
| **Base temperature** | The minimum daily average temperature a plant needs to grow at all. |
| **Baud rate** | The speed of a UART connection, measured in bits per second (9,600 baud is a common default). |
| **Binding (Azure Functions)** | A pre-configured connection between an Azure Function and another Azure service (input or output). |
| **Bit depth** | How many bits represent each audio sample (16-bit = 65,536 possible values); more bits = more precise sound. |
| **BLE (Bluetooth Low Energy)** | A short-range, very-low-power wireless protocol common in fitness trackers. |
| **Blob (Binary Large Object)** | Any file stored as raw bytes in cloud storage; in this course, mostly JSON documents. |
| **Blob container** | A named bucket or top-level folder in blob storage that holds blobs and sub-folders. |
| **Bounding box** | A rectangle around a detected object, defined by four numbers (top, left, height, width) as fractions of image size. |
| **Broker (MQTT)** | The central server that receives all MQTT messages and routes them to subscribers based on topics. |
| **BubbleLayer** | A map layer that renders every GeoJSON Point in its data source as a colored circle. |
| **C2D (Cloud-to-Device)** | Messages sent from a cloud application down to an IoT device (commands). |
| **Caesar Cipher** | A historical encryption method that shifts every letter by the same number of positions in the alphabet. |
| **Calibration** | Mapping a sensor's raw electrical output to a real physical measurement by comparing against known reference samples. |
| **Camera sensor** | An electronic chip covered with a grid of photodiodes that captures still images or video. |
| **Capacitive soil moisture sensor** | A sensor that measures how much electrical charge soil can store; wetter soil produces a lower voltage. |
| **Cardinality (function.json)** | Setting: `"one"` processes one event per function call; must be fixed from default `"many"` for IoT Hub triggers. |
| **Certification Authority (CA)** | A trusted organization that digitally signs X.509 certificates to verify identity. |
| **Channel (audio)** | A single independent audio stream (mono = 1, stereo = 2, 7.1 surround = 8). |
| **CIPO** | Controller Input, Peripheral Output -- the SPI wire carrying data from peripheral to controller. |
| **Clock cycle** | One tick of the CPU's internal clock; each tick, the CPU can execute one instruction. |
| **Cloud computing** | Renting computing resources (servers, storage, networking) from a large provider instead of buying your own. |
| **Cloud service** | Software running on Internet servers that processes IoT data, runs AI models, and sends commands back to devices. |
| **CMOS (Complementary Metal-Oxide Semiconductor)** | The most common and affordable type of camera sensor; inexpensive, low-power, ideal for IoT. |
| **Cognitive Services** | Microsoft's suite of pre-built cloud AI tools covering vision, speech, language, and decision-making. |
| **Cold path** | Storing data long-term in a data warehouse for historical batch analysis (yearly trends, cost optimization). |
| **Command** | A message sent from the cloud to an IoT device telling it to perform an action. |
| **Commercial IoT** | IoT used in workplaces (office occupancy sensors, retail stock monitoring, vehicle tracking). |
| **Compact model** | A smaller, exportable version of a Custom Vision model that can be downloaded and run on an edge device. |
| **Condenser microphone** | A microphone using two charged plates whose varying capacitance generates a signal; needs phantom power. |
| **Connected vehicle** | A vehicle equipped with a device that reports location and sensor data to a central IT system, typically over cellular. |
| **Connection string** | A single text string containing all credentials needed to connect to and authenticate with a cloud service. |
| **Consumer group** | An independent read cursor into IoT Hub's message stream; each consumer group has its own bookmark. |
| **Consumer IoT** | IoT products people buy for personal use at home (smart speakers, fitness trackers, smart thermostats). |
| **Container (Docker)** | A lightweight, isolated runtime environment that packages an app with all its dependencies. |
| **Container image** | A read-only template from which containers are created; includes the app code and all dependencies. |
| **Container registry** | A cloud storage service for hosting and distributing Docker container images. |
| **Container tag** | A name-and-version label on a container image (e.g., `classifier:v1`). |
| **Control circuit (relay)** | The low-voltage side of a relay (3.3V/5V from IoT device) that activates the electromagnet. |
| **COPI** | Controller Output, Peripheral Input -- the SPI wire carrying data from controller to peripheral. |
| **CORS (Cross-Origin Resource Sharing)** | A browser security mechanism that blocks cross-domain data reading unless the target server explicitly permits it. |
| **CounterFit** | A software tool that simulates IoT sensors and actuators on your PC so you can test device code without hardware. |
| **CPU (Central Processing Unit)** | The "brain" of a device that executes program instructions; speed measured in Hertz. |
| **Cryptography** | The field of techniques for encrypting and decrypting data. |
| **CSV (Comma-Separated Values)** | A plain-text file format where each line is a row and commas separate values into columns. |
| **curl** | A command-line tool for making raw HTTP requests (GET, POST, PUT) to web APIs. |
| **D2C (Device-to-Cloud)** | Messages sent from an IoT device up to the cloud (typically telemetry data). |
| **DAC (Digital-to-Analog Converter)** | Hardware that converts a binary number into a smoothly varying voltage for controlling analog actuators. |
| **Daemon thread** | A background thread that automatically terminates when the main program exits. |
| **Data visualization** | Converting raw numeric data into charts, maps, or diagrams that let a human grasp patterns at a glance. |
| **Data warehouse** | A specialized database designed to store enormous amounts of static historical data and run complex analytical queries. |
| **Decimal degrees** | A coordinate expressed as a single decimal number (e.g., 47.6423 deg) instead of separate degrees, minutes, and seconds. |
| **Decryption** | Unscrambling encrypted data back into readable form using a key. |
| **Deep learning** | A type of machine learning using very large neural networks with many layers; produces near-human quality TTS. |
| **Deployment manifest** | A JSON document that specifies which container images each IoT Edge device should run. |
| **Developer kit** | A general-purpose IoT board designed for prototyping, with extra pins and features not found in final products. |
| **Device twin** | A JSON document in IoT Hub holding desired and reported state for a device, enabling remote configuration. |
| **DHT11** | A combined digital humidity and temperature sensor; in CounterFit simulated as two separate virtual sensors. |
| **Digital agriculture / Agriculture 4.0** | Using data-collection tools (sensors, AI, cloud) to make farming decisions instead of relying on human observation. |
| **Digital sensor** | A sensor that returns either 0/1 (two states) or a binary number via a built-in ADC. |
| **Direct method** | A cloud-to-device command that requires the device to send back a response confirming whether it succeeded. |
| **DMS (Degrees, Minutes, Seconds)** | The traditional way of writing coordinates (e.g., 2 deg 17' 43"). |
| **Docker** | The most popular tool for building, sharing, and running containers. |
| **DockerFile** | A text recipe file with step-by-step instructions for building a Docker container image. |
| **Domain (Custom Vision)** | The base pre-trained model you choose (e.g., Food, General, Landmarks) that best matches your use case. |
| **DOMParser** | A JavaScript API for parsing XML or HTML text into a tree structure that code can navigate and query. |
| **Duty cycle** | The percentage of time a PWM signal stays on during one on-off cycle. |
| **Dynamic microphone** | A microphone using a moving magnet and coil to generate current; needs no external power; reversible. |
| **Eclipse Mosquitto** | A free, open-source MQTT broker; also provides the public test broker at `test.mosquitto.org`. |
| **Edge computing** | Processing IoT data on a local network device rather than sending everything to the cloud over the Internet. |
| **Edge device** | A device that processes sensor data locally or acts as a local hub; can operate offline. |
| **edgeAgent** | The IoT Edge system module that manages the lifecycle (install, start, stop, update) of all other modules. |
| **edgeHub** | The IoT Edge system module that routes messages between modules and to/from IoT Hub. |
| **Electromagnet** | A temporary magnet created by passing electricity through a wire coil; magnetized only when current flows. |
| **Encryption** | Scrambling readable data into unreadable gibberish using a secret key. |
| **Encryption key** | A secret value (like a very long password) used to scramble or unscramble data. |
| **Entity (LUIS)** | A specific piece of data extracted from a sentence (e.g., `number: 3`, `time-unit: minute`). |
| **Event Hub trigger** | An Azure Functions binding that fires every time a new message arrives on an IoT Hub endpoint. |
| **Event loop / Message loop** | A program structure where a main loop repeatedly checks for new input and responds to it. |
| **F1 Tier** | IoT Hub's free tier: 8,000 messages per day, maximum one per subscription. |
| **False positive** | A detection the model made that does not correspond to any real object in the image. |
| **FeatureCollection (GeoJSON)** | The top-level GeoJSON wrapper object holding an array of `Feature` objects. |
| **Fetch-decode-execute cycle** | The three-step loop a CPU repeats every clock tick: grab instruction, decode meaning, execute. |
| **Food (compact) domain** | The exportable version of the Food Custom Vision domain; used when deploying to IoT Edge. |
| **Food domain** | A Custom Vision base model pre-trained on food images; the right choice for fruit classification. |
| **Full-duplex** | Communication where data can flow in both directions simultaneously on separate wires. |
| **Function key** | A security key required as `?code=` URL parameter to call a deployed HTTP-triggered Azure Function. |
| **Gateway device** | An edge device that bridges incompatible or insecure devices to a wider network or IoT Hub. |
| **GDD (Growing Degree Days)** | A daily number representing how much "heat credit" a plant earned toward maturity; calculated from temperature data. |
| **GeoJSON** | An open standard JSON format for encoding geographic data -- points, lines, polygons, and feature collections. |
| **GeoJSON Polygon** | A closed shape defined as an array of `[lon, lat]` coordinate pairs where the last equals the first. |
| **Geofence** | A virtual perimeter (circle or polygon) drawn around a real-world location; crossing it triggers a programmed action. |
| **Geospatial coordinates** | A pair of numbers (latitude and longitude) that uniquely identify one point on Earth's surface. |
| **GGA sentence** | The NMEA message type that carries GPS Fix Data -- latitude, longitude, altitude, and satellite count. |
| **GPIO (General-Purpose Input/Output)** | Programmable metal pins on an IoT board that can be set to read a voltage (input) or send one (output). |
| **GPS (Global Positioning System)** | A satellite network enabling a receiver on Earth to calculate its exact position by triangulating signals. |
| **GPS constellation** | A named group of positioning satellites operated by one country (GPS=USA, GLONASS=Russia, Galileo=EU, BeiDou=China). |
| **GPS satellite** | An orbiting spacecraft continuously broadcasting its own position and an extremely precise timestamp via radio waves. |
| **Gravimetric water content** | Soil moisture measured as kilograms of water per kilogram of dry soil. |
| **GSV sentence** | The NMEA message type that lists details of every satellite currently visible to the receiver. |
| **Hat (Raspberry Pi)** | An add-on board that plugs into the Pi's 40 GPIO pins, adding extra capabilities like screens or sensor adapters. |
| **Hertz (Hz)** | Unit of CPU speed; 1 Hz = 1 cycle per second. 1 MHz = 1 million Hz, 1 GHz = 1 billion Hz. |
| **Hot path** | Processing data immediately in real time, used for alerts and urgent responses. |
| **HSM (Hardware Security Module)** | A physical chip on a device that stores secret keys securely; code can use but cannot extract the raw key values. |
| **HTTP 200** | The standard HTTP status code meaning "success." |
| **HTTP 404** | The standard HTTP status code meaning "not found." |
| **HTTP trigger** | An Azure Functions trigger type; the function executes when it receives an HTTP request. |
| **I2C (Inter-Integrated Circuit)** | A protocol where one controller talks to multiple peripherals over two shared wires (SDA + SCL), using device addresses. |
| **Idiom** | A phrase whose overall meaning cannot be derived by translating each word literally. |
| **IIoT (Industrial IoT)** | IoT used to control and monitor factory machinery at large scale, including predictive maintenance. |
| **Image classification** | AI technique that assigns a single label (and confidence) to an entire image without locating anything inside it. |
| **Image classifier** | An ML model that assigns a label (class) to an image based on its visual content. |
| **Infrastructure IoT** | IoT used to manage public systems -- smart cities (air quality) and smart power grids. |
| **Insights (architecture layer)** | The analysis layer that processes data, runs AI models, and produces decisions. |
| **Intent (LUIS)** | The goal or purpose of a user's sentence (e.g., `set timer`). |
| **Intermediate language (translation)** | A pivot language used when no direct language pair exists. |
| **Intonation** | The rise and fall of pitch in speech -- distinguishes a question (rising) from a statement (level). |
| **IoU (Intersection over Union)** | A number (0-1) measuring how much two bounding boxes overlap; used to determine if two detections are the same object. |
| **IoT (Internet of Things)** | Connecting everyday physical objects to the Internet so they can send sensor data and/or receive commands. |
| **ISO 8601** | An international standard format for writing dates and times computers can reliably read. |
| **Iteration (Custom Vision)** | A specific numbered version of a trained model; each training run creates a new iteration. |
| **JSON (JavaScript Object Notation)** | A simple text format for structured data using key/value pairs, used to encode telemetry and commands. |
| **Keep alive (MQTT)** | An MQTT feature that periodically checks if the connection to the broker is still alive during quiet periods. |
| **Kevin Ashton** | The person who coined the term "Internet of Things" in 1999. |
| **Key rotation** | Switching from a compromised symmetric key to a backup key while the compromised one is regenerated. |
| **Keyword spotting** | Synonym for wake word detection -- listening locally for a specific trigger phrase. |
| **Language pair (translation)** | A specific source->target translation direction (e.g., English->Spanish); not all pairs have direct support. |
| **Latitude** | The north-south angle measured from the equator (0 deg), ranging from -90 deg (South Pole) to +90 deg (North Pole). |
| **LED (Light-Emitting Diode)** | A simple digital actuator that lights up when it receives a digital "1" (HIGH) signal. |
| **Lens (camera)** | A curved glass/plastic element that focuses light from the scene onto the camera sensor. |
| **List entity (LUIS)** | A custom entity defined as a list of normalized values each with synonyms. |
| **Locale** | A language variant tied to a specific country/region (e.g., `en-GB` vs. `en-US`). |
| **Logistics** | The specific process of physically moving goods from one location to another (by truck, ship, or plane). |
| **Longitude** | The east-west angle measured from the Prime Meridian (0 deg at Greenwich), ranging from -180 deg to +180 deg. |
| **LoRaWAN (Long Range, Low Power)** | A wireless protocol for sending small data over kilometers; common in commercial farm sensors. |
| **LUIS (Language Understanding Intelligent Service)** | Microsoft's cloud service for training and querying NLU models. |
| **Machine learning (ML)** | A technique where a computer learns patterns from labeled examples rather than following hand-written rules. |
| **Machine Translation (MT)** | Traditional computer translation using rule databases and statistical selection from human-translated corpora. |
| **Mains electricity** | The high-voltage power delivered to homes and businesses through the national grid (230V/120V/100V). |
| **mAP (mean Average Precision)** | A single summary score for object detection quality, averaged across all object types. |
| **Maximum temperature (plants)** | The daily average temperature above which a plant stops growing to conserve water. |
| **MEMS microphone** | A microphone etched onto a silicon chip (Microelectromechanical Systems); tiny, used in phones and IoT devices. |
| **Meridian** | Any imaginary semicircle running from North Pole to South Pole; lines of constant longitude. |
| **Mesh network** | A network where each device connects to multiple nearby devices and messages hop from one to another. |
| **Message schema** | The agreed structure of data fields in messages exchanged between devices and cloud services. |
| **Microcontroller (MCU)** | A tiny, cheap, single-purpose computer on a chip with CPU, memory, and I/O pins; runs one program on bare metal. |
| **Microphone** | An analog sensor that converts sound waves (air vibrations) into electrical signals. |
| **Mirai Botnet** | A 2016 attack that took over thousands of IoT devices using default passwords to launch a massive internet disruption. |
| **Model (ML)** | The finished, trained result of ML -- a function that accepts new input and produces a prediction. |
| **Module (IoT Edge)** | A software unit (Docker container) deployed to an IoT Edge device. |
| **MP3** | A compressed audio format; much smaller files than WAV at similar perceived quality. |
| **MQTT (Message Queuing Telemetry Transport)** | The most popular IoT messaging protocol; uses a central broker and publish/subscribe topics. |
| **Neural Translation** | AI-based translation using deep learning models trained on large human-translated datasets. |
| **Neural voice** | A TTS voice generated by a deep learning model (suffix `Neural`); the most natural-sounding type. |
| **NLU (Natural Language Understanding)** | The subfield of NLP focused on extracting meaning, intent, and structured information from text. |
| **NLP (Natural Language Processing)** | The broad field of AI dealing with understanding, generating, and working with human language. |
| **NMEA 0183** | A text-based standard defining how GPS sensor output messages (sentences) are formatted. |
| **NMEA sentence** | One message from a GPS sensor, starting with `$`, containing a source code, type code, and data fields. |
| **Normalized coordinates** | Bounding box measurements expressed as 0-1 fractions of image dimensions, independent of pixel resolution. |
| **Normalized value (LUIS)** | The canonical form of a list entity (e.g., `minute`); all synonyms map back to this single value. |
| **NoSQL database** | A database that stores documents (usually JSON) without a predefined schema; different documents can have different fields. |
| **NTP (Network Time Protocol)** | A protocol for keeping a device's clock accurate over the Internet; needed because SAS tokens expire based on time. |
| **Object detection** | AI technique that finds, labels, and counts multiple objects in an image by drawing bounding boxes around each. |
| **OPC-UA** | An industrial machine-to-machine communication protocol used for factory-floor device integration. |
| **Optimum temperature** | The daily average temperature at which a plant grows fastest. |
| **Output circuit (relay)** | The high-voltage side of a relay (up to 250V/10A) that powers the connected device. |
| **Overlapping bounding boxes** | Two predicted boxes for the same object where one sits mostly inside the other; the lower-confidence one is a duplicate. |
| **paho-mqtt** | A Python library (`pip install paho-mqtt`) for connecting to and using MQTT. |
| **Partition** | A separate stream of data in IoT Hub; more partitions reduce bottlenecks when many services read simultaneously. |
| **PCM (Pulse Code Modulation)** | The standard technique for digital audio: measure voltage -> round to nearest value -> store as bits. |
| **Phantom power** | The external electrical power (usually 48V) required by condenser microphones to operate. |
| **Phoneme** | The smallest distinct unit of sound in a language; English has 44 phonemes from 26 letters. |
| **Photodiode** | A tiny semiconductor component that converts incoming light into an electrical signal; one per pixel in a camera. |
| **Photosynthesis** | The process where plants combine water, CO2, and light to produce their own food (carbohydrates) and release oxygen. |
| **Potentiometer** | A rotating dial sensor; the returned voltage depends on the dial's position. |
| **Prebuilt entity (LUIS)** | An entity type that LUIS provides out-of-the-box with no training required (e.g., `number`, `datetime`). |
| **Precision** | Of all items the model labeled as a given class, the fraction that were actually correct. |
| **Precision agriculture** | Observing and responding to crops at the individual-field level rather than treating the whole farm uniformly. |
| **Prediction (ML)** | The output of an ML model for new input, expressed as probabilities that sum to 1 (not a yes/no). |
| **Prediction URL** | The web endpoint where published Custom Vision models accept image classification/detection requests. |
| **Prediction-Key** | A secret string sent in the HTTP header to authenticate Custom Vision prediction API calls. |
| **Prime Meridian** | The 0 deg longitude line through the Royal Observatory in Greenwich, England, established in 1884. |
| **Private key** | The secret key in asymmetric encryption that only the owner has; can decrypt data encrypted with the matching public key. |
| **Probability threshold** | A minimum confidence cutoff (e.g., 0.5) below which ML predictions are thrown away as unreliable. |
| **Products on Shelves domain** | A pre-tuned Custom Vision domain specifically designed for detecting retail products on store shelves. |
| **Profanity masking** | A Translator service feature that detects and replaces or removes profane words in translations. |
| **Program memory** | Non-volatile storage on a microcontroller that holds your code; survives power-off. |
| **Proximity sensor** | A sensor that measures distance to an object by emitting a signal and timing its reflection (time-of-flight). |
| **Public key** | The key in asymmetric encryption that anyone can use to encrypt data; cannot decrypt. |
| **Publish (MQTT/Custom Vision)** | MQTT: to send a message to a topic. Custom Vision: to make a model iteration available for API calls. |
| **Publish/Subscribe (pub/sub)** | A messaging pattern where senders and receivers are decoupled -- they communicate through named topics on a broker. |
| **PWM (Pulse-Width Modulation)** | A technique that simulates an analog signal by rapidly pulsing a digital signal on and off at a variable duty cycle. |
| **pynmea2** | A Python library that parses raw NMEA sentences into objects with `.latitude` and `.longitude` attributes. |
| **QoS (Quality of Service)** | An MQTT guarantee level: 0 (at most once), 1 (at least once), 2 (exactly once). |
| **Quick Training** | Custom Vision's fast training mode that uses transfer learning on the selected domain. |
| **RAM (Random-Access Memory)** | Volatile, fast memory used while a program runs; all contents lost when power is removed. |
| **Raspberry Pi** | The most popular single-board computer; runs Linux, starts at US$5 (Zero) to US$35 (Pi 4). |
| **Raspberry Pi OS** | A version of Debian Linux that runs on all Raspberry Pi models. |
| **Recall** | Of all items that truly belong to a class, the fraction the model successfully found. |
| **Reference IoT architecture** | A design template organizing any IoT system into three layers: Things, Insights, Actions. |
| **Registry Manager (IoT Hub)** | A cloud-side tool for viewing registered devices, sending C2D messages, invoking direct methods, and updating twins. |
| **Relay** | An electromechanical switch: a small current activates an internal magnet that pulls a lever to close a separate high-power circuit. |
| **Resistive soil moisture sensor** | Two metal probes that measure how easily electricity flows through soil; wetter soil conducts better (lower resistance). |
| **Resource (Azure)** | Any individual cloud service you create (IoT Hub, virtual machine, database, etc.). |
| **Resource group (Azure)** | A logical container that groups related Azure resources; deleting the group deletes everything inside it. |
| **Restock notification** | An alert sent to staff or a robot when detected item count falls below SHELF_CAPACITY. |
| **Retained flag (MQTT)** | Makes the broker store the last message on a topic and send it immediately to any new subscriber. |
| **Retraining** | Adding images the model got wrong (corrected) to the training set and training again to improve accuracy. |
| **Ribbon microphone** | A microphone using a thin metal ribbon vibrating in a magnetic field; very sensitive, vintage. |
| **RNN (Recurrent Neural Network)** | A type of ML model that uses data from previous steps to inform decisions about the current step; used in speech recognition. |
| **RSA (Rivest-Shamir-Adleman)** | The most widely used mathematical algorithm for generating public/private key pairs. |
| **RTOS (Real-Time Operating System)** | A lightweight OS for microcontrollers that supports multitasking, networking, and GUIs. |
| **Ruggedized hardware** | Electronics designed to survive harsh industrial conditions (heat, vibration, noise, dust). |
| **Sample rate** | How many audio samples are taken per second, measured in kHz (e.g., 16 kHz = 16,000 samples/second). |
| **Sampling (audio)** | Measuring an analog signal at regular time intervals and converting each measurement to a digital number. |
| **SAS token (Shared Access Signature)** | A one-time-use token: contains hub URL, expiry time, and a cryptographic signature proving the device knows the key. |
| **SAS token expiry** | A time limit on a SAS token (usually 1 day) preventing attackers from saving and reusing an old token. |
| **SBC (Single-Board Computer)** | A full computer on one board, running an OS like Linux, with GPIO pins (e.g., Raspberry Pi). |
| **SCL** | The clock wire in an I2C connection. |
| **SDA** | The data wire in an I2C connection. |
| **Search buffer (geofence)** | The fuzzy distance zone (0-500 m, default 50 m) around a geofence edge to handle GPS inaccuracy. |
| **Self-signed certificate** | An X.509 certificate signed by its own creator instead of a trusted CA; acceptable only for testing. |
| **Semi-structured data** | Data with some organization but not fitting rigid tables (e.g., JSON with some shared and some varying fields). |
| **Sensor** | Hardware that measures a physical property and converts it into an electrical signal a computer can read. |
| **Sensor/actuator timing** | The delay between activating a device (e.g., pump) and the sensor detecting the resulting physical change. |
| **Serverless / FaaS (Functions as a Service)** | A cloud model where code runs only when triggered by an event; no server to manage, pay only per execution. |
| **Sexagesimal (base-60)** | The ancient Babylonian numbering system inherited by degrees/minutes/seconds -- 60 minutes per degree, 60 seconds per minute. |
| **SharedAccessKey** | The secret password component of an IoT Hub connection string; identical copies on device and in IoT Hub. |
| **SHELF_CAPACITY** | The known maximum number of items a shelf section can hold when fully stocked. |
| **Sketch (Arduino)** | An Arduino program consisting of `setup()` (runs once) and `loop()` (runs forever). |
| **SKU (Stock Keeping Unit)** | The pricing tier of an Azure service (e.g., F1 = free tier, S1 = standard tier). |
| **Smart City** | An urban area that uses IoT sensors to collect data and improve city operations (traffic, pollution, energy). |
| **Smart power grid** | A power grid gathering usage data at the individual-house level to optimize energy production and distribution. |
| **SPI (Serial Peripheral Interface)** | A controller-peripheral protocol using four wires (COPI, CIPO, SCLK, CS); full-duplex and fast. |
| **SQL database (RDBMS)** | A relational database where data lives in predefined tables with named columns and relationships; queried with SQL. |
| **SSML (Speech Synthesis Markup Language)** | An XML-based markup language controlling TTS output (language, voice, speed, pitch, pauses, emphasis). |
| **Staging slot (LUIS)** | A LUIS deployment environment used for testing before promoting the model to production. |
| **Statistical Machine Translation** | A translation method using statistical models trained on large collections of human-translated parallel text. |
| **Steinhart-Hart Equation** | The mathematical formula converting electrical resistance to temperature in thermistor-based sensors. |
| **Stepper motor** | An actuator that rotates in precise, fixed-angle steps based on electrical pulses. |
| **STOCK_TAG** | The specific product label to count among all detections (e.g., "tomato paste"). |
| **Stock counting** | Using object detection to count how many items of a specific product are visible on a shelf. |
| **Structured data** | Data with a fixed, unchanging format mapping neatly to database tables with predefined columns. |
| **STT (Speech to Text)** | The AI-powered process of converting spoken audio into written text. |
| **Stuxnet** | A computer worm that destroyed centrifuges by manipulating their valves -- the go-to example of why IoT security matters. |
| **Subscribe (MQTT)** | To tell the broker you want to receive all messages sent to a particular topic. |
| **Substitution cipher** | A historical encryption method where each letter is replaced by a different letter according to a fixed rule. |
| **Suggested tags (Custom Vision)** | A feature where a partially-trained model auto-suggests bounding boxes on new images to speed up labeling. |
| **Supervised learning** | ML training requiring each training example to have a correct label. |
| **Supply chain** | The full journey of a product from its origin (farm/factory) to the final customer, including all transport and storage. |
| **Symmetric encryption** | Encryption where the same key both encrypts and decrypts; faster but requires sharing the key securely. |
| **Synonym (LUIS)** | An alternative string mapped to a normalized value in a list entity (e.g., `"minutes"` -> `minute`). |
| **Tag (Custom Vision)** | A class label applied to a training image (e.g., `ripe`, `unripe`). |
| **Telemetry** | Sensor data sent from an IoT device to the cloud (from Greek for "measure remotely"). |
| **Thermistor** | A resistor whose resistance changes with temperature; used in analog temperature sensors. |
| **Things (architecture layer)** | The physical devices and sensors that gather data from the real world. |
| **Threading** | Running a piece of code in the background so the main program can continue doing other things simultaneously. |
| **Threshold** | A pre-set value that triggers an action when a sensor reading crosses it. |
| **Tight bounding box** | A bounding box drawn as close as possible to the edges of the object, without including excess background. |
| **Time-of-flight** | The technique of measuring distance by calculating the round-trip time of a reflected signal (light or sound). |
| **TinyML** | Techniques for compressing machine learning models to run on microcontrollers with tiny amounts of memory and battery. |
| **Topic (MQTT)** | A named channel used to route messages between publishers and subscribers. |
| **Top intent (LUIS)** | The intent with the highest confidence score for a given utterance. |
| **Training (ML)** | The process of an ML algorithm studying labeled data to learn patterns. |
| **Training data** | Input-output example pairs (e.g., photos + correct labels) used to train an ML model. |
| **Transfer learning** | Starting from a model already trained on a huge dataset, then re-training only its final layer on a small new dataset. |
| **Translation (Azure Speech Service)** | Simultaneous speech recognition + translation to another language in one step; SDK only. |
| **Transliteration** | Converting a word from one writing system to another by matching sounds rather than meaning. |
| **Transpiration** | Water evaporating from a plant's leaves, which pulls nutrients upward and cools the plant. |
| **Triangulation** | Determining your location by measuring distance from at least three known reference points (satellites). |
| **Trigger (Azure Functions)** | A function inside a Functions App that fires automatically when a specific type of event occurs. |
| **TTS (Text to Speech) / Speech synthesis** | The process of converting written text into spoken audio. |
| **UART (Universal Asynchronous Receiver-Transmitter)** | A direct two-device serial connection using Tx/Rx cross-connected wires and an agreed baud rate. |
| **UDID (Unique Data ID)** | The identifier returned by Azure Maps after uploading a geofence file; used in all subsequent API calls. |
| **UNIX Time** | A timestamp format counting seconds since midnight January 1, 1970 (UTC). |
| **Unstructured data** | Data without a consistent format -- each record may have different fields and types. |
| **Unsubscribe (MQTT)** | Telling the broker to stop forwarding messages on a topic. |
| **Unsupervised learning** | ML training that does not use labels -- the algorithm finds patterns on its own. |
| **Utterance** | An example sentence provided during training to teach LUIS what a particular intent looks like. |
| **UUID (Universally Unique Identifier)** | A randomly generated string used as a unique filename so no two records overwrite each other. |
| **Vigenere Cipher** | A substitution cipher using a keyword so each letter is shifted by a different amount, harder to break. |
| **Virtual environment (Python)** | An isolated copy of Python in its own folder so installed packages do not conflict across projects. |
| **Voice cloning** | Using transfer learning to train a TTS model to mimic a specific person's voice from a short audio sample. |
| **Voltage** | A measure of how strongly electricity is being "pushed" through a circuit. |
| **Volumetric water content** | Soil moisture measured as cubic meters of water per cubic meter of dry soil. |
| **Wake word** | A specific keyword ("Alexa," "Hey Siri") that a device listens for locally to trigger cloud-based speech recognition. |
| **Warm path** | Processing data shortly after it arrives, used for dashboards, reports, and short-term analytics. |
| **Watering cycle** | A defined sequence: pump on for a short pulse -> pump off -> wait for water to soak -> re-check moisture. |
| **WAV** | An uncompressed audio file format: 44-byte header followed by raw PCM audio bytes. |
| **Workload** | Any service that performs computing work -- AI models, applications, serverless functions. |
| **Wrong stock detection** | Using object detection to spot items on the wrong shelf (e.g., baby corn on the tomato paste shelf). |
| **X.509 Certificate** | A digital document containing a public key, signed by a trusted authority to prove the key belongs to the claimed owner. |
| **XMLHttpRequest** | A legacy JavaScript API for making HTTP requests; used in Module 3 to fetch blob JSON files. |
| **YOLO (You Only Look Once)** | A famous, very fast object detection model that can recognise 20 classes of everyday objects in real time. |
| **ZDA sentence** | The NMEA message type that carries the current date and time, including the local time zone. |
| **Zigbee** | A wireless mesh-networking protocol where devices relay messages for each other to reach a coordinator. |
## 5. COMPARISON TABLE BANK

Every X-vs-Y comparison from all six modules, consolidated into one reference organized by topic. These are classic writing-question material.

### 5.1 Hardware & Device Architecture

#### MCU vs. SBC (Module 1)

| Aspect | Microcontroller (Arduino/Wio Terminal) | Single-Board Computer (Raspberry Pi) |
|--------|----------------------------------------|--------------------------------------|
| **What it is** | Single-purpose chip: CPU + tiny memory + I/O pins. No OS. | Full computer on one board running Linux. |
| **Cost** | As low as US$0.03; dev kits US$4-$30 | US$5 (Pi Zero) to US$35+ (Pi 4B) |
| **Power use** | Extremely low (months/years on batteries) | Higher (needs proper power supply) |
| **Speed / Memory** | Wio Terminal: 120 MHz, 192 KB RAM, 4 MB storage | Pi 4B: 1.5 GHz quad-core, 2-8 GB RAM, SD card |
| **OS** | None (or lightweight RTOS) | Full Linux (Raspberry Pi OS) |
| **Programming** | C/C++; Arduino setup/loop pattern | Python; wide language support |
| **Best for** | Mass-produced single-purpose, battery-powered, cost-sensitive devices | Prototyping, education, projects needing an OS |

#### Prototype vs. Production (Module 4)

| | Prototype | Production |
|---|---|---|
| **Hardware** | Developer kit (Pi, breadboard) | Ruggedized (withstands heat, vibration, noise) |
| **Connectivity** | Direct internet from each device | Internal network; edge gateway; only aggregate data to cloud |
| **Configuration** | Hard-coded constants | Configurable via device twins |
| **Actuators** | LED indicators | Mechanical actuators (pneumatic pushers, gates) |
| **Industrial protocol** | Not used | OPC-UA for machine-to-machine communication |

### 5.2 Processing Location

#### Edge Processing vs. Cloud Processing (Modules 1, 4, 6)

| | Edge Processing | Cloud Processing |
|---|---|---|
| **What it is** | Processing on a local device near the sensors | Processing on remote servers in a data center |
| **Speed / Latency** | Instant (no network delay) | Depends on Internet speed (28ms+ transatlantic) |
| **Offline capability** | Works without Internet | Fails without Internet |
| **Privacy** | Data stays local | Data leaves the local network |
| **Computing power** | Limited (small device) | Massive (data centers with AI/ML) |
| **Scalability** | Limited -- must buy more hardware | Auto-scales instantly |
| **Maintenance** | You maintain hardware | Provider maintains hardware |
| **Best for** | Real-time, privacy-critical, remote locations, high-bandwidth data (video) | Complex analytics, AI training, cross-device coordination, long-term storage |

#### Decision on Device vs. Decision in Cloud (Module 4)

| | Decision on Device | Decision in Cloud |
|---|---|---|
| **What it is** | Device checks threshold locally; only sends messages when events occur | Device sends all raw readings; cloud checks thresholds |
| **Pros** | Fewer messages -> lower cost, faster response | Threshold changeable instantly without touching firmware |
| **Cons** | Changing threshold requires device twin or firmware update | More messages -> higher cost, slower response |
| **Mitigation** | **Device twin** enables remote threshold updates -- best of both | N/A |

### 5.3 Sensors

#### Analog vs. Digital Sensors (Module 1)

| | Analog Sensor | Digital Sensor |
|---|---|---|
| **Output** | Continuously varying voltage | 0/1 or binary number (via built-in ADC) |
| **Conversion needed** | Needs external ADC between sensor and device | May handle conversion internally |
| **Granularity** | Full range of values | Simple: on/off; advanced: fine-grained via internal ADC |
| **Example** | Light sensor (0-1023) via Grove hat ADC | Button (0 or 1); DHT11 (digital temp+humidity) |

#### Resistive vs. Capacitive Soil Moisture Sensors (Module 2)

| | Resistive | Capacitive |
|---|---|---|
| **How it works** | Two metal probes; electricity flows through water between them | Measures electrical field / charge storage of soil |
| **Moisture -> reading** | More water -> lower resistance -> **higher** voltage | More water -> **lower** voltage |
| **Durability** | Probes corrode from electrical current | No exposed metal; more durable |
| **Cost** | Cheaper | More expensive |
| **CounterFit** | Not simulated | Yes (virtual sensor simulates capacitive behavior) |

#### GPIO vs. Analog Pins (Module 2)

| | GPIO (Digital Only) | Analog Pins |
|---|---|---|
| **What they read** | Only ON (1) or OFF (0) | Range of values (0-1,023 at 10-bit) |
| **ADC built in?** | No -- external ADC needed | Yes -- ADC integrated |
| **Where found** | Raspberry Pi, Wio Terminal, Arduino | Wio Terminal, Arduino; NOT on Raspberry Pi natively |

#### Microphone Types (Module 6)

| | Dynamic | Condenser | MEMS |
|---|---|---|---|
| **Needs power?** | No | Yes (phantom 48V) | Yes |
| **Size** | Large | Medium | Tiny (on a chip) |
| **Sound quality** | Good (live use) | Best (studio) | Adequate (speech) |
| **IoT suitability** | Poor (size) | Poor (power/size) | **Best** |
| **Reversible?** | Yes (can be a speaker) | No | No |

### 5.4 Signal Processing

#### PWM vs. True Analog / DAC (Module 1)

| | PWM (Pulse-Width Modulation) | True Analog (DAC) |
|---|---|---|
| **What it does** | Simulates analog with rapid on/off pulses | Produces genuine smooth varying voltage |
| **Hardware needed** | Standard digital pin | Dedicated DAC circuit |
| **Output** | Square wave; average power varies with duty cycle | Smooth, continuous voltage level |
| **Example** | Controlling motor speed (75-150 RPM) via variable duty cycle | A dimmable light following exact voltage |

#### Audio Bit Depth Comparison (Module 6)

| Bit Depth | Values | Sound Quality | Use |
|---|---|---|---|
| **8-bit** | 256 (-128 to +127) | Crunchy, distorted | Old video-game audio, LoFi aesthetic |
| **16-bit** | 65,536 (-32,768 to +32,767) | Good -- speech recognition sweet spot | Consumer audio, this course |
| **24-bit** | ~16.7 million | Studio/mastering quality | Professional recording |

### 5.5 Connectivity Protocols

#### I2C vs. UART vs. SPI (Module 2)

| | I2C | UART | SPI |
|---|---|---|---|
| **Number of devices** | Multiple controllers + multiple peripherals | Exactly 2 | 1 controller + multiple peripherals |
| **Wires** | 2 shared (SDA + SCL) + power | 2 (Tx<->Rx) per pair | 4 (COPI, CIPO, SCLK, CS); +1 CS per peripheral |
| **Identification** | Hard-coded address per peripheral | Only two devices | CS wire wakes one at a time |
| **Speed** | Standard 100 Kbps; Fast 400 Kbps; High Speed 3.4 Mbps | Up to ~6.5 Mbps | No defined limit; often multiple MB/s |
| **Clock** | Yes (SCL) | No -- relies on baud rate | Yes (SCLK) |
| **Framing** | Start/stop conditions | Start + stop bits per byte | None (clock-synced) |
| **Full-duplex?** | No | Typically half-duplex | **Yes** |
| **Example use** | Multiple sensors on a board | GPS modules, serial consoles | Flash memory, cameras, fast sensors |

#### Wireless Protocols for IoT (Module 2)

| | BLE | LoRaWAN | WiFi | Zigbee |
|---|---|---|---|---|
| **Range** | Short (meters) | Long (kilometers) | Medium (tens of meters) | Medium (tens to hundreds) |
| **Power** | Very low | Very low | Higher | Low |
| **Topology** | Point-to-point or star | Star (devices -> hub) | Star (devices -> AP) | Mesh (devices relay) |
| **IoT farm use** | No (too short) | **Yes** -- commercial sensors | Maybe (if WiFi covers field) | Yes -- mesh covers large areas |

#### MQTT QoS Levels (Module 1)

| QoS | Name | Guarantee | Use When |
|-----|------|-----------|----------|
| **0** | At most once | Sent once, no acknowledgement | Routine telemetry; occasional loss acceptable |
| **1** | At least once | Re-sent until acknowledged; duplicates possible | Important data; missing worse than duplicates |
| **2** | Exactly once | Two-step handshake; no duplicates, no loss | Critical commands (emergency shutdown) |

### 5.6 IoT Hub Communication Modes

#### Public MQTT Broker vs. Azure IoT Hub (Module 2)

| | Public MQTT Broker | Azure IoT Hub |
|---|---|---|
| **Reliability** | No guarantees; can go offline | Professionally maintained; uptime SLA |
| **Security** | Anyone can publish/subscribe | Only registered devices with valid keys/certificates |
| **Performance** | Not designed for scale | Millions of messages/day |
| **Discovery** | No device registry | Built-in registry |
| **Cost** | Free | Free tier: 8,000 messages/day |

#### D2C vs. C2D vs. Direct Method vs. Device Twin (Module 2)

| | D2C | C2D | Direct Method | Device Twin |
|---|---|---|---|---|
| **Direction** | Device -> Cloud | Cloud -> Device | Cloud -> Device | Both ways |
| **Response required?** | No | No | **Yes** | N/A (auto-synced) |
| **Storage duration** | Configurable (default 1 day) | Configurable | Configurable | **Permanent** |
| **Typical use** | Sensor telemetry | App notifications | "Do this and confirm" | Device state + remote config |

### 5.7 Security

#### Symmetric vs. Asymmetric Encryption (Module 2)

| | Symmetric | Asymmetric |
|---|---|---|
| **Keys** | One shared key | Public key (encrypt) + Private key (decrypt) |
| **Key sharing** | Both parties must know key -- risky to share | Private key never shared |
| **Speed** | Faster | Slower |
| **Security** | Less secure -- key interception breaks everything | More secure |
| **IoT Hub usage** | SharedAccessKey -> SAS token | X.509 certificate |
| **Real-world pattern** | Bulk data after key exchange | Used to securely exchange the symmetric key first |

#### SAS Token vs. X.509 Certificate Authentication (Module 2)

| | Symmetric Key / SAS Token | X.509 Certificate |
|---|---|---|
| **Device needs** | Connection string (SharedAccessKey) | Private key + certificate files (.pem) |
| **How it authenticates** | Creates SAS token (URL+expiry+signature); Hub verifies | Presents certificate; Hub verifies CA signature |
| **Key management** | 2 keys per device for key rotation | One certificate shared across many devices |
| **Clock required?** | **Yes** -- accurate NTP-synced clock (token expires) | No clock dependency |
| **Self-signed OK?** | N/A (hub-generated key) | Testing only; production needs CA-signed |

### 5.8 Data & Storage

#### Structured vs. Unstructured Data (Module 3)

| | Structured (SQL) | Unstructured (NoSQL / Blob) |
|---|---|---|
| **Data shape** | Fixed schema; every row same columns | No fixed schema; documents can differ |
| **Adding fields** | ALTER TABLE; may cause downtime | Just include new field; zero DB changes |
| **Best for** | Financial records, user accounts | IoT telemetry from mixed device fleets |

#### Hot vs. Warm vs. Cold Data Paths (Module 3)

| | Hot Path | Warm Path | Cold Path |
|---|---|---|---|
| **Timing** | Immediate (real-time) | Within hours | Long-term (months/years) |
| **Processing** | Stream processing, instant triggers | Batch processing for reports/dashboards | Data warehouse, historical analytics |
| **Example** | Temp spike alert in refrigerated truck | Yesterday's mileage report | 5-year fuel cost optimization |

#### WAV vs. MP3 (Module 6)

| | WAV | MP3 |
|---|---|---|
| **Compression** | Uncompressed | Compressed (lossy) |
| **Structure** | 44-byte header + raw PCM | Encoded frames |
| **File size** | Large | Much smaller |
| **Best for** | Raw audio capture (ADC produces PCM directly) | Storage and streaming after processing |

### 5.9 AI / Machine Learning

#### Traditional Programming vs. Machine Learning (Module 4)

| | Traditional Programming | Machine Learning |
|---|---|---|
| **Method** | Human writes explicit rules | Model learns patterns from labeled examples |
| **Best for** | Simple, well-understood rules | Visual/text complexity, subtle patterns |
| **Pros** | Predictable, explainable, no training data | Handles complexity; adapts via retraining |
| **Cons** | Cannot handle visual variation; breaks on edge cases | Needs labeled data; predictions are probabilistic |

#### Image Classification vs. Object Detection (Module 5)

| | Image Classification | Object Detection |
|---|---|---|
| **What it does** | Assigns one label to whole image | Finds and labels multiple objects individually |
| **Output** | List of (tag, probability) for whole image | List of (tag, probability, bounding box) per object |
| **Can count items?** | No | Yes |
| **Tells you where?** | No | Yes -- bounding box coordinates |

#### Standard Model vs. Compact Model -- Custom Vision (Module 4)

| | Standard Model | Compact Model |
|---|---|---|
| **What it is** | Full-size, cloud-only | Smaller, exportable to edge |
| **Domain name** | `Food` | `Food (compact)` |
| **Deployment** | Cloud REST API with Prediction-Key | Docker container on IoT Edge; local REST API, no key |
| **Retraining** | Predictions tab auto-populates | Edge images never reach cloud; manual retraining |

#### Classifier vs. Object Detector Retraining (Module 5)

| | Classifier Retraining | Object Detector Retraining |
|---|---|---|
| **Effort** | Low -- just re-tag images | High -- every bounding box must be manually reviewed per image |
| **Process** | Add correct tags, re-run training | Confirm, resize, re-tag, or delete every box; then re-run training |

#### Raw Pixels vs. Normalized (0-1) Coordinates (Module 5)

| | Raw Pixels | Normalized (0-1) |
|---|---|---|
| **What it is** | Bounding box in pixel numbers (e.g., top=320px) | As fractions of image dimensions (e.g., top=0.4) |
| **Device-independent?** | No -- changes with resolution | Yes -- works at any resolution |

#### Early TTS vs. Modern Neural TTS (Module 6)

| | Early TTS | Modern Neural TTS |
|---|---|---|
| **Method** | Stitched pre-recorded phoneme snippets | Deep learning generates audio from scratch |
| **Sound** | Robotic, monotonous | Near-human quality |
| **Risk** | None | Voice cloning enables impersonation |

#### Machine Translation (MT) vs. Neural Translation (Module 6)

| | MT | Neural Translation |
|---|---|---|
| **Method** | Rule databases + statistical selection | Deep learning model trained end-to-end |
| **Model size** | Large (rule/phrase databases) | Smaller (neural weights) |
| **Processing** | Phrase-by-phrase or word-by-word | Entire sentence at once (better context) |

### 5.10 Azure Service Comparisons

#### Direct LUIS Call vs. HTTP Trigger Wrapping (Module 6)

| | Direct LUIS Call | HTTP Trigger -> LUIS |
|---|---|---|
| **LUIS key location** | On device (security risk) | Only in cloud (secure) |
| **Updating NLU model** | Must re-deploy firmware to every device | Update function once; all devices benefit |
| **Device code complexity** | Device must parse LUIS JSON | Device gets clean `{"seconds": N}` |
| **Latency** | One network hop (faster) | Two hops (device->function, function->LUIS, slightly slower) |

#### Azure Speech Service Translation vs. Translator Service (Module 6)

| | Speech Service (SDK) | Translator Service (REST API) |
|---|---|---|
| **Input** | Speech -> translated text (one step) | Text -> translated text |
| **Access** | SDK only (NOT REST API) | REST API (standard HTTP) |
| **Extra features** | None | Profanity masking, custom glossaries |

### 5.11 Geospatial

#### DMS vs. Decimal Degrees (Module 3)

| | DMS | Decimal Degrees |
|---|---|---|
| **Format** | `2 deg 17' 43"` | `2.295277 deg` |
| **Best for** | Paper maps, human reading | Computers, APIs, databases |
| **Conversion** | decimal = degrees + (minutes/60) + (seconds/3600) | Reverse: multiply fractional part by 60 for minutes |

#### $GPGGA vs. $GNGGA (Module 3)

| | `$GPGGA` | `$GNGGA` |
|---|---|---|
| **Satellites** | US GPS only | Multi-constellation (GPS + GLONASS + Galileo + BeiDou) |
| **Accuracy** | Fewer satellites, slower fixes | Better accuracy, faster fixes |

#### Circle vs. Polygon Geofence (Module 3)

| | Circle | Polygon |
|---|---|---|
| **Definition** | Center point + radius | List of `[lon, lat]` corner points; last = first |
| **Ease** | Simple to define | More data; mandatory `geometryId` |
| **Real-world match** | Rarely matches actual boundaries | Matches real-world shapes (campus, field, city) |

#### $Default vs. Custom Consumer Group (Module 3)

| | `$Default` | Custom (e.g., `geofence`) |
|---|---|---|
| **Creation** | Automatic with every IoT Hub | Manually created |
| **Use** | First or only reader | Every additional reader needing independent cursor |

#### lat,lon vs. [lon,lat] Order (Module 3)

| | Spoken/Written (`lat, lon`) | GeoJSON (`[lon, lat]`) |
|---|---|---|
| **Where used** | Human communication, DB columns, many API params | GeoJSON, Azure Maps `atlas.data.Point()` |
| **Trap** | Natural order | Common mistake -- swapping places markers on wrong side of globe |

#### enqueuedtime vs. Current Time for Timestamps (Module 3)

| | `event.iothub_metadata['enqueuedtime']` | `datetime.now()` |
|---|---|---|
| **What it records** | When IoT Hub received the message | When the function processed it |
| **Accuracy** | Closest to actual reading time | Could be seconds/minutes later |
| **Best practice** | **Use this** | Wrong for IoT |

---

## 6. PREDICTED EXAM QUESTIONS

Compiled and de-duplicated from all modules. 15-20 questions, tagged as `[MC]` (multiple choice) or `[WRITING]` (short answer / essay). Grouped by topic with a one-line hint for each writing question.

### Topic: IoT Fundamentals & Architecture

**Q1. `[MC]` "Which of the following is NOT a category of IoT applications?"**
Know the four categories (Consumer, Commercial, Industrial/IIoT, Infrastructure) and one example of each. A distractor like "Medical IoT" or "Educational IoT" may be used -- those are not one of the four taught in the course.

**Q2. `[WRITING]` "Compare a microcontroller and a single-board computer. When would a product designer choose one over the other?"**
*Strong answer touches on:* Cost (MCU: as low as $0.03; SBC: $5-$35), power (MCU: months on battery; SBC: wall power), memory (120 MHz/192 KB vs. 1.5 GHz/8 GB), OS (none vs. Linux), programming (C/setup-loop vs. Python), and use cases (mass-produced single-purpose vs. prototyping/OS-needed).

**Q3. `[WRITING]` "What is the Things -> Insights -> Actions reference architecture? Map a given IoT system onto these three layers."**
*Strong answer touches on:* Define each layer. Map the system's physical devices -> Things, processing/analysis/AI -> Insights, commands/dashboards/alerts -> Actions. Module 4's fruit quality system is the canonical example, but the question could present a novel scenario.

**Q4. `[WRITING]` "Compare edge computing and cloud computing. Describe when you would choose each."**
*Strong answer touches on:* Latency (instant vs. network-dependent), offline capability (works vs. fails), privacy (data stays local vs. leaves), computing power (limited vs. massive), and specific scenarios (factory with bad Internet -> edge; weather station sending hourly -> cloud). The best answer notes that real systems blend both.

### Topic: Sensors & Data Acquisition

**Q5. `[MC]` "Which sensor type requires an external ADC to be read by a Raspberry Pi?"**
Raspberry Pi has no native analog pins. Any analog sensor (like a standard light sensor or resistive soil moisture probe) needs an external ADC board (Grove hat). Digital sensors (DHT11, button) can connect directly to GPIO.

**Q6. `[WRITING]` "Explain what ADC and PWM are and why they are necessary in IoT."**
*Strong answer touches on:* Physical world is analog (continuous); computers are digital (0/1). ADC converts analog sensor voltage to a binary number the computer can process (e.g., 1.65V -> 511 on 10-bit). PWM simulates analog output from digital-only pins by varying duty cycle (LED dimming, motor speed). Gives concrete numbers: 10-bit ADC -> 0-1023; PWM duty cycle 0-100%.

**Q7. `[WRITING]` "Explain why a relay is needed to control a water pump from an IoT device, and describe the sensor/actuator timing problem in automated irrigation."**
*Strong answer touches on:* IoT devices output 3.3V-5V at <1A -- insufficient for pumps. Relay uses electromagnet to switch a separate high-power circuit (up to 250V/10A). Timing problem: water takes ~20s to soak through soil to sensor. Naive on-until-wet causes over-watering. Solution: watering cycle -- 5s pump pulse -> 20s wait -> re-check -> repeat. Server unsubscribes from telemetry during the cycle.

### Topic: Connectivity & Protocols

**Q8. `[MC]` "Match the protocol to its defining characteristic."**
Expect a question where characteristics are listed and you must identify I2C (addresses, 2 shared wires), UART (baud rate, start/stop bits, no clock), SPI (chip select, full-duplex, 4 wires), or MQTT (broker, publish/subscribe, QoS levels). Know the comparison table cold.

**Q9. `[WRITING]` "Describe the sequence of events in an MQTT-based IoT system, from sensor reading to actuator response."**
*Strong answer walks through:* Device reads sensor -> formats as JSON -> publishes to telemetry topic -> broker routes to subscribed server -> server processes, decides -> publishes command to command topic -> broker routes to device -> device receives and calls actuator. Uses correct terms: publish, subscribe, broker, topic, telemetry, command. Mentions QoS choice (telemetry: QoS 0 or 1; critical command: QoS 2).

### Topic: Cloud & Data Management

**Q10. `[WRITING]` "Explain why a logistics company tracking a mixed fleet of vehicles should use a NoSQL database rather than a SQL database."**
*Strong answer touches on:* Different vehicle types send different data fields (tractor: GPS only; refrigerated truck: GPS + temperature). NoSQL accepts any JSON shape without schema migration; SQL requires ALTER TABLE for every new field. Adding a new sensor type in NoSQL = zero database changes; in SQL = schema change + NULL handling for all existing rows.

**Q11. `[MC]` "Classify a scenario as hot, warm, or cold path data."**
Hot = real-time (temperature spike alert <3 sec). Warm = operational report within hours (daily mileage, map visualization). Cold = long-term historical analysis (5-year fuel cost trends). Know the latency requirement for each.

**Q12. `[WRITING]` "Compare the four IoT Hub communication modes: D2C, C2D, Direct Method, and Device Twin. When would you use each?"**
*Strong answer touches on:* D2C (device->cloud, telemetry, no response, default 1-day storage). C2D (cloud->device, commands, no response required). Direct Method (cloud->device, response required -- confirm execution). Device Twin (bidirectional, synchronized JSON, permanent storage, use for remote configuration). Give a concrete example for each.

**Q13. `[MC/WRITING]` "What problem do consumer groups solve in IoT Hub?"**
*Strong answer:* Without separate consumer groups, multiple readers share one cursor and miss messages. Each consumer group = independent bookmark. `$Default` is auto-created; create additional ones for each independent reader. Rule: one application per consumer group.

### Topic: Security

**Q14. `[WRITING]` "Compare symmetric and asymmetric encryption. Give one real-world example of an IoT security failure and explain what made it possible."**
*Strong answer touches on:* Symmetric = one shared key, faster, less secure (key must be shared). Asymmetric = public/private key pair, slower, more secure (private key never shared). Real-world failure: Mirai botnet (default passwords on DVRs/cameras) or fish tank thermostat (insecure IoT on corporate network). Names Stuxnet as canonical industrial IoT example.

**Q15. `[WRITING]` "What is a device twin and what problem does it solve for IoT devices in production?"**
*Strong answer:* A device twin is a JSON document in IoT Hub with desired and reported properties, permanently stored. It solves remote configuration -- change a threshold from the cloud dashboard, device adapts without physical access or firmware update. Example from Module 4: proximity sensor threshold changed from 10 cm to 8 cm via device twin. Contrast with hard-coded constants in prototypes.

### Topic: AI / Machine Learning

**Q16. `[WRITING]` "Explain transfer learning and why it matters for IoT projects. Give examples from at least two modules."**
*Strong answer:* Training from scratch needs millions of images and GPU time. Transfer learning starts from a pre-trained model and fine-tunes only the final layer on a small dataset (15-50 images). Module 4: Custom Vision "Food" domain -> fruit classifier with 30 images/class. Module 5: "Products on Shelves" domain -> object detector. Module 6: Custom speech models (fine-tuning STT for environment) and voice cloning (fine-tuning TTS on a person's voice).

**Q17. `[MC]` "Which of the following best describes the difference between image classification and object detection?"**
Classification = one label for whole image (what is this?). Object detection = bounding boxes + labels per object (how many and where?). Wrong answer options may say "object detection is slower" or mix up which returns bounding boxes.

**Q18. `[WRITING]` "Explain why overlapping bounding boxes are a problem for stock counting and describe how they are handled."**
*Strong answer:* The detector sometimes draws two nearly identical boxes around the same object at different confidences (false positive duplicate). This overcounts items -> shelf looks fuller than it is -> restock never triggers. Solution: if two same-tag boxes overlap significantly (box2 >80% inside box1), discard the lower-confidence one. Mentions IoU conceptually and the 80% containment rule.

**Q19. `[WRITING]` "Trace the full pipeline from user speech to timer alert in the voice-controlled smart timer."**
*Strong answer walks through:* Button press -> MEMS microphone captures audio -> PCM sampling (16-bit, 16 kHz) -> streaming to SD card (too large for 192 KB RAM) -> Azure Speech Service STT converts to text -> HTTP trigger -> LUIS extracts intent (`set timer`) + entities (`number: 3`, `time-unit: minute`) -> function calculates total seconds -> TTS speaks confirmation (SSML with neural voice) -> daemon thread counts down -> TTS speaks alert. For multi-language: TranslationRecognizer converts input speech to English; Translator REST API converts output back.

### Topic: Geospatial

**Q20. `[MC]` "GDD Calculation: A corn crop has a base temperature of 10 deg C. On a day with T_max = 22 deg C and T_min = 14 deg C, what is the GDD?"**
Formula: `GDD = ((T_max + T_min) / 2) - T_base = ((22 + 14) / 2) - 10 = 18 - 10 = 8 GDD`. If the daily average is below base temperature, GDD = 0 (not negative). Expect a distractor answer of -2 for a below-base day.

**Q21. `[MC]` "An NMEA GGA sentence contains `4738.538654,N`. What is the latitude in decimal degrees?"**
Recognize `(dd)dmm.mmmm` format: `47 + (38.538654 / 60) = 47.6423109 deg`. Trap answer forgets to divide by 60.

**Q22. `[MC]` "A geofence API returns `"distance": -12`. Is the vehicle inside or outside the geofence?"**
Negative = inside. |-12| = 12 m inside, within the 50 m search buffer. Positive = outside. +/-999 = beyond the search buffer. Follow-up: "Why not immediately trigger alert for `distance: 12` (positive)?" Because GPS inaccuracy could mean the truck is actually inside -- the search buffer handles this.

**Q23. `[MC]` "Given latitude 47.64 and longitude -122.14, write the JavaScript to create a GeoJSON Point for Azure Maps."**
Correct: `new atlas.data.Point([-122.14, 47.64])` -- longitude first. Trap answer: `[47.64, -122.14]`. This is the most common and hardest-to-debug geospatial programming mistake.

---

## 7. FLAGGED GAPS

The following concepts were either missing from the source material, mentioned only in passing, or explained incompletely. Treat this document as exam-sufficient on its own -- but if you have extra study time, these are the items worth double-checking against course slides, your own notes, or a quick web search.

### Across All Modules

1. **AMQP is name-dropped in Modules 1 and 2 but never explained.** Mentioned as an alternative transport protocol for IoT Hub (alongside MQTT and HTTPS). Know that AMQP (Advanced Message Queuing Protocol) exists as a competitor to MQTT -- more feature-rich but heavier. For this exam, knowing it is one of three IoT Hub transport options is sufficient.

2. **HTTP/HTTPS mentioned as MQTT alternatives but no comparison given.** Module 1 lists them as "other protocols" without context. HTTPS is the standard web protocol -- more overhead per message than MQTT, but universally supported. For this exam: MQTT is purpose-built for IoT (lightweight, pub/sub), HTTPS is general-purpose web (heavier, request/response).

3. **RTOS names (Azure RTOS, FreeRTOS, Zephyr) listed but never differentiated.** Module 1 Lesson 2 names them with zero explanation. They are lightweight operating systems for microcontrollers providing multitasking, networking, and GUI support. A question like "Which of these is an RTOS?" listing them alongside Linux or Windows would be fair.

### Module 1

4. **Mesh networking mentioned but not explained.** Lesson 2 says devices can use "mesh networking (e.g., Bluetooth) to talk to each other, connecting via a hub device." Zigbee is the mesh example covered in Module 2. A mesh network means each device relays messages for its neighbors -- if device A cannot reach the hub directly, it routes through device B.

5. **Baud rate (9600) used in code but not formally defined in Module 1.** `Serial.begin(9600)` in Arduino sets serial communication speed to 9,600 bits per second. Both devices must agree on this number. Properly explained in Module 2's UART section.

6. **JSON syntax trap:** Python dicts use single quotes (`{'light': 143}`), but valid JSON requires double quotes (`{"light": 143}`). The course Python examples use single quotes, which work in Python but are technically not JSON.

### Module 2

7. **GDD floor-at-zero rule:** When the daily average is below base temperature, GDD = 0, not negative. A day averaging 8 deg C with a base of 10 deg C yields 0 GDD. Plants do not "lose" accumulated growth on cold days.

8. **Resistive sensor voltage direction under-explained.** The lesson says "voltage increases as moisture increases" without showing the circuit. Both sensor types are treated as interchangeable "analog sensors" code-wise; this could confuse students about CounterFit's capacitive sensor behaving oppositely.

9. **Device Twin introduced but never implemented in code in Module 2.** Implementation appears in Module 4. Exam questions may still test the concept based on Module 2 text.

10. **Quantum computing threat to encryption is a one-line mention.** Module 2 Lesson 10 notes quantum computing "may be able to break all known encryption." Could appear as a distractor: "Which poses a future threat to modern cryptography?" -> "quantum computing."

### Module 3

11. **Event Hub vs. IoT Hub relationship is blurred.** IoT Hub exposes an "Event Hub compatible endpoint" internally. The Functions trigger uses Event Hub protocols. For exam purposes: IoT Hub is the device-facing service; its internal message stream is accessible via Event Hub protocols.

12. **CounterFit referenced as virtual sensor simulator but not formally introduced in Module 3.** Know that CounterFit simulates IoT sensors (including GPS) by sending fake data over a local network socket when you lack physical hardware.

13. **"RUC" (Road User Charges) used without expansion.** New Zealand's diesel vehicle tax compliance example. Know the concept: some governments charge road tax per km; GPS on connected vehicles can distinguish public road km (taxable) from private land km (exempt).

14. **pynmea2 parsing shown but full capabilities not explored.** Only `.latitude` and `.longitude` are extracted. The GGA sentence also includes altitude (`msg.altitude`), satellite count, and fix quality. If exam asks "which NMEA message type contains altitude" -> GGA.

### Module 4

15. **Unsupervised learning mentioned but never explained.** "Unsupervised learning does not require labeled data (not covered here)." If it appears as a distractor, only know it exists as contrast to supervised learning -- no mechanism or example needed.

16. **GPU / cloud compute cost gestured at but not quantified.** Lesson 15 says training needs GPUs and cloud lets you "rent GPU time." For the exam: know that model training from scratch needs massive GPU compute; cloud makes this accessible on a pay-per-use basis.

17. **SPI protocol name-dropped without explanation in Module 4.** Cameras connect via SPI but the acronym is never defined. Module 2 provides the full explanation -- refer back to that.

18. **OPC-UA mentioned once with no depth.** Industrial machine-to-machine protocol for factory floors. One-line mention. Know it exists as an industrial IoT protocol; no comparison or mechanism needed.

19. **Deployment manifest JSON structure shown partially.** Only the `ImageClassifier` module block is printed. If asked "which section specifies container credentials?" -> `registryCredentials`. The full JSON syntax is not exam-critical.

### Module 5

20. **No explanation of how IoU is actually calculated.** Lesson 19 defines the acronym but never shows the formula. Lesson 20 uses a simpler "80% containment" check. An exam might conceptually ask about IoU; know it measures overlap (0-1) between two boxes.

21. **Precision vs. Recall definitions context-switch** between classification (per-image) and object detection (per-box) contexts. In object detection: precision = "of all boxes predicted, how many were correct"; recall = "of all real objects, how many were found."

22. **No real vs. synthetic shelf image discussion.** Training instructions say "show objects as if on store shelves" but do not discuss whether kitchen-table photos work. The Products on Shelves domain is tuned for retail shelving; non-shelf backgrounds may reduce accuracy.

23. **No discussion of lighting, camera angle, or occlusion.** Real shelves have glare, shadows, products behind other products. The lessons assume clear front-facing photos. A real deployment would need to handle these.

### Module 6

24. **Wio Terminal RAM (192 KB) cited without explanation of what it is or why that number matters.** A student unfamiliar with microcontrollers may wonder if 192 KB is typical (yes, mid-range IoT MCU range). The key point: 192 KB / 32 KB per second = ~5 seconds of audio before RAM fills.

25. **Function key and `code` query parameter distinction** between local (`func start` -- no key needed) and cloud deployment (`?code=` required) not fully explained.

26. **Threading (`threading.Thread`, `daemon`) used without explaining what a thread is.** A thread is a separate sequence of instructions running concurrently with the main program. The daemon thread auto-terminates when main exits. Used for the timer countdown so the main program can continue listening for new button presses.

27. **Profanity masking and custom glossary described but no examples given.** Profanity masking detects/replaces profane words in translations. Custom glossary forces specific terms (e.g., "Raspberry Pi") to stay untranslated or be translated in a specific way.
