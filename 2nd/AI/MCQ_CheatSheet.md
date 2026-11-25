# Deep Learning & PyTorch — Ultra-Dense MCQ Cheat Sheet

---

## 1. Comparison & Contrast Matrices ("The Professors' Trap")

### Activation Functions

| Concept               | Primary Mechanism                                               | Best Used For                                                                      | The MCQ Trick                                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sigmoid**           | Squashes output to (0,1); S-shaped; σ(x) = 1/(1+e^(-x))         | Binary classification output layer; historical networks                            | **Trap:** "Sigmoid is zero-centered" — FALSE (outputs are always positive, causing zigzag gradient updates). Sigmoid is NOT zero-centered. Also: sigmoid saturates at extremes → vanishing gradients.     |
| **Tanh**              | Squashes output to (-1,1); zero-centered; tanh(x) = 2σ(2x)-1    | Hidden layers (historically); RNN hidden states                                    | **Trap:** Tanh IS zero-centered (unlike sigmoid), but STILL suffers from vanishing gradients at saturation. MCQ may claim tanh solves vanishing gradient — it does not.                                   |
| **ReLU**              | f(x) = max(0, x); piecewise linear                              | Default for hidden layers in CNNs/MLPs                                             | **Trap:** "ReLU is differentiable everywhere" — FALSE. It is non-differentiable at x=0. Also: neurons can "die" (output always 0) if learning rate too high or bad initialization → "Dying ReLU problem." |
| **Leaky ReLU**        | f(x) = x for x>0, αx for x≤0 (e.g. α=0.01)                      | Mitigate dying ReLU; hidden layers                                                 | **Trap:** Leaky ReLU prevents DEAD neurons, not just dying ones. Has non-zero gradient for negative inputs (unlike ReLU).                                                                                 |
| **GELU**              | Gaussian Error Linear Unit; smooth approximation of ReLU        | Transformers (BERT, GPT); modern architectures                                     | **Trap:** GELU is smoother than ReLU and used in Transformers, NOT CNNs typically. Not to be confused with Swish/SiLU.                                                                                    |
| **Linear (identity)** | f(x) = x; no transformation                                     | Regression output layer (predict continuous value); final layer with no activation | **Trap:** If ALL layers use linear activation, the entire network collapses to a single linear transformation — no matter how deep, it can only learn linear functions. Non-linearity is essential.       |
| **Softmax**           | Converts logits to probability distribution; exp(x_i)/Σexp(x_j) | Multi-class classification output (sums to 1)                                      | **Trap:** Softmax is NOT a loss function — it's an activation. CrossEntropyLoss in PyTorch already includes softmax internally (use raw logits, not probabilities).                                       |

### Loss Functions

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **MSELoss (L2 Loss)** | (y_pred - y_true)²; penalizes large errors quadratically | Regression with normally distributed errors | **Trap:** MSE is sensitive to outliers due to squaring. Not suitable when CE loss is needed. Using MSE for classification is a common distractor. |
| **L1Loss (MAE)** | &#124;y_pred - y_true&#124;; mean absolute error | Regression with outliers present (robust) | **Trap:** "MAE = torch.nn.L1Loss" from slides. MAE is MORE robust to outliers than MSE but has constant gradient magnitude — slower convergence near optimum. |
| **BCEWithLogitsLoss** | Binary Cross Entropy with built-in sigmoid | Binary classification (spam/not spam) | **Trap:** BCEWithLogitsLoss = Sigmoid + BCELoss combined (numerically stable). Do NOT apply sigmoid before this loss. If you see sigmoid + BCELoss separate → suggest BCEWithLogitsLoss instead. |
| **CrossEntropyLoss** | LogSoftmax + NLLLoss combined | Multi-class classification (≥3 classes) | **Trap:** CrossEntropyLoss expects **raw logits** (no softmax) as input and **class indices** (not one-hot) as targets in PyTorch. Input shape: [batch, num_classes]; target shape: [batch]. Applying softmax before CE loss will double-softmax and produce wrong gradients. |
| **NLLLoss** | Negative Log-Likelihood | Multi-class (after LogSoftmax layer) | **Trap:** NLLLoss expects log-probabilities (after LogSoftmax), not raw logits. Often combined with LogSoftmax. CrossEntropyLoss = LogSoftmax + NLLLoss. |
| **CTC Loss** | Aligns variable-length input sequences to output labels without explicit alignment | Handwriting recognition, speech recognition | **Trap:** CTC does NOT require one-to-one input/output alignment. Used when input and label sequences have unknown alignment (from RNN lecture). |

### Normalization: Batch Norm vs. Dropout vs. Layer Norm

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **Batch Normalization** | Normalizes activations across the batch dimension (μ, σ per channel) | CNNs; accelerates training; allows higher learning rates | **Trap:** BatchNorm behaves DIFFERENTLY in train vs eval mode. In training: uses batch statistics. In eval: uses running averages. MCQ may say "BatchNorm uses batch statistics during inference" — FALSE. |
| **Dropout** | Randomly zeroes a fraction p of neurons during training | Fully-connected layers; prevents co-adaptation | **Trap:** Dropout is ONLY active during training. During eval/inference, dropout is OFF (all neurons active, outputs scaled by 1-p or equivalently weights are not dropped). MCQ: "Dropout regularizes by randomly removing neurons during testing" — FALSE. Dropout > 0.5 is rarely used. |
| **Layer Normalization** | Normalizes across features (per sample) | Transformers; RNNs; NLP | **Trap:** LayerNorm normalizes across feature dimension (not batch). Doesn't depend on batch size — good for NLP where batch sizes vary. |

### CNN Pooling Types

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **Max Pooling** | Takes maximum value in each window | Downsampling; translation invariance; dominant in CNNs | **Trap:** During backprop, gradient flows ONLY through the max-activated neuron (active path). Other neurons get zero gradient. This is "gradient routing." |
| **Average Pooling** | Takes mean value in each window | Smooth downsampling; often at the end before classifier | **Trap:** During backprop, gradient is distributed EVENLY to ALL nodes in the pooling window. Also has NO learnable parameters — just like max pooling. |

### Weight Update Strategies (Gradient Descent Variants)

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **Batch GD** | Update weights after processing ALL samples | Small datasets; convex optimization | **Trap:** Computationally expensive per update; memory intensive. Smooth convergence but slow. |
| **Stochastic GD (SGD)** | Update weights after EACH sample | Online learning; very large datasets | **Trap:** Very noisy updates (high variance); but better generalization due to noise. "SGD" is often used in PyTorch to mean mini-batch SGD with momentum. |
| **Mini-batch GD** | Update weights after each batch of n samples (e.g., 32) | Standard approach; balances noise & speed | **Trap:** Default approach. batch_size is a hyperparameter. Smaller batch → noisier gradients but better generalization. Larger batch → more stable but may generalize worse. |
| **SGD with Momentum** | Accumulates past gradients (velocity); reduces oscillation | Faster convergence; escape local minima | **Trap:** Momentum helps navigate ravines and reduces zigzagging. It does NOT guarantee global minimum. |

### RNN vs LSTM vs Bidirectional

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **RNN** | Hidden state from previous timestep fed to current; BPTT for learning | Short sequences; when computational efficiency is key | **Trap:** RNN suffers from vanishing gradient — impact of input at time t decays as &#124;w&#124;^n across n timesteps. If &#124;w&#124; > 1 → exploding; if &#124;w&#124; < 1 → vanishing. RNN cannot learn long-term dependencies well. |
| **LSTM** | 3 gates (input, output, forget) controlling data flow through cell state; enables constant gradient flow | Long sequences; when long-term dependencies matter | **Trap:** LSTM "completely overcomes" vanishing gradient via additive cell state (gradient can flow unchanged: ×1.0). Gates use sigmoid for (0,1) control signals. MCQ: "LSTM has 2 gates" — FALSE (3 gates: forget, input, output). |
| **Bidirectional RNN/LSTM** | Two RNNs: one forward (t=1→T), one backward (t=T→1); outputs concatenated | When both past AND future context matter (e.g., phoneme recognition) | **Trap:** Bidirectional requires the ENTIRE sequence to be available (cannot be used for real-time prediction). Not suitable for autoregressive generation. |

### Dataset Splits

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **Training Set** | Data used to update model weights via gradient descent | Learning patterns | **Trap:** Model directly fits to this data. Overfitting means performing well here but poorly elsewhere. |
| **Validation Set** | Data used for hyperparameter tuning and early stopping | Preventing overfitting; model selection | **Trap:** The model sees this data during training (for evaluation, not weight updates). MCQ may say "validation set is never seen during training" — FALSE (it's seen for evaluation purposes). |
| **Test Set** | Data held out until final evaluation only | Final unbiased performance estimate | **Trap:** Test set should be used ONLY ONCE at the very end. If you tune hyperparameters based on test set performance, you've contaminated your evaluation. |

### ML vs DL (Key Distinctions)

| Concept | Primary Mechanism | Best Used For | The MCQ Trick |
|---|---|---|---|
| **Traditional ML** | Shallow algorithms: Random Forest, Gradient Boosted, SVM, Naive Bayes, Nearest Neighbour | Structured/tabular data; when interpretability needed | **Trap:** Still superior for many tabular data problems. "Deep learning always outperforms traditional ML" — FALSE. |
| **Deep Learning** | Neural networks: FCNN, CNN, RNN, Transformer | Unstructured data: images, text, audio | **Trap:** DL requires large amounts of data typically. Rule #1: "If you can build a simple rule-based system that doesn't require ML, do that." |
| **Classic Programming** | Rules + Data → Answers (human writes rules) | Deterministic problems | **Trap:** In ML/DL paradigm: Data + Answers → Rules (model learns rules). Slide: "Starts with Inputs + Outputs, Figures out Rules." |

---

## 2. PyTorch Workflow & Syntax Gotchas

### The Training Loop — EXACT Order (Critical)
```
For each epoch:
  For each batch:
    1. optimizer.zero_grad()       # MUST be first! Reset gradients
    2. y_pred = model(X)           # Forward pass
    3. loss = loss_fn(y_pred, y)   # Compute loss (must be SCALAR for .backward())
    4. loss.backward()             # Backprop: compute gradients
    5. optimizer.step()            # Update weights using gradients
```
**Trap:** If `zero_grad()` is omitted, gradients **accumulate** across batches → incorrect updates. If `.backward()` is called before computing loss, it will fail. If `.step()` is called before `.backward()`, no gradients exist to apply.

### model.eval() vs torch.no_grad() vs torch.inference_mode()

| Mode | What it does | When to use |
|---|---|---|
| **model.train()** | Enables dropout, BatchNorm uses batch stats, gradients tracked | Training (default) |
| **model.eval()** | Disables dropout, BatchNorm uses running averages, BUT gradients still tracked | Validation/testing — MUST call this |
| **torch.no_grad()** | Disables gradient computation (saves memory); does NOT change model mode | Inference, evaluation — blocks autograd |
| **torch.inference_mode()** | Like no_grad but faster (more aggressive optimization); does NOT change model mode | Testing loop (shown in slides as preferred) |

**Trap:** `model.eval()` does NOT disable gradient tracking! You still need `torch.inference_mode()` or `torch.no_grad()` to stop grad tracking. Also: `torch.inference_mode()` is faster than `torch.no_grad()` and recommended in slides for testing.

### nn.Module Requirements
- **Must** subclass `nn.Module`
- **Must** override `forward()` method
- `super().__init__()` must be called in `__init__()`
- Parameters with `requires_grad=True` are tracked by autograd (default for `nn.Parameter` and `nn.Module` layers)
- **Trap:** Calling `model.forward(x)` directly works but bypasses hooks. Use `model(x)` (calls `__call__` which handles hooks and then `forward`).

### Conv2d Parameter Count Formula
```
Number of parameters = in_channels × out_channels × kernel_size² (+ out_channels for bias)
```
For `nn.Conv2d(in_channels=3, out_channels=10, kernel_size=5, bias=True)`:
= 3 × 10 × 5 × 5 + 10 = 750 + 10 = 760

**Trap:** MCQ may forget the bias term or confuse in_channels and out_channels order. Also: Pooling layers have **zero** learnable parameters.

### Input/Output Tensor Shapes

| Component | Shape Convention | Notes |
|---|---|---|
| **Image (NCHW)** | `[batch, channels, height, width]` | PyTorch default (Channels First) |
| **Image (NHWC)** | `[batch, height, width, channels]` | TensorFlow default (Channels Last) |
| **Conv2d Input** | `[N, C_in, H, W]` | 1 for grayscale, 3 for RGB |
| **Conv2d Output** | `[N, C_out, H_out, W_out]` | H_out, W_out depend on stride/padding |
| **Linear Input** | `[N, in_features]` | Must flatten before Linear layer |
| **Classification Output** | `[N, num_classes]` | Raw logits (before softmax) |
| **CrossEntropyLoss target** | `[N]` | Class indices (long), NOT one-hot |

### Conv2d Output Size Formula
```
H_out = floor((H_in + 2×padding - dilation×(kernel_size-1) - 1) / stride + 1)
```
Simplified (dilation=1):
```
H_out = floor((H_in + 2P - K) / S + 1)
```
- `padding='same'`: output size = input size (when stride=1)
- `padding='valid'` or `padding=0`: output size decreases
- **Trap:** Stride=2 with padding=0 roughly halves spatial dimensions (common for downsampling).

### DataLoader Essentials
- `shuffle=True`: Critical for training (prevents model from learning batch order). Should be `False` for validation/test.
- `batch_size`: Number of samples per batch. Common value: 32.
- `collate_fn`: Optional function to customize how samples are combined into a batch.
- Dataset class must implement `__getitem__(index)` and `__len__()`.

### GPU/MPS Operations
- `tensor.to(device)` or `model.to(device)` moves to GPU
- Both model AND data must be on same device
- **Trap:** Loss function doesn't automatically move — but loss input tensors must be on same device as model output.

### Autograd & Gradient Gotchas
- `loss.backward()` expects loss to be a **scalar** (0-dimensional tensor)
- For non-scalar loss: compute `.mean()` before `.backward()` or pass gradients argument
- Gradient accumulation is by design (not a bug) — must zero between batches
- `retain_graph=True` keeps computation graph after backward (needed if computing multiple losses from same graph)

### PyTorch Building Blocks (from slides table)

| Module | Purpose |
|---|---|
| `torch.nn` | All building blocks for computational graphs |
| `torch.nn.Module` | Base class for ALL neural networks |
| `torch.nn.Parameter` | Wrapper for tensors that should be learned |
| `torch.optim` | Optimization algorithms (SGD, Adam, etc.) |
| `torch.utils.data.Dataset` | Map between key(label) and sample(features) pairs |
| `torch.utils.data.DataLoader` | Python iterable over a Dataset |
| `torchvision.transforms` | Image preprocessing/augmentation pipeline |
| `torchvision.datasets` | Pre-built datasets (FashionMNIST, etc.) |
| `torchvision.models` | Pre-trained model architectures |

---

## 3. Hyperparameter Scenarios ("If X, then Y")

### Learning Rate
| If... | Then... |
|---|---|
| Learning rate **too high** | Loss **explodes** or oscillates wildly; may diverge; NaN values appear |
| Learning rate **too low** | Training converges very slowly; may get stuck; requires more epochs |
| Learning rate starts high, decays over time | Faster initial progress + stable convergence (learning rate scheduling) |
| Learning rate is **exactly right** | Loss decreases smoothly and converges to minimum |

### Batch Size
| If... | Then... |
|---|---|
| Batch size **too small** (e.g., 1-4) | **Noisy gradient estimates** but better generalization; training unstable; slow GPU utilization |
| Batch size **too large** (e.g., full dataset) | Stable but poor generalization; might converge to sharp minima; memory-intensive |
| Batch size = **32** | Common sweet spot; balances noise and efficiency |
| `shuffle=True` not set | Model learns order-dependent patterns; poor generalization |

### Dropout Rate
| If... | Then... |
|---|---|
| Dropout = **0.0** | No dropout; potential overfitting on small datasets |
| Dropout = **0.5** | Standard starting point for fully-connected layers (50% neurons dropped) |
| Dropout > **0.7** - **0.9** | **Extreme underfitting**; too few active neurons; model cannot learn |
| Dropout applied to convolutional layers | Less common; usually applied to FC layers only |

### Epochs
| If... | Then... |
|---|---|
| Epochs **too few** | **Underfitting**; model hasn't learned sufficient patterns |
| Epochs **too many** | **Overfitting**; training loss decreases but validation loss increases |
| **Early stopping** implemented | Training stops when validation loss stops improving; prevents overfitting |

### Model Complexity
| If... | Then... |
|---|---|
| **Too few layers/units** | **Underfitting**; model lacks capacity to capture patterns |
| **Too many layers/units** | **Overfitting**; model memorizes training data |
| Adding more **hidden layers** (depth) | Learns more complex, hierarchical features |
| Adding more **hidden units** (width) | Increases model capacity per layer |

### Activation Function Choice
| If... | Then... |
|---|---|
| **Linear** activation in hidden layers | Network is equivalent to a single linear layer; **cannot learn non-linear functions** (Universal Approximation Theorem requires non-linearity) |
| **ReLU** in hidden layers | Standard choice; efficient; but watch for dying neurons |
| **Sigmoid** in output (binary) + BCE | Standard for binary classification (but use BCEWithLogitsLoss instead) |
| **Softmax** in output (multi-class) | Use with CrossEntropyLoss (PyTorch CE already includes softmax) |
| **No activation** in output (regression) | Used with MSE or MAE loss for continuous value prediction |

### Data Augmentation
| If... | Then... |
|---|---|
| Training data is **limited** | Apply augmentation (rotation, flip, zoom, shift) to increase diversity |
| Augmentation is too aggressive | Model cannot recognize original patterns; underfitting |
| No augmentation on small dataset | High risk of overfitting |
| Augmentation goal | Learn **invariant features** (slide: "Objectives: learning invariant features") |

---

## 4. Tensor Dimension & Layer Math

### Tensor Dimension Hierarchy
- **Scalar**: 0 dimensions, shape `[]`, ndim=0
- **Vector**: 1 dimension, shape `[n]`, ndim=1
- **Matrix**: 2 dimensions, shape `[m, n]`, ndim=2
- **Tensor**: n dimensions, shape `[d1, d2, ..., dn]`, ndim=n

### Axis Convention (NumPy/PyTorch)
```
Shape: (2, 4, 3)
       │  │  │
       │  │  └─ axis=2 (last dim, axis=-1)
       │  └──── axis=1
       └─────── axis=0 (first dim)
```

### MatMul (Dot Product) Rule
```
Matrix A: [m × n] · Matrix B: [n × p] → Result: [m × p]
                  └─ inner dims must match ─┘     └─ outer dims ─┘
```
- **Trap:** A `[3, 3]` @ B `[3, 2]` → `[3, 2]`. A `[3, 3]` @ B `[5, 3]` → **ERROR** (inner dims don't match: 3 ≠ 5).

### Broadcasting Rules
Arrays are compatible if:
1. Dimensions are equal, or
2. One dimension is 1 (broadcasted to match)

Example: shape `(3, 4)` + scalar `5` → broadcasting `5` to `(3, 4)`

**Trap:** `shape (3, 4) + shape (4,)` works (the 4-dimension broadcasts). `shape (3, 4) + shape (3,)` does NOT work without adding a new axis: reshape `(3,)` to `(3, 1)`.

### Reshape vs. Transpose vs. View
- **reshape**: Changes shape without changing data (can return a copy if needed)
- **view**: Like reshape but requires contiguous memory
- **transpose/permute**: Reorders axes (swaps dimensions)
- **flatten**: Converts to 1D
- Reshape with `-1`: auto-computes that dimension
- NHWC → NCHW: permute dims from `[0, 3, 1, 2]`

### Representing Data as Tensors
| Data Type | Tensor Shape |
|---|---|
| Grayscale Image (single) | `[H, W]` or `[1, H, W]` |
| RGB Image (single) | `[3, H, W]` (NCHW) or `[H, W, 3]` (NHWC) |
| Batch of RGB images | `[B, 3, H, W]` (PyTorch default) |
| Audio (single) | `[Time]` or `[Time, Channels]` |
| Batch of audio | `[B, Time, Channels]` |
| Text tokens (batch) | `[B, SeqLen]` |
| 1D time series (batch) | `[B, Time]` |
| Tabular data (batch) | `[B, Features]` |

---

## 5. "Which of the Following is FALSE?" — High-Yield Targets

1. **FALSE: "Pooling layers have learnable parameters."**
   Pooling layers (both MaxPool and AvgPool) have **zero** learnable weights. They are fixed operations. During backprop: max-pool routes gradient only to the max-activated path; average-pool distributes gradient evenly.

2. **FALSE: "model.eval() disables gradient computation."**
   `model.eval()` only changes behavior of layers (dropout off, batch norm uses running stats). Gradient tracking is controlled by `torch.no_grad()` or `torch.inference_mode()`. Both are needed for proper evaluation.

3. **FALSE: "Sigmoid is a zero-centered activation function."**
   Sigmoid outputs are always positive (range: 0 to 1), making it NOT zero-centered. Tanh IS zero-centered (range: -1 to 1). This causes zigzag gradient dynamics in sigmoid.

4. **FALSE: "CrossEntropyLoss expects one-hot encoded targets."**
   PyTorch's `CrossEntropyLoss` expects **class indices** (integer labels, shape `[N]`), NOT one-hot vectors. Input should be raw logits (no softmax), shape `[N, num_classes]`.

5. **FALSE: "A deep neural network with only linear activations can learn arbitrary non-linear functions."**
   Multiple linear layers in sequence mathematically collapse to a single linear transformation. Non-linear activation functions are **required** for the Universal Approximation Theorem to apply. The theorem states MLP with non-linear activation can approximate any function.

6. **FALSE: "LSTM has two gates: input and forget."**
   LSTM has **three** gates: **forget gate**, **input gate**, and **output gate**. Gates use sigmoid activation (outputs 0-1) to control data flow: DataOut = DataIn × ControlSignal.

7. **FALSE: "Weight sharing in CNNs means each neuron has unique weights for each spatial position."**
   Weight sharing means the **same filter** (kernel weights) is applied across all spatial positions (sliding window). This drastically reduces parameter count compared to fully-connected layers.

8. **FALSE: "In max-pooling backpropagation, the gradient is distributed equally to all neurons in the pooling window."**
   In max-pooling, gradient flows **only through the activated (max-valued) neuron**. In average-pooling, gradient IS distributed equally to all neurons. These are opposites.

9. **FALSE: "Batch Normalization uses the same mean and variance during training and evaluation."**
   During **training**: BatchNorm uses batch statistics (mean, variance of the current mini-batch). During **evaluation**: it uses **running averages** accumulated during training. `model.eval()` switches this behavior.

10. **FALSE: "Dropout is applied during both training and inference."**
    Dropout is ONLY active during training. During inference (`model.eval()`), all neurons are used and no dropping occurs. The weights are effectively scaled to account for this.

11. **FALSE: "The test set should be used to select the best model checkpoint during training."**
    The **validation set** is used for model selection and early stopping. The test set is reserved for the **final evaluation only**. Using the test set for decisions contaminates your unbiased performance estimate (stated in slides: "Final exam (test set) — See if the model is ready for the wild").

12. **FALSE: "A larger batch size always leads to better model performance."**
    Larger batches give more stable gradients but often **worse generalization**. Smaller batches introduce noise that acts as implicit regularization, helping the model escape sharp minima and find flatter minima that generalize better.

13. **FALSE: "F1-score is the harmonic mean of accuracy and precision."**
    F1-score = 2 × (precision × recall) / (precision + recall). It's the harmonic mean of **precision and recall**, NOT accuracy. For imbalanced datasets, F1 is better than accuracy.

14. **FALSE: "Stride in Conv2d is always equal to 1."**
    Stride defaults to 1 but can be set to 2 or higher for downsampling. Stride=2 halves spatial dimensions approximately. The slide shows stride default as 1 in PyTorch.

15. **FALSE: "RNN can effectively learn dependencies across hundreds of timesteps."**
    Due to the **vanishing gradient** problem (signal decays as &#124;w&#124;^n), vanilla RNNs struggle with long sequences. If &#124;w&#124; < 1, the gradient vanishes exponentially. LSTM was specifically designed to overcome this via the constant error carousel (cell state with identity connections).

16. **FALSE: "backward() can only be called once per computation graph."**
    By default, the computation graph is freed after `backward()` to save memory. But with `loss.backward(retain_graph=True)`, the graph is preserved and `backward()` can be called multiple times.

17. **FALSE: "The number of parameters in a Conv2d layer is: in_channels × kernel_size × kernel_size."**
    The correct formula is: `in_channels × out_channels × kernel_size² + out_channels` (bias). The out_channels factor is commonly forgotten.

18. **FALSE: "NumPy arrays can contain elements of different data types."**
    NumPy arrays are **homogeneous**: all elements must be the same dtype. Python lists CAN store mixed types. NumPy arrays are "more efficient" but "more dynamic" (referring to list flexibility in slides).

19. **FALSE: "In image-to-sequence models, the decoder uses only the CNN output for generation."**
    The CNN output (feature vector) is used to **initialize** the decoder RNN's initial state. The decoder then generates the output sequence token by token.

20. **FALSE: "Stochastic gradient descent updates weights after processing a mini-batch of samples."**
    Stochastic GD updates after **each individual sample**. **Mini-batch** GD updates after each mini-batch. **Batch** GD updates after all samples. These are distinct concepts (from SGD lecture slide: "Stochastic → each sample → update weight; Minibatch → each minibatch (n-samples) → update weight; Gradient Descent → Batch → all samples").

---

## Quick-Reference: Key Terms & Acronyms

| Term | Definition |
|---|---|
| **BPTT** | Backpropagation Through Time — gradient is sum of gradients across all timesteps |
| **Generalization** | Model's ability to perform well on unseen data |
| **Overfitting** | Model performs well on training data but poorly on test data |
| **Underfitting** | Model fails to capture patterns even in training data |
| **One-hot encoding** | Target as vector with 1 at class index, 0 elsewhere (e.g., digit "0" → [1,0,0,0,0,0,0,0,0,0]) |
| **Weight sharing** | Same weights (kernel) applied across all spatial positions in CNN |
| **Invariant features** | Features that remain stable under transformations (rotation, translation) — learned via data augmentation |
| **Epoch** | One complete pass through all training samples |
| **Logits** | Raw output of the last linear layer (before softmax/sigmoid) |
| **requires_grad** | PyTorch flag that tracks gradient for a parameter (default True for nn.Parameter) |
| **Autograd** | PyTorch's automatic differentiation engine |
| **Computation Graph** | Directed acyclic graph representing the forward computation of a model |
| **Gradient Vector** | Points in direction of steepest **ascent** (slides: "Outward of the minimum point") |
| **Collate function** | Custom function to combine individual samples into a batch in DataLoader |
| **Seen whole dataset** | Model has seen VALIDATION data (for tuning) but should NOT have seen TEST data before final evaluation |
