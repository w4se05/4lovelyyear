---
title: The Cheatcheatsheet — Modules 3 to 7, Explained for Absolute Beginners
subtitle: Plain English first, then the real math, for every concept
---

# 🧠 The Cheatcheatsheet

> **How to use this:** Every concept below has two parts:
> - 🟢 **Plain English** — the "explain it like I've never touched a computer" version.
> - 🔵 **The Real Math** — the actual formula/mechanism, so you can also answer technical exam questions.
>
> Read 🟢 first every time. Only move to 🔵 once the plain version clicks.

---

## MODULE 3 — How a Neural Network Thinks and Learns

### 3.1 What even is a "neuron"?

🟢 **Plain English**
Imagine one tiny decision-maker. It's handed a few numbers (inputs). It decides how much it cares about each one (that's called a **weight** — a bigger weight = "I care about this input a lot"). It adds them all up, adds a small personal bias/nudge, and then passes that total through a filter to decide its final output. Stack thousands of these little decision-makers into layers, and you get a **neural network**:

```
Input Layer → Hidden Layer(s) → Output Layer
```

Data goes in one side, gets transformed step by step, and a prediction comes out the other side.

🔵 **The Real Math**
$$z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b = \mathbf{w}^T\mathbf{x} + b$$
$$\hat{y} = \text{activation}(z)$$

- $w_i$ = weight for input $x_i$ (learned).
- $b$ = bias (learned) — shifts the threshold at which the neuron "fires."
- In PyTorch, `nn.Linear(in_features=4, out_features=8)` means 8 separate neurons, each with its own 4-number weight vector. Weight matrix shape: `(8,4)`. Bias shape: `(8,)`.

---

### 3.2 Why can't the network just be "simple math" (no filter)?

🟢 **Plain English**
If every decision-maker only ever did plain addition and multiplication, then no matter how many layers you stack, the *whole* network still only knows how to draw a straight line. It could never learn a curvy, complicated pattern (like "is this a cat or not"). The filter (called an **activation function** — Sigmoid, ReLU, Tanh, etc.) is what lets the network bend and learn actual complicated shapes.

> ⚠️ **Common exam trap:** "A deep network with only linear (straight-line) activations can still learn complicated, curvy functions." — **FALSE.** No matter how deep, it mathematically collapses into ONE simple straight-line transform.

🔵 **The Real Math**
$$f(x) = W_3(W_2(W_1x)) = (W_3W_2W_1)x = W_{eq}x$$

Matrix multiplication is associative — multiplying three matrices together in a row is the same as multiplying them into one single combined matrix $W_{eq}$. So stacking linear (non-activated) layers is mathematically pointless; you always get back one linear map, regardless of depth.

**Universal Approximation Theorem:** a network with non-linear activations and enough hidden neurons can approximate *any* continuous function. Non-linearity is the essential ingredient — depth alone does nothing without it.

---

### 3.3 How does it actually "learn"? (Backpropagation)

🟢 **Plain English**
The network makes a guess. You compare the guess to the correct answer and get a number representing "how wrong was I" (called the **loss**). Then, working backward through the network, you ask: "Which weights caused the most damage, and in which direction should I nudge them to be less wrong?" This backward blame-assignment process is called **backpropagation**. Once you know which direction makes things worse, you simply step in the *opposite* direction. That's called **gradient descent** — like walking downhill on a mountain of "wrongness" toward the valley where wrongness is lowest.

🔵 **The Real Math**
The gradient (vector of partial derivatives) points in the direction of steepest **ascent** (more wrongness):
$$\nabla_\theta L = \left[\frac{\partial L}{\partial w_1}, \frac{\partial L}{\partial w_2}, \dots, \frac{\partial L}{\partial b}\right]$$

For $\hat{y} = f(z)$, where $z = wx + b$, the **chain rule** gives:
$$\frac{\partial L}{\partial w} = \underbrace{\frac{\partial L}{\partial \hat{y}}}_{\text{how wrong the loss was}} \cdot \underbrace{\frac{\partial \hat{y}}{\partial z}}_{\text{activation's local slope}} \cdot \underbrace{\frac{\partial z}{\partial w}}_{=\,x}$$

Since we want to go **downhill** (less wrong), we subtract:
$$w_{\text{new}} = w_{\text{old}} - \eta \cdot \frac{\partial L}{\partial w}$$

$\eta$ (eta) = **learning rate** = how big a step to take each time.

In code, this exact recipe is: `optimizer.zero_grad()` (erase old corrections) → `loss.backward()` (compute new corrections) → `optimizer.step()` (apply the corrections).

> ⚠️ **Trap:** Forgetting `zero_grad()` means old corrections **pile up (accumulate)** on top of new ones across batches — this is intentional PyTorch behavior, not a bug, but forgetting to reset it breaks training.

---

### 3.4 Loss functions — how "wrongness" is measured

🟢 **Plain English**
Different jobs need different ways of scoring "how wrong." Predicting a house price is scored differently than predicting "cat vs. dog." Below is the cheat table:

| Loss | Used for | Plain description |
|---|---|---|
| **MSE (L2)** | Predicting a number (e.g. price) | Squares the error — big mistakes get punished *extra* hard |
| **MAE (L1)** | Predicting a number, but with weird outlier data | Just takes the plain difference — more forgiving of huge mistakes, but improves more slowly |
| **BCEWithLogitsLoss** | Yes/No questions (spam or not) | Built-in Sigmoid + error scoring combined into one safe operation |
| **CrossEntropyLoss** | Choosing among 3+ categories | Combines "turn scores into probabilities" + "score the error" into one step |
| **CTC Loss** | Matching a long recording/drawing to a short answer | Explained fully in Module 7 |

🔵 **The Real Math**

| Loss | Formula | Trap to remember |
|---|---|---|
| MSE | $\frac{1}{N}\sum (y_{pred}-y_{true})^2$ | Sensitive to outliers (squaring amplifies big errors) |
| MAE | $\frac{1}{N}\sum \lvert y_{pred}-y_{true}\rvert$ | Constant-size gradient → slower fine-tuning near the answer |
| BCEWithLogitsLoss | Sigmoid + BCE, fused | Never apply sigmoid yourself first — "double-sigmoid" bug |
| CrossEntropyLoss | LogSoftmax + NLLLoss, fused: $-\log\left(\frac{e^{z_y}}{\sum_j e^{z_j}}\right)$ | Wants **raw logits** `[N,classes]` + **integer** class labels `[N]` — NOT one-hot vectors |
| NLLLoss | Negative log-likelihood | Expects **already-log-probability** inputs (i.e., after LogSoftmax) |

---

### 3.5 Keeping the network from "cheating" (Normalization & Regularization)

🟢 **Plain English**
Sometimes a network gets *too good* at memorizing the training examples specifically, instead of learning the general pattern — like a student who memorizes exact practice-exam answers instead of understanding the topic. This is called **overfitting**. Two popular fixes:

- **Dropout**: during practice (training) only, randomly "turn off" some neurons each round — like practicing a sport with a randomly tied hand, so no single neuron becomes a crutch. During the actual test (evaluation), every neuron works normally again.
- **BatchNorm**: keeps the numbers flowing through the network in a stable, consistent range, so training doesn't become wild and unstable.

🔵 **The Real Math**

- **BatchNorm** (training): $\hat{x} = \dfrac{x-\mu_{batch}}{\sqrt{\sigma^2_{batch}+\epsilon}}$, then rescaled by learnable $\gamma,\beta$. At **evaluation** time, it switches to a **running average** of $\mu,\sigma$ collected during training (not the current batch, which might even be size 1).
- **Dropout**: zeroes each neuron independently with probability $p$, **training only**; fully off at evaluation.
- **LayerNorm**: normalizes across the *feature* dimension per single sample — behaves identically in train and eval, and doesn't depend on batch size (useful for NLP/Transformers).

> ⚠️ **Traps:** "BatchNorm uses batch statistics during inference" — FALSE (uses running average). "Dropout is active during training AND inference" — FALSE (training only).

---

## MODULE 4 — The Training Recipe (PyTorch Workflow)

### 4.1 The exact steps, in the exact order

🟢 **Plain English**
Training a model is like following a strict 5-step recipe, over and over, for every small group ("batch") of examples:

1. **Wipe the whiteboard** — clear any leftover correction notes from last time.
2. **Make a guess** — run the data forward through the network.
3. **Check how wrong** — compare the guess to the true answer.
4. **Trace the blame backward** — figure out which weights caused the error.
5. **Fix the weights slightly** — nudge everything a little bit better.

You repeat this recipe for every batch, and doing it once for *all* batches in the whole dataset is called one **epoch**.

🔵 **The Real Math / Code**

```python
optimizer.zero_grad()          # 1. reset gradients — otherwise they ACCUMULATE
y_pred = model(X)              # 2. forward pass
loss = loss_fn(y_pred, y)      # 3. must produce a SCALAR (single number)
loss.backward()                # 4. backprop — fills in .grad for every parameter
optimizer.step()                # 5. w -= lr * w.grad, for every parameter
```

> ⚠️ **Traps:** Calling `.step()` before `.backward()` → no gradients exist yet to apply. Calling `.backward()` before computing the loss → fails outright. `.backward()` requires a **scalar** loss — if your loss is a vector, call `.mean()` first, or supply an explicit `gradient=` argument.

**Vocabulary:**

| Term | Meaning |
|---|---|
| Sample | one single data point |
| Batch | a small group of samples processed together (e.g., 32) |
| Epoch | one full pass through **all** training data |
| Iteration / Step | one weight update = processing one batch |

---

### 4.2 "Practice mode" vs. "Test mode" — the biggest trap in this whole module

🟢 **Plain English**
During practice (training), the network uses some randomness tricks (like Dropout) to avoid memorizing. During the real test (evaluation), you want its honest, consistent best answer, so those tricks get turned off. But — and this is the trap — turning off "training mode" does **not** automatically stop the network from calculating how it *would* improve. You separately have to tell it "don't bother computing corrections right now, we're just testing" — because that calculation is pure wasted effort during testing.

🔵 **The Real Math**

| Mode | Changes Dropout/BatchNorm behavior? | Still tracks gradients? |
|---|---|---|
| `model.train()` | ✅ Yes | ✅ Yes |
| `model.eval()` | ✅ Yes | ✅ **Yes — still tracks!** (the trap) |
| `torch.no_grad()` | ❌ No | ❌ No — turns tracking off |
| `torch.inference_mode()` | ❌ No | ❌ No (stricter/faster version) |

**Correct testing pattern (need BOTH):**
```python
model.eval()
with torch.no_grad():
    output = model(x)
```

> ⚠️ **Trap:** "`model.eval()` disables gradient computation" — FALSE. It only changes layer *behavior*; you still need `no_grad()`/`inference_mode()` on top.

---

### 4.3 Different "flavors" of gradient descent

🟢 **Plain English**
All flavors do the same "walk downhill" idea — they just differ in **how much data you look at before taking one step**:

| Flavor | Looks at... before updating | Personality |
|---|---|---|
| **Batch GD** | the *entire* dataset | slow, smooth, expensive |
| **Stochastic GD (SGD)** | just *one single* example | fast but jumpy/noisy — the noise can actually help avoid getting stuck |
| **Mini-batch GD** | a small group (e.g., 32 examples) — the real-world default | balanced — this is what people mean 99% of the time, even when the tool is literally named "SGD" |

> ⚠️ **Trap:** "SGD updates weights after a mini-batch" — FALSE. True SGD updates after **each single sample**; mini-batch GD is the separate, distinct category (even though PyTorch's `SGD` optimizer is almost always used in mini-batch mode in practice).

🔵 **The Real Math**
$$\theta_{t+1} = \theta_t - \eta \cdot \nabla_\theta L(\theta_t;\mathcal{B}_t)$$
where $\mathcal{B}_t$ = the entire dataset (Batch GD), one sample (SGD), or a fixed-size subset (mini-batch GD).

---

### 4.4 Dial-turning: what happens if you crank settings up or down

🟢 **Plain English**

| Setting | Too LOW | Too HIGH |
|---|---|---|
| Learning rate | learns painfully slowly, might get stuck | takes overly huge steps → bounces around wildly or blows up entirely (NaN) |
| Batch size | noisy, slower per step, but often generalizes *better* | very stable, but often generalizes *worse* and eats more memory |
| Dropout rate | risk of memorizing (overfitting) | too many neurons switched off → can't learn at all (underfitting) |
| Number of epochs | model hasn't learned enough yet (underfitting) | model starts memorizing training data specifically (overfitting) |

> ⚠️ **Trap:** "A bigger batch size always makes the model perform better" — FALSE. Bigger batches give smoother, more stable gradient steps, but you lose helpful "noise" that pushes the model toward better-generalizing solutions.

🔵 **The Real Math**
`torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)` — if the gradient vector's overall size (L2 norm) exceeds `max_norm`, it gets rescaled down. This is the direct fix for the "learning rate/gradient explodes" problem.

---

## MODULE 5 — Convolutional Neural Networks (For Images)

### 5.1 How a computer "looks" at a picture

🟢 **Plain English**
Imagine trying to find a cat in a photo — instead of staring at the whole image at once, you use a small magnifying glass that slides across the image bit by bit, looking for one specific tiny pattern (an edge, a curve, a whisker-like texture). This sliding magnifying glass is called a **filter/kernel**.

The clever trick: the **exact same magnifying glass** is reused at every single position across the image (this is called **weight sharing**) — you don't need a separate "edge detector" trained specifically for the top-left corner versus the bottom-right corner; the same one works everywhere. This is what makes CNNs so much more efficient than a regular fully-connected network for images.

> ⚠️ **Trap:** "Weight sharing means each spatial position gets its own unique weights" — FALSE, that's the *opposite* of weight sharing.

🔵 **The Real Math**

**Parameter count for one convolution layer:**
$$\text{Params} = C_{in} \times C_{out} \times K^2 \;(+\, C_{out} \text{ if using bias})$$

$C_{in}$ = input channels, $C_{out}$ = output channels/filters, $K$ = kernel size (e.g., 3 for a 3×3 filter). Each output filter has its own full $C_{in}\times K\times K$ set of weights, plus one bias number per output channel.

**Output spatial size after a conv layer:**
$$H_{out} = \left\lfloor \frac{H_{in} + 2P - K}{S} + 1 \right\rfloor$$

$P$ = padding, $S$ = stride. Stride of 2 (with 0 padding) roughly **halves** the image size each time — the standard way to shrink an image as you go deeper.

> ⚠️ **Trap:** "Stride is always 1" — FALSE, it defaults to 1 but is very frequently set to 2+ specifically to shrink the image.

---

### 5.2 Pooling — simplifying the picture

🟢 **Plain English**
After detecting features, you shrink the image down by summarizing small little regions — either by keeping only the *strongest* signal found (**max pooling**) or by *averaging* everything in that region (**average pooling**). This makes the network faster, smaller, and more tolerant of the object being slightly shifted in the photo.

🔵 **The Real Math**

| | Max Pooling | Average Pooling |
|---|---|---|
| Forward | keeps $\max(x_1,...,x_k)$ in the window | keeps $\frac{1}{k}\sum x_i$ |
| Learnable parameters | **zero** | **zero** |
| Backward (gradient flow) | ALL gradient flows to only the one neuron that was the max; everyone else gets 0 | gradient is split **evenly**: $\frac{1}{k}$ to every neuron in the window |

> ⚠️ **Trap:** "In max-pooling, gradient is distributed evenly to all neurons" — FALSE, that's the description of *average* pooling; they are direct opposites.

---

## MODULE 6 — Recurrent Networks (For Sequences: Speech, Handwriting, Text)

### 6.1 Why order matters, and how the network "remembers"

🟢 **Plain English**
Some data has an inherent order — a sentence, a piece of music, a stroke of handwriting. A regular network looks at everything all at once and has no sense of "what came before." A **Recurrent Neural Network (RNN)** instead reads one step at a time, carrying forward a running "memory" of everything it has seen so far — like reading a sentence word by word while keeping the plot so far in your head.

**The big problem:** across a *long* sequence, that memory tends to fade out — like a rumor getting quieter and quieter each time it's whispered down a long line of people. This fading-memory issue is called the **vanishing gradient problem**, and it means plain RNNs are bad at remembering things from far in the past.

🔵 **The Real Math**

$$h_t = f(W_h h_{t-1} + W_x x_t + b)$$

The same weight matrices $W_h, W_x$ are reused at *every* timestep — weight sharing across time.

**Backpropagation Through Time (BPTT):**
$$\frac{\partial L}{\partial W} = \sum_{t=1}^{T}\frac{\partial L_t}{\partial W}$$

You "unroll" the recurrence into $T$ copies and sum up the gradient contribution from every single timestep. Because the same $W$ gets reused, the chain rule ends up multiplying roughly the same factor over and over:

$$\frac{\partial h_T}{\partial h_1} \propto W^{T-1}$$

- If $\lvert w \rvert < 1$ → shrinks exponentially toward zero → **vanishing gradient** (early timesteps get almost no learning signal).
- If $\lvert w \rvert > 1$ → grows exponentially → **exploding gradient** (unstable, NaNs).

> ⚠️ **Trap:** "A vanilla RNN can effectively learn dependencies across hundreds of timesteps" — FALSE. This exact failure is why LSTM was invented.

---

### 6.2 LSTM — giving the network a *real* long-term memory

🟢 **Plain English**
LSTM (Long Short-Term Memory) fixes the fading-memory problem with a smarter internal memory system that has **3 gates** — think of them like three valves controlling: what old information to *forget*, what new information to *let in*, and what to *output* right now. This lets important information survive much longer without fading, because updates to the memory are done by *adding* new information rather than constantly multiplying the old memory down toward zero.

> ⚠️ **Trap:** "LSTM has 2 gates (input and forget)" — FALSE, there are **3**: forget, input, output.
> ⚠️ **Trap:** "LSTM completely and permanently solves vanishing gradients" — treat with caution; it substantially helps, but isn't an absolute guarantee for arbitrarily long sequences.

🔵 **The Real Math**

$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$

- $f_t$ (forget gate), $i_t$ (input gate), later $o_t$ (output gate) — each is $\sigma(\cdot) \in (0,1)$, computed from $[h_{t-1}, x_t]$.
- Because the cell state $C_t$ updates **additively** (a "+", not repeated multiplication), the gradient path $\frac{\partial C_T}{\partial C_1}$ doesn't automatically decay geometrically the way a plain RNN's does — this is called the "constant error carousel."

---

### 6.3 Bidirectional RNN / BiLSTM — reading both directions

🟢 **Plain English**
Instead of only reading left-to-right (only knowing the past), you also run a *second* reader right-to-left (knowing the future), then combine both views at every point — like reading a mystery novel twice, once forward and once backward, and merging what you learned each time. The catch: this only works if you already have the **entire** sequence available up front — you can't do this in real time (e.g., live speech transcription), since you'd need to already know the ending.

🔵 **The Real Math**

$$h_t^{bi} = [\,h_t^{\rightarrow}\, ;\, h_t^{\leftarrow}\,], \qquad \dim(h_t^{bi}) = 2 \times \text{hidden\_size}$$

```python
self.lstm = nn.LSTM(input_size=4, hidden_size=256, num_layers=2,
                     batch_first=True, bidirectional=True)
# output shape: (B, T, 512)   ← 256 × 2, because forward + backward are concatenated
self.linear = nn.Linear(512, num_classes)   # in_features MUST be 512, not 256
```

> ⚠️ **Trap:** BiLSTM needs the entire sequence available up front — unusable for real-time/streaming/autoregressive generation.

---

## MODULE 7 — CTC: Matching a Long Recording to a Short Answer

### 7.1 The core problem

🟢 **Plain English**
Think about handwriting or speech recognition. You end up with **way more raw readings** than actual letters — e.g., 600 pen-position readings for handwriting that only spells out 5-10 symbols. And critically: nobody tells the computer exactly *which* raw reading corresponds to *which* letter. **CTC (Connectionist Temporal Classification)** is the clever trick that solves this without needing anyone to manually match them up.

🔵 **The Real Math**

$$L_{CTC}(x,y) = -\log\sum_{\pi\in\mathcal B^{-1}(y)}\prod_{t=1}^{T}p(\pi_t\mid x)$$

- $\pi$ = one specific path of length $T$ through the label+blank alphabet.
- $\mathcal{B}$ = the "collapsing function" (merge repeats, remove blanks — see below).
- $\mathcal{B}^{-1}(y)$ = the set of **all** paths that collapse down to correct answer $y$.
- Instead of requiring a "correct" alignment to be specified, CTC sums the probability over **every** alignment consistent with the answer, computed efficiently via a forward-backward dynamic-programming algorithm (not brute force).

> ⚠️ **Trap:** "CTC requires one-to-one input/output alignment" — FALSE. CTC exists *specifically* to avoid needing that.

---

### 7.2 The "blank" token and the collapsing rule

🟢 **Plain English**
The network predicts *something* at every single raw timestep — often the same letter over and over, because your pen stays on the "a" stroke for many readings in a row. There's a special **blank** symbol meaning "nothing new is happening right now." To turn that messy, repetitive raw output into the final clean answer, you do exactly two steps, **in this order**:

1. **Squash consecutive repeats** into one.
2. **Remove all the blanks.**

The blank is the trick that lets the computer tell the difference between "one long letter stretched across many frames" versus "the same letter genuinely appearing twice in a row."

🔵 **The Real Math / Worked Examples**

```
Path:   [H, H, ε, E, ε, L, ε, L, O]     (NO blank between the two L's)
Step 1: [H, ε, E, ε, L, ε, O]            (collapse repeats — the two L's merge into one!)
Step 2: [H, E, L, O]
→ Output: "HELO"   ⚠️ NOT "HELLO" — the L's collapsed because nothing separated them

Path:   [H, H, ε, E, ε, L, ε, ε, L, O]   (blank DOES exist between the two L's)
Step 1: [H, ε, E, ε, L, ε, L, O]          (L's stay separate — blank protected them)
Step 2: [H, E, L, L, O]
→ Output: "HELLO" ✅ — correct, because the blank kept the two L's distinct
```

**Blank index rule:** blank must be **index 0** in the vocabulary.

**Required PyTorch shape fix:**
```python
log_probs = model(features)                 # model naturally outputs (B, T, C)
loss = nn.CTCLoss(blank=0)(
    log_probs.permute(1, 0, 2),             # (T, B, C) — REQUIRED, nn.CTCLoss demands time-major
    targets, input_lens, target_lens
)
```

> ⚠️ **Trap:** Forgetting `.permute(1,0,2)` before `CTCLoss` is one of the single most common project bugs.

---

### 7.3 Measuring how good the answer is: Word Error Rate (WER)

🟢 **Plain English**
WER answers: "on average, how many little edits (insert one letter, delete one letter, or swap one letter) would it take to turn the model's guess into the actually-correct answer?" A WER of 1.0 (100% wrong) right at the *start* of training doesn't necessarily mean something is broken — it usually just means the model is currently guessing "nothing" (all-blanks) for everything, which is a completely normal early phase.

🔵 **The Real Math**

$$WER = \frac{\sum_i \text{EditDistance}(\hat y_i, y_i)}{\sum_i \lvert y_i\rvert}$$

Numerator = total edit distance (insertions + deletions + substitutions) across all examples; denominator = total number of correct-answer tokens across all examples. Edit distance itself is computed with a classic dynamic-programming recurrence (Levenshtein distance):

$$dp[i][j] = \begin{cases} dp[i-1][j-1] & \text{if } pred_i = ref_j \\ 1 + \min(dp[i-1][j],\, dp[i][j-1],\, dp[i-1][j-1]) & \text{otherwise}\end{cases}$$

> ⚠️ **Trap:** "WER=1.0 at the start means the code is broken" — FALSE, it's a normal early-training symptom (all-blank predictions), not necessarily a bug.

---

## 📖 Full Glossary (Quick Reference)

| Term | Plain-English meaning |
|---|---|
| **Weight** | how much a neuron "cares" about one particular input |
| **Bias** | a personal nudge/threshold each neuron adds |
| **Activation function** | the filter that lets networks learn curvy, non-straight-line patterns |
| **Loss** | a single number measuring "how wrong" the prediction was |
| **Gradient** | the direction that makes things *more* wrong; we step opposite it |
| **Learning rate** | how big a step to take each update |
| **Backpropagation** | tracing the error backward to know how to adjust every weight |
| **Epoch** | one full pass through all the training data |
| **Batch** | a small group of examples processed together |
| **Overfitting** | memorizing the training examples instead of learning the general pattern |
| **Underfitting** | failing to even learn the training examples well |
| **Dropout** | randomly disabling neurons during training to prevent over-reliance on any one of them |
| **BatchNorm** | keeping numbers flowing through the network in a stable range |
| **Convolution/Kernel/Filter** | a small sliding "magnifying glass" that detects one visual pattern anywhere in an image |
| **Weight sharing** | reusing the exact same filter/weights everywhere (across space in CNNs, across time in RNNs) |
| **Pooling** | shrinking an image down by summarizing small regions (max or average) |
| **RNN** | a network that reads data step-by-step, carrying memory forward |
| **Vanishing gradient** | the "fading memory" problem where long-past information stops influencing learning |
| **LSTM** | an RNN upgrade with a 3-gate memory system that fights the vanishing gradient problem |
| **BiLSTM** | reads a sequence both forward and backward, then combines both views |
| **CTC** | a technique that matches a long raw sequence to a short final answer, without needing manual alignment |
| **Blank token** | CTC's special "nothing happening here" symbol, used to tell repeated letters apart from stretched-out ones |
| **WER** | Word Error Rate — average number of edits needed to fix a prediction into the correct answer |

---

> ✅ **How to actually study this document:**
> 1. Read every 🟢 section first, out loud if it helps, until you could explain it to a friend with zero background.
> 2. Only then look at the 🔵 math — you'll notice it's just a precise way of writing what you already understood.
> 3. Pay extra attention to every ⚠️ Trap box — these are the exact sentences exam questions love to twist into "which of these is FALSE?" questions.