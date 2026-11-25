## 1. MODULE OVERVIEW

This module tackles the real-world problem of **tracking vehicles in a supply chain using IoT**. When trucks, ships, or tractors carry goods across cities or countries, logistics managers need to know where every vehicle is, when it will arrive, and whether it has entered or left critical zones. The four lessons build a complete pipeline: first, Lesson 11 explains **how GPS works** and how a device extracts coordinates from satellite signals. Lesson 12 shows **how to store that GPS data in the cloud**, choosing the right type of database for messy, ever-changing IoT data. Lesson 13 walks through **turning raw coordinates into a visual map** so a human can see routes at a glance. Finally, Lesson 14 introduces **geofences** — invisible digital boundaries that trigger alerts when a vehicle crosses them, closing the loop from sensing to action.

---

## 2. KEY CONCEPTS

### 2.1 Supply Chain & Logistics

- **Plain-language definition**: The *supply chain* is the entire journey a product takes from where it is made or grown (a farm, a factory) to the person who ultimately buys it. *Logistics* is the narrower job of physically moving the goods from one place to another — loading a truck, shipping it, unloading at a warehouse.
- **Why it matters**: Without visibility into this journey, managers cannot reroute delayed trucks, prepare unloading crews, or prove compliance with driver-safety laws. IoT adds real-time location data to this blind process.
- **Concrete example from the material**: A farmer packs boxes of produce → a truck carries them to a central warehouse → boxes are sorted onto a second truck with mixed produce → delivered to the supermarket. IoT lets the supermarket know the second truck's ETA so the loading dock is ready.

### 2.2 Connected Vehicles

- **Plain-language definition**: A *connected vehicle* is any vehicle (car, truck, tractor) that has an onboard device sending data — location, speed, engine status, cargo temperature — back to a central computer system over the internet (usually via a cellular network, since vehicles are outside WiFi range).
- **Why it matters**: It enables six concrete business benefits at once: location tracking, route optimization, tax-by-mileage compliance, driver-safety monitoring, legal driving-hours enforcement, and refrigerated-cargo temperature surveillance. Each of these would otherwise require separate manual checks.
- **Concrete example from the material**: A refrigerated truck's temperature sensor reports a spike. The system sees this plus the truck's GPS location and reroutes it to the nearest cold-storage facility before the cargo spoils. At the same time, the driver's engine-on hours are tracked to ensure they don't exceed the legal limit.

### 2.3 Geospatial Coordinates (Latitude, Longitude, and Formats)

- **Plain-language definition**: A coordinate is a pair of numbers that pinpoints one spot on the Earth's surface.
  - *Latitude*: how far north or south you are, measured from the equator (0°). The North Pole is 90° (positive), the South Pole is −90° (negative).
  - *Longitude*: how far east or west you are, measured from the Prime Meridian (0°), an imaginary line running pole-to-pole through the Royal Observatory in Greenwich, England. Goes from −180° (west) to 180° (east); −180° and 180° are the same line on the opposite side of the Earth.
- **Why it matters**: Any IoT location system must speak this universal "address language." Mixing up latitude and longitude order, or misreading a negative sign, places a truck on the wrong continent.
- **Concrete example from the material**: The Microsoft campus in Redmond, WA is at `47.6423109, -122.1390293` — about 47.6° north of the equator and 122.1° west of Greenwich.

### 2.4 DMS vs. Decimal Degrees

- **Plain-language definition**: Location can be written in two styles:
  - *Degrees-Minutes-Seconds (DMS)*: inherited from ancient Babylonian base-60 math. 1 degree = 60 minutes, 1 minute = 60 seconds. Example: `2°17'43"`.
  - *Decimal degrees*: the same location written as a single decimal number. Example: `2.295277°`.
- **Why it matters**: Humans sometimes use DMS on paper maps; computers always use decimal degrees. You must be able to convert between them. The conversion formula: `decimal = degrees + (minutes/60) + (seconds/3600)`.
- **Concrete example from the material**: At the equator, 1° of latitude ≈ 111.3 km. So 1 minute ≈ 1.855 km, and 1 second ≈ 31 m — useful for grasping GPS precision.

### 2.5 Global Positioning System (GPS)

- **Plain-language definition**: A network of satellites orbiting Earth, each continuously broadcasting "I am here, and the time is exactly X." A GPS receiver on the ground listens for these signals. By measuring how long each signal took to arrive (radio waves travel at a known constant speed), the receiver calculates its distance from each satellite it can hear. With distances from at least 3 satellites, it *triangulates* its own exact position on Earth. A fourth satellite also provides altitude (height above sea level).
- **Why it matters**: GPS is the foundational sensing technology for all IoT location tracking. Without understanding its accuracy limits and requirements (clear sky view), you cannot design a reliable logistics system.
- **Concrete example from the material**: Before 2000, the US military intentionally degraded civilian GPS accuracy to ~5 m. After 2000, accuracy improved to ~30 cm in good conditions. Multiple countries now run their own satellite *constellations* (USA's GPS, Russia's GLONASS, EU's Galileo, China's BeiDou, Japan's QZSS, India's NAVIC), and modern receivers listen to several simultaneously for faster, more accurate fixes.

> **Important detail**: GPS satellites carry *atomic clocks* so precise they must be corrected for Einstein's relativity — time literally ticks slightly slower for the fast-moving satellites than it does on the ground (38 microseconds/day drift), and the system is designed to compensate for this.

### 2.6 NMEA 0183 and GPS Data Parsing

- **Plain-language definition**: NMEA 0183 is a text-based standard that GPS sensors use to output their readings. Think of it as the "language" a GPS module speaks. Each message is called a *sentence*, and it always starts with a `$` character followed by a code that identifies the speaker (e.g., `GP` for US GPS, `GN` for multi-constellation) and the type of information in the message.
- **Why it matters**: You never need to buy the $2,000 official specification — open-source libraries like `pynmea2` (Python) can parse these sentences for you. But you must recognize the format and know which sentence type contains what data.
- **Concrete example from the material**: A `GGA` sentence (GPS Fix Data) looks like:
  ```
  $GNGGA,020604.001,4738.538654,N,12208.341758,W,1,3,,164.7,M,-17.1,M,,*67
  ```
  The latitude is `4738.538654,N` → 47° + (38.538654 / 60)° = **47.6423109°** (North = positive). The longitude is `12208.341758,W` → 122° + (08.341758 / 60)° = **122.1390293°** (West = negative). The `pynmea2.parse()` function does this arithmetic automatically and returns `msg.latitude` and `msg.longitude` as simple decimal numbers.

> **Key trap**: NMEA coordinates use the format `(dd)dmm.mmmm` — the minutes part includes decimal seconds. You must divide the minutes portion by 60 to convert to decimal degrees.

### 2.7 Structured vs. Unstructured Data

- **Plain-language definition**:
  - *Structured data* looks like an Excel spreadsheet: fixed columns (name, date-of-birth, address), every row has the same shape, and you can link tables together by shared IDs. Stored in *relational databases* (SQL).
  - *Unstructured data* has no fixed shape — one document might have 3 fields, the next might have 7 fields of completely different types. Stored in *document databases* (NoSQL) or as raw files in *blob storage*.
- **Why it matters**: **IoT data is unstructured by nature.** A tractor might send only GPS coordinates. A delivery truck sends GPS + speed + driver ID. A refrigerated truck sends all of that plus temperature. Forcing all of these into one rigid table would mean constantly altering the database schema. NoSQL/document storage accepts any JSON shape without changes.
- **Concrete example from the material**: A fleet adds a new truck with a built-in weight scale sensor. In a NoSQL database, you simply start including a `weight` field in that truck's JSON documents. In a SQL database, you'd need to alter the table definition and handle NULL values for all existing rows.

### 2.8 SQL vs. NoSQL Databases

- **Plain-language definition**:
  - *SQL databases* (also called RDBMS — Relational Database Management Systems): data lives in predefined tables with named columns. You query using the SQL language. Example: a `users` table and a `purchases` table linked by a user ID.
  - *NoSQL databases* (also called document databases): you insert whatever JSON document you want. No predefined schema. Documents live in containers/folders, and different documents in the same container can look completely different.
- **Why it matters**: Choosing the wrong one creates ongoing maintenance pain. For IoT with heterogeneous devices, NoSQL is the natural fit. For financial ledgers with strict, unchanging structure, SQL is better.
- **Concrete example from the material**: In this module, GPS readings are stored as individual JSON blob files in Azure Blob Storage (a form of NoSQL/unstructured storage), not in a SQL table.

### 2.9 Hot, Warm, and Cold Data Paths

- **Plain-language definition**: A way to classify how urgently data needs to be processed after it arrives:
  - *Hot path*: act on it immediately (real-time). Example: "A refrigerated truck's temperature just spiked — alert the driver NOW."
  - *Warm path*: process it shortly after receipt for reports and dashboards. Example: "Generate yesterday's mileage report this morning."
  - *Cold path*: store it long-term for batch analytics. Example: "Analyze the last 5 years of fuel costs per route to optimize for next year's budget."
- **Why it matters**: You don't build the same infrastructure for all three. Hot-path needs stream processing and instant triggers. Cold-path data goes to a *data warehouse* (a database optimized for storing enormous amounts of unchanging historical data and running complex queries).
- **Concrete example from the material**: The GPS telemetry in this module is **warm path** — it is stored to blob storage for the map visualization and reporting built in Lessons 13–14, not processed in real time.

### 2.10 Azure Blob Storage

- **Plain-language definition**: A cloud service for storing *blobs* (Binary Large Objects) — which really just means "files of any kind" — JSON documents, images, videos, log files. Blobs live inside *containers* (think: named buckets or top-level folders), which can themselves contain sub-folders. A storage account can hold multiple containers.
- **Why it matters**: It is the cheapest, simplest cloud storage for IoT telemetry. In this module, each GPS reading becomes one tiny JSON file named with a unique ID, organized by device ID in a folder: `gps-sensor/<uuid>.json`.
- **Concrete example from the material**: Setting public access on a blob container (`PublicAccess.Container`) makes every blob inside it readable by anyone with the URL — this is what allows the web-page map in Lesson 13 to fetch GPS data directly from storage.

### 2.11 Data Visualization

- **Plain-language definition**: Turning raw numbers into pictures (charts, maps, gauges) so a human can spot patterns, outliers, and trends instantly instead of scanning rows of a spreadsheet.
- **Why it matters**: The goal is faster decision-making. A table of 24 hourly soil-moisture readings tells you nothing at a glance; a line chart shows exactly when moisture dropped and irrigation kicked in. For GPS data, the best visualization is points on a map.
- **Concrete example from the material**: A depot worker views a web map with colored bubbles showing all incoming trucks. They can see: how many trucks are approaching, which type each is (refrigerated vs. dry), and each truck's ETA. This lets them decide which bay to open and whether to ready cold storage.

### 2.12 Azure Maps and GeoJSON

- **Plain-language definition**: *Azure Maps* is Microsoft's cloud-based mapping platform — like Google Maps but built for embedding in your own applications. *GeoJSON* is a standard JSON format for describing geographic things: points, lines, polygons. Any mapping tool that understands GeoJSON can plot your data.
- **Why it matters**: You need to bridge the gap between "I have a list of coordinates" and "I see them on a map." GeoJSON is the standard data format for that bridge.
- **Concrete example from the material**: To plot a single GPS point:
  ```json
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-122.139, 47.642]
    }
  }
  ```
  Azure Maps reads this, draws a circle at that location, and adds it to a *BubbleLayer* (a layer that renders points as bubbles/circles).

> **Critical trap**: GeoJSON always uses `[longitude, latitude]` order — the **opposite** of how coordinates are usually spoken and written (`latitude, longitude`). Swapping them places your marker on the wrong side of the globe.

### 2.13 CORS (Cross-Origin Resource Sharing)

- **Plain-language definition**: A browser security rule that says "a web page from website-A.com cannot read data from website-B.com unless B explicitly gives permission." Without it, a malicious page could silently steal your data from another site.
- **Why it matters**: In Lesson 13, an HTML page loaded from your local computer (or a static hosting service) tries to fetch JSON blobs from `https://<storage>.blob.core.windows.net`. These are different *origins*, so the browser blocks the request by default. You must enable CORS on the storage account with `--origins "*"` (allow any website) and `--methods GET` (only reading, not writing), specifically for the blob service (`--services b`).
- **Concrete example from the material**: The `az storage cors add` command in Lesson 13 configures this permission.

### 2.14 Geofences

- **Plain-language definition**: An invisible, digital boundary drawn around a real-world area on a map. When a GPS-tracked device crosses that boundary, the system triggers an action (alert, log entry, automated message). Think of it like a virtual tripwire.
- **Why it matters**: Location data alone is just dots on a map. Geofences turn location data into *actionable events*. Four major use cases: alerting a depot when a truck arrives (reduces wait time), tracking mileage on public vs. private roads for tax purposes, detecting theft (vehicle leaves the farm unexpectedly), and enforcing location compliance (a truck carrying pesticides must not enter an organic zone).
- **Concrete example from the material**: A geofence polygon is defined as a GeoJSON `Polygon` with coordinates in `[lon, lat]` order. The last coordinate must equal the first to close the shape (a rectangle = 5 points). The polygon is uploaded to Azure Maps, which returns a UDID (Unique Data ID). Every subsequent GPS reading is sent to the Azure Maps Geofence API with that UDID, and the API returns a `distance` value telling you whether the point is inside or outside.

#### Geofence Distance Values (Must Memorize)

| Distance | Meaning |
|---|---|
| `999` | Outside the geofence by more than the search buffer (>50 m by default) |
| `0` to `50` (positive) | Just outside, but within the search buffer "fuzzy zone" |
| `-999` | Inside the geofence by more than the search buffer (>50 m in) |
| `-50` to `0` (negative) | Just inside, within the search buffer zone |

> **The search buffer explained**: GPS is never perfect — it can be off by several meters. A reading that shows a truck 5 m outside a depot fence might actually be inside. The search buffer (default 50 m, configurable 0–500 m) creates a "fuzzy edge" where distances are reported precisely (±50 m) rather than the blunt ±999. Real systems should also check multiple consecutive readings, vehicle speed, and known road paths before acting — to avoid false triggers from a single bad GPS fix.

### 2.15 Consumer Groups

- **Plain-language definition**: A *consumer group* is like a separate, independent bookmark into the stream of messages arriving at IoT Hub. If two applications share the same consumer group, they fight over which messages each has read and they miss data. Each application needs its own consumer group so it can keep its own independent place in the stream.
- **Why it matters**: In this module, the Functions App has two triggers that both need to read the same GPS messages: one stores them to blob storage (Lesson 12), the other checks them against the geofence (Lesson 14). Without a second consumer group, they would interfere. The `$Default` consumer group is created automatically; you create additional ones (e.g., `geofence`) as needed.
- **Concrete example from the material**: The `function.json` for each trigger specifies which `consumerGroup` it connects to — `$Default` for the blob-storage trigger, `geofence` for the geofence-check trigger.

---

## 3. KEY TERMS

| Term | One-line plain-language definition |
|---|---|
| **Supply chain** | The full journey of a product from its origin (farm/factory) to the final customer, including all transport and storage steps. |
| **Logistics** | The specific process of physically moving goods from one location to another (e.g., by truck, ship, or plane). |
| **Connected vehicle** | A vehicle equipped with a device that reports location and sensor data to a central IT system, typically over cellular networks. |
| **Geospatial coordinates** | A pair of numbers (latitude and longitude) that uniquely identify one point on Earth's surface. |
| **Latitude** | The north–south angle measured from the equator (0°), ranging from −90° (South Pole) to +90° (North Pole). |
| **Longitude** | The east–west angle measured from the Prime Meridian (0° at Greenwich, England), ranging from −180° to +180°. |
| **Prime Meridian** | The 0° longitude reference line running from North Pole to South Pole through the Royal Observatory in Greenwich, England, established in 1884. |
| **Antimeridian (180th meridian)** | The line exactly opposite the Prime Meridian on the far side of Earth; −180° and +180° refer to the same line. |
| **Meridian** | Any imaginary semicircle running from the North Pole to the South Pole; lines of constant longitude. |
| **Sexagesimal (base-60)** | The ancient Babylonian numbering system inherited by degrees/minutes/seconds — 60 minutes per degree, 60 seconds per minute. |
| **Decimal degrees** | A coordinate expressed as a single decimal number (e.g., 47.6423°) instead of separate degrees, minutes, and seconds. |
| **DMS** | Abbreviation for Degrees, Minutes, Seconds — the traditional way of writing coordinates. |
| **GPS (Global Positioning System)** | A satellite network (originally US-built) that enables a receiver on Earth to calculate its exact position by triangulating signals from multiple satellites. |
| **GPS satellite** | An orbiting spacecraft that continuously broadcasts its own position and an extremely precise timestamp via radio waves. |
| **Triangulation** | Determining your location by measuring your distance from at least three known reference points (the satellites). |
| **Atomic clock** | An extremely accurate clock (used inside GPS satellites) that must be corrected for relativistic time dilation caused by the satellite's speed and altitude. |
| **GPS constellation** | A named group of positioning satellites operated by one country or union (e.g., GPS = USA, GLONASS = Russia, Galileo = EU, BeiDou = China). |
| **NMEA 0183** | A text-based standard defining how GPS sensor output messages (called *sentences*) are formatted; created by the National Marine Electronics Association. |
| **NMEA sentence** | One message from a GPS sensor, always starting with `$`, containing a source code, type code, and comma-separated data fields. |
| **GGA sentence** | The NMEA message type that carries GPS Fix Data — latitude, longitude, altitude, and satellite count. |
| **ZDA sentence** | The NMEA message type that carries the current date and time, including the local time zone. |
| **GSV sentence** | The NMEA message type that lists details of every satellite currently visible to the receiver. |
| **`(dd)dmm.mmmm` format** | The coordinate format used inside NMEA sentences: `dd` = whole degrees, `mm.mmmm` = minutes with decimal seconds. Must convert to decimal degrees by dividing `mm.mmmm` by 60. |
| **`$GPGGA`** | Prefix for a GGA sentence from a US-only GPS receiver. |
| **`$GNGGA`** | Prefix for a GGA sentence from a receiver listening to multiple satellite constellations simultaneously. |
| **pynmea2** | A Python library that parses raw NMEA sentences into objects with simple `.latitude` and `.longitude` attributes (decimal degrees). |
| **Structured data** | Data with a fixed, unchanging format that maps neatly to database tables with predefined columns (e.g., a person's name and date of birth). |
| **Unstructured data** | Data without a consistent format — each record may have different fields and types (e.g., JSON documents from different IoT device types). |
| **Semi-structured data** | Data that has some organization but does not fit into rigid tables (e.g., JSON documents with some shared fields and some varying fields). |
| **SQL database (RDBMS)** | A relational database where data lives in predefined tables with named columns and relationships between tables; queried using the SQL language. |
| **Schema** | The blueprint defining what columns and types a database table has. A SQL database requires a schema upfront; a NoSQL database does not. |
| **NoSQL database (document database)** | A database that stores documents (usually JSON) without a predefined schema; different documents in the same container can have different fields. |
| **Hot path** | Processing data immediately in real time, used for alerts and urgent responses. |
| **Warm path** | Processing data shortly after it arrives, used for dashboards, reports, and short-term analytics. |
| **Cold path** | Storing data long-term in a data warehouse for historical batch analysis (yearly trends, cost optimization). |
| **Data warehouse** | A specialized database designed to store enormous amounts of static historical data and run complex analytical queries efficiently. |
| **Azure Blob Storage** | Microsoft's cloud service for storing unstructured files (blobs) — JSON, images, videos — organized into containers and folders. |
| **Blob (Binary Large Object)** | Any file stored as raw bytes in cloud storage; in this module, mostly JSON documents. |
| **Blob container** | A named bucket or top-level folder in blob storage that holds blobs and sub-folders; analogous to a database table. |
| **`PublicAccess.Container`** | A setting that makes every blob in a container publicly readable by URL — necessary for a web page to fetch blobs directly. |
| **`BlobServiceClient`** | Python SDK class for connecting to an entire storage account. |
| **`ContainerClient`** | Python SDK class for interacting with one specific blob container. |
| **`upload_blob()`** | Python SDK method that uploads raw bytes as a new blob file. |
| **UUID (Universally Unique Identifier)** | A randomly generated string (e.g., `a9487ac2-...`) used as a unique filename so no two GPS readings overwrite each other. |
| **`event.iothub_metadata['enqueuedtime']`** | The timestamp recording when IoT Hub received a message — preferred over the current function time because messages may be delayed. |
| **Connection string** | A single text string containing all credentials (account name, key) needed to access a cloud service; stored as an environment variable or app setting. |
| **Data visualization** | Converting raw numeric data into charts, maps, or diagrams that let a human understand patterns and make decisions at a glance. |
| **Azure Maps** | Microsoft's cloud platform providing maps, routing, traffic, and geofencing services, usable through Web SDK, Android SDK, or REST API. |
| **Azure Maps Web SDK** | A JavaScript library that embeds an interactive map into a web page and lets you add data layers on top. |
| **`atlas.Map`** | The main JavaScript class that creates a map control inside a `<div>` element on a web page. |
| **`atlas.source.DataSource`** | A GeoJSON data container attached to a map; all points, lines, and polygons are added to it. |
| **`atlas.layer.BubbleLayer`** | A map layer that renders every GeoJSON Point in its data source as a colored circle (bubble). |
| **`atlas.data.Point`** | A JavaScript object representing one GeoJSON Point geometry with `[longitude, latitude]` coordinates. |
| **`atlas.data.Feature`** | A JavaScript object wrapping a geometry (e.g., a Point) with optional properties, forming one "thing" on the map. |
| **GeoJSON** | An open standard JSON format for encoding geographic data — points, lines, polygons, and collections of features. |
| **FeatureCollection** | The top-level GeoJSON wrapper object that holds an array of `Feature` objects. |
| **`[lon, lat]` order** | The GeoJSON rule that coordinates are always longitude-first, latitude-second — the reverse of how they are normally spoken. |
| **CORS (Cross-Origin Resource Sharing)** | A browser security mechanism that blocks web pages from reading data across different domain origins unless the target server explicitly permits it. |
| **`restype=container&comp=list`** | Two URL query parameters that tell Azure Blob Storage to return an XML list of all blobs in a container. |
| **`DOMParser`** | A JavaScript API for parsing XML or HTML text into a tree structure that code can navigate and query. |
| **`XMLHttpRequest`** | A legacy JavaScript API for making HTTP requests; used here to fetch individual blob JSON files. |
| **`parseFloat()`** | A JavaScript function that converts a string to a decimal number — used because GPS values arrive as strings inside JSON. |
| **`subscriptionKey`** | The API key for an Azure Maps account; passed in every API call for authentication. |
| **Geofence** | A virtual perimeter (circle or polygon) drawn around a real-world location; crossing it triggers a programmed action. |
| **GeoJSON Polygon** | A closed shape defined as an array of `[lon, lat]` coordinate pairs where the last point equals the first point. |
| **`geometryId`** | A required unique identifier inside the `properties` of each geofence polygon feature uploaded to Azure Maps; without it, the API rejects the upload. |
| **UDID (Unique Data ID)** | The identifier returned by Azure Maps after you upload a geofence file; used in all subsequent API calls to reference that geofence. |
| **`searchBuffer`** | The fuzzy distance zone (0–500 m, default 50 m) around a geofence edge; within this zone the API returns exact distance instead of ±999, to handle GPS inaccuracy gracefully. |
| **`distance` (geofence API response)** | The distance in meters from the test point to the nearest geofence edge; positive = outside, negative = inside. |
| **`999` / `-999` (distance magic numbers)** | Sentinel values meaning "beyond the search buffer" — `999` = definitely outside, `-999` = definitely inside. |
| **Consumer group** | An independent read cursor into IoT Hub's message stream; each consumer group has its own bookmark so multiple apps can read the same messages without interfering. |
| **`$Default` consumer group** | The consumer group automatically created with every IoT Hub; used by the event monitor CLI tool and the first Functions trigger. |
| **`consumerGroup` (function.json)** | The setting in an Azure Functions trigger configuration that specifies which consumer group it reads from. |
| **curl** | A command-line tool for making raw HTTP requests (GET, POST, PUT) to web APIs. |
| **`requests` (Python library)** | A Python library that simplifies making HTTP calls; `requests.get(url, params=dict)` appends the dictionary as `?key=value` query parameters automatically. |
| **Azure Maps Geofence API** | The REST endpoint `atlas.microsoft.com/spatial/geofence/json` that checks whether a `[lat, lon]` point is inside or outside an uploaded geofence. |
| **Event Hub trigger** | An Azure Functions binding type that fires a function every time a new message arrives on an IoT Hub (or Event Hub) endpoint. |
| **`event.get_body()`** | The Azure Functions SDK method that returns the raw bytes of the IoT Hub message, which must be decoded from UTF-8 and parsed as JSON. |
| **`event.iothub_metadata['connection-device-id']`** | Metadata automatically attached by IoT Hub that identifies which device sent the message. |
| **Resource group** | A logical container in Azure that groups related cloud resources (IoT Hub, storage, functions, maps) so they can be managed and deleted together. |

---

## 4. COMPARISONS & TRADEOFFS

| Concept A | Concept B | What each is | When to use A | When to use B | Key Tradeoff |
|---|---|---|---|---|---|
| **DMS** (degrees, minutes, seconds) | **Decimal degrees** | Two ways of writing the same coordinate. DMS = `2°17'43"`; decimal = `2.295277`°. | Paper maps, traditional navigation, human reading. | Every computer system, GPS libraries, databases, APIs. | DMS is human-legible but requires conversion math; decimal degrees are computation-ready but harder to visualize mentally. |
| **Structured data** (SQL) | **Unstructured data** (NoSQL / blob) | Structured = fixed schema, tables, relationships. Unstructured = free-form JSON documents with varying fields. | Financial records, user accounts, any data where every record must have the exact same fields. | IoT telemetry from a mixed fleet of devices sending different sensor data. | SQL enforces data quality (no missing fields) at the cost of flexibility. NoSQL accepts anything but requires the application to handle missing or extra fields. |
| **SQL database** (RDBMS) | **NoSQL database** (document store) | SQL = tables with predefined columns, linked by keys. NoSQL = containers of JSON documents with no enforced schema. | When the data shape is known, stable, and every record follows it. | When device types change, new sensors are added, or data fields vary per message — as with IoT fleets. | Schema changes in SQL require ALTER TABLE operations and may cause downtime. Adding fields in NoSQL requires zero database changes — just start including the field in new documents. |
| **Hot path** | **Warm path** | Hot = immediate real-time processing. Warm = processing shortly after receipt. | Temperature alerts in a refrigerated truck, theft detection (driver leaves a geofenced farm). | Daily mileage reports, dashboard generation, route tracing on a map. | Hot-path requires streaming infrastructure and incurs higher compute cost. Warm-path can use cheaper batch processing and tolerate minutes of delay. |
| **Warm path** | **Cold path** | Warm = processed within hours for operational reports. Cold = stored indefinitely for long-term analytics in a data warehouse. | Map visualizations, this week's delivery performance report. | Year-over-year fuel cost analysis, optimal route planning using 5 years of data. | Warm storage is queryable quickly but expensive to retain forever. Cold data warehouses are cheaper per gigabyte but slower to query and designed for read-only historical analysis. |
| **`$GPGGA`** | **`$GNGGA`** | Both are GGA (GPS Fix Data) NMEA sentences. GP = US GPS constellation only. GN = multi-constellation receiver. | A single-constellation GPS receiver (older/cheaper). | A modern receiver listening to GPS + GLONASS + Galileo + BeiDou simultaneously for better accuracy and faster fixes. | GP-only is simpler but may have fewer visible satellites; GN provides better accuracy and reliability in challenging environments (urban canyons, dense foliage). |
| **Circle geofence** | **Polygon geofence** | Circle = center point + radius distance. Polygon = custom shape defined by a list of `[lon, lat]` corner points. | A simple round zone around a single building or depot; easy to define with just a center and radius. | An irregularly shaped area like a campus, school zone, city boundary, or organic field that must be precisely excluded. | Circles are trivial to define but rarely match real-world boundaries. Polygons match reality but require more data and a mandatory `geometryId` property for Azure Maps. |
| **`$Default` consumer group** | **Custom consumer group** (e.g., `geofence`) | Both are independent read cursors into the same IoT Hub message stream. `$Default` is built-in; custom ones are created manually. | The first or only reader of IoT Hub messages. | Every additional reader that needs its own independent view of the same messages (e.g., a second Functions trigger). | Without separate consumer groups, multiple readers share the same cursor and messages get missed. Each consumer group = one bookmark. Rule of thumb: one application per consumer group. |
| **`latitude, longitude` (spoken/written)** | **`[longitude, latitude]` (GeoJSON)** | Two ordering conventions for coordinates. | Human communication, database columns, most API parameters (`?lat=...&lon=...`). | GeoJSON format, Azure Maps `atlas.data.Point([lon, lat])`. | Getting the order wrong silently places points in completely wrong locations. This is one of the most common (and hardest to debug) mistakes in geospatial programming. |
| **`event.iothub_metadata['enqueuedtime']`** | **Current time (`datetime.now()`)** | Two ways to timestamp a stored GPS reading. | The correct choice — it records when the data reached IoT Hub, which is closest to when the GPS reading was actually taken. | Wrong for IoT — it records when the function processed the message, which could be seconds or minutes later if the function was busy. | Using current time loses the true temporal sequence of GPS readings and may misrepresent vehicle speed and route order. |

---

## 5. LIKELY EXAM ANGLES

1. **Coordinate formats and conversion (multiple choice + calculation).** A professor might ask: "An NMEA GGA sentence contains `4738.538654,N`. What is the latitude in decimal degrees?" You must recognize the `(dd)dmm.mmmm` format and compute `47 + (38.538654 / 60) = 47.6423109`. Reverse questions — "Convert 47.6423° to DMS" — are also fair game. Expect a trap answer that forgets to divide by 60.

2. **SQL vs. NoSQL — why IoT data calls for NoSQL (short answer).** "Explain why a logistics company tracking a mixed fleet of tractors, delivery vans, and refrigerated trucks should use a NoSQL database rather than a SQL database." You need to argue: different vehicle types send different fields, new sensors get added over time, NoSQL accepts any JSON shape without schema migration, and forcing heterogeneous data into one rigid table creates constant ALTER TABLE overhead.

3. **Hot/Warm/Cold paths — classify a scenario (multiple choice).** "A trucking company wants to detect when a refrigerated trailer's temperature exceeds 5°C and alert the driver within 3 seconds. Which data path should be used?" (Answer: hot path.) "The same company wants to generate a monthly report of fuel costs per route. Which path?" (Answer: cold path.) Expect scenarios that test whether you understand the latency requirement for each path.

4. **Geofence distance interpretation (multiple choice).** Given a JSON response snippet containing `"distance": 999`, `"distance": -999`, `"distance": 23`, or `"distance": -12`, ask "Is the vehicle inside or outside the geofence?" You must know: positive = outside, negative = inside, ±999 = beyond the search buffer (>50 m), small values = within the fuzzy search-buffer zone. A follow-up might ask: "Why would you not immediately trigger an alert for `distance: 12`?" (Because GPS inaccuracy could mean the truck is actually inside.)

5. **Consumer groups — why they exist and what problem they solve (short answer).** "You have one IoT Hub and two Azure Functions that both need to read the same GPS messages — one stores them to blob storage, one checks them against a geofence. Why can't both functions just read from the same endpoint, and how do you fix it?" You must explain that they would share a read cursor and miss messages, and that creating a second consumer group gives each function its own independent cursor.

6. **GeoJSON coordinate order (trap question).** "Given a GeoJSON Point, write the JavaScript code to create it from a GPS reading of latitude 47.64, longitude -122.14." The correct answer is `new atlas.data.Point([-122.14, 47.64])` — longitude first. Expect a distractor answer with `[47.64, -122.14]`.

---

## 6. GAPS / AMBIGUITIES

- **"Event Hub endpoint" vs. "IoT Hub" is not clearly distinguished.** Lesson 12 states that the Functions trigger uses `"type": "eventHubTrigger"` and connects to an IoT Hub connection string. The material does not explain *why* IoT Hub exposes an "Event Hub-compatible endpoint" or what Event Hubs are independently. For exam purposes, treat them as: IoT Hub is the device-facing message ingestion service, and its internal message stream is accessible using Event Hub protocols (which is what the Functions trigger uses). The concepts are intentionally blurred at this introductory level.

- **CounterFit is referenced as a virtual sensor simulator but never formally introduced in these lessons.** Lesson 11 mentions it as a "text socket sensor" that sends NMEA sentences, and the code reads from `socket.connect(('127.0.0.1', 5000))`. If the exam asks about device setup, know that CounterFit is a simulated-device tool used when you don't have physical hardware — it pretends to be a GPS sensor by sending fake NMEA data over a local network socket.

- **Hardware guides are mentioned but not included.** Lesson 11 references three external files (`pi-gps-sensor.md`, `wio-terminal-gps-sensor.md`, `virtual-device-gps-sensor.md`) that are not part of this four-lesson set. If exam questions about specific hardware wiring or pin connections appear, they likely come from those supplementary files, which were not provided.

- **"RUC" (Road User Charges) is used without expansion.** Lesson 11 mentions New Zealand's RUC as an example of tax compliance for diesel vehicles. The full term is never spelled out. For exam purposes, it is enough to know: some governments charge road tax per kilometer driven, and GPS tracking on connected vehicles can automatically distinguish kilometers on public roads (taxable) from those on private land (exempt).

- **The relationship between `azure-iot-device` and `IoTHubDeviceClient` is assumed rather than taught.** Lesson 11 imports `IoTHubDeviceClient` and calls `device_client.send_message()` without explaining what a device client is, how it authenticates, or what a device connection string looks like. For this module's exam, treat `IoTHubDeviceClient` as a pre-configured object that knows how to securely send JSON messages from the device to IoT Hub — the setup steps are in earlier modules, not in this Transport module.

- **`pynmea2` parsing is shown but the library's full capabilities are not explored.** The lesson only uses `.latitude` and `.longitude`. The GGA sentence also includes altitude (`msg.altitude`), satellite count, and fix quality — none of which are discussed. If an exam question asks "which NMEA message type contains altitude," the answer is GGA, but the lesson does not explicitly show how to extract it beyond noting that GGA "contains latitude, longitude, altitude, and number of satellites."

- **REST API query parameter syntax is briefly mentioned but may confuse.** The note in Lesson 14 says "add `?key=value` after the URL, separated by `&`" — this is correct but may leave a beginner thinking they must manually construct URLs. The Python code actually uses `requests.get(url, params=dict)`, which does this construction automatically. Both approaches are valid; the `requests` library approach is safer because it handles URL-encoding of special characters.