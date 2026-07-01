# Module 02 – Farm: Study Sheet

## 1. MODULE OVERVIEW

This module teaches how to use IoT (Internet of Things — everyday objects equipped with internet-connected sensors) to monitor and automate plant growth on a farm. It begins with predicting plant maturity from temperature data (Lesson 5), moves to measuring soil moisture and understanding how sensors communicate with computers (Lesson 6), then builds an automated watering system using that moisture data (Lesson 7). The second half migrates this system from a basic, insecure messaging approach to Microsoft Azure's professional cloud service (Lesson 8), moves the decision-making logic to serverless cloud functions (Lesson 9), and finally secures the entire setup so only authorized devices and services can communicate (Lesson 10). The arc is: collect data → understand hardware → automate an action → professionalize with cloud → secure it.

---

## 2. KEY CONCEPTS

### 2.1 Growing Degree Days (GDD) — Lesson 5

**Plain-language definition:** GDD is a number that tells you how much "heat credit" a plant earned today toward reaching maturity. You calculate it from the day's highest and lowest temperatures, minus the plant's minimum required temperature. If the day averages too cold, the plant earns zero GDD that day.

**Why it matters:** Without GDD, a farmer must physically inspect every field to guess whether crops are ready. GDD lets a computer predict harvest dates from temperature data alone, saving enormous labor and preventing crops from being harvested too early or too late.

**Concrete example:** Corn has a base temperature of 10°C and needs 800–2,700 GDD to mature. If Monday had a high of 16°C and a low of 12°C, the GDD earned = ((16 + 12) / 2) − 10 = **4 GDD**. The farmer knows the corn still needs roughly 796 more GDD before harvest.

**Formula:**
```
GDD = ((T_max + T_min) / 2) − T_base
```

**Architecture pattern:** IoT sensor reads temperature → publishes via MQTT (a lightweight messaging protocol) → server saves to a CSV file → nightly job calculates GDD → alerts farmer near maturity.

**Three plant temperature thresholds (all based on daily averages):**
- **Base temperature** — the minimum warmth a plant needs to grow at all.
- **Optimum temperature** — the temperature where growth is fastest.
- **Maximum temperature** — above this, the plant stops growing to conserve water.

### 2.2 Soil Moisture & Why It Matters — Lesson 6

**Plain-language definition:** Soil moisture is how much water is held in the soil around a plant's roots. Sensors measure this electrically and convert the reading into a number.

**Why it matters:** Plants are roughly 90% water and need it for three purposes:
1. **Photosynthesis** — the chemical process where plants use water, CO₂, and light to make their own food (carbohydrates) and release oxygen.
2. **Transpiration** — water evaporating through leaf pores pulls nutrients up from the roots and cools the plant, similar to human sweating.
3. **Structure** — water inside plant cells keeps them rigid; without enough water, the plant wilts and collapses.

Too little water = plant cannot grow. Too much water = roots cannot absorb oxygen, roots die, plant dies. IoT lets us measure moisture precisely and water only when needed.

### 2.3 Soil Moisture Sensor Types — Lesson 6

**Resistive sensor (two-probe):**
- Works like: two metal probes in soil; electricity flows more easily through wet soil (water conducts electricity well). A reading of higher current = more moisture = lower resistance.
- Tradeoff: simpler and cheaper, but the probes corrode over time from the electrical current passing through them.

**Capacitive sensor (electrical-field):**
- Works like: measures how much electrical charge the soil can store (capacitance). Wet soil stores charge differently from dry soil. The sensor converts this into a voltage: wetter soil produces a **lower** voltage.
- Tradeoff: more durable (no exposed metal corroding), but typically more expensive.

**Critical distinction for exams:**
- Resistive sensor: moisture ↑ → resistance ↓ → voltage ↑ (upward slope).
- Capacitive sensor: moisture ↑ → capacitance changes → voltage **↓** (downward slope). The CounterFit virtual sensor used in the course simulates a capacitive sensor: higher ADC reading = drier soil.

### 2.4 Sensor Communication Protocols — Lesson 6

Every sensor needs a physical way to connect (hardware) and a set of rules for sending data (protocol — a well-defined method for communication).

#### GPIO (General-Purpose Input/Output)
- **What it is:** Programmable metal pins on an IoT board (like a Raspberry Pi) that you can set to either *read* a voltage (input mode) or *send* a voltage (output mode).
- **How it works:** A button wired to a GPIO input pin sends 5V when pressed (read as "1") and 0V when released (read as "0"). An LED wired to a GPIO output pin lights up when the pin sends 3.3V.
- **Limitation:** GPIO pins only understand digital (on/off, 1/0). To read an analog sensor (which returns a range of voltages), you need an ADC.

#### Analog Pins + ADC (Analog-to-Digital Converter)
- **What it is:** A GPIO pin with a built-in ADC — a tiny circuit that converts a continuous voltage range into a discrete digital number.
- **How it works:** On a 3.3V board with a 10-bit ADC, 0V → value 0, 3.3V → value 1,023, and 1.65V → value 511. This creates 1,024 possible values (2^10).
- **Where you find them:** Built into Arduino and Wio Terminal. The Raspberry Pi has no native analog pins — you need an external ADC board (like a Grove hat).

#### I²C (Inter-Integrated Circuit, pronounced "I-squared-C")
- **What it is:** A protocol where one controller can talk to multiple peripherals (sensors/displays) over just two shared wires: SDA (data) and SCL (clock).
- **How it works:** Every peripheral has a fixed hard-coded address. The controller sends a message starting with the target address, so only the intended device responds. Think of it like a school PA system where each message begins with a specific classroom number.
- **Speeds:** Standard (100 Kbps), Fast (400 Kbps — Raspberry Pi's maximum), High Speed (3.4 Mbps, rare).
- **Modern terminology:** Uses "controller/peripheral" instead of the older "master/slave."

#### UART (Universal Asynchronous Receiver-Transmitter)
- **What it is:** A direct two-device connection where each device has a Tx (transmit) pin and an Rx (receive) pin. Tx of device A connects to Rx of device B, and vice versa.
- **How it works:** Data is sent one bit at a time (serial). Both devices must agree on a **baud rate** — the speed in bits per second (9,600 baud is a common default). Each byte is wrapped with a **start bit** (signals data is coming) and a **stop bit** (signals byte is complete). No clock wire is used — timing relies on the agreed baud rate.
- **Max speed:** ~6.5 Mbps.

#### SPI (Serial Peripheral Interface)
- **What it is:** A controller-peripheral protocol using four wires: COPI (controller → peripheral), CIPO (peripheral → controller), SCLK (clock), and CS (chip select — one per peripheral).
- **How it works:** The controller uses the CS wire to wake up one specific peripheral at a time, then exchanges data over COPI/CIPO synchronized to the clock. No start/stop bits needed because everything is clock-synced.
- **Full-duplex:** The controller can send and receive data simultaneously on separate wires.
- **Speed:** No defined limit; often multiple MB/s. Designed for very short distances (e.g., processor to flash memory chip on the same circuit board).

### 2.5 Wireless Protocols — Lesson 6

| Protocol | Range | Key Characteristic |
|----------|-------|-------------------|
| **BLE** (Bluetooth Low Energy) | Short | Common in fitness trackers; very low power |
| **LoRaWAN** (Long Range, Low Power) | Long (kilometers) | Used in commercial farm sensors; sends data to a central hub |
| **WiFi** | Medium | Standard home/office WiFi |
| **Zigbee** | Medium | Devices form a mesh — each relays messages for its neighbors until reaching a coordinator that connects to the internet. Named after honeybee waggle dances. |

### 2.6 Sensor Calibration — Lesson 6

**Plain-language definition:** Calibration is matching a sensor's raw electrical output to a real-world measurement you care about. A soil moisture sensor might output 615 — but 615 what? Calibration tells you that 615 means, for example, "25% water content in this particular soil."

**Why it matters:** Raw electrical readings are meaningless by themselves. The same moisture level produces different readings in sandy soil vs. clay soil because electrical properties differ by soil type.

**Process:**
1. Take sensor readings from a field soil sample.
2. Send a portion of that same soil to a lab to measure actual water content (gravimetric: kg water per kg dry soil; or volumetric: m³ water per m³ dry soil).
3. Plot lab-measured moisture (X-axis) against sensor reading (Y-axis) on a graph.
4. Fit a line to the points — use that line to convert future sensor readings to real moisture percentages.

A few lab measurements can calibrate a sensor for an entire field.

### 2.7 Relays — Lesson 7

**Plain-language definition:** A relay is an electrically-controlled mechanical switch. A tiny current from an IoT device (3.3V, less than 1A) activates an internal electromagnet that physically pulls a metal lever, closing a separate high-power circuit — similar to how your finger flips a light switch that controls mains electricity (230V/120V).

**Why it matters:** IoT devices output only 3.3V–5V at less than 1 amp — far too weak to directly power a water pump. A relay bridges this gap, letting a low-power IoT board safely control high-power devices (the Grove relay handles up to 250V at 10A).

**How it works:**
1. IoT device sends a high signal (3.3V/5V) to the relay's **control circuit**.
2. Current flows through a coil inside the relay → coil becomes an electromagnet → pulls a lever → lever touches switch contacts → **output circuit** completes.
3. Pump (connected to the output circuit) now receives electricity from an external power supply and runs.
4. IoT device sends a low signal → electromagnet deactivates → lever springs back → output circuit opens → pump stops.
5. The relay makes an audible **click** when the lever moves.

**Key specs:** Grove relay output circuit handles up to **250V at 10A**.

### 2.8 Sensor & Actuator Timing — Lesson 7

**Plain-language definition:** When you water soil, the moisture reading does not change instantly. Water takes time (often 20+ seconds) to soak through the soil to reach the sensor. This delay between *doing an action* (turning on a pump) and *seeing the result* (moisture reading dropping) is the sensor/actuator timing problem.

**Why it matters:** A naive approach (keep pump running until sensor says "wet enough") would massively over-water — the sensor still reads "dry" long after enough water has been delivered. Excess water suffocates roots.

**Solution — Watering Cycle:**
1. Turn pump on for a fixed short pulse (e.g., 5 seconds).
2. Turn pump off.
3. Wait for water to soak through to the sensor (e.g., 20 seconds).
4. Re-check moisture.
5. If still too dry, repeat.

**Overlapping telemetry fix:** Since the device sends moisture readings every 10 seconds but a watering cycle takes ~25 seconds, new telemetry could arrive mid-cycle and trigger a second overlapping cycle. The server fixes this by **unsubscribing from telemetry during the watering cycle**, then re-subscribing when done. Other services can still read the data from the broker.

### 2.9 The Cloud — Lesson 8

**Plain-language definition:** The "cloud" means renting someone else's computers instead of buying and running your own. You pay only for what you use, scaling up during busy times and down during quiet times.

**Before the cloud:** Companies built their own data centers — buying physical servers, managing power, cooling, networking, security, and software updates. This was expensive, slow to scale, and required specialized staff.

**With the cloud:** A provider (Microsoft Azure, Google Cloud, Amazon AWS) owns massive data centers (Azure's span multiple square kilometers) and rents slices of them. Benefits:
- Pay per use, not per machine bought.
- Scale up/down instantly.
- Provider handles hardware, power, cooling, security.
- Economies of scale mean lower total cost.

### 2.10 Azure IoT Hub — Lesson 8

**Plain-language definition:** Azure IoT Hub is Microsoft's professionally managed replacement for a basic MQTT broker. It's a cloud service purpose-built to handle millions of IoT devices reliably and securely.

**Problems with a public MQTT broker (like `test.mosquitto.org`):**
- No reliability guarantees (could be turned off).
- Anyone can listen to or inject messages (no security).
- Cannot handle scale (designed for a few test messages).
- No way to list or manage connected devices.

**How IoT Hub solves these:**
- Professionally maintained with uptime guarantees.
- Only registered devices with valid secret keys or certificates can connect.
- Handles millions of messages per day.
- Built-in device registry — knows all registered devices.
- Free tier (F1) available for learning: 8,000 messages/day, max 1 per subscription.

**Four Communication Modes in IoT Hub:**

| Mode | Direction | Key Characteristic |
|------|-----------|-------------------|
| **D2C** (Device-to-Cloud) | Device → Hub | Telemetry messages from device to cloud |
| **C2D** (Cloud-to-Device) | Hub → Device | Commands from cloud application to device |
| **Direct Method** | Hub → Device | A command that **requires a response** so the application knows whether the device successfully executed it |
| **Device Twin** | Both ways | A JSON document synchronized between device and IoT Hub; stores device-reported state and cloud-desired settings. **Stored permanently** (unlike D2C messages, which are stored for only 1 day by default). |

**Under the hood:** IoT Hub uses MQTT, HTTPS, or AMQP as the transport protocol. D2C messages flow through an **Event Hub compatible endpoint** (Microsoft's message-streaming service).

### 2.11 Connection Strings & SAS Tokens — Lesson 8

**Plain-language definition:** A connection string is a single text value that contains everything a device needs to identify itself to the cloud: the hub's web address, the device's name, and a shared secret password.

**Structure:**
```
HostName=soil-moisture-sensor.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=Bhry+...
```

The **SharedAccessKey** is a symmetric key — the same secret value known to both the device and the IoT Hub. It is never sent over the network directly. Instead, on first connection, the device creates a **SAS token** (Shared Access Signature) that includes: the hub URL, an expiry time, and a signature created by encrypting the URL+expiry with the SharedAccessKey. The hub decrypts the signature with its copy of the key and verifies the match. The expiry time prevents "replay attacks" where a captured token is reused later.

**Important:** Because SAS tokens expire based on clock time, the IoT device must have an accurate clock — typically synchronized via **NTP (Network Time Protocol)**.

### 2.12 Serverless / Azure Functions — Lesson 9

**Plain-language definition:** "Serverless" means you write small chunks of code that run only when something triggers them — like a new message arriving from a sensor. There *are* servers underneath, but you never manage them; the cloud provider handles everything automatically.

**Why it matters for IoT:** A farm might have 10 sensors today but 10,000 next year. Serverless code automatically scales — the provider runs your function in parallel for every message, no matter how many arrive. You pay only for the time your code actually runs (often fractions of a cent per execution), and $0 when no messages arrive.

**How it works in this module (Azure Functions):**
1. The IoT device sends a D2C message to IoT Hub.
2. IoT Hub routes it through the Event Hub compatible endpoint.
3. An Azure Function with an **Event Hub trigger** fires automatically when the message arrives.
4. The function's code reads the soil moisture value from the message body.
5. If moisture > 450 (too dry), the function uses the **IoT Hub Registry Manager** to send a `relay_on` direct method back to the specific device that sent the telemetry.

**Registry Manager:** A tool that lets cloud code view registered devices, send C2D messages, invoke direct methods, and update device twins. It needs its own connection string (with `ServiceConnect` policy permissions). Unlike the MQTT version (which broadcast commands to all devices), the Registry Manager sends a direct method to the **one specific device** that sent the telemetry — this works properly with multiple independent sensors.

**Key files in a Functions App:**
- `function.json` — defines what triggers the function and what bindings (connections to other services) it uses.
- `__init__.py` — the actual Python code.
- `local.settings.json` — local development settings (connection strings); never deployed to cloud, never committed to source control.

**Critical bug fix:** The default Azure Functions template sets `cardinality` to `"many"` and `eventHubName` to a default value. For IoT Hub, you must change `cardinality` to `"one"` and `eventHubName` to `""` (empty), because the connection string already identifies the hub.

### 2.13 IoT Security & Cryptography — Lesson 10

**Plain-language definition:** IoT security means making sure that (a) only your real sensors can send data to your cloud, (b) only your cloud can send commands to your sensors, and (c) nobody can read your data in transit. Without security, a rival farmer could send fake "wet" readings that prevent your irrigation from ever turning on.

**Real-world security failures cited in the module:**
- **Mirai Botnet (2016):** Malware scanned the internet for IoT devices (DVRs, cameras) still using factory-default usernames/passwords, enslaved them, and used them to launch a massive attack that took down large portions of the internet.
- **Fish tank thermostat (2018):** Hackers used an insecure WiFi-connected thermostat on a casino's fish tank as an entry point to steal data from the casino's corporate network.
- **CloudPets:** A database of internet-connected toy users (including children's voice recordings) was left publicly accessible on the internet.

#### Encryption & Decryption
- **Encryption** — scrambling readable data into gibberish using a secret key, so only someone with the key can read it.
- **Decryption** — unscrambling encrypted data back into readable form using the key.
- **Cryptography** — the overall field/technique of encryption and decryption.

#### Symmetric vs. Asymmetric Encryption

**Symmetric encryption:**
- One shared key for both encrypting and decrypting.
- Like: a single key that both locks and unlocks a box.
- Faster, but less secure — both parties must know the key, so the key must be shared somehow. If intercepted during sharing, security is broken.

**Asymmetric encryption:**
- Two mathematically related keys: a **public key** (can only encrypt) and a **private key** (can only decrypt).
- Like: a mailbox where anyone can drop mail in (public key) but only you have the key to open it (private key).
- Slower, but more secure — the private decryption key never needs to be shared.
- In practice, systems combine both: use asymmetric encryption to securely share a symmetric key, then use the faster symmetric key for all subsequent data.

**RSA (Rivest–Shamir–Adleman):** The most widely used algorithm for generating public/private key pairs.

#### X.509 Certificates
- **Problem:** How do you know a public key really belongs to who it claims? An impostor could publish a fake public key.
- **Solution:** An X.509 certificate is a digital document containing a public key plus metadata, digitally signed by a trusted third party called a **Certification Authority (CA)**. You trust the certificate because you trust the CA — like trusting a passport because you trust the issuing government.
- **Self-signed certificates:** Signed by the creator (not a CA). Fine for testing, never acceptable for real production use.
- **IoT advantage:** One X.509 certificate can be shared across many devices. Upload the certificate to IoT Hub once; all devices use the same certificate. Each device only needs its own private key (which never leaves the device).

**Azure IoT Hub supports both authentication methods:**
1. **Symmetric key** (connection string with SharedAccessKey → SAS token flow). Devices have 2 keys for **key rotation** — if one is compromised, switch to the backup while the first is regenerated. Keys should ideally be stored in an **HSM** (Hardware Security Module) — a special chip that holds keys securely so code can use them but cannot extract them.
2. **X.509 certificate** (asymmetric). Generated via Azure CLI: `az iot hub device-identity create --am x509_thumbprint --output-dir .` creates a `.pem` private key file and a `.pem` certificate file.

---

## 3. KEY TERMS

| Term | One-line plain-language definition |
|------|-----------------------------------|
| IoT (Internet of Things) | Everyday physical objects equipped with sensors and internet connectivity to collect and exchange data. |
| Digital Agriculture / Agriculture 4.0 | Using data-collection tools (sensors, AI, cloud) to make farming decisions instead of relying solely on human observation. |
| Precision Agriculture | Observing and responding to crops at the level of individual fields or even parts of fields, rather than treating the whole farm uniformly. |
| Agriculture Value Chain | The entire journey of food from farm to table, including shipping, processing, warehousing, and e-commerce. |
| Growing Degree Days (GDD) | A daily number representing how much "heat credit" a plant earned toward maturity; calculated from temperature data. |
| Base Temperature | The minimum daily average temperature a plant needs to grow at all. |
| Optimum Temperature | The daily average temperature at which a plant grows fastest. |
| Maximum Temperature | The daily average temperature above which a plant stops growing to conserve water. |
| DHT11 | A combined digital humidity and temperature sensor; in CounterFit it is simulated as two separate virtual sensors (humidity on pin N, temperature on pin N+1). |
| CSV (Comma-Separated Values) | A plain-text file format where each line is a row and commas separate values into columns. |
| ISO 8601 | An international standard format for writing dates and times in a way computers can reliably read (e.g., `2021-04-19T17:21:36-07:00`). |
| Photosynthesis | The process where plants combine water, CO₂, and light to produce their own food (carbohydrates) and release oxygen. |
| Transpiration | Water evaporating from a plant's leaves, which pulls nutrients upward and cools the plant. |
| Resistive Soil Moisture Sensor | Two metal probes that measure how easily electricity flows through soil; wetter soil conducts better (lower resistance). |
| Capacitive Soil Moisture Sensor | A sensor that measures how much electrical charge soil can store; wetter soil produces a lower voltage output. |
| Calibration | Mapping a sensor's raw electrical output to a real physical measurement (e.g., converting a voltage to "% soil moisture") by comparing against known reference samples. |
| Gravimetric Water Content | Soil moisture measured as kilograms of water per kilogram of dry soil. |
| Volumetric Water Content | Soil moisture measured as cubic meters of water per cubic meter of dry soil. |
| Steinhart-Hart Equation | The mathematical formula that converts electrical resistance to temperature in thermistor-based sensors. |
| GPIO (General-Purpose Input/Output) | Programmable pins on an IoT board that can be set to read a voltage (input) or send a voltage (output). |
| ADC (Analog-to-Digital Converter) | A circuit that converts a continuous voltage range into a discrete digital number (e.g., 0–1,023 for a 10-bit ADC). |
| I²C (Inter-Integrated Circuit) | A protocol where one controller talks to multiple peripherals over two shared wires (data and clock), using device addresses to identify the target. |
| SDA | The data wire in an I²C connection. |
| SCL | The clock wire in an I²C connection. |
| UART (Universal Asynchronous Receiver-Transmitter) | A direct two-device serial connection where Tx (transmit) connects to Rx (receive); uses a shared baud rate and start/stop bits instead of a clock wire. |
| Baud Rate | The speed of a UART connection, measured in bits per second (9,600 baud is a common default). |
| SPI (Serial Peripheral Interface) | A controller-peripheral protocol using separate wires for data-in, data-out, clock, and chip-select; full-duplex and fast. |
| COPI | Controller Output, Peripheral Input — the SPI wire carrying data from the controller to the peripheral. |
| CIPO | Controller Input, Peripheral Output — the SPI wire carrying data from the peripheral to the controller. |
| Full-Duplex | Communication where data can flow in both directions simultaneously on separate wires. |
| BLE (Bluetooth Low Energy) | A short-range, very-low-power wireless protocol common in fitness trackers. |
| LoRaWAN (Long Range, Low Power) | A wireless protocol for sending small amounts of data over kilometers; common in commercial farm sensors. |
| Zigbee | A wireless mesh-networking protocol where devices relay messages for each other to reach a coordinator connected to the internet. |
| Mesh Network | A network where each device connects to multiple nearby devices and messages hop from one to another until reaching the destination. |
| Relay | An electromechanical switch: a small electric current activates an internal magnet that physically pulls a lever to close a separate high-power circuit. |
| Electromagnet | A temporary magnet created by passing electricity through a wire coil; magnetized only when current flows. |
| Mains Electricity | The high-voltage power delivered to homes and businesses through the national grid (230V/120V/100V depending on country). |
| Control Circuit | The low-voltage side of a relay (3.3V/5V from IoT device) that activates the electromagnet. |
| Output Circuit | The high-voltage side of a relay (up to 250V/10A) that powers the connected device (e.g., water pump). |
| Sensor/Actuator Timing | The delay between activating a device (e.g., turning on a pump) and the sensor detecting the resulting physical change (e.g., soil becoming wetter). |
| Watering Cycle | A defined sequence: pump on for a short pulse → pump off → wait for water to soak through → re-check moisture. |
| Threading | Running a piece of code in the background so the main program can continue doing other things simultaneously. |
| Unsubscribe (MQTT) | Telling the message broker to stop forwarding messages on a topic; used during the watering cycle to prevent overlapping commands. |
| Cloud Computing | Renting computing resources (servers, storage, networking) from a large provider instead of buying and running your own. |
| Microsoft Azure | Microsoft's cloud platform; the cloud service used throughout this course. |
| Azure IoT Hub | Microsoft's managed cloud service for securely connecting, monitoring, and controlling millions of IoT devices. |
| Resource (Azure) | Any individual cloud service you create (an IoT Hub, a virtual machine, a database, etc.). |
| Resource Group (Azure) | A logical folder that groups related Azure resources together; deleting the group deletes everything inside it. |
| SKU (Stock Keeping Unit) | The pricing tier of an Azure service (e.g., F1 = free tier, S1 = standard tier). |
| F1 Tier | IoT Hub's free tier: 8,000 messages per day, maximum one per subscription, includes most features. |
| Partition | A separate stream of data in IoT Hub; more partitions reduce bottlenecks when many services read simultaneously. |
| D2C (Device-to-Cloud) | Messages sent from an IoT device up to the cloud (typically telemetry data). |
| C2D (Cloud-to-Device) | Messages sent from a cloud application down to an IoT device (commands). |
| Direct Method | A cloud-to-device command that requires the device to send back a response confirming whether it succeeded. |
| Device Twin | A JSON document kept in sync between the device and IoT Hub — the device reports its state, and the cloud can set desired configuration. Stored permanently. |
| Connection String | A single text value containing the hub web address, device ID, and shared secret key needed to authenticate to IoT Hub. |
| SharedAccessKey | The secret password component of a connection string; identical copies exist on the device and in IoT Hub. |
| SAS Token (Shared Access Signature) | A one-time-use token sent on first connection: contains the hub URL, an expiry time, and a cryptographic signature to prove the device knows the SharedAccessKey without actually sending it. |
| UNIX Time | A timestamp format counting seconds since midnight January 1, 1970 (UTC). |
| Annotations | Extra properties automatically attached to IoT Hub messages (device ID, enqueue time, sequence number). |
| NTP (Network Time Protocol) | A protocol for keeping a device's clock accurate over the internet; needed because SAS tokens expire based on time. |
| Serverless / FaaS (Functions as a Service) | A cloud model where code runs only when triggered by an event; no server to manage, pay only per execution. |
| Azure Functions | Microsoft's serverless computing service. |
| Trigger | A function inside a Functions App that fires automatically when a specific type of event occurs. |
| Binding | A pre-configured connection between an Azure Function and another Azure service (input binding brings data in; output binding sends data out). |
| Event Hub Trigger | An Azure Function trigger type that fires when a new message arrives on an Event Hub stream (used to consume IoT Hub D2C messages). |
| IoT Hub Registry Manager | A cloud-side tool for viewing registered devices, sending C2D messages, invoking direct methods, and updating device twins. |
| `CloudToDeviceMethod` | The Azure IoT SDK class for building a direct method request to send to a device. |
| Cardinality | A `function.json` setting: `"one"` means process one event per function call; must be manually fixed from the default `"many"` for IoT Hub triggers. |
| Azurite | A local emulator that mimics Azure Storage on your development PC so you can test Functions Apps without connecting to the cloud. |
| `local.settings.json` | A local-only configuration file for Azure Functions (stores connection strings for development); never deployed or committed. |
| Application Settings | The cloud equivalent of `local.settings.json`; set via CLI and read by functions as environment variables. |
| Encryption | Scrambling readable data into unreadable gibberish using a secret key. |
| Decryption | Unscrambling encrypted data back into readable form using a key. |
| Encryption Key | A secret value (like a very long password) used to scramble or unscramble data. |
| Cryptography | The field of techniques for encrypting and decrypting data. |
| Substitution Cipher | A historical encryption method where each letter is replaced by a different letter according to a fixed rule. |
| Caesar Cipher | A substitution cipher that shifts every letter by the same number of positions in the alphabet. |
| Vigenère Cipher | A substitution cipher using a keyword so each letter is shifted by a different amount, making it harder to break. |
| Symmetric Encryption | Encryption where the same key both encrypts and decrypts; faster but requires sharing the key securely. |
| Asymmetric Encryption | Encryption using a public key (encrypt only) and a private key (decrypt only); slower but the private key never leaves its owner. |
| Public Key | The key in asymmetric encryption that anyone can use to encrypt data; cannot decrypt. |
| Private Key | The secret key in asymmetric encryption that only the owner has; can decrypt data encrypted with the matching public key. |
| RSA (Rivest–Shamir–Adleman) | The most widely used mathematical algorithm for generating public/private key pairs. |
| X.509 Certificate | A digital document containing a public key, signed by a trusted authority to prove the key genuinely belongs to the claimed owner. |
| Certification Authority (CA) | A trusted organization that digitally signs X.509 certificates to verify identity. |
| Self-Signed Certificate | An X.509 certificate signed by its own creator instead of a trusted CA; acceptable only for testing. |
| Key Rotation | Switching from a compromised symmetric key to a backup key while the compromised one is regenerated. |
| HSM (Hardware Security Module) | A physical chip on a device that stores secret keys securely; code can use the keys but cannot read the raw key values. |
| `.pem` File | A standard file format for storing cryptographic keys and certificates (Privacy Enhanced Mail). |
| Mirai Botnet | A 2016 attack that took over thousands of IoT devices (all using default passwords) to launch a massive internet disruption. |
| SAS Token Expiry | A time limit on a SAS token (usually 1 day) that prevents attackers from saving and reusing an old token. |

---

## 4. COMPARISONS & TRADEOFFS

### Resistive vs. Capacitive Soil Moisture Sensors (Lesson 6)

| | Resistive | Capacitive |
|---|---|---|
| **How it works** | Two metal probes in soil; electricity flows through water between them | Measures electrical field / charge storage of soil |
| **What moisture does to reading** | More water → lower resistance → **higher** voltage output | More water → **lower** voltage output |
| **Durability** | Probes corrode over time from the electrical current | No exposed metal; more durable |
| **Cost** | Cheaper and simpler | More expensive |
| **Used in CounterFit** | No | Yes (virtual sensor simulates capacitive behavior) |

### GPIO vs. Analog Pins (Lesson 6)

| | GPIO (Digital Only) | Analog Pins |
|---|---|---|
| **What they can read/output** | Only ON (1) or OFF (0) | A range of values (0–1,023 at 10 bits) |
| **ADC built in?** | No — external ADC needed for analog sensors | Yes — ADC is integrated |
| **Where found** | Raspberry Pi, Wio Terminal, Arduino | Wio Terminal, Arduino; NOT on Raspberry Pi natively |
| **Use with soil moisture sensor?** | Only with an external ADC board (e.g., Grove hat) | Direct connection |

### I²C vs. UART vs. SPI (Lesson 6)

| | I²C | UART | SPI |
|---|---|---|---|
| **Number of devices** | Multiple controllers + multiple peripherals | Exactly 2 devices | 1 controller + multiple peripherals |
| **Wires needed** | 2 shared (SDA + SCL) + power/ground | 2 (Tx↔Rx cross-connected) per pair | 4 (COPI, CIPO, SCLK, CS); one extra CS wire per peripheral |
| **How devices are identified** | Each peripheral has a hard-coded address in the message | Only two devices — no addressing needed | Chip Select (CS) wire wakes one peripheral at a time |
| **Speed** | Standard 100 Kbps, Fast 400 Kbps, High Speed 3.4 Mbps | Up to ~6.5 Mbps | No defined limit; often multiple MB/s |
| **Clock** | Yes (SCL wire from controller) | No clock wire — relies on agreed baud rate | Yes (SCLK wire from controller) |
| **Start/Stop framing** | Start and stop conditions on bus | Start bit + stop bit per byte | None needed (clock-synced) |
| **Full-duplex?** | No (half-duplex — shared data wire) | Separate Tx/Rx wires but typically half-duplex | Yes (separate COPI and CIPO wires) |
| **Typical use** | Multiple sensors/actuators on a board | GPS modules, serial consoles, some sensors | Flash memory chips, displays, fast sensors |

### BLE vs. LoRaWAN vs. WiFi vs. Zigbee (Lesson 6)

| | BLE | LoRaWAN | WiFi | Zigbee |
|---|---|---|---|---|
| **Range** | Short (meters) | Long (kilometers) | Medium (tens of meters) | Medium (tens to hundreds of meters) |
| **Power use** | Very low | Very low | Higher | Low |
| **Topology** | Point-to-point or star | Star (devices → hub) | Star (devices → access point) | Mesh (devices relay for each other) |
| **Best for IoT farm use** | No (too short range) | **Yes** — commercial farm soil moisture sensors use this | Maybe (if WiFi covers the field) | Yes — mesh covers large areas without a massive WiFi network |

### Public MQTT Broker vs. Azure IoT Hub (Lesson 8)

| | Public MQTT Broker | Azure IoT Hub |
|---|---|---|
| **Reliability** | No guarantees; can go offline anytime | Professionally maintained; uptime SLA |
| **Security** | Anyone can publish/subscribe | Only registered devices with valid keys/certificates |
| **Performance** | Not designed for scale | Handles millions of messages/day |
| **Discovery** | No device registry | Built-in registry of all known devices |
| **Cost** | Free | Free tier (F1): 8,000 messages/day |

### D2C vs. C2D vs. Direct Method vs. Device Twin (Lesson 8)

| | D2C | C2D | Direct Method | Device Twin |
|---|---|---|---|---|
| **Direction** | Device → Cloud | Cloud → Device | Cloud → Device | Both ways |
| **Response required?** | No | No | **Yes** — device must respond | N/A (synchronized) |
| **Storage duration** | Configurable (default 1 day) | Configurable | Configurable | **Permanent** |
| **Typical use** | Sensor telemetry | App notifications | "Do this thing and confirm" | Device state and configuration |
| **Used in this module?** | Yes (soil moisture) | No | Yes (relay_on / relay_off) | Mentioned, not implemented |

### Symmetric vs. Asymmetric Encryption (Lesson 10)

| | Symmetric | Asymmetric |
|---|---|---|
| **Keys** | One shared key | Public key (encrypt) + Private key (decrypt) |
| **Key sharing** | Both parties must know the key — the key must be shared, which is risky | Private key never shared; public key can be posted publicly |
| **Speed** | Faster | Slower (more complex math) |
| **Security** | Less secure — key interception breaks everything | More secure — private key never leaves its owner |
| **Used in IoT Hub as** | SharedAccessKey → SAS token authentication | X.509 certificate authentication |
| **Real-world combined approach** | Used for bulk data after initial key exchange | Used only to securely exchange the symmetric key |

### Symmetric Key (SAS Token) vs. X.509 Certificate Authentication in IoT Hub (Lesson 10)

| | Symmetric Key / SAS Token | X.509 Certificate |
|---|---|---|
| **What the device needs** | Connection string (SharedAccessKey) | Private key file (.pem) + certificate file (.pem) |
| **How it authenticates** | Creates a SAS token (URL + expiry + encrypted signature); IoT Hub decrypts and verifies | Presents X.509 certificate; IoT Hub verifies the CA signature |
| **Key management** | 2 keys per device for key rotation | One certificate can be shared across many devices |
| **Clock requirement** | **Yes** — accurate NTP-synced clock required (SAS token expires) | No clock dependency |
| **Python SDK method** | `IoTHubDeviceClient.create_from_connection_string()` | `IoTHubDeviceClient.create_from_x509_certificate()` |
| **Self-signed OK?** | N/A (uses hub-generated symmetric key) | Self-signed certificates OK for testing only; production needs CA-signed |

---

## 5. LIKELY EXAM ANGLES

1. **GDD calculation and interpretation (multiple choice + short answer):** "A corn crop has a base temperature of 10°C. On a day with T_max = 22°C and T_min = 14°C, what is the GDD? If the variety needs 800 GDD to mature and has accumulated 720 GDD so far, is it ready to harvest?" Expect the formula GDD = ((T_max + T_min) / 2) − T_base to be applied, and for you to recognize that GDD cannot go below zero (a day below base temperature yields 0 GDD, not a negative number — though the simplified lesson doesn't cover the floor-at-zero rule, the concept is implicit when it says "minimum for growth").

2. **Sensor communication protocols (multiple choice):** "Which protocol uses a chip-select wire to activate one peripheral at a time?" (SPI). "Which protocol requires both devices to agree on a baud rate?" (UART). "Which protocol sends addressed packets over two shared wires?" (I²C). "Which protocol is full-duplex with separate data-in and data-out wires?" (SPI). "Which protocol uses start and stop bits?" (UART). Be able to match protocol names to their defining characteristics.

3. **Relay operation and sensor timing problem (short answer):** "Explain why a relay is needed to control a water pump from an IoT device, and describe the sensor/actuator timing problem in automated irrigation. How does the watering-cycle approach solve it?" Key points: IoT devices output 3.3V–5V at <1A, insufficient for pumps; relay uses an electromagnet to switch a separate high-power circuit; water takes ~20s to soak through to the sensor; naive on-until-wet causes over-watering; solution is 5s pump pulse → 20s wait → re-check → repeat; server unsubscribes from telemetry during the cycle.

4. **Azure IoT Hub communication modes (multiple choice + short answer):** "Which IoT Hub communication mode requires a response from the device?" (Direct Method). "Which mode stores data permanently?" (Device Twin). "How long are D2C messages stored by default?" (1 day). "What service underlies the D2C message path in IoT Hub?" (Azure Event Hubs). "What is the name of the endpoint used to read D2C messages from an Azure Function?" (Event Hub compatible endpoint).

5. **Security concepts and real-world risks (short answer/essay):** "Compare symmetric and asymmetric encryption. Which does IoT Hub use for SAS token authentication vs. X.509 certificate authentication? Give one real-world example of an IoT security failure and what made it possible." Expect: symmetric = one shared key, faster, less secure; asymmetric = public/private key pair, slower, more secure; SAS token = symmetric (SharedAccessKey → HMAC signature); X.509 = asymmetric; Mirai botnet exploited default passwords on DVRs/cameras.

---

## 6. GAPS / AMBIGUITIES

- **GDD floor-at-zero rule not stated:** The lesson presents GDD = ((T_max + T_min) / 2) − T_base but does not explicitly state what happens when the result is negative (i.e., a day entirely below base temperature). In real agronomy, GDD is floored at 0 — a plant does not "lose" accumulated growth on a cold day. The lesson's examples all use above-base temperatures, so this edge case is not addressed. An exam might test this nuance.

- **Resistive sensor voltage direction is under-explained:** Lesson 6 says "for resistive sensors, voltage increases as moisture increases" but doesn't explain the circuit that produces this behavior. The lesson calls both sensor types "analog sensors" and treats them as interchangeable from a code perspective, which could confuse students about why CounterFit's capacitive sensor behaves with the opposite slope.

- **Steinhart-Hart equation is named but not used:** The equation is mentioned as the way temperature sensors convert resistance to temperature, but no formula is given and it never appears in any exercise. It is included as a key term but is unlikely to be tested beyond name recognition.

- **Device Twin concept is introduced but never implemented in code:** Lesson 8 describes Device Twins in detail (synchronized JSON, permanent storage), but no lesson has the student actually create, read, or update a device twin. Exam questions may still ask about the concept based on the text description.

- **C2D messages are defined but never used:** Lesson 8 defines Cloud-to-Device messages as a communication mode, but the project uses Direct Methods (not C2D) for relay control. The distinction between C2D (fire-and-forget, no response required) and Direct Methods (response required) is conceptually important but the student never codes a C2D message.

- **AMQP is mentioned but never explained:** Lesson 8 notes that "under the hood, IoT Hub communication can use MQTT, HTTPS, or AMQP." AMQP (Advanced Message Queuing Protocol) is never defined or described. Students only need to know it exists as a transport option.

- **Quantum computing threat is mentioned but not elaborated:** Lesson 10 notes that quantum computing "may be able to break all known encryption in a very short time." This is a throwaway line with no further context. An exam is unlikely to ask about it in depth, but it could appear as a "which of these poses a future threat to modern cryptography?" question.
