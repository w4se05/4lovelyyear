# Module 05 — Retail: Study Sheet

---

## 1. MODULE OVERVIEW

A supermarket shelf can run out of stock or have items placed in the wrong spot, leading to lost sales or spoiled goods. This module solves that problem by teaching an IoT system to **look at a shelf photo and count the items on it** using a type of AI called object detection. Lesson 19 covers how to train such an AI model inside a cloud service (Azure Custom Vision) by drawing boxes around products in training images. Lesson 20 then shows how to run that trained model from a real IoT device (e.g., a camera pointed at a shelf), count visible items, filter out mistakes the model might make, and send a restock alert when the count is too low.

---

## 2. KEY CONCEPTS

### Concept 1: Object Detection (versus Image Classification)

- **Plain-language definition**: Image classification looks at a whole photo and says "this is a cat." Object detection looks at the same photo, draws a box around each cat, counts how many there are, and tells you where each one sits in the picture.
- **Why it matters**: For a retail shelf, you need to know *how many* cans of tomato paste are visible and *which slots* are empty — a whole-image label cannot answer either question.
- **Concrete example from the material**: A picture containing cashew nuts and three cans of tomato paste. The object detector returns four separate results — one for cashew nuts and three for tomato paste — each with its own bounding box and confidence percentage.

### Concept 2: Bounding Box

- **Plain-language definition**: A rectangle drawn around a detected object in a photo, described by four numbers: how far the box is from the top edge, how far from the left edge, how tall it is, and how wide it is.
- **Why it matters**: Without a bounding box, you cannot count objects (two side-by-side cans would look like one big blob) and you cannot tell a restocking robot exactly which shelf slot is empty.
- **Concrete example from the material**: On a 600×800 pixel image, a tomato paste can detected at pixel position (top=320, left=240, height=240, width=120) converts to normalized coordinates (top=0.4, left=0.4, height=0.3, width=0.2).

### Concept 3: Normalized Coordinates (0–1 Scale)

- **Plain-language definition**: Instead of giving bounding-box numbers in raw pixels (which change if the image is resized), every coordinate is expressed as a fraction. "Top = 0.4" means "the box starts 40% of the way down from the top of the image" — it stays correct whether the image is thumbnail-sized or poster-sized.
- **Why it matters**: IoT cameras may produce different image resolutions; normalized coordinates make the numbers resolution-independent, so the same code works across different hardware.
- **Concrete example from the material**: All four bounding-box fields (`top`, `left`, `height`, `width`) are fractions between 0 and 1; a 320-pixel top coordinate in an 800-pixel-tall image becomes 320/800 = 0.4.

### Concept 4: Overlapping Bounding Boxes (False Positive Filtering)

- **Plain-language definition**: Sometimes the object detector gets "nervous" and draws two nearly identical boxes around the same physical object, one slightly inside the other, each with a different confidence percentage. The lower-confidence one is a mistake (a false positive).
- **Why it matters**: If the code doesn't filter these duplicates, it will overcount items on the shelf — thinking there are 9 cans when only 8 exist — and never send the restock alert when stock is actually low.
- **Concrete example from the material**: Detection 1 says tomato paste at 78.3% in box [0.2, 0.4, 0.3, 0.2]; Detection 2 says tomato paste at 64.3% in box [0.21, 0.41, 0.28, 0.19]. Box 2 sits almost entirely inside Box 1 → discard Box 2 (lower probability).

### Concept 5: Probability Threshold

- **Plain-language definition**: A cut-off number (e.g., 0.5 = 50%) that tells the system "ignore any detection the model is less than 50% confident about."
- **Why it matters**: Without this, the model's wild guesses get counted as real items, producing phantom stock that makes the shelf look fuller than it really is.
- **Concrete example from the material**: The lesson code sets `PROBABILITY_THRESHOLD = 0.5` and filters predictions with `if p['probability'] >= PROBABILITY_THRESHOLD`.

### Concept 6: Transfer Learning

- **Plain-language definition**: Instead of training an AI model from scratch (which needs millions of images), you take a model that has already learned to recognise general shapes and objects, and you fine-tune it on your specific task — like teaching it to spot tomato paste cans instead of general "bottles" or "cans."
- **Why it matters**: A beginner collecting 15–50 shelf photos cannot train a model from zero that works. Transfer learning makes this practical by reusing existing knowledge.
- **Concrete example from the material**: The lesson references YOLO — a popular pre-trained model that knows 20 general object classes — and notes it can be retrained via transfer learning to detect custom objects like cashew nuts.

### Concept 7: Model Retraining for Object Detection

- **Plain-language definition**: After the first training round, you feed the model new images it hasn't seen. The model draws its best-guess boxes, you correct the mistakes (move boxes, change labels, delete false detections), and then retrain. The model learns from these corrections.
- **Why it matters**: A model trained once on a limited set of images will make mistakes on real-world shelf photos (different lighting, angles, product arrangements). Retraining with corrections steadily improves accuracy.
- **Concrete example from the material**: In the Custom Vision Predictions tab, each red bounding box must be manually reviewed: confirm correct ones, resize misaligned ones, fix wrong tags, delete phantom detections — then click Train again.

### Concept 8: Stock Counting Pipeline

- **Plain-language definition**: A sequence of steps an IoT device runs: (1) take a photo of the shelf, (2) send it to the cloud AI, (3) get back a list of detected objects with boxes and confidences, (4) discard low-confidence and overlapping duplicates, (5) count the remaining items of the target product, (6) compare the count to the shelf's known capacity, (7) alert staff if count is too low.
- **Why it matters**: This is the complete blueprint for how a real IoT retail system works end-to-end, connecting the trained model (Lesson 19) to a functioning device (Lesson 20).
- **Concrete example from the material**: The Python code in Lesson 20 implements each stage — `get_image()` → `detect_stock()` → `filter_predictions()` → `count_stock()` — and produces the output `"RESTOCK NEEDED: 1 item(s) missing"`.

---

## 3. KEY TERMS

| Term | Plain-language definition |
|---|---|
| **Object detection** | AI technique that finds, labels, and counts multiple objects in an image by drawing a bounding box around each one. |
| **Image classification** | AI technique that assigns a single label (and confidence) to an entire image without locating anything inside it. |
| **Bounding box** | A rectangle around a detected object, defined by four numbers (top, left, height, width) as fractions of the image size. |
| **Normalized coordinates** | Bounding box measurements expressed as 0–1 fractions of image width/height, so they work regardless of pixel dimensions. |
| **Tag (object detection)** | The name/label assigned to an object inside a bounding box when training (e.g., "tomato paste"). |
| **Tight bounding box** | A bounding box drawn as close as possible to the edges of the object, without including excess background. |
| **Precision** | Of all the boxes the model predicted for a tag, what fraction were actually correct (not false alarms). |
| **Recall** | Of all the real objects in the image, what fraction did the model successfully detect (didn't miss). |
| **mAP (mean Average Precision)** | A single summary score for object detection quality, averaged across all object types. |
| **IoU (Intersection over Union)** | A number (0–1) measuring how much two bounding boxes overlap; used to decide if two detections are really the same object. |
| **Probability threshold** | A minimum confidence cutoff (e.g., 0.5) below which predictions are thrown away as unreliable. |
| **Overlapping bounding boxes** | Two predicted boxes for the same object where one box sits mostly inside the other; the lower-confidence one is a duplicate to discard. |
| **YOLO (You Only Look Once)** | A famous, very fast object detection model that can recognise 20 classes of everyday objects in real time. |
| **Transfer learning** | Taking a model already trained on general images and fine-tuning it to recognise your specific objects instead. |
| **Products on Shelves** | A pre-tuned Custom Vision domain specifically designed for detecting retail products sitting on store shelves. |
| **Suggested tags** | A Custom Vision feature where a partially-trained model auto-suggests bounding boxes on new images to speed up labelling. |
| **Custom Vision** | Microsoft's cloud service for training image classification and object detection models without writing AI code. |
| **Stock counting** | Using object detection to count how many items of a specific product are visible on a shelf. |
| **SHELF_CAPACITY** | The known maximum number of items a shelf section can hold when fully stocked. |
| **STOCK_TAG** | The specific product label to count among all detections (e.g., "tomato paste"). |
| **Restock notification** | An alert sent to staff or a robot when the detected item count falls below SHELF_CAPACITY. |
| **Wrong stock detection** | Using object detection to spot items that are on the wrong shelf (e.g., baby corn on the tomato paste shelf). |
| **`/detect/` (API path)** | The REST API URL path for calling the object detection endpoint (different from `/classify/` used for image classification). |
| **`boundingBox` (API field)** | The JSON field in each prediction result containing the four normalized coordinates (top, left, height, width). |
| **Prediction-Key** | The secret authentication token sent in the HTTP header to prove you are allowed to call the Custom Vision API. |
| **False positive** | A detection the model made that does not correspond to any real object in the image (a mistake). |
| **Iteration** | A specific trained version of the model; each retraining session produces a new iteration that can be published separately. |

---

## 4. COMPARISONS & TRADEOFFS

### Comparison 1: Image Classification vs. Object Detection

| Aspect | Image Classification | Object Detection |
|---|---|---|
| **What it is** | Assigns one label to the whole image. | Finds and labels multiple individual objects inside the image. |
| **Output** | A list of (tag, probability) pairs for the entire image. | A list of (tag, probability, bounding box) for each detected object. |
| **Can count items?** | No. | Yes. |
| **Tells you where?** | No. | Yes — bounding box coordinates. |
| **Training data needed** | Images tagged with class labels. | Images with manual bounding boxes drawn around every object. |
| **Use when** | You only need to know *what* is in the photo (e.g., "this shelf has cashew nuts"). | You need to know *how many* and *where* (e.g., count cans, locate empty slots). |

### Comparison 2: Classifier Retraining vs. Object Detector Retraining

| Aspect | Classifier Retraining | Object Detector Retraining |
|---|---|---|
| **What it is** | Adding or re-tagging images and re-running training. | Manually reviewing every predicted bounding box (confirm, resize, re-tag, or delete), then re-running training. |
| **Effort** | Low — just add correct tags. | High — every box on every image must be inspected and adjusted individually. |
| **When it matters** | Enough for simple whole-image decisions. | Critical when the model will be used to count items in real-world varying conditions. |

### Comparison 3: Raw Pixel Coordinates vs. Normalized (0–1) Coordinates

| Aspect | Raw Pixels | Normalized (0–1) |
|---|---|---|
| **What it is** | Bounding box positions given in actual pixel numbers (e.g., top=320px). | Bounding box positions given as fractions of image dimensions (e.g., top=0.4). |
| **Device-independent?** | No — changes if image resolution changes. | Yes — same fraction works at any resolution. |
| **Use when** | Rarely — only if you control exact camera resolution and it never changes. | Always — the standard for object detection APIs and portable code. |

### Comparison 4: `/classify/` API Path vs. `/detect/` API Path

| Aspect | `/classify/` | `/detect/` |
|---|---|---|
| **What it is** | The Custom Vision REST endpoint for image classification. | The Custom Vision REST endpoint for object detection. |
| **Response includes** | `tagName` + `probability` only. | `tagName` + `probability` + `boundingBox`. |
| **Use when** | You trained a classification model. | You trained an object detection model. |

---

## 5. LIKELY EXAM ANGLES

1. **"Which of the following best describes the difference between image classification and object detection?"** — Expect multiple-choice answers that test whether you know classification gives one label for the whole image while object detection gives bounding boxes and counts per object. A wrong answer might say "object detection also classifies but is slower" or mix up which returns bounding boxes.

2. **"Explain why overlapping bounding boxes are a problem for stock counting and describe how they are handled."** — A short-answer question asking you to describe the duplicate-filtering process: a physical can cannot be inside another can, so when two same-tag boxes overlap significantly, the lower-probability one is a false positive and must be discarded. Should mention the overlap-calculation logic.

3. **"A bounding box is returned with top=0.25, left=0.4, height=0.15, width=0.1. What is the right edge of this box as a fraction of image width?"** — A calculation question testing whether you know `right = left + width` (0.4 + 0.1 = 0.5) and `bottom = top + height` (0.25 + 0.15 = 0.4). Tests understanding of normalized coordinates.

4. **"List and briefly describe three steps in the stock-counting pipeline that happen after receiving the API response."** — Expect you to mention: (1) apply probability threshold to discard low-confidence detections, (2) remove overlapping/duplicate bounding boxes for the same tag, (3) count remaining detections matching the target STOCK_TAG and compare to SHELF_CAPACITY.

5. **"Why is retraining an object detector more complex than retraining a classifier? Describe the process."** — Short-answer expecting you to explain that object detector retraining requires manual review of every bounding box per image (confirm, resize, re-tag, delete), whereas classifier retraining only needs correct tags assigned to whole images. Should mention the Predictions tab workflow.

---

## 6. GAPS / AMBIGUITIES

- **No explanation of how IoU is actually calculated** — Lesson 19 defines the acronym and says it's a metric, but never shows the formula. Lesson 20 uses a simpler "is box2 mostly inside box1?" check instead of true IoU. A professor might expect you to know the IoU concept even though the calculation isn't shown.

- **Precision vs. Recall definitions are context-switching** — In Lesson 19 these are defined in the context of object detection (per-box), but in earlier modules a student may have learned them in a classification context. The difference isn't explicitly called out. Make sure you know that in object detection, precision = "of all *boxes predicted*, how many were right" and recall = "of all *real objects*, how many were found."

- **Suggested Tags feature is mentioned but the mechanics are thin** — The lesson says "use Suggested Tags after 15+ images" but does not explain *how* the semi-trained model generates box suggestions or what a student should do if suggestions are wildly wrong. Treat this as a feature name to recognise, not a process to memorise.

- **No real vs. synthetic shelf image discussion** — The training data instructions say "show objects as if on store shelves" but do not discuss whether photos of a kitchen table with cans on it would work. The Products on Shelves domain is tuned for real retail shelving; substituting non-shelf backgrounds may reduce accuracy. This is an unstated assumption worth flagging.

- **Lesson 20's overlap filter uses a custom 80%-containment check, not formal IoU** — The code function `boxes_overlap()` checks whether box2's area is more than 80% inside box1. This is a useful heuristic but simpler than the standard IoU + NMS (Non-Maximum Suppression) approach used in production object detectors. An exam might conceptually ask about "how to handle overlapping detections" — either answer (the 80% containment rule from the lesson or mentioning IoU) should be acceptable, but know both terms.

- **No discussion of lighting, camera angle, or occlusion** — Real shelves have glare, shadows, products pushed to the back, and items behind other items. The lessons assume clear, front-facing shelf photos. A real deployment would need to handle these, but the module stays silent on these challenges.

- **The `F0` (free) tier constraint** — The lesson mentions you can only have one free Custom Vision resource at a time. This isn't an AI concept but could be a practical exam nuisance if the student is asked about Azure setup constraints.
