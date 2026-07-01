# IoT Flashcards — Complete Quiz Bank Study Guide

#flashcards

> All 144 questions from the official quiz bank, with explanations written for absolute beginners.

---
## Lesson 1 — Introduction to IoT: Pre-Lecture Quiz

**Q1.** The I in IoT stands for:
- Internet
- Iridium
- Ironing
?
ANSWER: **Internet**
WHY: IoT is short for "Internet of Things," so the first letter simply stands for Internet — the global network that connects all these devices.

**Q2.** What's the estimated number of IoT devices in use by the end of 2020?
- 30
- 30 million
- 30 billion
?
ANSWER: **30 billion**
WHY: By 2020, IoT had already exploded globally — 30 million sounds big but is far too small for a world of sensors and smart devices. 30 is absurdly low.
TRAP: 30 million sounds like a large number, but IoT devices already outnumbered people on Earth.

**Q3.** Smartphones are IoT devices
- True
- False
?
ANSWER: **True**
WHY: A smartphone connects to the internet and has many built-in sensors (camera, GPS, accelerometer). Any device that senses the world and connects to the internet fits the definition of an IoT device.

## Lesson 1 — Introduction to IoT: Post-Lecture Quiz

**Q1.** IoT devices need to be connected to the Internet at all time
- True
- False
?
ANSWER: **False**
WHY: The keyword is "always." Many IoT devices can work offline and sync data later when they reconnect. Think of a fitness tracker that stores steps and uploads them when you open the app.
TRAP: Beginners assume "IoT = internet, so it must always be online." But IoT devices are designed to handle intermittent connections.

**Q2.** IoT devices are always secure
- True
- False
?
ANSWER: **False**
WHY: Security is one of the biggest challenges in IoT. Many cheap or poorly designed devices have weak or no security features. The word "always" makes this statement false — nothing is "always" secure.

**Q3.** AI can be run on low powered IoT devices
- True
- False
?
ANSWER: **True**
WHY: Modern AI models can be compressed into small, efficient versions (called "compact" or "tiny" models) that run directly on low-cost, low-power chips without needing the cloud.

## Lesson 2 — A deeper dive into IoT: Pre-Lecture Quiz

**Q1.** The T in IoT stands for:
- Transistors
- Things
- Turkeys
?
ANSWER: **Things**
WHY: IoT = Internet of Things. The "Things" are the physical objects — sensors, gadgets, appliances — that are connected to the internet.
TRAP: "Transistors" is wrong because transistors are tiny electronic components inside chips, not the devices themselves.

**Q2.** IoT devices gather information from the world around them using:
- Sensors
- Actuators
- Carrier pigeons
?
ANSWER: **Sensors**
WHY: Sensors are components that detect physical conditions (temperature, motion, light, etc.) and convert them into electrical signals that a device can read. Actuators do the opposite — they perform actions.
TRAP: Actuators control the physical world (like motors and lights). They are the OUTPUT, not the INPUT.

**Q3.** IoT devices draw more power than the average desktop or laptop computer
- True
- False
?
ANSWER: **False**
WHY: IoT devices are designed to be small, cheap, and energy-efficient. Many run on small batteries for months or years. A desktop computer draws hundreds of watts; an IoT sensor may draw milliwatts.

## Lesson 2 — A deeper dive into IoT: Post-Lecture Quiz

**Q1.** The three steps in a CPU instruction cycle are:
- Decode, Execute, Fetch
- Fetch, Decode, Execute
- Stop, Collaborate, Listen
?
ANSWER: **Fetch, Decode, Execute**
WHY: The order matters. First the CPU FETCHES (grabs) an instruction from memory, then DECODES (figures out what it means), then EXECUTES (carries it out). Think of it like: read the recipe step → understand it → do it.
TRAP: "Decode, Execute, Fetch" has the wrong order — you can't execute something you haven't fetched yet.

**Q2.** What operating system do Raspberry Pis run?
- They don't run an OS
- Windows 95
- Raspberry Pi OS
?
ANSWER: **Raspberry Pi OS**
WHY: Raspberry Pi OS (formerly called Raspbian) is the official, optimized operating system made specifically for Raspberry Pi hardware. Raspberry Pis do run an OS — they are full computers.
TRAP: Windows 95 is a joke answer. Raspberry Pis definitely run an OS — they're not microcontroller boards.

**Q3.** IoT devices typically run faster and have more memory than the average desktop or laptop computer
- True
- False
?
ANSWER: **False**
WHY: IoT devices are designed to be cheap and low-power, so they deliberately use slower processors and less memory. A typical desktop has gigabytes of RAM; a basic IoT microcontroller may have only kilobytes.

## Lesson 3 — Interact with the physical world with sensors and actuators: Pre-Lecture Quiz

**Q1.** An LED is a sensor:
- True
- False
?
ANSWER: **False**
WHY: An LED (Light Emitting Diode) produces light — it's an output device, not an input device. Sensors detect things; LEDs display or signal things. LED = actuator, not sensor.
TRAP: Beginners may think any electronic component is a "sensor." But if it produces an output (light, motion, sound), it's an actuator.

**Q2.** Sensors are used to:
- Gather data from the physical world
- Control the physical world
- Only monitor temperature
?
ANSWER: **Gather data from the physical world.**
WHY: The word "sensor" comes from "sense" — just like your five senses gather information about the world, electronic sensors gather data about temperature, humidity, light, motion, etc.
<!--SR:!2026-07-04,3,250-->

**Q3.** Actuators are used to:
- True
- False
?
ANSWER: **Control the physical world.**
WHY: The word "actuator" comes from "act" or "activate" — they perform actions. Examples: motors spin, LEDs light up, pumps push water, relays switch power on/off.

## Lesson 3 — Interact with the physical world with sensors and actuators: Post-Lecture Quiz

**Q1.** Digital sensors send data as:
- Voltage ranges
- High and low voltages only
- Emails
?
ANSWER: **High and low voltages only**
WHY: "Digital" means only two states — ON (high voltage) and OFF (low voltage), like 1 and 0 in binary. A button is a digital sensor: it's either pressed or not pressed.
TRAP: "Voltage ranges" describes analog sensors, which can send any value along a continuous range (like a dimmer switch, not just on/off).

**Q2.** What digital signal is sent when a button is pressed?
- 0
- 1
?
ANSWER: **1**
WHY: When you press a button, it completes an electrical circuit, sending a HIGH voltage (represented as 1). When released, it's LOW (0). Press = 1, release = 0.
TRAP: Beginners might pick 0, thinking the button "starts" at rest. But the question asks what signal is sent WHEN pressed.
<!--SR:!2026-07-04,3,250-->

**Q3.** You can control analog actuators from a digital device using pulse-width modulation
- True
- False
?
ANSWER: **True**
WHY: PWM (Pulse-Width Modulation) is a clever trick — it rapidly switches a digital signal on and off so fast that an analog device "sees" it as a varying level. For example, a dimmed LED is actually blinking extremely fast.

## Lesson 4 — Connect your device to the Internet: Pre-Lecture Quiz

**Q1.** IoT devices always need to be connected to the Internet to work:
- True
- False
?
ANSWER: **False**
WHY: "Always" is the trap word. Devices can operate locally without internet and only connect periodically to sync data or receive updates. A smart thermostat still controls your temperature even if the Wi-Fi is down.

**Q2.** IoT devices always communicate over HTTP, the same as web apps and other web APIs:
- False
- True
?
ANSWER: **False**
WHY: HTTP is heavy and power-hungry for small devices. IoT commonly uses lightweight protocols like MQTT (Message Queueing Telemetry Transport), which uses far less bandwidth and battery. "Always" is the red flag.

**Q3.** IoT devices rely on the cloud for all their decision making:
- False
- True
?
ANSWER: **False**
WHY: "All" is the trap. Edge computing allows devices to process data and make decisions locally without sending anything to the cloud. A security camera can detect motion on-device without needing the cloud.

## Lesson 4 — Connect your device to the Internet: Post-Lecture Quiz

**Q1.** Data gathered from sensors and sent to the cloud is called:
- Telemetry
- Commands
- Measurements
?
ANSWER: **Telemetry**
WHY: Telemetry is the standard IoT term for automated data collection and transmission from a remote device to a central system. Think "tele" (far away) + "metry" (measuring) = measuring from afar.
TRAP: "Measurements" is close in meaning, but "telemetry" is the precise technical term used in IoT.

**Q2.** What should happen to a command if the IoT device is offline:
- It should always be resent when the device is back online
- It should never be resent when the device is back online
- It depends on the command, the device and the requirements of the IoT app
?
ANSWER: **It depends on the command, the device and the requirements of the IoT app**
WHY: There is no one-size-fits-all rule. A "turn on lights" command might expire after 30 seconds (no point turning lights on if the person left). A firmware update command might need to be queued and delivered whenever the device reconnects. Context always matters.
TRAP: Beginners look for a simple yes/no answer, but real IoT systems must handle each scenario differently.

**Q3.** MQTT, or Message Queueing Telemetry Transport, has message queues:
- True
- False
?
ANSWER: **False**
WHY: Despite the word "Queueing" in the name, MQTT does NOT actually use message queues. It uses a publish/subscribe model — devices publish messages to topics, and other devices subscribe to those topics to receive them. The name is misleading.
TRAP: "It's in the name, so it must be true" — this is a classic trick question. The name is historical and doesn't reflect the actual architecture.

## Lesson 5 — Predict plant growth: Pre-Lecture Quiz

**Q1.** IoT devices can be used to support agriculture
- True
- False
?
ANSWER: **True**
WHY: IoT sensors can monitor soil moisture, temperature, light levels, and humidity — all critical for farming. Farmers use IoT to make data-driven decisions about irrigation, fertilization, and harvesting.

**Q2.** Plant needs include: (pick the best answer)
- Carbon dioxide, water, nutrients
- Carbon dioxide, water, nutrients, light
- Carbon dioxide, water, nutrients, light, warmth
?
ANSWER: **Carbon dioxide, water, nutrients, light, warmth**
WHY: The question says "pick the best answer" — this means choose the most complete list. Plants need ALL five for photosynthesis and healthy growth. The other options leave something out.
TRAP: Three-ingredient or four-ingredient lists seem complete, but "best answer" means the one that lists everything plants need.

**Q3.** Sensors are too expensive for farmers in developed nations to use:
- False
- True
?
ANSWER: **False**
WHY: IoT sensors have become very affordable in recent years. Farmers in developed nations already widely use precision agriculture technology including soil sensors, drones, and GPS-guided equipment.

## Lesson 5 — Predict plant growth: Post-Lecture Quiz

**Q1.** Plant growth is dependant on temperature
- True
- False
?
ANSWER: **True**
WHY: Temperature directly controls the speed of chemical reactions inside plants. Too cold = growth stops entirely. Too hot = enzymes break down. Each plant has a specific temperature range where it grows best.

**Q2.** The temperatures to consider for plant growth are:
- Minimum, maximum
- Base, optimal, maximum
- Maximum only
?
ANSWER: **Base, optimal, maximum**
WHY: These are the three key temperature thresholds for any plant: Base = the minimum temperature where growth begins. Optimal = the temperature where growth is fastest. Maximum = the temperature above which growth stops (the plant gets heat stress).
TRAP: "Minimum, maximum" misses the optimal — the middle range where plants actually thrive.

**Q3.** Growing Degree Days are calculated using which formula:
- (day max + day min) - plant base
- ((day max + day min) / 2) - plant base
- ((day min + plant base) / 2)
?
ANSWER: **((day max + day min) / 2) - plant base**
WHY: GDD measures heat accumulation over time. First, you average the day's high and low temperatures (add them, divide by 2). Then subtract the plant's base temperature — the minimum temperature at which that plant grows. This tells you how much "growing heat" the plant received that day.
TRAP: The formula without dividing by 2 gives you the sum, not the average — it would dramatically overestimate growth.

## Lesson 6 — Detect soil moisture: Pre-Lecture Quiz

**Q1.** IoT devices can be used to detect ambient properties like soil moisture
- True
- False
?
ANSWER: **True**
WHY: Soil moisture sensors are a standard IoT component, especially in smart agriculture. They measure how much water is in the soil and send that data for analysis and automated watering decisions.

**Q2.** Which of these can cause problems for plant growth (pick one)?
- Too little water
- Too much water
- Too little or too much water
?
ANSWER: **Too little or too much water**
WHY: Both extremes are harmful. Too little water = wilting and death from dehydration. Too much water = roots rot because they can't get oxygen. The correct answer is the one that covers both dangers.
TRAP: Picking only "too little" or only "too much" ignores the other half of the problem.

**Q3.** All sensors are provided pre-calibrated for standard units:
- True
- False
?
ANSWER: **False**
WHY: "All" is rarely true in technology. Many sensors need to be calibrated by the user — factors like manufacturing variance, environment, and voltage levels mean each sensor may read slightly differently until calibrated against a known standard.

## Lesson 6 — Detect soil moisture: Post-Lecture Quiz

**Q1.** When measuring soil moisture, one difference between resistive and capacitive moisture sensors is:
- As moisture levels go up the voltage goes up for resistive sensors and down for capacitive sensors
- As moisture levels go up the voltage goes down for resistive sensors and up for capacitive sensors
- As moisture levels go up the voltage goes up for both resistive and capacitive sensors
?
ANSWER: **As moisture levels go up the voltage goes up for resistive sensors and down for capacitive sensors**
WHY: Resistive sensors: more water = more electrical conductivity between the probes = voltage rises. Capacitive sensors: more water changes the electrical field in the opposite way, so the voltage drops. They behave in opposite directions as moisture changes.
<!--SR:!2026-07-04,3,250-->

**Q2.** The SPI protocol supports:
- Only one controller and only one peripheral
- Only one controller and multiple peripherals
- Multiple controllers and multiple peripherals
?
ANSWER: **Only one controller and multiple peripherals**
WHY: SPI (Serial Peripheral Interface) uses a master-slave architecture. There is one "boss" (controller/master) that controls all communication, and multiple "workers" (peripherals/slaves) that only respond when the controller talks to them.

**Q3.** The I2C protocol supports:
- Only one controller and only one peripheral
- Only one controller and multiple peripherals
- Multiple controllers and multiple peripherals
?
ANSWER: **Multiple controllers and multiple peripherals**
WHY: I2C (Inter-Integrated Circuit) is more flexible than SPI. It supports multiple controllers on the same bus and multiple peripherals, with each device having a unique address. This makes it ideal for connecting many different sensors to one system.
<!--SR:!2026-07-04,3,250-->

## Lesson 7 — Automated plant watering: Pre-Lecture Quiz

**Q1.** IoT devices are powerful enough to control water pumps
- True
- False
?
ANSWER: **False**
WHY: IoT devices run on low voltage (typically 3.3V or 5V) and can't provide the high current needed to drive a pump directly. They need a relay — a switch that lets the low-power device control a high-power circuit. The IoT device controls the relay; the relay controls the pump.
TRAP: "They can control pumps" is true ONLY with a relay in between. The device by itself cannot.

**Q2.** Actuators can be used to control power to additional devices
- True
- False
?
ANSWER: **True**
WHY: A relay is a type of actuator that switches power on and off to another device. This is how a tiny IoT board can turn on a large water pump, a heater, or a lighting system.

**Q3.** Sensors detect changes from actuators immediately
- True
- False
?
ANSWER: **False**
WHY: There is always a delay. If a pump starts watering soil, it takes time for the water to soak in and reach the moisture sensor. If a heater turns on, the temperature sensor won't register the change instantly. Physical processes take time.
<!--SR:!2026-07-04,3,250-->

## Lesson 7 — Automated plant watering: Post-Lecture Quiz

**Q1.** A relay is what type of switch:
- Electrical
- Electromechanical
- Mechanical
?
ANSWER: **Electromechanical**
WHY: A relay combines electrical and mechanical parts: an electromagnet (electrical) physically moves a metal contact (mechanical) to open or close a circuit. That's what "electromechanical" means.
TRAP: "Electrical" would mean purely electronic with no moving parts. "Mechanical" would mean purely physical. A relay is both.

**Q2.** A relay allows:
- A low power device to control a higher power device
- A high power device to control a low power device
- Runners to run a race passing a baton between them
?
ANSWER: **A low power device to control a higher power device**
WHY: This is the entire purpose of a relay — it's a bridge. A tiny 3.3V signal from a microcontroller energizes an electromagnet, which physically closes a switch on a separate high-voltage circuit (like a 120V water pump). The low-power side and high-power side are electrically isolated.
TRAP: It's not the other way around — a high-power device doesn't need a relay to control a low-power device.

**Q3.** Actuators should always respond instantly to sensor readings:
- True
- False
?
ANSWER: **False**
WHY: Instant response can be wasteful or harmful. If a moisture sensor reads "dry" for one second, you don't want the pump to turn on — the soil might be temporarily dry on the surface but wet underneath. Delays, averaging, and thresholds prevent over-reaction.

## Lesson 8 — Migrate your plant to the cloud: Pre-Lecture Quiz

**Q1.** A public MQTT broker is fine to use for a commercial IoT project
- True
- False
?
ANSWER: **False**
WHY: Public MQTT brokers have no security guarantees — anyone can listen to your data or even send fake commands to your devices. Commercial projects need private, secured infrastructure.
TRAP: Public brokers work for learning and prototyping, but "commercial" implies real products with real security requirements.

**Q2.** Cloud computing allows you to:
- Only rent computers
- Rent computers and application platforms only
- Rent computers, application platforms, software, serverless platforms and other services
?
ANSWER: **Rent computers, application platforms, software, serverless platforms and other services**
WHY: The cloud is not just about renting virtual machines. It's a full ecosystem: you can rent raw computing power (IaaS), pre-built platforms (PaaS), ready-to-use software (SaaS), and serverless functions that run only when triggered. The most complete answer is correct.
<!--SR:!2026-07-04,3,250-->

**Q3.** There are multiple cloud vendors with data centers in many different countries across 6 continents
- True
- False
?
ANSWER: **True**
WHY: Major cloud providers (Microsoft Azure, Amazon AWS, Google Cloud) have data centers on every inhabited continent — North America, South America, Europe, Asia, Africa, and Australia — giving them near-global coverage.

## Lesson 8 — Migrate your plant to the cloud: Post-Lecture Quiz

**Q1.** To request control of an actuator and get a response from an IoT device, app code can use a:
- Device to cloud message
- Device twin
- Direct method request
?
ANSWER: **Direct method request**
WHY: A direct method is a cloud-to-device command that asks the device to do something immediately AND waits for a response (like "turn on pump" → "pump turned on"). It's a request-reply pattern.
TRAP: "Device twin" stores device state/properties but doesn't issue immediate commands. "Device to cloud message" goes the opposite direction (device → cloud).

**Q2.** IoT Hub lets any device connect without any security:
- False
- True
?
ANSWER: **False**
WHY: IoT Hub requires every device to authenticate before connecting. This is fundamental — an unsecured hub would be a massive security risk. Devices typically authenticate using connection strings or certificates.

**Q3.** IoT Hub names must be unique:
- True
- False
?
ANSWER: **True**
WHY: The IoT Hub name becomes part of a public URL (like `yourhub.azure-devices.net`). URLs must be globally unique across all of Azure — no two IoT Hubs can share the same name, just like no two websites can share the same domain.
<!--SR:!2026-07-04,3,250-->

## Lesson 9 — Migrate your application logic to the cloud: Pre-Lecture Quiz

**Q1.** You can use Serverless code to respond to IoT events
- True
- False
?
ANSWER: **True**
WHY: Serverless functions (like Azure Functions) can be set to trigger automatically whenever new data arrives from an IoT device. You don't need a full-time running server — the code runs only when there's work to do, saving cost and complexity.

**Q2.** When you send IoT events to IoT Hub:
- Only one service can read events off the IoT Hub
- Any number of services can read events off the IoT Hub
- Services cannot read events from IoT Hub, they have to connect to the device directly
?
ANSWER: **Any number of services can read events off the IoT Hub**
WHY: IoT Hub supports multiple consumer groups. Each service that reads from the hub gets its own independent copy of the data stream. You could have one service storing data, another analyzing it, and a third sending alerts — all reading the same events independently.

**Q3.** When reading events off IoT hub, you can only do so using code that runs in the cloud
- True
- False
?
ANSWER: **False**
WHY: You can read IoT Hub events from anywhere — a local server in your office, an on-premises data center, or even another IoT device. The hub is accessible from any network, not just cloud services. The word "only" makes this false.
<!--SR:!2026-07-02,1,230-->

## Lesson 9 — Migrate your application logic to the cloud: Post-Lecture Quiz

**Q1.** Azure Functions can be run and debugged locally:
- True
- False
?
ANSWER: **True**
WHY: You can develop and test serverless functions on your own computer before deploying them to the cloud. The Azure Functions runtime runs locally, letting you set breakpoints, inspect variables, and fix bugs just like any other code.

**Q2.** Serverless code can only be written in JavaScript and COBOL:
- False
- True
?
ANSWER: **False**
WHY: "Only" and the mention of COBOL (a very old language from the 1960s) are both clues that this is false. Serverless platforms support many modern languages: C#, Python, Java, TypeScript, PowerShell, Go, and more.
TRAP: COBOL is a joke red herring — no modern serverless platform primarily uses COBOL.

**Q3.** When deploying a Functions App to the cloud, you need to create and deploy:
- A Functions App only
- A Functions App and a Storage Account only
- A Functions App, a Storage Account, and Application Settings
?
ANSWER: **A Functions App, a Storage Account, and Application Settings**
WHY: All three are required. The Functions App is the container that runs your code. The Storage Account stores logs, triggers, and function code. Application Settings hold configuration values like connection strings and API keys. You can't deploy with just one or two of these.

## Lesson 10 — Keep your plant secure: Pre-Lecture Quiz

**Q1.** IoT devices are always secure
- True
- False
?
ANSWER: **False**
WHY: This question appears multiple times because it's one of the most important concepts in IoT. IoT security is hard — many devices ship with default passwords, unencrypted connections, or unpatched vulnerabilities. Never assume "always secure."

**Q2.** There are no documented cases of hackers using an IoT device to hack into a network:
- True
- False
?
ANSWER: **False**
WHY: There are many well-documented real-world cases. In one famous example, hackers breached a casino's database through an internet-connected fish tank thermometer. IoT devices are a common entry point for cyberattacks because they're often the weakest link in network security.

**Q3.** You can share your IoT device connection string with anyone
- True
- False
?
ANSWER: **False**
WHY: A connection string is like a password that grants access to your IoT Hub. Sharing it with anyone gives them the ability to impersonate your device, send fake data, or receive commands meant for your device. Treat connection strings like passwords.

## Lesson 10 — Keep your plant secure: Post-Lecture Quiz

**Q1.** Symmetric key encryption compares to asymmetric key encryption in which ways:
- Symmetric key encryption is slower than asymmetric
- Symmetric key encryption is more secure than asymmetric
- Symmetric key encryption is faster than asymmetric, but less secure
- Symmetric key encryption is slower than asymmetric, but more secure
?
ANSWER: **Symmetric key encryption is faster than asymmetric, but less secure**
WHY: Symmetric = one shared key for both encrypting and decrypting. It's fast because it uses simpler math, but risky — if anyone steals the key, they can both read AND forge messages. Asymmetric = two keys (public + private). It's slower but more secure because the private key never needs to be shared.
TRAP: Don't mix up which is faster and which is more secure. Symmetric = FAST (good for IoT devices). Asymmetric = MORE SECURE (good for initial authentication).

**Q2.** Self-signed X.509 certificates are ideal for a production environment
- True
- False
?
ANSWER: **False**
WHY: Self-signed certificates are not trusted by any certificate authority — they're like making your own ID card instead of getting a government-issued one. For real production systems, you need certificates issued by a trusted Certificate Authority (CA) that browsers and services will accept.

**Q3.** X.509 certificates:
- Should never be shared between IoT devices
- Can be shared between devices
- Should be kept secure and never used by any devices
?
ANSWER: **Can be shared between devices**
WHY: Unlike symmetric keys (which should ideally be unique per device), X.509 certificates can technically be installed on multiple devices. This is useful when you want a group of devices to authenticate using the same certificate. However, best practice often still favors unique certificates per device.

## Lesson 11 — Location tracking: Pre-Lecture Quiz

**Q1.** Your location can be defined using
- Latitude only
- Longitude only
- Latitude and Longitude
?
ANSWER: **Latitude and Longitude**
WHY: You need both coordinates. Latitude tells you how far north or south you are (horizontal lines on a map). Longitude tells you how far east or west you are (vertical lines). One without the other gives you only a line, not a point.
TRAP: Latitude or longitude alone can't pinpoint a location — it's like giving someone your street name but not your house number.

**Q2.** The types of sensors that can track your location are called:
- GPS
- PGP
- GIF
?
ANSWER: **GPS**
WHY: GPS (Global Positioning System) is the satellite network that provides location data. A GPS receiver in your device listens to signals from orbiting satellites and calculates your position.
TRAP: PGP is encryption software. GIF is an image format. Only GPS does location.

**Q3.** There is no value in tracking vehicle locations
- True
- False
?
ANSWER: **False**
WHY: Vehicle tracking has enormous value in fleet management (delivery trucks), logistics (when will my package arrive?), ride-sharing (Uber/Lyft), theft recovery, and even insurance (safe driving discounts). The statement is clearly false.

## Lesson 11 — Location tracking: Post-Lecture Quiz

**Q1.** GPS data is sent from sensors using:
- Latitude and Longitude coordinates
- Addresses
- NMEA sentences
?
ANSWER: **NMEA sentences**
WHY: NMEA (National Marine Electronics Association) is the standard text format that GPS modules use. An NMEA sentence looks like a coded string of text containing latitude, longitude, altitude, speed, and other data all in one line. It's the "language" GPS modules speak.
TRAP: Latitude and longitude are the DATA inside the NMEA sentence, not the format/way the data is transmitted. The question asks how the data is SENT.

**Q2.** To get a good GPS fix you need to receive signals from at least how many satellites
- 1
- 2
- 3
?
ANSWER: **3**
WHY: You need at least 3 satellites for triangulation (2D position on Earth's surface). Each satellite gives you a distance, and where the three distance spheres intersect is your location. Four satellites give you altitude too (3D fix), but the minimum for a "good fix" is 3.

**Q3.** GPS sensors send data over:
- SPI
- UART
- Email
?
ANSWER: **UART**
WHY: UART (Universal Asynchronous Receiver-Transmitter) is a simple serial communication protocol. GPS modules almost always use UART to send NMEA sentences to a microcontroller, because it's simple, reliable, and doesn't require a clock signal.
TRAP: SPI is another protocol, but it's not what standard GPS modules typically use for their primary data output.

## Lesson 12 — Store location data: Pre-Lecture Quiz

**Q1.** IoT data is stored by IoT Hub
- True
- False
?
ANSWER: **False**
WHY: IoT Hub is a message broker — it receives and routes messages, but it does NOT store them long-term. Think of it as a post office: it handles delivering mail but doesn't keep the letters forever. You need a separate database or storage service to actually keep the data.
TRAP: It seems logical that a "hub" would store things. But in Azure, IoT Hub passes data through; you must set up storage separately.

**Q2.** Data can be divided into the following two types
- Blob and table
- Structured and unstructured
- Red and blue
?
ANSWER: **Structured and unstructured**
WHY: Structured data = organized in tables with rows and columns (like a spreadsheet of temperature readings). Unstructured data = free-form with no predefined format (like images, videos, audio recordings, or raw text). These are the two fundamental categories of all data.

**Q3.** Serverless code can be used to write IoT data to a database
- True
- False
?
ANSWER: **True**
WHY: This is one of the most common IoT patterns: IoT Hub receives data → triggers a serverless function → the function writes the data to a database. The whole pipeline runs automatically with no permanent server running.

## Lesson 12 — Store location data: Post-Lecture Quiz

**Q1.** IoT data that needs to be processed immediately is on which path:
- Hot
- Warm
- Cold
?
ANSWER: **Hot**
WHY: The hot path = real-time processing. Data is analyzed the moment it arrives (like detecting an intruder from a security sensor). Warm path = processed within minutes/hours. Cold path = stored for later batch analysis (like monthly reports). "Hot" means "now."

**Q2.** Azure storage has the following storage types:
- Boxes, tubs, bins
- Blob, table, queue and file
- Hot, warm, cold
?
ANSWER: **Blob, table, queue and file**
WHY: These are the four core Azure storage services: Blob = for unstructured objects (images, videos, backups). Table = for structured NoSQL data. Queue = for message queuing between apps. File = for file shares accessible via SMB protocol.
TRAP: "Hot, warm, cold" are data processing paths, not storage types. "Boxes, tubs, bins" is a joke answer.

**Q3.** Azure Functions can be bound to database to write return values to the database
- True
- False
?
ANSWER: **True**
WHY: Azure Functions support output bindings — you can configure a function so that its return value is automatically written to a database table. This eliminates the need to write database connection code manually. It's a key serverless feature.

## Lesson 13 — Visualize location data: Pre-Lecture Quiz

**Q1.** Very large tables of data are an easy way to quickly look up data
- True
- False
?
ANSWER: **False**
WHY: Large tables without proper indexing become slow to query. As data grows, you need indexes (like a book's index), aggregation, and summarization to maintain fast lookups. Raw large tables get slower, not easier.

**Q2.** GPS data can be visualized on maps
- True
- False
?
ANSWER: **True**
WHY: GPS coordinates (latitude, longitude) map directly to points on a map. This is the most natural visualization for location data — each GPS reading becomes a dot or marker on a map.

**Q3.** On maps of large areas, the same distance drawn on the map represents the same distance on the real world no matter where on the map the measurement is taken
- True
- False
?
ANSWER: **False**
WHY: Map projections distort distances because you're flattening a sphere onto a rectangle. On a Mercator projection (like Google Maps), Greenland looks as big as Africa, but Africa is actually 14 times larger. A centimeter near the poles represents much more real-world distance than a centimeter near the equator.
TRAP: This seems like it should be true on an intuitive level, but the Earth is round and maps are flat — something has to distort.

## Lesson 13 — Visualize location data: Post-Lecture Quiz

**Q1.** The service to draw maps on a web page is called:
- Azure Maps
- Azure Atlas
- Azure World VIsualizer
?
ANSWER: **Azure Maps**
WHY: Azure Maps is Microsoft's mapping platform — it provides APIs and SDKs to display interactive maps on websites and in apps, similar to Google Maps but integrated with the Azure ecosystem.
TRAP: "Azure Atlas" and "Azure World Visualizer" are made-up names that sound plausible but don't exist.

**Q2.** Azure maps plots data using:
- GeoJSON
- Lists of latitude and longitude
- Lists of addresses
?
ANSWER: **GeoJSON**
WHY: GeoJSON is a standard format for encoding geographic data in JSON (JavaScript Object Notation). It can represent points, lines, and polygons with their coordinates. Azure Maps uses GeoJSON as its primary data format for plotting locations.
TRAP: "Lists of latitude and longitude" describes what's inside GeoJSON, but GeoJSON is the actual format specification Azure Maps expects.

**Q3.** Blobs can be retrieved via a URL
- True
- False
?
ANSWER: **True**
WHY: Every blob in Azure Blob Storage gets a unique URL. If the blob is publicly accessible, anyone with the URL can access it. If private, you need authentication (a shared access signature appended to the URL).

## Lesson 14 — Geofences: Pre-Lecture Quiz

**Q1.** GPS coordinates can be used to check if something is in a defined area
- True
- False
?
ANSWER: **True**
WHY: A geofence is a virtual boundary defined by GPS coordinates (like drawing a circle or polygon on a map). You can check whether a given GPS coordinate falls inside that boundary — this is the core concept of geofencing.

**Q2.** GPS is incredibly accurate so can indicate with precision of less than 1M when a device enters a given area
- True
- False
?
ANSWER: **False**
WHY: Consumer GPS accuracy is typically 5-10 meters, not under 1 meter. Buildings, trees, weather, and satellite geometry all degrade accuracy. Sub-meter GPS exists but requires expensive specialized equipment, not standard smartphone/sensor GPS.
TRAP: Movies and TV shows make GPS seem pinpoint-accurate. Real-world consumer GPS is much rougher.

**Q3.** Geofences are useful when tracking vehicles to:
- Determine when a vehicle enters a given area only
- Determine when a vehicle leaves a given area only
- Determine when a vehicle enters or leaves a given area
?
ANSWER: **Determine when a vehicle enters or leaves a given area**
WHY: Both events are valuable. Entering triggers actions like "welcome" messages, fare calculations, or "arrived at destination." Leaving triggers alerts like "vehicle left the depot" or "truck departed the warehouse." You need both.
TRAP: Choosing only "enters" or only "leaves" gives you only half the picture.

## Lesson 14 — Geofences: Post-Lecture Quiz

**Q1.** To have multiple services pull data from an IoT Hub, you need to create multiple:
- Consumer groups
- Pipes
- IoT Hubs
?
ANSWER: **Consumer groups**
WHY: A consumer group gives a service its own independent view of the data stream, with its own cursor/position tracking. If two services share a consumer group, they'll split the data. Separate consumer groups = each service sees all data independently.

**Q2.** The default search buffer for a geofence call is:
- 5m
- 50m
- 500m
?
ANSWER: **50m**
WHY: The 50-meter buffer accounts for GPS inaccuracy. Instead of checking exactly on the boundary line (which GPS might miss), the system checks a 50-meter wide zone around the boundary. This prevents false negatives where a device is right at the edge but GPS says it's slightly outside.

**Q3.** Points inside the geofence have a distance:
- Less than 0 (a negative value)
- Greater than 0 (a positive value)
?
ANSWER: **Less than 0 (a negative value)**
WHY: The geofence API returns a signed distance: negative values mean INSIDE the boundary (how deep inside), zero means exactly ON the boundary, and positive values mean OUTSIDE (how far away). Think of it like being inside a building: negative floors are the basement.

## Lesson 15 — Train a fruit quality detector: Pre-Lecture Quiz

**Q1.** Cameras can be used as IoT sensors
- True
- False
?
ANSWER: **True**
WHY: A camera captures visual data from the physical world — that's exactly what a sensor does. In IoT, cameras are used for quality inspection, security monitoring, traffic analysis, facial recognition, and many other sensing tasks.

**Q2.** Fruit can be sorted using cameras
- True
- False
?
ANSWER: **True**
WHY: Computer vision AI can analyze images of fruit to detect ripeness, bruises, size, and color — then trigger automated sorting systems to separate good fruit from bad. This is already used in real-world food processing plants.

**Q3.** Images-based AI models are incredibly complex and time consuming to train, requiring hundreds of thousands of images:
- True
- False
?
ANSWER: **False**
WHY: Transfer learning changes this completely. You start with a model already trained on millions of general images, then "fine-tune" it with just a small set of your specific images (as few as 5 per category). This takes minutes, not weeks.

## Lesson 15 — Train a fruit quality detector: Post-Lecture Quiz

**Q1.** The technique custom vision uses to train a model with only a few images is called:
- Transformational learning
- Transaction learning
- Transfer learning
?
ANSWER: **Transfer learning**
WHY: Transfer learning = "transferring" knowledge from a big pre-trained model to your specific task. The base model already knows what edges, shapes, and textures look like. You just teach it your specific categories (ripe vs. unripe fruit). This is why you don't need thousands of images.
TRAP: "Transformational learning" and "transaction learning" sound similar but are made-up terms.

**Q2.** Image classifiers can be trained using:
- Only 1 image per tag
- At least 5 images per tag
- At least 50 images per tag
?
ANSWER: **At least 5 images per tag**
WHY: Custom Vision's minimum requirement is 5 labeled images per category/tag to train a classifier. More images = better accuracy, but 5 is the hard minimum to get started.
TRAP: 1 image is too few for the AI to learn what makes that category unique. 50 is enough but the question asks for the MINIMUM.

**Q3.** The hardware that allows ML models to be trained quickly, as well as making the graphics on our Xbox look amazing are called:
- PGU
- GPU
- PUG
?
ANSWER: **GPU**
WHY: GPU = Graphics Processing Unit. Originally designed for video game graphics, GPUs turned out to be perfect for machine learning because both tasks require doing thousands of simple math operations in parallel. Training AI and rendering games use the same kind of hardware.
TRAP: "PGU" and "PUG" are nonsense acronyms. GPU is the real term.
<!--SR:!2026-07-04,3,250-->

## Lesson 16 — Check fruit quality from an IoT device: Pre-Lecture Quiz

**Q1.** IoT devices are not powerful enough to use cameras:
- True
- False
?
ANSWER: **False**
WHY: Many IoT devices (especially single-board computers like Raspberry Pi) have dedicated camera ports and enough processing power to capture and process images. The statement says "not powerful enough," which is too absolute.
<!--SR:!2026-07-04,3,250-->

**Q2.** Camera sensors use film to capture images
- True
- False
?
ANSWER: **False**
WHY: Digital camera sensors use electronic light-sensing chips (CMOS or CCD sensors), not physical film. These chips convert light into electrical signals pixel by pixel. Film is analog photography technology, not digital.
TRAP: Don't confuse traditional film cameras with modern digital sensors. IoT uses digital.

**Q3.** Camera sensors send which type of data
- Digital
- Analog
?
ANSWER: **Digital**
WHY: Modern digital camera sensors output digital data — each pixel is represented as a number (or three numbers for color: red, green, blue). This digital data can then be processed by software and AI models.
TRAP: While light is analog, the camera sensor CONVERTS it to digital output. The question asks what type of data the sensor SENDS.

## Lesson 16 — Check fruit quality from an IoT device: Post-Lecture Quiz

**Q1.** A published version of a custom vision model is called an:
- Iteration
- Instance
- Iguana
?
ANSWER: **Iteration**
WHY: Every time you train and publish a model in Custom Vision, it creates a new "iteration" — a numbered version of your model. Iteration 1 might have mediocre accuracy; Iteration 5 might be much better after adding more training images.
TRAP: "Instance" sounds similar but isn't the term Custom Vision uses. "Iguana" is a joke answer (the reptile).
<!--SR:!2026-07-04,3,250-->

**Q2.** When images are sent for classification, they then become available to retrain the model:
- True
- False
?
ANSWER: **True**
WHY: Custom Vision can store the images you submit for prediction and let you tag them later. These real-world images from actual usage are extremely valuable for improving model accuracy because they show exactly what the model encounters in practice.

**Q3.** You don't need to use images captured from an IoT device to train the model as the cameras are as good quality as phone cameras:
- True
- False
?
ANSWER: **False**
WHY: IoT device cameras often have different quality, angle, lighting conditions, and resolution than phone cameras. Training with images from the actual device the model will run on produces much better real-world accuracy. Phone images may not represent what the IoT camera sees.
<!--SR:!2026-07-01,0,230-->

## Lesson 17 — Run your fruit detector on the edge: Pre-Lecture Quiz

**Q1.** Edge computing can be more secure than cloud computing.
- True
- False
?
ANSWER: **True**
WHY: Processing data locally on the edge device means sensitive data never has to travel over the internet or sit on someone else's server. If you're analyzing security camera footage, processing it on-device means the video never leaves your building.

**Q2.** Running an ML model on an edge device is less accurate than running an ML model in the cloud.
- True
- False
?
ANSWER: **False**
WHY: It's the same model with the same weights and parameters — accuracy doesn't change based on WHERE the model runs. A model that's 95% accurate in the cloud is still 95% accurate on an edge device. The only difference is speed and resource usage.
TRAP: Beginners might think "edge = weaker = less accurate." But the math is identical regardless of location.
<!--SR:!2026-07-04,3,250-->

**Q3.** Edge devices always need an Internet connection.
- True
- False
?
ANSWER: **False**
WHY: The whole point of edge computing is local processing WITHOUT needing the cloud. An edge device can run its AI model, make decisions, and control actuators completely offline. Internet is only needed when you want to sync data or receive updates.
TRAP: "Always" is the red flag. Edge devices CAN work offline by design.

## Lesson 17 — Run your fruit detector on the edge: Post-Lecture Quiz

**Q1.** What kind of format or domain do we need for Custom Vision ML models to properly run on an edge device?
- General
- Quick Training
- Standard
- Compact
- Food
- Remote Deployment
?
ANSWER: **Compact**
WHY: Compact models are optimized versions that are smaller in file size and use less memory — specifically designed to run on resource-constrained edge devices. A regular model might be too large or too slow for a small IoT device.
TRAP: "General" and "Food" are classification DOMAINS (what the model detects), not the deployment FORMAT. The question asks about the format.

**Q2.** What is a container?
- Self-contained applications that hold ML models
- Self-contained applications that run in isolation from other programs
- Self-contained applications that run programs only on edge devices
- self-contained applications that handle communication between the cloud and edge devices
?
ANSWER: **Self-contained applications that run in isolation from other programs.**
WHY: A container packages an application with everything it needs to run (code, libraries, settings) into one portable unit. "Isolation" is key — containers don't interfere with each other or the host system. They run the same way on any device.
TRAP: Containers aren't only for ML models, only for edge devices, or only for cloud communication. They're a general-purpose packaging technology.

**Q3.** How do you do Custom Vision model retraining for ML models deployed on edge devices?
- Take images on the edge device, save to the edge device, and point the ML model to the new image folder
- Upload images from the edge device to the cloud, retrain the model in Custom Vision, then re-deploy onto the edge device
- Take images on the edge device and check the prediction output
?
ANSWER: **Upload images from the edge device to the cloud, retrain the model in Custom Vision, then re-deploy onto the edge device.**
WHY: The edge device collects images and runs the current model, but the actual TRAINING happens in the cloud (Custom Vision service requires cloud resources). After retraining, you download the new improved model and deploy it back to the edge device. It's a cycle: collect → upload → retrain → redeploy.

## Lesson 18 — Trigger fruit quality detection from a sensor: Pre-Lecture Quiz

**Q1.** Which part of your IoT application gathers data?
- Things
- Cloud services
- Edge devices
?
ANSWER: **Things**
WHY: The "Things" in IoT are the physical devices with sensors — they're the ones that directly interact with the real world and collect data. Cloud services process data, edge devices run logic, but only the "things" gather the raw data.

**Q2.** The only outputs of an IoT application are actuators.
- True
- False
?
ANSWER: **False**
WHY: "Only" makes this false. Outputs include actuators (physical actions), but also: dashboard displays, email/SMS alerts, database records, reports, API responses, and notifications to other systems. IoT applications have many types of output.

**Q3.** Things don't need to connect directly to IoT Hub, they can use edge devices as gateways.
- True
- False
?
ANSWER: **True**
WHY: An edge device can act as a gateway — small, low-power sensors talk to the edge device locally (via Bluetooth, Zigbee, etc.), and the edge device aggregates their data and forwards it to IoT Hub. This is a very common IoT architecture pattern.

## Lesson 18 — Trigger fruit quality detection from a sensor: Post-Lecture Quiz

**Q1.** The three components of architecting an IoT application are
- Things, Insights, Actions
- Things, Internet, Databases
- AI, Blockchain, FizzBuzzers
?
ANSWER: **Things, Insights, Actions**
WHY: This is the fundamental IoT architecture: THINGS gather data from the physical world → INSIGHTS process and analyze that data to find meaning → ACTIONS respond based on those insights (send alerts, trigger actuators, update dashboards).
TRAP: "Things, Internet, Databases" misses the decision-making and action components. "AI, Blockchain, FizzBuzzers" is a joke answer.

**Q2.** The component that communicates between the things and the components that create insights is:
- Azure Functions
- IoT Hub
- Azure Maps
?
ANSWER: **IoT Hub**
WHY: IoT Hub sits in the middle as the messaging bridge. Things send data to IoT Hub; services that create insights read from IoT Hub. It decouples the data producers from the data consumers so neither needs to know about the other directly.

**Q3.** How do time of flight proximity sensors work?
- They send laser beams and time how long till they bounce off an object
- They use sound and measure how long till the sound bounces off an object
- They use very large rulers
?
ANSWER: **They send laser beams and time how long till they bounce off an object**
WHY: "Time of flight" literally means measuring how long light takes to travel. The sensor fires a laser pulse, starts a very fast timer, waits for the reflection to return, and calculates distance = (speed of light × time) / 2. The "divided by 2" is because the light travels to the object AND back.
TRAP: Sound-based measurement is SONAR (like a bat or submarine), not time-of-flight. Time-of-flight uses LIGHT (lasers).

## Lesson 19 — Train a stock detector: Pre-Lecture Quiz

**Q1.** AI models cannot be used to count objects?
- True
- False
?
ANSWER: **False**
WHY: Object detection AI models are specifically designed to both identify AND count objects in images. Counting is a standard capability — the model returns how many instances of each object type it found.
<!--SR:!2026-07-04,3,250-->

**Q2.** IoT and AI can be used in retail for:
- Stock checking only
- A wide range of uses including stock checking, monitoring for mask where where required, tracking footfall, automated billing
- IoT and AI cannot be used in retail
?
ANSWER: **A wide range of uses including stock checking, monitoring for mask where required, tracking footfall, automated billing**
WHY: The most complete answer is correct. IoT+AI in retail goes far beyond just counting stock — it includes customer tracking, safety compliance (mask detection), automated checkout, theft prevention, and inventory management. The narrow answers miss most of the value.

**Q3.** Object detection involves:
- Detecting objects in an image and tracking their location and probability
- Counting objects in an image only
- Classifying images
?
ANSWER: **Detecting objects in an image and tracking their location and probability**
WHY: Object detection does three things: (1) finds what objects are present, (2) draws bounding boxes showing WHERE each object is, and (3) gives a confidence score (probability) for each detection. It's more than just counting or classifying — it locates.
TRAP: "Counting objects only" and "classifying images" are incomplete. Object detection includes all three: detection + location + probability.

## Lesson 19 — Train a stock detector: Post-Lecture Quiz

**Q1.** Object detectors only return one result no matter how many objects are detected
- True
- False
?
ANSWER: **False**
WHY: Object detectors return a separate result for EACH object detected. If there are 10 cans of soda in an image, the detector returns 10 individual results, each with its own bounding box and confidence score.

**Q2.** What is the best domain to use in Custom Vision for stock counting
- General
- Food
- Products on shelves
?
ANSWER: **Products on shelves**
WHY: Custom Vision offers specialized domains optimized for specific scenarios. "Products on shelves" is specifically designed for retail shelf recognition — it's pre-tuned for the angles, lighting, and arrangements typical of store shelves.
TRAP: "General" would work but is less optimized. "Food" is for food items specifically. "Products on shelves" is purpose-built for this exact task.

**Q3.** At least how many images do you need to train an object detector?
- 1
- 15
- 100
?
ANSWER: **15**
WHY: Object detection needs more training data than simple image classification (which needs only 5 per tag). The model has to learn not just what an object looks like but also its boundaries and location, which requires at least 15 labeled images per tag in Custom Vision.
TRAP: 5 is the minimum for image CLASSIFICATION, not object DETECTION. Object detection is harder and needs more data.

## Lesson 20 — Check stock from an IoT device: Pre-Lecture Quiz

**Q1.** IoT devices are not powerful enough to use object detectors
- True
- False
?
ANSWER: **False**
WHY: With compact model formats and optimized inference engines, IoT devices can run object detection locally. Modern edge hardware includes dedicated AI accelerators that make on-device object detection practical.

**Q2.** Object detectors give you:
- The count of objects detected
- The count and location of objects detected
- The count, location and probability of objects detected
?
ANSWER: **The count, location and probability of objects detected**
WHY: The most complete answer is correct. Object detectors return all three: HOW MANY objects (count), WHERE they are (location/bounding box), and HOW CONFIDENT the model is about each detection (probability/confidence score).
TRAP: "The count of objects detected" and "The count and location" are partially correct but incomplete — they leave out probability.

**Q3.** Object detectors can be used to detect where missing stock should be to allow robots to automatically stock shelves
- True
- False
?
ANSWER: **True**
WHY: By comparing the detected objects against a planogram (a diagram of where products SHOULD be), the system can identify empty spots. A robot can then be dispatched to fill those specific gaps. This is active research and real-world retail automation.

## Lesson 20 — Check stock from an IoT device: Post-Lecture Quiz

**Q1.** To count stock you only need to consider the count of objects detected by the object detector
- True
- False
?
ANSWER: **False**
WHY: Raw counts can be misleading. You also need to consider the probability threshold (low-confidence detections might be wrong), filter overlapping bounding boxes (the same object detected twice), and verify against expected positions. Pure count without quality checks is unreliable.

**Q2.** Bounding boxes use:
- Percentage based coordinates
- Pixel based coordinates
- Centimeter based coordinates
?
ANSWER: **Percentage based coordinates**
WHY: Bounding boxes use values from 0 to 1 representing percentage of image width and height (e.g., left=0.2, top=0.3, width=0.4, height=0.5). This makes the coordinates independent of image resolution — they work the same on a 640×480 image or a 4K image.
TRAP: Pixel-based coordinates would break if the image is resized. Percentage-based coordinates scale automatically.

**Q3.** Can detected objects overlap?
- Yes
- No
?
ANSWER: **Yes**
WHY: Objects can overlap in an image — products stacked behind each other on a shelf, or items partially obscured. The object detector will return overlapping bounding boxes for each detected object, even if one is partially hidden behind another.

## Lesson 21 — Recognize speech with an IoT device: Pre-Lecture Quiz

**Q1.** IoT devices can be used to recognize speech:
- True
- False
?
ANSWER: **True**
WHY: Smart speakers (like Amazon Echo, Google Home) are IoT devices that recognize speech every day. With a microphone and speech recognition AI, IoT devices convert spoken words into text and commands.

**Q2.** Voice assistants should send all the audio they hear to the cloud for processing:
- True
- False
?
ANSWER: **False**
WHY: Sending ALL audio constantly would be a massive privacy violation and bandwidth waste. Voice assistants typically use a local "wake word" detector (like "Hey Google") that runs on-device — only audio after the wake word is sent to the cloud. Also, the word "should" implies a best practice, which this is not.
<!--SR:!2026-07-04,3,250-->

**Q3.** To recognize speech, IoT devices need large microphones:
- True
- False
?
ANSWER: **False**
WHY: Modern MEMS (Micro-Electro-Mechanical Systems) microphones are tiny — just a few millimeters across — and are used in smartphones, earbuds, and IoT devices. Size is not a barrier. Multiple small microphones can work together (beamforming) for better audio quality.

## Lesson 21 — Recognize speech with an IoT device: Post-Lecture Quiz

**Q1.** Microphones are what type of sensor?
- Digital
- Analog
?
ANSWER: **Analog**
WHY: Sound waves are continuous (analog) pressure variations in the air. A microphone converts these varying sound waves into a continuously varying voltage — that's an analog signal. The conversion to digital (via an ADC — Analog to Digital Converter) happens AFTER the microphone.
TRAP: It's tempting to say "digital" because the final data a computer processes is digital. But the microphone sensor ITSELF outputs analog — something else converts it later.

**Q2.** Sound waves are converted to digital signals using:
- Pulse Code Modulation
- Pure Code Multiplication
- Pulse Width Maximization
?
ANSWER: **Pulse Code Modulation**
WHY: PCM (Pulse Code Modulation) is the standard method for digitizing audio. It works by SAMPLING the analog waveform thousands of times per second (sample rate) and assigning each sample a numeric value (bit depth). CD-quality audio is 44,100 samples/second at 16 bits each.
TRAP: The other two options are made-up acronyms designed to look similar.

**Q3.** 1 second of 16-bit audio sampled at 16KHz is how large?
- 1KB
- 16KB
- 32KB
?
ANSWER: **32KB**
WHY: 16 bits = 2 bytes per sample. 16 KHz = 16,000 samples per second. So: 2 bytes × 16,000 = 32,000 bytes = 32KB (since 1KB = 1,024 bytes, this is approximately 32KB).
TRAP: 16KB would be correct if you forgot that 16 bits = 2 bytes (not 1 byte). The bit depth (16) and sample rate (16,000) look similar, but you must multiply them.

## Lesson 22 — Understand language: Pre-Lecture Quiz

**Q1.** Language understanding involves looking for fixed words:
- True
- False
?
ANSWER: **False**
WHY: NLU (Natural Language Understanding) interprets MEANING, not just keywords. "Turn on the light" and "Can you make it brighter in here?" mean the same thing but share no fixed words. Fixed-word matching is how old command-line programs worked, not modern AI language understanding.

**Q2.** Language understanding involves:
- Looking at the individual words in a sentence and trying to get the meaning
- Finding pre-defined sentences and using those to get the meaning
- Looking at the whole sentence and trying to get the meaning using the context of the words
?
ANSWER: **Looking at the whole sentence and trying to get the meaning using the context of the words**
WHY: Words change meaning based on context. "Set a timer" vs "Set the table" — "set" means completely different things. NLU looks at the full sentence and the relationships between words to determine intent, not just individual words in isolation.

**Q3.** Cloud providers have AI services that can understand language:
- True
- False
?
ANSWER: **True**
WHY: Almost every major cloud provider offers language understanding services: Azure has LUIS, Google has Dialogflow, Amazon has Lex, IBM has Watson Assistant. These are ready-to-use cloud APIs that understand natural language.

## Lesson 22 — Understand language: Post-Lecture Quiz

**Q1.** Sentences are understood by being broken down into:
- Ideas and explanations
- Intents and entities
- Imps and elves
?
ANSWER: **Intents and entities**
WHY: Intent = the GOAL or ACTION the user wants (e.g., "set a timer," "check weather," "play music"). Entity = the specific DETAILS or PARAMETERS (e.g., "3 minutes," "New York," "jazz"). Every NLU system breaks sentences down this way.
TRAP: "Ideas and explanations" sounds philosophical but isn't the technical term. "Imps and elves" is a joke answer.

**Q2.** The Microsoft service for language understanding is called:
- LUIS
- Luigi
- Jarvis
?
ANSWER: **LUIS**
WHY: LUIS = Language Understanding Intelligent Service. It's Microsoft Azure's NLU service that extracts intents and entities from user sentences.
TRAP: Luigi is a Nintendo video game character (Mario's brother). Jarvis is Iron Man's AI assistant. LUIS is the real product name.

**Q3.** In the sentence 'set a 3 minute timer' the:
- The intent is 3 minutes and the entity is a timer
- The intent is minutes, and the entity is 3 timers
- The intent is set a timer and the entity is 3 minutes
?
ANSWER: **The intent is set a timer and the entity is 3 minutes**
WHY: The user's GOAL (intent) is to create a timer. The specific DURATION (entity) is "3 minutes." Think of it as: intent = the verb phrase (what to do), entity = the noun/value (the details).
TRAP: Swapping intent and entity is the most common mistake. Ask: "What does the user want to DO?" = intent. "What are the specifics?" = entity.

## Lesson 23 — Set a timer and provide spoken feedback: Pre-Lecture Quiz

**Q1.** Speech generated by AI models sounds monotonous and robotic
- True
- False
?
ANSWER: **False**
WHY: Modern neural text-to-speech (TTS) produces remarkably natural-sounding voices with proper intonation, emotion, and rhythm. The old robotic-sounding speech is outdated technology. Current AI voices can be nearly indistinguishable from human speech.

**Q2.** AI models can only create speech in American English:
- True
- False
?
ANSWER: **False**
WHY: "Only" makes this false. Modern TTS services support hundreds of voices across dozens of languages and regional accents — British English, Spanish, Mandarin, Arabic, Japanese, and many more. American English is just one of many options.

**Q3.** AI models would convert 1234 into which spoken phrase:
- One two three four
- One thousand two hundred and thirty four
- It can be 'one two three four' or 'one thousand two hundred and thirty four' depending on the context
?
ANSWER: **It can be 'one two three four' or 'one thousand two hundred and thirty four' depending on the context**
WHY: AI text-to-speech uses context to decide. "Enter PIN: 1234" → read as digits. "The hall seats 1234 people" → read as a number. This is called "text normalization" and is a key part of modern TTS systems.
TRAP: Neither format is always correct. Good TTS adapts based on surrounding text.

## Lesson 23 — Set a timer and provide spoken feedback: Post-Lecture Quiz

**Q1.** The three parts of speech generation are:
- Text analysis, understanding analysis, sound generation
- Text analysis, linguistic analysis, wave form generation
- Word analysis, audio production
?
ANSWER: **Text analysis, linguistic analysis, wave form generation**
WHY: Step 1 (Text Analysis): understand and normalize the raw text (handle numbers, abbreviations, symbols). Step 2 (Linguistic Analysis): determine pronunciation, stress, intonation, and rhythm (how it should sound). Step 3 (Wave Form Generation): produce the actual audio signal.
<!--SR:!2026-07-04,3,250-->

**Q2.** Can speech generation models be trained to sound like existing people:
- True
- False
?
ANSWER: **True**
WHY: Given enough voice samples, AI can create a custom voice model that mimics a specific person's speaking style, pitch, and cadence. This technology is called "voice cloning" or "custom voice." It requires careful ethical and legal considerations.

**Q3.** The markup language used to encode speech is called:
- SSML
- MSSL
- SpeechXML
?
ANSWER: **SSML**
WHY: SSML = Speech Synthesis Markup Language. It's an XML-based language that lets you control exactly how text is spoken: pronunciation, pauses, pitch, speaking rate, volume, and emphasis. Think of it like HTML for speech instead of web pages.

## Lesson 24 — Support multiple languages: Pre-Lecture Quiz

**Q1.** Language understanding only understands English:
- True
- False
?
ANSWER: **False**
WHY: "Only" makes this false. LUIS and other NLU services support dozens of languages including Spanish, French, German, Chinese, Japanese, Portuguese, and many more. English is not the only language.

**Q2.** AI speech to text models understand multiple languages:
- True
- False
?
ANSWER: **True**
WHY: Speech recognition services support many languages, and some can even auto-detect which language is being spoken without being told. You can speak Spanish to a device configured for Spanish, and it will transcribe correctly.

**Q3.** AI translation involves swapping individual words for their translated version:
- True
- False
?
ANSWER: **False**
WHY: Word-by-word translation produces garbage results. Languages have different grammar, word order, idioms, and cultural context. Modern neural translation considers the ENTIRE sentence to produce a natural-sounding translation that preserves meaning.
TRAP: This is what early (pre-AI) translation systems tried to do, and they failed badly. Modern AI translation is fundamentally different.

## Lesson 24 — Support multiple languages: Post-Lecture Quiz

**Q1.** Machine translation has been researched for nearly:
- 70 years
- 17 years
- 7 years
?
ANSWER: **70 years**
WHY: Machine translation research began in the early 1950s, shortly after the first computers were built. It's one of the oldest problems in AI — researchers have been working on it since the 1950s, making it roughly 70+ years of research history.
TRAP: 7 or 17 years feels more "modern" because recent breakthroughs (neural MT) happened in the last decade, but the field itself is much older.

**Q2.** AI language translators are called:
- Noddy translators
- Neural translators
- Nothing - AI cannot be used for translation
?
ANSWER: **Neural translators**
WHY: Modern translation systems use neural networks (deep learning), so they're called "neural machine translation" (NMT) systems. The term "neural" refers to the artificial neural networks that power them.
TRAP: "Noddy translators" is a made-up name. "Nothing - AI cannot be used for translation" is clearly false given tools like Google Translate.
<!--SR:!2026-07-04,3,250-->

**Q3.** What alien languages does the Microsoft translator support:
- Na'vi
- Alienese
- Klingon
?
ANSWER: **Klingon**
WHY: Microsoft added Klingon (from Star Trek) as a fun demonstration of the flexibility of their translator. It's a real, usable language option — not a joke answer. It shows that the translation engine can learn any language given enough training data, even constructed ones.
TRAP: Na'vi (from Avatar) and Alienese (from Futurama) are not supported, though they're also fictional languages.
<!--SR:!2026-07-03,2,230-->

---

# MUST-KNOW FACTS

These are the 25 single facts that appear most often or are most likely to be tested. Memorize these one-liners.

1. IoT = Internet of Things — the network of physical devices with sensors that connect to the internet.
2. Telemetry = data sent FROM a device TO the cloud.
3. Sensors GATHER data from the physical world (input); actuators CONTROL the physical world (output).
4. LED = actuator, not sensor. It produces output (light).
5. Digital signals = only high (1/on) and low (0/off). Analog signals = continuous voltage ranges.
6. PWM (Pulse-Width Modulation) lets a digital device control analog things by rapidly switching on/off.
7. IoT devices do NOT "always" need internet — they can work offline and sync later.
8. IoT devices do NOT use HTTP — they use lightweight protocols like MQTT.
9. MQTT does NOT have message queues despite the word "Queueing" in its name. It uses publish/subscribe.
10. IoT Hub is a message broker, NOT a storage service — it routes data but doesn't keep it.
11. IoT devices are NOT more powerful than desktops — they're designed to be cheap, low-power, and efficient.
12. A relay is an ELECTROMECHANICAL switch that lets a low-power device control a high-power device.
13. CPU instruction cycle order: Fetch → Decode → Execute (in that exact order).
14. SPI = one controller + multiple peripherals. I2C = multiple controllers + multiple peripherals.
15. GPS data is sent as NMEA sentences over UART protocol.
16. GPS needs at least 3 satellites for a good position fix.
17. Plant growing temperatures: Base (minimum), Optimal (best), Maximum (stops growth).
18. GDD formula: ((day max + day min) / 2) - plant base. Divide by 2 first, then subtract.
19. Both too little AND too much water harm plants — extremes in either direction are bad.
20. Transfer learning = using a pre-trained model as a starting point so you only need ~5 images per tag.
21. Image classification needs at least 5 images per tag. Object detection needs at least 15.
22. GPU = the hardware that accelerates both game graphics and machine learning training.
23. A Custom Vision model version is called an ITERATION. The edge deployment format is COMPACT.
24. Intent = what the user wants to DO. Entity = the specific DETAILS (e.g., intent: "set timer," entity: "3 minutes").
25. Symmetric encryption = faster but less secure (one shared key). Asymmetric = slower but more secure (public + private key pair).
