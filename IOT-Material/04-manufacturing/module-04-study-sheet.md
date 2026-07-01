# Module 04 — Manufacturing: Study Sheet

## 1. MODULE OVERVIEW

This module teaches how to use cameras, AI, and IoT infrastructure to
automate fruit-quality inspection on a factory conveyer belt — replacing
manual human sorting with machines that can detect ripeness, disease, and
bruising. Lesson 15 trains an AI image classifier in the cloud using
transfer learning so it can tell ripe from unripe fruit with only a handful
of example photos. Lesson 16 connects that cloud model to a real IoT camera
and sends captured images for prediction via a REST API. Lesson 17 moves
the trained model out of the cloud and onto a local edge device (faster,
cheaper, keeps data private). Lesson 18 ties everything into a complete
system: a proximity sensor on the belt triggers the camera, the edge
classifier decides ripe/unripe, and the whole pipeline is orchestrated
through the Things → Insights → Actions reference architecture that applies
to any IoT project.

---

## 2. KEY CONCEPTS

### 2.1 Traditional Programming vs. Machine Learning

- **Plain-language definition:** Traditional programming means a human
  writes exact step-by-step rules ("if pixel is green, it's unripe").
  Machine learning (ML) means you show the computer lots of examples with
  correct answers, and it figures out the rules by itself.

- **Why it matters:** Manual rules can't handle messy real-world variety
  (shades of green, shadows, bruises, odd-shaped fruit). ML learns patterns
  a human could never write down explicitly, making it practical for visual
  inspection.

- **Concrete example:** Give a computer millions of banana photos each
  labeled "ripe" or "unripe." After training, it can look at a brand-new
  banana photo it has never seen and output "ripe: 99.7%, unripe: 0.3%."

### 2.2 Training, Model, Prediction

- **Plain-language definition:**
  - **Training:** The process where an ML algorithm studies labeled
    example data to learn patterns — like studying flashcards before a test.
  - **Model:** The finished, trained "brain" — a function that takes new
    input and produces output. Think of it as the result after studying.
  - **Prediction:** What the model outputs for a new, never-before-seen
    input. Predictions are *probabilities* (e.g., 98.9% unripe), not
    absolute yes/no answers.

- **Why it matters:** These three steps form the entire ML workflow. Every
  ML-based IoT feature follows this same pattern: collect labeled data →
  train a model → use it to make predictions on live sensor data.

- **Concrete example:** Upload banana photos tagged `ripe` or `unripe` to
  Custom Vision (training data). Run Quick Training → get a model
  (Iteration 1). Upload a new banana photo → the model predicts `ripe:
  99.7%`.

### 2.3 Image Classifier

- **Plain-language definition:** A specific type of ML model that looks at
  a picture and assigns it to one of several predefined categories (called
  "classes" or "tags"), such as "ripe banana" vs. "unripe banana." It does
  not describe the image — it just picks the best-matching label.

- **Why it matters:** Image classifiers are the core technology behind
  automated visual inspection in factories, medical scan analysis, facial
  recognition, and many other IoT applications involving cameras.

- **Concrete example:** The model trained in Lesson 15 classifies a fruit
  photo into one of two tags: `ripe` or `unripe`. It outputs the
  probability for each tag and the code picks the highest one.

### 2.4 Transfer Learning

- **Plain-language definition:** Instead of training a model from scratch
  (which needs millions of images and enormous computing power), you start
  with a model that was already trained on a huge, general collection of
  images. You then "fine-tune" only the last layer of that model using your
  small, specific set of photos. It's like taking someone who already knows
  how to recognize shapes and edges and teaching them just the new labels
  you care about.

- **Why it matters:** Transfer learning makes image classification
  practical for small projects. You can train an accurate classifier with
  as few as 5–30 images per category, using free cloud services, without
  needing a supercomputer.

- **Concrete example:** Custom Vision's "Food" domain is a model
  pre-trained on food images. You upload ~30 ripe banana photos and ~30
  unripe banana photos; Quick Training retrains only the final
  classification layer. Result: a classifier that distinguishes ripe from
  unripe bananas.

### 2.5 Azure Custom Vision

- **Plain-language definition:** A cloud-based website and API (part of
  Microsoft's Cognitive Services) that lets you upload images, tag them,
  train an image classifier, and publish it for use by other programs —
  all without writing any ML code or understanding the underlying math. It
  uses transfer learning under the hood.

- **Why it matters:** It removes the barrier to entry for image
  classification in IoT projects. A beginner can go from zero to a working
  classifier in minutes using a free tier.

- **Concrete example:** The `fruit-quality-detector` project is created in
  the Custom Vision web portal with project type "Classification →
  Multiclass" and domain "Food." After uploading and tagging images, the
  green "Train" button runs transfer learning and shows precision/recall
  metrics.

### 2.6 Precision, Recall, AP (Average Precision)

- **Plain-language definition:**
  - **Precision:** When the model says "this is ripe," how often is it
    actually right? (Out of everything it labeled "ripe," what fraction
    really was ripe?)
  - **Recall:** Out of all the truly ripe fruit, how many did the model
    manage to find? (Did it miss any?)
  - **AP:** A single number that summarizes overall model quality by
    averaging precision across different confidence thresholds.

- **Why it matters:** A model with high precision but low recall is too
  cautious (misses a lot). A model with high recall but low precision cries
  wolf (too many false alarms). Both numbers matter depending on the
  application — in food sorting, letting unripe fruit through is worse than
  occasionally re-checking a ripe one.

- **Concrete example:** After training in Custom Vision, the Performance
  tab displays Precision, Recall, and AP for each tag (`ripe`, `unripe`)
  at the top of the page.

### 2.7 Camera Sensors (CMOS/APS)

- **Plain-language definition:** A camera sensor is a flat chip covered
  with millions of tiny light-measuring dots called **photodiodes** (one
  per pixel). A lens focuses light from the scene onto this chip. The most
  common type today is **CMOS** (Complementary Metal-Oxide Semiconductor),
  which is inexpensive and low-power — ideal for IoT devices. The sensor
  plus lens together capture an image as a grid of brightness values.

- **Why it matters:** Understanding the hardware explains practical
  constraints in IoT: camera resolution is limited by the microcontroller's
  RAM, images are much larger than simple sensor readings (like a single
  temperature number), and protocols like **SPI** are needed for the high
  data transfer rate.

- **Concrete example:** A Raspberry Pi camera module captures a 640×480
  JPEG image. The Pi's camera library handles SPI communication internally;
  the programmer just calls `camera.capture()`.

### 2.8 Custom Vision REST API (Prediction)

- **Plain-language definition:** Once a model is published, any program on
  any device can send an image to a web address (URL) and receive back a
  JSON list of predicted tags with probabilities. The request must include
  a secret **Prediction-Key** in the HTTP headers for authentication.

- **Why it matters:** This is the bridge between the AI model and the IoT
  device. The device captures an image, sends it as raw bytes via HTTP
  POST, and gets back the classification — no AI libraries needed on the
  device itself.

- **Concrete example:** An IoT device sends a POST request to
  `https://<location>.api.cognitive.microsoft.com/customvision/v3.0/Prediction/<id>/classify/iterations/Iteration2/image`
  with the header `Prediction-Key: <key>` and the image as the request
  body. Response: `{"predictions": [{"tagName": "ripe", "probability":
  0.9995}, ...]}`.

### 2.9 Edge Computing

- **Plain-language definition:** Instead of sending all data to a distant
  cloud server over the internet for processing, you put a powerful
  computer on the same local network as the IoT devices (the "edge" of the
  network) and run the AI models there. The cloud is still used for
  long-term storage, analytics, and management — but the real-time
  decision-making happens locally.

- **Why it matters:** Edge computing gives you speed (no internet lag),
  offline capability (works when internet is down), cost savings (fewer
  cloud compute fees), and privacy (images of factory products never leave
  the building). The tradeoff is that you must maintain the edge device
  yourself.

- **Concrete example:** The fruit classifier model is exported from Custom
  Vision, packaged as a Docker container, and deployed to an IoT Edge
  device on the factory floor. The camera device sends images to
  `http://<edge_device_ip>/image` instead of the cloud API — same JSON
  response format, no Prediction-Key required, and the images never touch
  the internet.

### 2.10 Containers & Docker

- **Plain-language definition:** A container is like a lightweight,
  isolated mini-computer running inside your real computer. It packages an
  application together with all its dependencies (libraries, runtimes,
  configuration) so it runs the same way everywhere. **Docker** is the most
  popular tool for creating and managing containers. A **DockerFile** is a
  recipe (text file) that lists the instructions for building a container.

- **Why it matters:** Containers solve the "it works on my machine"
  problem. When Custom Vision exports a model, it gives you a DockerFile
  that builds a container with the model and a web server inside. That
  container runs identically on a developer laptop, a Raspberry Pi, or a
  cloud VM.

- **Concrete example:** Export the fruit classifier from Custom Vision as
  a DockerFile → `docker build -t registry.azurecr.io/classifier:v1 .` →
  `docker push` to a registry → IoT Edge downloads and runs it.

### 2.11 Azure IoT Edge

- **Plain-language definition:** A service that lets you manage and deploy
  software (as containers) to edge devices from the cloud. The edge device
  registers with IoT Hub (with an `--edge-enabled` flag), and you push a
  **deployment manifest** (a JSON file listing which containers to run)
  from the cloud. IoT Edge handles downloading, starting, monitoring, and
  updating those containers automatically.

- **Why it matters:** It gives you cloud-style management for devices that
  are physically on-premises. You can update the AI model by pushing a new
  container version from the cloud without touching the factory floor
  hardware.

- **Concrete example:** `az iot edge set-modules --content deployment.json`
  pushes a deployment manifest that tells the edge device to run the
  `ImageClassifier` container from Azure Container Registry. Running
  `iotedge list` on the device shows all running modules.

### 2.12 Reference IoT Architecture: Things → Insights → Actions

- **Plain-language definition:** A mental model for designing any IoT
  system as three layers:
  - **Things:** The physical devices and sensors that collect data
    (cameras, proximity sensors, GPS modules).
  - **Insights:** The analysis layer where data is processed, AI models
    make predictions, and decisions are formed (Azure Functions, edge
    classifiers, analytics dashboards).
  - **Actions:** What happens as a result — commands sent back to devices
    (turn on an LED, trigger an actuator) or visualizations shown to humans.

- **Why it matters:** It provides a reusable template for system design.
  When facing a new IoT problem, you ask: what are my Things? what Insights
  do I need? what Actions should result? — and the architecture flows from
  there.

- **Concrete example:** Fruit quality control system — **Thing:**
  proximity sensor + camera + edge classifier + LED; **Insight:** Azure
  Function decides whether to trigger a photo and whether an alert is
  needed; **Action:** cloud-to-device commands tell the camera to capture
  and the LED to light up.

### 2.13 Proximity Sensor & Time-of-Flight

- **Plain-language definition:** A sensor that measures how far away an
  object is. It works by shooting out a pulse of electromagnetic radiation
  (laser, infrared light, or ultrasonic sound), waiting for the reflection
  to bounce back, and calculating distance from the round-trip time — a
  technique called **time-of-flight**.

- **Why it matters:** In the fruit-sorting system, the proximity sensor
  detects when a piece of fruit has arrived at the camera's position on the
  conveyer belt, acting as the trigger to capture and classify an image.

- **Concrete example:** A proximity sensor on the belt reads `distance: 5`
  cm (fruit present, ≤10 cm threshold). This reading is sent to IoT Hub,
  which triggers an Azure Function to send a `take_photo` command to the
  camera device.

### 2.14 Device Twin

- **Plain-language definition:** A JSON document stored in IoT Hub that
  pairs with each device. It has two sides: **desired** state (what the
  cloud wants the device to do — e.g., "threshold = 10") and **reported**
  state (what the device says it is actually doing). The device
  automatically syncs with its twin when desired properties change.

- **Why it matters:** It solves the problem of remote configuration. If
  the distance threshold for fruit detection needs to change from 10 cm to
  8 cm, you update the device twin in the cloud — the device picks up the
  change without any firmware update or physical access.

- **Concrete example:** The proximity sensor device reads its distance
  threshold from the device twin's desired properties rather than a
  hard-coded constant. An operator changes the threshold from a cloud
  dashboard, and the device adapts within seconds.

### 2.15 Decision Location: Cloud vs. Device

- **Plain-language definition:** When a sensor reading crosses a threshold
  (e.g., distance ≤ 10 cm = fruit detected), should the device itself
  decide "fruit is present" and send only that conclusion, or should it
  send every raw reading to the cloud and let the cloud decide?

- **Why it matters:** This is a fundamental tradeoff in every IoT design:
  device-side decisions mean fewer messages (lower cost, less bandwidth) but
  require device twins for remote configuration. Cloud-side decisions mean
  more messages but allow instant threshold changes without touching the
  device.

- **Concrete example:** The `proximity_device.py` code in Lesson 18 makes
  the decision on the device (`if distance <= DISTANCE_THRESHOLD:`), only
  sending a message when fruit is actually detected — reducing message
  count and cost.

### 2.16 Prototype vs. Production

- **Plain-language definition:** A prototype proves the concept works with
  developer-friendly hardware (Raspberry Pi, breadboard, direct internet
  connection). A production system survives in a real factory with
  **ruggedized** hardware (withstands heat, vibration, noise), uses internal
  network communication through a gateway edge device, replaces hard-coded
  values with device-twin configuration, and replaces indicator LEDs with
  real actuators (pneumatic pushers that physically remove bad fruit from
  the belt).

- **Why it matters:** Students need to understand that what they build in
  the course is a starting point — real-world deployment adds layers of
  hardening, configurability, and physical automation.

- **Concrete example:** The LED alert in the prototype becomes an
  automated mechanical gate or air-puff system that sorts fruit into
  separate bins in production.

---

## 3. KEY TERMS

| Term | Plain-Language Definition (one line) |
|------|--------------------------------------|
| Machine Learning (ML) | A technique where a computer learns patterns from labeled examples rather than following hand-written rules. |
| Training | The process of an ML algorithm studying labeled data to learn patterns. |
| Training data | Input-output example pairs (e.g., banana photos + correct label) used to train an ML model. |
| Model | The finished, trained result of ML — a function that accepts new input and produces a prediction. |
| Prediction | The output of an ML model for new input, expressed as probabilities that sum to 1 (not a yes/no). |
| Image classifier | An ML model that assigns a label (class) to an image based on its visual content. |
| Supervised learning | ML training that requires each training example to have a correct label. |
| Unsupervised learning | ML training that does not use labels — the algorithm finds patterns on its own. |
| Transfer learning | Starting from a model already trained on a huge dataset, then re-training only its final layer on a small new dataset. |
| Custom Vision | Microsoft's cloud-based tool for uploading images, tagging them, training image classifiers, and publishing them via API. |
| Cognitive Services | Microsoft's suite of pre-built cloud AI tools covering vision, speech, language, and decision-making. |
| Domain (Custom Vision) | The base pre-trained model you choose (e.g., Food, General, Landmarks) that best matches your use case. |
| Food domain | A Custom Vision base model pre-trained on food images; the right choice for fruit classification. |
| Compact model | A smaller version of a Custom Vision model that can be downloaded and run on an edge device. |
| Food (compact) | The exportable version of the Food domain — used when you need to deploy the model to IoT Edge. |
| Tag | A class label applied to a training image (e.g., `ripe`, `unripe`). |
| Quick Training | Custom Vision's fast training mode that uses transfer learning on the selected domain. |
| Iteration | A specific numbered version of a trained model; each training run creates a new iteration. |
| Precision | Of all images the model labeled as a given class, the fraction that were actually correct. |
| Recall | Of all images that truly belong to a class, the fraction the model successfully found. |
| AP (Average Precision) | A single-number summary metric averaging precision across all confidence thresholds. |
| Retraining | Adding images the model got wrong (with correct labels) to the training set and training again to improve accuracy. |
| Predictions tab | The Custom Vision page showing images from Quick Test, where you can re-tag incorrect results for retraining. |
| Publish (Custom Vision) | Making a model iteration available for external API calls, generating a Prediction URL and Prediction-Key. |
| Prediction URL | The web endpoint where published Custom Vision models accept image classification requests. |
| Prediction-Key | A secret string sent in the HTTP `Prediction-Key` header to authenticate prediction API calls. |
| `application/octet-stream` | The HTTP content-type header value meaning "raw binary data" — used when sending image bytes. |
| Camera sensor | An electronic chip covered with a grid of photodiodes that captures still images or video. |
| APS (Active-Pixel Sensor) | A type of image sensor where each pixel has its own active electronic circuit. |
| CMOS | Complementary Metal-Oxide Semiconductor — the most common and affordable type of APS camera sensor. |
| Photodiode | A tiny semiconductor component that converts incoming light into an electrical signal; one per pixel. |
| Lens | A curved glass/plastic element that focuses light from the scene onto the camera sensor; inverts the image. |
| SPI | A high-speed communication protocol used to transfer large data like images between a camera and a microcontroller. |
| Edge computing | Processing IoT data on a local network device rather than sending everything to the cloud over the internet. |
| Workload | Any service that performs computing work — AI models, applications, serverless functions. |
| Azure IoT Edge | A service that deploys and manages container-based workloads on edge devices, orchestrated from IoT Hub. |
| Module (IoT Edge) | A software unit (Docker container) deployed to an IoT Edge device; built-in modules include `edgeAgent` and `edgeHub`. |
| `edgeAgent` | The IoT Edge system module that manages the lifecycle (install, start, stop, update) of all other modules. |
| `edgeHub` | The IoT Edge system module that routes messages between modules and to/from IoT Hub. |
| Container | A lightweight, isolated runtime environment that packages an app with all its dependencies. |
| Docker | The most popular tool for building, sharing, and running containers. |
| DockerFile | A text recipe file with step-by-step instructions for building a Docker container image. |
| Container image | A read-only template from which containers are created; includes the app code and all its dependencies. |
| Container tag | A name-and-version label on a container image (e.g., `classifier:v1`). |
| Container registry | A cloud storage service for hosting and distributing container images (e.g., Azure Container Registry). |
| Azure Container Registry (ACR) | Microsoft's paid cloud service for storing Docker container images that IoT Edge devices pull from. |
| Deployment manifest | A JSON document that specifies which container images each IoT Edge device should run. |
| `iotedge list` | A command run directly on an edge device to display all running IoT Edge modules and their status. |
| `iotedge logs` | A command run on an edge device to view the console output of a specific IoT Edge module. |
| Reference IoT architecture | A design template that organizes any IoT system into three layers: Things, Insights, Actions. |
| Things (architecture layer) | The physical devices and sensors that gather data from the real world. |
| Insights (architecture layer) | The analysis layer that processes data, runs AI models, and produces decisions. |
| Actions (architecture layer) | What the system does with insights — sending commands to devices, showing dashboards, triggering alerts. |
| Proximity sensor | A sensor that measures distance to an object by emitting a signal and timing its reflection (time-of-flight). |
| Time-of-flight | The technique of measuring distance by calculating the round-trip time of a reflected signal (light or sound). |
| Threshold | A pre-set value that triggers an action when a sensor reading crosses it (e.g., distance ≤ 10 cm = fruit present). |
| Device twin | A JSON document in IoT Hub holding desired and reported state for a device, enabling remote configuration. |
| Message schema | The agreed structure of data fields in messages exchanged between devices and cloud services. |
| C2D (Cloud-to-Device) | A message sent from IoT Hub down to a specific device — used for commands and configuration. |
| D2C (Device-to-Cloud) | A message sent from a device up to IoT Hub — used for telemetry and status reports. |
| `IoTHubRegistryManager` | An Azure SDK class that sends C2D messages and manages device identities from cloud code. |
| `client.on_message_received` | A Python SDK property that registers a callback to handle incoming C2D messages on a device. |
| OPC-UA | An industrial machine-to-machine communication protocol used for factory-floor device integration. |
| Ruggedized hardware | Electronics designed to survive harsh industrial conditions (heat, vibration, noise, dust). |
| Gateway device | An edge device that bridges incompatible or insecure devices to a wider network or IoT Hub. |
| EventHub trigger | An Azure Functions binding that runs code automatically when IoT Hub receives a new device message. |

---

## 4. COMPARISONS & TRADEOFFS

### 4.1 Traditional Programming vs. Machine Learning

| | Traditional Programming | Machine Learning |
|---|---|---|
| **What it is** | A human writes an explicit algorithm: "if green → unripe, if yellow → ripe" | A model learns patterns from labeled examples; the algorithm is generic, the data defines the behavior |
| **When to use it** | When rules are simple and well-understood (e.g., geofence: if point is inside polygon boundary, output "inside") | When the patterns are too subtle or complex for human-authored rules (e.g., detecting bruising, disease spots on fruit) |
| **Pros** | Predictable, explainable, no training data needed | Handles visual/text complexity; adapts to new examples via retraining |
| **Cons** | Cannot handle visual variation (lighting, angles, partial occlusion); breaks on edge cases | Needs labeled training data; predictions are probabilistic, not certain; can learn spurious correlations (e.g., rulers in cancer photos) |

### 4.2 Cloud Computing vs. Edge Computing

| | Cloud Computing | Edge Computing |
|---|---|---|
| **What it is** | All processing happens on remote internet servers (data center) | Processing happens on a local device on the same network as IoT sensors |
| **When to use it** | When internet is reliable, latency is acceptable, data volume is manageable, and you want zero hardware maintenance | When you need low latency, offline operation, privacy, cost reduction, or must bridge incompatible devices |
| **Pros** | Auto-scales; multi-region redundancy; no hardware maintenance; easy to update | Fast (no internet lag); works offline; lowers cloud costs; keeps data private; acts as gateway for insecure/incompatible devices |
| **Cons** | Requires internet; higher latency (28ms+ transatlantic); ongoing cloud fees; data leaves your network | Cannot auto-scale easily; less geographic redundancy; you must maintain the hardware yourself |

> The lesson recommends a **blend**: use edge for real-time classification, cloud for long-term storage, analytics, and model management.

### 4.3 Decision on Device vs. Decision in Cloud

| | Decision on Device | Decision in Cloud |
|---|---|---|
| **What it is** | The device itself checks if a sensor reading crosses a threshold and only sends messages when an event occurs | The device sends every raw sensor reading to the cloud; cloud code checks thresholds |
| **When to use it** | When message cost/bandwidth matters, response must be fast, and thresholds change rarely | When thresholds need frequent adjustment, or the decision logic is complex and benefits from cloud-side data aggregation |
| **Pros** | Fewer messages → lower cost, less bandwidth; faster response (no round-trip to cloud) | Threshold can be changed instantly without touching device firmware |
| **Cons** | Changing the threshold requires a device twin or firmware update | More messages → higher cost, more bandwidth; slower response time |
| **Mitigation** | Use a **device twin** to push new threshold values to the device remotely — combines fast local decisions with remote configurability |

### 4.4 Standard Model vs. Compact Model (Custom Vision)

| | Standard Model | Compact Model |
|---|---|---|
| **What it is** | A full-size model that runs only in the Custom Vision cloud service | A smaller, exportable model that can be downloaded and run on an edge device |
| **When to use it** | When you call the classifier from a device with internet access and cloud latency is acceptable | When you need the classifier to run on a local edge device (offline, low latency, privacy) |
| **Domain name** | `Food` | `Food (compact)` |
| **Deployment** | Called via cloud REST API with Prediction-Key | Exported as a DockerFile → built into a container → deployed to IoT Edge; REST API runs locally, no Prediction-Key needed |
| **Retraining** | Incorrect predictions appear in the Predictions tab automatically; easy retraining workflow | Edge classifier images never reach Custom Vision → no automatic Predictions tab entries; manual retraining workflow required |

### 4.5 Prototype vs. Production System

| | Prototype | Production |
|---|---|---|
| **Hardware** | Developer kit (Raspberry Pi, breadboard) | Ruggedized components rated for factory heat, vibration, noise |
| **Connectivity** | Direct internet connection for all messages | Internal network; only aggregate data goes to cloud; edge gateway handles local processing |
| **Configuration** | Hard-coded constants (e.g., `DISTANCE_THRESHOLD = 10`) | Configurable via device twins; no code change needed to adjust thresholds |
| **Actuators** | LED alert (visual indicator) | Automated mechanical actuator (pusher, gate, air puff) that physically sorts fruit |
| **Industrial protocol** | Not used | OPC-UA for machine-to-machine factory-floor communication |

---

## 5. LIKELY EXAM ANGLES

1. **"Which of these is an example of machine learning vs. traditional programming?" (Multiple choice)**
   - Expect a question presenting a scenario (e.g., "A system uses if-else rules to filter GPS coordinates") and asking whether it's ML or traditional programming. Know the difference: ML learns patterns from data; traditional programming follows explicit human-written rules.

2. **"Explain the training → model → prediction pipeline and why ML predictions are probabilities, not yes/no answers." (Short answer)**
   - Be ready to draw the flow: labeled examples (training data) → training process creates a model → model takes new input → outputs probabilities for each class → code picks the highest. Explain that probabilities let you gauge confidence and set custom thresholds.

3. **"Describe transfer learning and explain why it matters for IoT projects." (Short answer / essay)**
   - Cover: training from scratch needs millions of images and huge GPUs; transfer learning starts from a pre-trained model and re-trains only the final layer on your small dataset (5–30 images). This makes image classification feasible for small teams with limited data, using free cloud services. Mention the Custom Vision "Food" domain as an example.

4. **"Compare edge computing and cloud computing — give two pros and two cons for each, and describe a scenario where you'd choose edge." (Short answer)**
   - Use the comparison table above. A good scenario: a factory with unreliable internet that needs real-time fruit sorting (pick edge). A bad scenario: a weather station with a reliable connection sending one temperature reading per hour (cloud is fine).

5. **"What is the Things → Insights → Actions architecture? Map the fruit quality detector system onto these three layers." (Essay / diagram)**
   - **Things:** Proximity sensor device, camera device, edge classifier module, LED device. **Insights:** Azure Function (processes proximity events, sends camera commands; processes classification results, decides if alert is needed). **Actions:** C2D command to camera (`take_photo`), C2D command to LED (`alert`). Reference the sequence diagram from Lesson 18.

6. **"What is a device twin and what problem does it solve for IoT devices in production?" (Multiple choice or short answer)**
   - A device twin is a JSON document in IoT Hub with desired and reported state. It solves the problem of remotely configuring device parameters (like distance thresholds) without physically accessing the device or updating firmware.

---

## 6. GAPS / AMBIGUITIES

- **Unsupervised learning is mentioned but not explained:** Lesson 15 says "Unsupervised learning doesn't require labeled data (not covered here)" but never elaborates. If the exam includes it as a distractor option, the student only knows it exists as a contrast to supervised learning — no mechanism, no example. Worth supplementing with a short external definition if it appears in practice questions.

- **GPU / cloud compute cost is gestured at but not quantified:** Lesson 15 says training needs GPUs and cloud services let you "rent GPU time," but no concrete cost or comparison is given. For a beginner, "GPU" is introduced only as "same hardware that renders video games" — this is fine for the scope, but a question about *why* cloud training is needed might expect deeper understanding.

- **SPI protocol is name-dropped without explanation:** Lesson 16 mentions that cameras connect via SPI but never defines the acronym (Serial Peripheral Interface) or describes how it works. The lesson says "the camera library handles the communication protocol," which tells the student they don't need to implement it — but an MCQ might test whether SPI is for sensors vs. cameras vs. something else.

- **OPC-UA is mentioned once with no depth:** Lesson 18 introduces OPC-UA as "machine-to-machine communication protocol used in industrial automation" in a single note. No comparison with other protocols, no explanation of where it fits in the architecture. Likely a footnote for completeness rather than exam material, but it's an exposed term.

- **Deployment manifest JSON structure is shown partially:** Only the `ImageClassifier` module block is printed. The `systemModules`, `routes`, and `$edgeHub` desired properties are described in a table but the full JSON is never shown. If an exam question asks "which section of the deployment manifest specifies container credentials?" the student should know `registryCredentials` from the table — but the actual syntax is not visible.

- **No explicit lesson on IoT Hub message routing:** Lesson 18 uses `IoTHubRegistryManager` for C2D messages and EventHub triggers for D2C messages, but the concept of message routing (how IoT Hub decides which messages go to which Function) is implicit. The student sees `EventHub trigger` in the Function code but is never told it's a built-in IoT Hub routing path.

- **The `Food` vs. `Food (compact)` domain distinction appears abruptly in Lesson 17:** Lesson 15 sets up the project with the `Food` domain; Lesson 17 retroactively says "change domain to `Food (compact)`" for export. The relationship between domain choice and export capability is not explained upfront. The student might wonder: why didn't we just pick `Food (compact)` from the start?
