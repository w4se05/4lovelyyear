# Final Exam — Answer Key

| Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|---|--------|
| 1 | B | 11 | B | 21 | A | 31 | B | 41 | B |
| 2 | B | 12 | C | 22 | B | 32 | A | 42 | C |
| 3 | D | 13 | B | 23 | C | 33 | B | 43 | B |
| 4 | B | 14 | B | 24 | C | 34 | B | 44 | B |
| 5 | A | 15 | A | 25 | C | 35 | B | 45 | B |
| 6 | A | 16 | B | 26 | B | 36 | A | 46 | B |
| 7 | B | 17 | B | 27 | B | 37 | B | 47 | B |
| 8 | B | 18 | B | 28 | A | 38 | B | 48 | A |
| 9 | B | 19 | B | 29 | B | 39 | B | 49 | B |
| 10 | A | 20 | C | 30 | B | 40 | B | 50 | B |

---

## Section Breakdown
- **NumPy:** Q1–Q12
- **Pandas:** Q13–Q18
- **ML Fundamentals:** Q19–Q26
- **Neural Networks:** Q27–Q36
- **Training:** Q37–Q44
- **RNN:** Q45–Q50

---

## Detailed Explanations

### Section A — NumPy

**1. Answer: B.** `a.shape` returns `(3, 4, 5)`. Index `[1]` of that tuple is the second dimension, `4`.

**2. Answer: B.** `axis=0` always refers to the outermost (first) dimension — for a 3D array, that's the "depth"/batch dimension. Operating along `axis=0` collapses that dimension.

**3. Answer: D.** `a` has 6 elements. `2×3=6` ✓, `3×2=6` ✓, `6×1=6` ✓, but `2×4=8 ≠ 6`, so it fails.

**4. Answer: B.** Transpose reverses the axes order, so `(4, 3)` becomes `(3, 4)`.

**5. Answer: A.** The `*` operator on NumPy arrays is element-wise multiplication by default: `[1*4, 2*5, 3*6] = [4, 10, 18]`. Dot product would require `np.dot` or `@`.

**6. Answer: A.** Indexing with an array of integers (fancy indexing) picks out elements at those positions: index 0 → 10, index 2 → 30.

**7. Answer: B.** `np.where(condition, x, y)` returns `x` where the condition is True and `y` where False: `[10>20→0, 20>20→0, 30>20→30, 40>20→40]` = `[0, 0, 30, 40]`.

**8. Answer: B.** `axis=1` means "collapse across columns, per row," so you get one index per row — shape `(3,)`.

**9. Answer: B.** `np.sort` returns the values in sorted order; `np.argsort` returns the *indices* that would produce that sorted order.

**10. Answer: A.** `axis=0` concatenation stacks along rows, adding row counts: `2+2=4` rows, columns stay `3` → `(4, 3)`.

**11. Answer: B.** Broadcasting compares shapes starting from the trailing (rightmost) dimension. `(3, 4)` vs `(4,)`: the trailing dimensions are `4` and `4` — they match, so `(4,)` broadcasts across every row of `(3, 4)`. `(3,)` alone would need `np.newaxis` (to become `(3, 1)`) before it could broadcast against the columns of `(3, 4)`.

**12. Answer: C.** `np.newaxis` inserts a new axis of size 1 at the specified position. Placing it after the existing axis (`a[:, np.newaxis]`) turns `(5,)` into `(5, 1)`.

### Section B — Pandas

**13. Answer: B.** `loc` is label-based indexing; `iloc` is purely integer-position-based indexing.

**14. Answer: B.** `loc` slicing is inclusive of the end label (`2:5` includes row labeled `5`), while `iloc` slicing follows Python convention and excludes the endpoint (`2:5` stops before position `5`).

**15. Answer: A.** `axis=0` (the default) stacks DataFrames vertically, appending rows on top of each other.

**16. Answer: B.** `axis=1` aligns on the shared index and places columns side-by-side.

**17. Answer: B.** `df.loc[row_label, column_label]` is the correct syntax for label-based access to a single cell.

**18. Answer: B.** `iloc` uses integer position regardless of the actual index labels, so `df.iloc[0:3]` reliably gives the first three rows.

### Section C — Machine Learning Fundamentals

**19. Answer: B.** Predicting a continuous numeric value (like price) is regression, not a discrete category (classification) or grouping (clustering).

**20. Answer: C.** Grouping data without predefined labels is unsupervised clustering.

**21. Answer: A.** The defining distinction is the presence (supervised) or absence (unsupervised) of labeled outputs during training.

**22. Answer: B.** Spam vs. not-spam is a two-category (binary) classification problem, and it uses labeled data (spam/not spam), so it's supervised.

**23. Answer: C.** Discovering natural groupings with no predefined categories is a clustering task; K-means is a classic clustering algorithm.

**24. Answer: C.** Predicting a numeric score is regression.

**25. Answer: C.** Clustering's defining trait is grouping similar points together without needing labeled data.

**26. Answer: B.** Having historical labeled outcomes to predict for new inputs is the hallmark of supervised learning.

### Section D — Neural Networks

**27. Answer: B.** A layer applies a linear transformation (weights + bias) followed typically by a non-linear activation function, converting inputs to a new representation.

**28. Answer: A.** Weights scale the importance/contribution of each input; bias allows shifting the output independent of the inputs (like an intercept term).

**29. Answer: B.** Without non-linear activation functions, no matter how many layers are stacked, the network could only represent linear functions — activations enable modeling complex patterns.

**30. Answer: B.** Stacking only linear transformations is mathematically equivalent to a single linear transformation — depth adds no extra expressive power without non-linearity.

**31. Answer: B.** The gradient vector points in the direction of steepest ascent of the loss with respect to all parameters; we move opposite to it to reduce loss.

**32. Answer: A.** The partial derivative `∂L/∂w_ij` measures the sensitivity of the loss to a small change in that specific weight.

**33. Answer: B.** Gradient descent moves weights *opposite* to the gradient (since the gradient points toward increasing loss), scaled by the learning rate: `w = w - lr * gradient`.

**34. Answer: B.** Too large a learning rate causes overshooting past minima, leading to oscillation or divergence rather than smooth convergence.

**35. Answer: B.** In a forward pass, each layer's output becomes the next layer's input, propagating information forward through the network.

**36. Answer: A.** Sigmoid squashes values into (0,1) and saturates for large |x|, causing vanishing gradients; ReLU (max(0,x)) avoids saturation for positive inputs, helping gradients flow better (though it can suffer "dying ReLU" for negative inputs).

### Section E — Training

**37. Answer: B.** A batch is a subset of the training set fed through the network together before the weights are updated once.

**38. Answer: B.** One epoch = one full pass through every sample in the training dataset (which may consist of many batches).

**39. Answer: B.** Training data fits the model, validation data helps tune hyperparameters/model choice and monitor generalization during training, and the test set gives a final, unbiased estimate of performance on unseen data.

**40. Answer: B.** Overfitting means the model has essentially memorized training data patterns (including noise) and fails to generalize to new data.

**41. Answer: B.** The classic overfitting signature: training loss continues to fall while validation loss bottoms out and then rises — the gap between them widens.

**42. Answer: C.** Early stopping monitors validation performance and halts training once it stops improving, preventing the model from continuing to overfit the training data.

**43. Answer: B.** Standard order: forward pass (compute predictions) → compute loss → backpropagate to get gradients → update weights using those gradients.

**44. Answer: B.** The validation set is used only to evaluate/guide the model (e.g., hyperparameter tuning, early stopping) — it never directly updates weights via backpropagation, unlike the training set.

### Section F — Recurrent Neural Networks

**45. Answer: B.** Feedforward networks treat each input independently and have no built-in mechanism to remember or use information from previous time steps, so they can't naturally capture sequential/temporal dependencies.

**46. Answer: B.** "Left-to-right context" means that, at any position in the sequence, the model's hidden state only reflects information from earlier (leftward) positions, not later ones — a property of standard (unidirectional) RNNs.

**47. Answer: B.** Unfolding visualizes/implements the same recurrent cell (same shared weights) repeated once per time step, connected in a chain, to make forward/backward computation across a sequence tractable.

**48. Answer: A.** BPTT is standard backpropagation applied to this unfolded computational graph, propagating error gradients backward across every time step back to the start of the sequence.

**49. Answer: B.** A bidirectional RNN runs one RNN forward (left-to-right) and another backward (right-to-left), then combines both, so each time step's representation has access to both past and future context.

**50. Answer: B.** CTC allows training sequence-to-sequence models (like speech recognizers) when you don't know the exact alignment between input frames and output labels — it marginalizes over all valid alignments during training.
