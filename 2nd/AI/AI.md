Here is a structured and beautifully formatted Markdown version of your project documentation, optimized for Obsidian.

---

# Complete Project Documentation

## Overview

This notebook implements **CROHME-CTC**: an end-to-end CTC-based pipeline for recognising online handwritten mathematical expressions from the CROHME 2019 dataset.

> **Pipeline Flow:**
> * **InkML strokes**
> * → `feature_extraction` ($dx/d$, $dy/d$, $d$, `pen_up`)
> * → `InkmlDataset` / `collate_fn` / `DataLoader`
> * → `LSTMTemporalClassifier` (BiLSTM + Linear + LogSoftmax)
> * → `nn.CTCLoss`
> * → `GreedyCTCDecoder` / `BeamCTCDecoder`
> * → `edit_distance` / `word_error_rate` / `split_wer`
> * → **WandB** logs + checkpoints
> 
> 

---

## Task 1 – Vocabulary (`get_unique_tokens`, `Vocab`)

### What it does

* `get_unique_tokens` reads every annotation file (tab-separated `inkml_path\tlabel`) and returns the set of all non-empty label tokens.
* `Vocab` wraps a `char2idx` / `idx2char` bidirectional mapping.

### Key Design Decision

The blank token `""` is inserted into the token set and the set is sorted lexicographically. Because the empty string sorts before every printable character, **blank always receives index 0** — exactly what `nn.CTCLoss` requires without any hard-coding.

### How to use

```python
vocab = Vocab()
vocab.build_vocab([TRAIN_ANNOTATION, VAL_ANNOTATION, TEST_ANNOTATION])

vocab.save(VOCAB_PATH)          # serialises char2idx as JSON
vocab.load(VOCAB_PATH)          # reloads later

ids    = vocab.encode(["Right", "\\sqrt", "2"])   # → [37, 74, 10]
tokens = vocab.decode(ids)                        # → ["Right", "\\sqrt", "2"]

```

---

## Task 2 – Feature Extraction (`feature_extraction`)

### What it does

Converts raw InkML strokes into a fixed-width feature tensor of shape `(T, 4)`.

| Column | Formula | Meaning |
| --- | --- | --- |
| **0** | $\Delta x / d$ | Normalised horizontal displacement |
| **1** | $\Delta y / d$ | Normalised vertical displacement |
| **2** | $d = \sqrt{\Delta x^2 + \Delta y^2}$ | Euclidean step size |
| **3** | `pen_up` $\in \{0, 1\}$ | $1$ when crossing between strokes |

### Key Design Decisions

* **Vectorization:** Strokes are concatenated into one point array before differencing, so NumPy computes all differences in a single vectorised call.
* **NaN Handling:** Zero-distance steps ($\Delta x = 0, \Delta y = 0$) are dropped to avoid $0/0$ `NaN`.
* **Data Filtering:** Only the first two columns ($x, y$) of each point are used; extra columns (e.g., timestamps) are silently ignored.

---

## Task 3 – Dataset (`InkmlDataset`)

### What it does

A `torch.utils.data.Dataset` that maps an annotation row to a `(features, targets, input_len, target_len)` tuple.

### Key Design Decisions

* Annotation parsing happens in `__init__` so disk I/O is front-loaded.
* Rows with empty labels are skipped at parse time.
* `__getitem__` is lazy: it parses the InkML file and runs feature extraction on demand, so memory usage scales with batch size, not dataset size.

---

## Task 4 – Collating and DataLoaders (`collate_fn`, `create_dataloaders`)

### What it does

* `collate_fn` pads variable-length samples into rectangular tensors and returns `(features, targets, input_lens, target_lens)`.
* `create_dataloaders` builds train (shuffled), validation, and test loaders.

### Key Design Decisions

* `pad_sequence(..., batch_first=True)` gives `(B, T_max, 4)` features and `(B, U_max)` targets, both consistent with PyTorch batch-first conventions.
* `num_workers=0` default prevents `BrokenPipeError` when dataset classes are defined inside notebook cells.

---

## Task 5 – Model (`LSTMTemporalClassifier`)

### Architecture

| Layer | Parameters |
| --- | --- |
| **BiLSTM** | `hidden_size=256`, `num_layers=2`, `batch_first=True`, `bidirectional=True` |
| **Linear** | `hidden_size` $\times 2 \rightarrow$ `num_classes` ($512 \rightarrow 109$) |
| **LogSoftmax** | `dim=-1` |

**Output shape:** `(B, T, num_classes)` – log-probabilities at every timestep.

### Key Design Decision

`LogSoftmax` is applied inside the model so the output is immediately consumable by `nn.CTCLoss`. The caller must permute to `(T, B, C)` before passing to the loss (handled in `compute_ctc_loss`).

---

## Task 6 – Decoder and Metrics

### Greedy Decoding Steps (`GreedyCTCDecoder`)

1. Argmax over class dim at each timestep.
2. Collapse consecutive repeated IDs.
3. Remove blank (`id = 0`).
4. Map remaining IDs to tokens via `vocab.idx2char`.

### Metrics

* **Edit Distance (`edit_distance`):** Standard Levenshtein DP with a two-row rolling array.
* **Word Error Rate (`word_error_rate`):** 
$$WER = \frac{\sum_i ED(\hat{y}_i, y_i)}{\sum_i |y_i|}$$



---

## Task 7 – CTC Training Utilities

| Function | Role |
| --- | --- |
| `compute_ctc_loss` | Unpack batch → forward → `CTCLoss` (with permute) |
| `decode_batch` | Slice each sample to real length, greedy decode, decode target IDs |
| `train_one_epoch` | `model.train()`, iterate batches, backward, clip, step |
| `evaluate_model` | `model.eval()`, `torch.no_grad()`, decode, compute WER + diagnostics |

> **Diagnosing `val_wer = 1.0**`
> Early in training, the blank class is an easy alignment; the model emits blank for every timestep, producing empty decoded sequences. Empty predictions have edit distance equal to the full target length, giving $WER = 1.0$. Watch `val_empty_pred_rate` and `val_avg_pred_len` to confirm.

---

## Task 8 – WandB Manual Training (`fit_with_early_stopping`)

### What it does

Runs `num_epochs` of manual training with:

* Gradient clipping (`grad_clip_norm`).
* Per-epoch WandB logging (`train_loss`, `val_loss`, `val_wer`, `val_empty_pred_rate`).
* Checkpoint saving whenever `val_loss` improves by $\ge$ `min_delta`.
* Early stopping after `patience` epochs without improvement.

### Config Defaults

```python
config = {
    "lr": 1e-3, "batch_size": 32, "num_epochs": 20,
    "hidden_size": 256, "num_layers": 2,
    "patience": 5, "min_delta": 1e-4, "grad_clip_norm": 5.0,
}

```

**Student ID:** Set `STUDENT_ID = "104240581"` before running.

---

## Task 9 – Test and Inference

After training, the best checkpoint is reloaded and evaluated on the test set.
`evaluate_model` returns `loss`, `wer`, `empty_pred_rate`, `avg_pred_len`, and `avg_target_len`. A single test sample is decoded with both the greedy decoder and the beam decoder; strokes, feature channels, and the emission probability plot are displayed.

---

## Task 10 – WER-based Retraining (`fit_with_early_stopping_wer`)

Same loop as Task 8, but tracks **validation WER** instead of validation loss for checkpointing and early stopping. Supports resuming from a `config["resume_from_checkpoint"]` path so a loss-pretrained model can be fine-tuned specifically for recognition accuracy.

---

## Bonus Tasks

### Bonus Task 1 – Symbol / Relation WER (`split_wer`)

Partitions each token sequence into symbols (everything not in `RELATION_TOKENS`) and relations (`Above`, `Below`, `Inside`, `NoRel`, `Right`, `Sub`, `Sup`). Computes corpus-level WER independently for each partition, returning `{wer, wer_sym, wer_rel}`. All three metrics are logged to WandB.

* **Why it's useful:** Relation WER exposes structural parsing errors separately from symbol recognition errors, enabling more targeted model improvements.

### Bonus Task 2 – Relation-Constraint Loss (`compute_relation_constraint_loss`)

* **Motivation:** Structural-relation tokens should not be predicted during pen-down timesteps, because relations describe connections between symbol groups, not points within a single stroke.
* **Formula:**

$$L_{constraint} = -\log\!\left(1 - \overline{p_{rel} \cdot pen\_down} + \varepsilon\right)$$


$$L_{total} = L_{CTC} + \lambda \cdot L_{constraint}$$


* **Usage:** `compute_ctc_loss_with_constraint` exposes this as a drop-in replacement for `compute_ctc_loss` with an extra `lam` argument (default $0.1$).

### Bonus Task 3 – Beam-Search Decoder (`BeamCTCDecoder`)

A pure-Python / pure-PyTorch implementation of prefix-beam CTC search (Hannun et al., 2014). Maintains `beam_width` incomplete-prefix hypotheses scored by accumulated log-probability, applying CTC merging rules at each step. Shares the same interface as `GreedyCTCDecoder`:

```python
beam_dec = BeamCTCDecoder(vocab, beam_width=10)

tokens   = beam_dec(emission)          # (T, C) → list[str]
batch    = beam_dec(emission_batch)    # (B, T, C) → list[list[str]]

```

### Bonus Task 4 – Enhanced Visual Inspectors

| Function | Description |
| --- | --- |
| `plot_inkml_annotated` | Draws strokes and overlays decoded token labels at the timestep of peak model confidence for each token. |
| `plot_emission_heatmap` | Full probability heatmap (top-k classes $\times$ timesteps) with pen-up transition markers. |