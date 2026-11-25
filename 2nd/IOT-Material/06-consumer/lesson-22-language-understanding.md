---
tags: [iot, consumer, nlp, language-understanding, luis, intents, entities, http-trigger, azure-functions, smart-timer]
project: "06 - Consumer"
lesson: 22
topic: "Understand Language"
---

# Lesson 22 — Understand Language

## Overview

This lesson introduces **Natural Language Understanding (NLU)** — using AI to extract meaning and intent from text. It covers **LUIS (Language Understanding Intelligent Service)** from Microsoft, including the concepts of **intents** (what the user wants) and **entities** (the specifics they mention). The lesson shows how to train a LUIS model for a smart timer (detecting "set timer" intent with time entities), test and publish it, and then call it from an **Azure Functions HTTP trigger** so IoT devices can call a REST endpoint directly for immediate responses.

## Concepts

### Language Understanding (Natural Language Understanding)

**Language understanding** (also called NLU, part of **NLP — natural language processing**) deals with reading comprehension — making computers understand the meaning of words and sentences.

**Why it's hard for computers:**
- "Play the latest album by Taylor Swift" requires understanding: music needs to be played; it's by a specific artist; "latest" means sorted chronologically; the whole album is required.
- A fixed-phrase parser would fail if the user says "Set a timer for 3 minutes" instead of "Set a 3 minute timer" — even though both mean the same thing.

> [!NOTE]
> Language understanding models don't truly "understand" language the way humans do. They extract key details from text — intents and entities — to perform a specific task.

**Approach:** Language understanding models are trained on general language, then fine-tuned using transfer learning on specific examples (utterances) for a specific domain — in the same way Custom Vision uses a small set of images.

---

### LUIS (Language Understanding Intelligent Service)

**LUIS** is Microsoft's Cognitive Service for language understanding. It learns from example sentences (utterances) and extracts:
- **Intents**: What the user wants to do.
- **Entities**: The specific data values in the sentence.

**LUIS portal**: [luis.ai](https://luis.ai)

**Azure resources needed:**
- `LUIS.Authoring`: For training models (free F0 tier).
- Optionally: `LUIS.Prediction` for production (free tier allows 1,000 predictions/month).

---

### Intents and Entities

**Intent**: The purpose or goal of a sentence.
**Entity**: A piece of specific data extracted from the sentence.

| Sentence | Intent | Entities |
|----------|--------|----------|
| "Play the latest album by Taylor Swift" | *play music* | artist: Taylor Swift, type: album, timing: latest |
| "Set a 3 minute timer" | *set timer* | number: 3, time-unit: minute |
| "Cancel my timer" | *cancel timer* | (none) |
| "Order 3 large pineapple pizzas and a caesar salad" | *order food* | item: pizza (3 large pineapple), item: salad (caesar) |

**Utterances**: Example sentences provided during training to teach LUIS a specific intent.

---

### Entities for the Smart Timer

For "set timer", two entity types are needed:

1. **`number`** (prebuilt): LUIS's built-in number entity — recognizes numerals and written-out numbers (3, four, 17, thirty).

2. **`time unit`** (list): Custom list entity.
   - Normalized value: `minute` → Synonyms: `minute`, `minutes`
   - Normalized value: `second` → Synonyms: `second`, `seconds`

**Entity matching:** LUIS matches written and numeric forms: "four minutes" = `number: 4, time-unit: minute`.

---

### Training Utterances for `set timer` Intent

Provide varied examples so LUIS learns different phrasings:

```
set a 1 second timer
set a 4 minute timer
set a four minute six second timer
set a 9 minute 30 second timer
set a timer for 1 minute and 12 seconds
set a timer for 3 minutes
set a timer for 3 minutes and 1 second
set a timer for three minutes and one second
set a timer for 1 minute and 1 second
set a timer for 30 seconds
set a timer for 1 second
```

> [!TIP]
> Mix numeric and written-out numbers ("3" and "three") — LUIS needs to see both to handle both reliably.

As utterances are entered, LUIS automatically detects and labels entities (underlines them in the portal).

---

### LUIS API Response

**curl test:**
```sh
curl "<endpoint_url>/luis/prediction/v3.0/apps/<app_id>/slots/staging/predict" \
     --request GET \
     --get \
     --data "subscription-key=<primary_key>" \
     --data "verbose=false" \
     --data "show-all-intents=true" \
     --data-urlencode "query=set a timer for 45 minutes and 12 seconds"
```

**Response:**
```json
{
    "query": "set a timer for 45 minutes and 12 seconds",
    "prediction": {
        "topIntent": "set timer",
        "intents": {
            "set timer": { "score": 0.97031575 },
            "None": { "score": 0.02205793 }
        },
        "entities": {
            "number": [45, 12],
            "time-unit": [
                ["minute"],
                ["second"]
            ]
        }
    }
}
```

**Entity structure:**
- `number`: flat array of extracted numbers in the order spoken.
- `time-unit`: array of arrays — each time unit is a one-element array (allows multiple synonyms to map to the same normalized value).

**Pairing numbers and time units:** They are in the same order as spoken → pair by index:
- Index 0: number = 45, time-unit = "minute" → 45 × 60 = 2700 seconds
- Index 1: number = 12, time-unit = "second" → 12 seconds
- **Total: 2712 seconds**

---

### HTTP Trigger (Azure Functions)

**Why use an HTTP trigger instead of calling LUIS directly?**

| Direct device call to LUIS | Via HTTP trigger (serverless) |
|--------------------------|-------------------------------|
| LUIS key baked into device firmware | LUIS key never on device |
| All devices must be updated when LUIS changes | Only update the function — all devices automatically get new behavior |
| Harder to test | Easy to test with curl |

**HTTP triggers** allow Azure Functions to listen for REST requests and respond:
- URL: `http://localhost:7071/api/text-to-timer`
- Method: POST
- Body: `{"text": "set a 3 minute timer"}`
- Response: `{"seconds": 180}`

**Cloud-deployed URL:** `https://<APP_NAME>.azurewebsites.net/api/text-to-timer?code=<FUNCTION_KEY>`

> [!NOTE]
> When deployed to Azure, HTTP triggers require a function app key by default. Pass it as the `code` query parameter.

## Hardware / Setup

**Azure resources:**

1. LUIS Authoring resource:
```sh
az cognitiveservices account create --name smart-timer-luis-authoring \
                                    --resource-group smart-timer \
                                    --kind LUIS.Authoring \
                                    --sku F0 \
                                    --yes \
                                    --location <location>
```

> [!CAUTION]
> LUIS is not available in all regions. If you get `InvalidApiSetId`, try a different region (e.g., `westus`, `eastus`).

2. LUIS portal: [luis.ai](https://luis.ai) → New app → Name: `smart-timer` → Culture: your language.

3. Azure Functions app: `smart-timer-trigger`

**Install pip packages:**
```sh
pip install azure-cognitiveservices-language-luis
```

**`local.settings.json`:**
```json
{
    "Values": {
        "LUIS_KEY": "<primary key>",
        "LUIS_ENDPOINT_URL": "<endpoint url>",
        "LUIS_APP_ID": "<app id>"
    }
}
```

## Code Walkthrough

### Create HTTP Trigger

```sh
func new --name text-to-timer --template "HTTP trigger"
```

HTTP trigger URL: `http://localhost:7071/api/text-to-timer`

---

### Full `text-to-timer/__init__.py`

```python
import json
import logging
import os
import azure.functions as func
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials


def main(req: func.HttpRequest) -> func.HttpResponse:
    # 1. Read environment settings
    luis_key = os.environ['LUIS_KEY']
    endpoint_url = os.environ['LUIS_ENDPOINT_URL']
    app_id = os.environ['LUIS_APP_ID']

    # 2. Create LUIS client
    credentials = CognitiveServicesCredentials(luis_key)
    client = LUISRuntimeClient(endpoint=endpoint_url, credentials=credentials)

    # 3. Extract text from request body
    req_body = req.get_json()
    text = req_body['text']
    logging.info(f'Request - {text}')

    # 4. Send prediction request to LUIS
    prediction_request = {'query': text}
    prediction_response = client.prediction.get_slot_prediction(app_id, 'Staging', prediction_request)

    # 5. Process response
    if prediction_response.prediction.top_intent == 'set timer':
        numbers = prediction_response.prediction.entities['number']
        time_units = prediction_response.prediction.entities['time unit']
        total_seconds = 0

        # 6. Pair numbers with time units by index
        for i in range(0, len(numbers)):
            number = numbers[i]
            time_unit = time_units[i][0]  # each time-unit is a list: ['minute'] or ['second']

            if time_unit == 'minute':
                total_seconds += number * 60
            else:
                total_seconds += number

        logging.info(f'Timer required for {total_seconds} seconds')

        # 7. Return total seconds as JSON
        payload = {'seconds': total_seconds}
        return func.HttpResponse(json.dumps(payload), status_code=200)

    # 8. Return 404 if intent not recognized
    return func.HttpResponse(status_code=404)
```

**Code explanation:**

| Line | Explanation |
|------|-------------|
| `CognitiveServicesCredentials(luis_key)` | Wraps the LUIS API key in a credentials object |
| `LUISRuntimeClient(endpoint, credentials)` | Creates the LUIS client to call the prediction API |
| `req.get_json()` | Parses the POST body as JSON |
| `req_body['text']` | Extracts the recognized speech text sent from the IoT device |
| `prediction_request = {'query': text}` | LUIS prediction input — the text to classify |
| `client.prediction.get_slot_prediction(app_id, 'Staging', request)` | Calls the LUIS staging slot for a prediction |
| `prediction_response.prediction.top_intent` | The intent with the highest probability |
| `prediction_response.prediction.entities['number']` | List of extracted numbers in order spoken |
| `prediction_response.prediction.entities['time unit']` | List of extracted time units in order spoken |
| `time_units[i][0]` | Each time unit is a nested list — `[0]` gets the normalized value |
| `total_seconds += number * 60` | Converts minutes to seconds |
| `func.HttpResponse(json.dumps(payload), status_code=200)` | Returns JSON response with HTTP 200 |
| `func.HttpResponse(status_code=404)` | Returns HTTP 404 (not found) if intent was not `set timer` |

---

### Test with curl

```sh
curl --request POST 'http://localhost:7071/api/text-to-timer' \
     --header 'Content-Type: application/json' \
     --include \
     --data '{"text":"set a 2 minutes 27 second timer"}'
```

**Expected response:**
```output
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8

{"seconds": 147}
```

**Functions output log:**
```output
[2021-06-26T19:45:53.577Z] Timer required for 147 seconds
[2021-06-26T19:45:53.746Z] Executed 'Functions.text-to-timer' (Succeeded, ...)
```

---

### Call from IoT Device

```python
import requests

FUNCTION_URL = 'http://<IP_ADDRESS>:7071/api/text-to-timer'
# For cloud: 'https://<APP_NAME>.azurewebsites.net/api/text-to-timer?code=<FUNCTION_KEY>'


def get_timer_seconds(text):
    """Send recognized text to the Functions app and get timer duration in seconds."""
    response = requests.post(
        FUNCTION_URL,
        json={'text': text}
    )
    if response.status_code == 200:
        return response.json()['seconds']
    return None


# --- Main flow ---
text = recognize_speech()  # From Lesson 21
if text:
    seconds = get_timer_seconds(text)
    if seconds:
        print(f"Setting timer for {seconds} seconds")
```

## How It Works

```mermaid
flowchart LR
    Mic[Microphone] -->|audio| SDK[Speech SDK\nrecognize_once]
    SDK -->|"set a 3 minute timer"| Device[IoT Device app.py]
    Device -->|POST /api/text-to-timer\n{"text": "set a 3 minute timer"}| Fn[Azure Functions\ntext-to-timer]
    Fn -->|get_slot_prediction| LUIS[LUIS API\nStaging slot]
    LUIS -->|topIntent: set timer\nnumber: [3]\ntime unit: [minute]| Fn
    Fn -->|number=3, unit=minute → 180s| Fn
    Fn -->|{"seconds": 180}| Device
    Device -->|set countdown 180s| Timer[Timer]
```

## Key Terms

| Term | Definition |
|------|------------|
| Language understanding (NLU) | AI that extracts meaning, intent, and structured data from free-form text |
| NLP (Natural Language Processing) | The broader field of AI dealing with text understanding, generation, and translation |
| LUIS (Language Understanding Intelligent Service) | Microsoft Cognitive Service for training and calling language understanding models |
| Intent | The goal or purpose of a user's sentence (e.g., `set timer`, `cancel timer`) |
| Entity | A specific piece of data extracted from a sentence (e.g., number, time unit) |
| Utterance | An example sentence used to train a LUIS intent |
| Prebuilt entity | An entity type provided out-of-the-box by LUIS (e.g., `number`, `location`) |
| List entity | A custom entity defined by a list of values and their synonyms |
| Normalized value | The canonical form of an entity value (e.g., `minute` for both "minute" and "minutes") |
| Synonym | An alternative form of a normalized value in a list entity (e.g., "minutes" for `minute`) |
| Top intent | The intent with the highest prediction probability for a given utterance |
| Staging slot | A LUIS deployment environment for testing before production release |
| `LUIS_APP_ID` | The unique identifier for a LUIS application |
| `LUIS_KEY` | The API key for the LUIS authoring or prediction resource |
| `LUISRuntimeClient` | Python SDK class for calling the LUIS prediction API |
| `get_slot_prediction` | SDK method that sends a text query to a specific LUIS deployment slot |
| HTTP trigger | An Azure Functions trigger type that responds to HTTP requests (GET/POST) |
| `func.HttpRequest` | Azure Functions Python class representing an incoming HTTP request |
| `func.HttpResponse` | Azure Functions Python class for building an HTTP response |
| `req.get_json()` | Parses the POST body of an HTTP request as JSON |
| HTTP 200 | Standard success status code for HTTP responses |
| HTTP 404 | "Not found" status code; returned when the intent is not recognized |
| Function key | A security key required to call a deployed Azure Functions HTTP trigger |
| `code` query parameter | The URL parameter used to pass a function key to a deployed HTTP trigger |

## Summary

- **Language understanding** extracts **intent** (what the user wants) and **entities** (specific values) from free-form text.
- LUIS models are trained using example sentences (**utterances**) and fine-tuned using transfer learning.
- **Intents**: e.g., `set timer`, `cancel timer`. Each needs at least 5–10+ varied utterances.
- **Entities** for smart timer: prebuilt `number` + custom list `time unit` (minute/minutes, second/seconds).
- Entities are ordered as spoken → pair by index: `numbers[i]` → `time_units[i][0]`.
- Convert: minutes × 60 + seconds = total seconds.
- LUIS response: `topIntent`, `intents` (all with scores), `entities` (by type, in order spoken).
- Use an **HTTP trigger** (not direct LUIS call) so LUIS key stays in the cloud and updating LUIS doesn't require re-deploying device firmware.
- Test curl: `POST /api/text-to-timer` with `{"text": "..."}` → `{"seconds": N}`.
- IoT device sends recognized text → gets seconds back → sets countdown timer.
- Cloud deployment URL: `https://<APP_NAME>.azurewebsites.net/api/text-to-timer?code=<FUNCTION_KEY>`.
