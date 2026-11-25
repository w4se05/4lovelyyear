# Final Exam — Data Science & Machine Learning Foundations

**Format:** 50 Multiple Choice Questions | **Open Book** | Choose the single best answer for each question.

**Time suggestion:** 90 minutes

---

## Section A — NumPy (Q1–Q12)

**1.** Given `a = np.zeros((3, 4, 5))`, what does `a.shape[1]` return?

A) 3
B) 4
C) 5
D) 12

**2.** For an array `a` with shape `(2, 3, 4)`, what does `axis=0` refer to when calling `a.sum(axis=0)`?

A) The innermost (last) dimension
B) The outermost (first) dimension
C) The total number of elements
D) The middle dimension only

**3.** An array `a` has shape `(6,)`. Which of the following reshape calls will raise an error?

A) `a.reshape(2, 3)`
B) `a.reshape(3, 2)`
C) `a.reshape(6, 1)`
D) `a.reshape(2, 4)`

**4.** If `a` has shape `(4, 3)`, what is the shape of `a.T`?

A) `(4, 3)`
B) `(3, 4)`
C) `(12,)`
D) `(1, 12)`

**5.** What is the result of `np.array([1, 2, 3]) * np.array([4, 5, 6])`?

A) `[4, 10, 18]`
B) `32` (dot product)
C) `[1, 2, 3, 4, 5, 6]`
D) An error, since element-wise multiplication requires `np.multiply`

**6.** Given `a = np.array([10, 20, 30, 40])`, what does `a[np.array([0, 2])]` return?

A) `[10, 30]`
B) `[20, 40]`
C) `[10, 20]`
D) An error, since arrays cannot be used as indices

**7.** What does `np.where(a > 20, a, 0)` do for `a = np.array([10, 20, 30, 40])`?

A) Returns the indices where `a > 20`
B) Returns `[0, 0, 30, 40]`
C) Returns `[True, False, True, True]`
D) Raises an error because `np.where` needs exactly one argument

**8.** For a 2D array `a` of shape `(3, 4)`, what does `np.argmax(a, axis=1)` return?

A) A single scalar — the index of the overall maximum
B) An array of shape `(3,)` with the index of the max in each row
C) An array of shape `(4,)` with the index of the max in each column
D) The maximum values themselves, not their indices

**9.** What is the key difference between `np.sort(a)` and `np.argsort(a)`?

A) `np.sort` returns indices, `np.argsort` returns sorted values
B) `np.sort` returns sorted values, `np.argsort` returns the indices that would sort the array
C) They are identical functions with different names
D) `np.argsort` only works on 1D arrays

**10.** You have `a` with shape `(2, 3)` and `b` with shape `(2, 3)`. What shape does `np.concatenate([a, b], axis=0)` produce?

A) `(4, 3)`
B) `(2, 6)`
C) `(2, 3, 2)`
D) An error, since shapes must differ to concatenate

**11.** Which pair of shapes can be broadcast together?

A) `(3, 4)` and `(4, 3)`
B) `(3, 4)` and `(4,)`
C) `(3, 4)` and `(3,)`
D) `(3, 4)` and `(2, 4)`

**12.** Given `a` with shape `(5,)`, what is the shape of `a[:, np.newaxis]`?

A) `(5,)`
B) `(1, 5)`
C) `(5, 1)`
D) `(5, 5)`

---

## Section B — Pandas (Q13–Q18)

**13.** What is the main difference between `df.loc[]` and `df.iloc[]`?

A) `loc` selects by integer position, `iloc` selects by label
B) `loc` selects by label, `iloc` selects by integer position
C) They behave identically for all DataFrames
D) `loc` only works on columns, `iloc` only works on rows

**14.** Given a DataFrame `df` indexed by integers `0` to `9`, what does `df.loc[2:5]` return compared to `df.iloc[2:5]`?

A) Both return rows 2, 3, 4 (5 excluded)
B) `df.loc[2:5]` includes row 5, `df.iloc[2:5]` excludes row 5
C) `df.iloc[2:5]` includes row 5, `df.loc[2:5]` excludes row 5
D) Both raise an error since slicing is not supported

**15.** If `df1` has columns `['A', 'B']` and `df2` has columns `['A', 'B']`, what does `pd.concat([df1, df2], axis=0)` do?

A) Stacks the DataFrames vertically (adds rows)
B) Stacks the DataFrames horizontally (adds columns)
C) Merges on a common key
D) Raises an error because column names match

**16.** What does `pd.concat([df1, df2], axis=1)` do if `df1` and `df2` have the same row index but different columns?

A) Adds `df2`'s rows below `df1`'s rows
B) Aligns on index and adds `df2`'s columns beside `df1`'s columns
C) Overwrites `df1` entirely
D) Produces a single column of concatenated strings

**17.** To select the value in row label `'x'` and column `'price'`, which is correct?

A) `df.iloc['x', 'price']`
B) `df.loc['x', 'price']`
C) `df['x']['price']`
D) `df.at['price', 'x']`

**18.** You want the first 3 rows of a DataFrame regardless of what the index labels are. Which is most appropriate?

A) `df.loc[0:3]`
B) `df.iloc[0:3]`
C) `df.loc[:3]`
D) `df['rows'][0:3]`

---

## Section C — Machine Learning Fundamentals (Q19–Q26)

**19.** A model predicts a continuous numeric value, such as a house price. This is an example of:

A) Classification
B) Regression
C) Clustering
D) Reinforcement learning

**20.** A model groups customers into segments without being told the segment labels beforehand. This is:

A) Supervised classification
B) Supervised regression
C) Unsupervised clustering
D) Semi-supervised regression

**21.** Which of the following best distinguishes supervised from unsupervised learning?

A) Supervised learning uses labeled data; unsupervised learning finds structure in unlabeled data
B) Supervised learning is always more accurate
C) Unsupervised learning always requires more data than supervised learning
D) Supervised learning cannot be used for regression tasks

**22.** Spam email detection (spam vs. not spam) is best described as:

A) Regression
B) Binary classification
C) Clustering
D) Unsupervised anomaly detection with no ground truth

**23.** An e-commerce company wants to discover natural groupings in shopping behavior without predefined categories. Which approach fits best?

A) Linear regression
B) Logistic regression
C) K-means clustering
D) Binary classification

**24.** Predicting a student's exam score (0–100) from hours studied is an example of:

A) Classification
B) Clustering
C) Regression
D) Unsupervised learning

**25.** Which statement about clustering is TRUE?

A) Clustering requires labeled training data
B) Clustering assigns a continuous numeric output to each input
C) Clustering groups similar data points together without predefined labels
D) Clustering is a type of supervised learning

**26.** A hospital has patient records labeled with disease outcomes and wants to predict outcomes for new patients. Which learning paradigm applies?

A) Unsupervised learning
B) Supervised learning
C) Clustering
D) Dimensionality reduction only

---

## Section D — Neural Networks (Q27–Q36)

**27.** In a fully connected neural network, what is the role of a "layer"?

A) It stores the final loss value only
B) It transforms inputs into outputs via weighted sums and (usually) an activation function
C) It only stores hyperparameters like learning rate
D) It is only used during data preprocessing

**28.** What do the weights and bias in a neuron represent?

A) Weights scale each input's contribution; the bias shifts the weighted sum independent of input
B) Weights determine the number of layers; bias determines the number of neurons
C) Weights are fixed constants that never change during training
D) Bias always equals zero in modern networks

**29.** Why are activation functions necessary in neural networks?

A) They reduce the number of parameters in the model
B) They introduce non-linearity, allowing the network to model complex, non-linear relationships
C) They are only used to normalize the input data
D) They replace the need for a loss function

**30.** A network uses only linear activation functions in every layer. What happens?

A) The network becomes more powerful than one with non-linear activations
B) The entire network still behaves like a single linear transformation, regardless of depth
C) It becomes impossible to compute a forward pass
D) The gradients cannot be computed at all

**31.** What does the "gradient vector" of a loss function with respect to the network's parameters represent?

A) The set of all output predictions
B) The direction and rate of steepest increase of the loss with respect to each parameter
C) The final accuracy of the model
D) The number of epochs needed to converge

**32.** For a specific weight `w_ij`, what does `∂L/∂w_ij` (the gradient for that weight) tell us?

A) How much the loss `L` would change with a small change in that specific weight
B) The absolute value of the weight itself
C) The learning rate to use for that weight
D) Whether the weight belongs to the input or output layer

**33.** In standard gradient descent, the weight update rule is:

A) `w = w + learning_rate * gradient`
B) `w = w - learning_rate * gradient`
C) `w = gradient / learning_rate`
D) `w = w * gradient`

**34.** If the learning rate is set far too high during training, what is the most likely outcome?

A) Training converges faster with no downside
B) The loss may oscillate or diverge instead of converging smoothly
C) The gradients become exactly zero
D) The model automatically switches to a smaller batch size

**35.** During a forward pass, the output of one layer becomes:

A) The bias of the next layer only
B) The input to the next layer
C) The gradient for the next layer
D) Discarded and unused

**36.** Which statement correctly compares Sigmoid and ReLU activation functions?

A) Sigmoid squashes outputs to (0, 1) and can suffer from vanishing gradients; ReLU outputs 0 for negatives and tends to avoid this issue for positive inputs
B) ReLU squashes outputs to (0, 1); Sigmoid is linear
C) Both functions are identical in behavior and gradient properties
D) Sigmoid is never used in neural networks

---

## Section E — Training Neural Networks (Q37–Q44)

**37.** What is a "batch" in the context of training a neural network?

A) The entire dataset used in one epoch
B) A subset of the training data processed together before one weight update
C) The number of layers in the network
D) The final test set used for evaluation

**38.** What defines one "epoch" during training?

A) One forward pass on a single sample
B) One complete pass through the entire training dataset
C) One update of a single weight
D) The total number of batches ever processed across all training runs

**39.** Why do we split data into training, validation, and test sets?

A) To speed up computation only
B) To train on one part, tune/select models using another, and get an unbiased final performance estimate on unseen data
C) Because algorithms require exactly three files to run
D) Validation and test sets are the same thing, just renamed

**40.** Overfitting occurs when:

A) The model performs well on both training and unseen data
B) The model performs well on training data but poorly generalizes to unseen (validation/test) data
C) The model fails to learn anything from the training data
D) The training loss and validation loss both increase together

**41.** Which training curve pattern is the clearest sign of overfitting?

A) Training loss and validation loss both decrease and plateau together
B) Training loss keeps decreasing while validation loss starts increasing after some point
C) Training loss increases while validation loss decreases
D) Both losses stay flat from the start

**42.** How does early stopping help prevent overfitting?

A) It increases the learning rate once validation loss stops improving
B) It stops training once the model perfectly memorizes the training set
C) It halts training when validation performance stops improving (or starts worsening), preventing further overfitting
D) It removes the validation set from consideration entirely

**43.** In a typical training loop, what is the correct order of steps for one batch?

A) Update weights → forward pass → compute loss → backpropagate
B) Forward pass → compute loss → backpropagate (compute gradients) → update weights
C) Backpropagate → forward pass → update weights → compute loss
D) Compute loss → update weights → forward pass → backpropagate

**44.** What is the primary role of the validation set during training?

A) It is used to update the model's weights directly via backpropagation
B) It monitors generalization performance and guides decisions like early stopping or hyperparameter tuning, without being used for weight updates
C) It replaces the need for a test set entirely
D) It is only used once, after all training is complete

---

## Section F — Recurrent Neural Networks (Q45–Q50)

**45.** Why can't a standard feedforward network be used directly on a time series without modification?

A) Feedforward networks cannot process numeric data
B) Feedforward networks have no natural way to capture the sequential order/dependency between time steps
C) Feedforward networks always require exactly one input feature
D) Feedforward networks only work on image data

**46.** In an RNN processing text left-to-right, what does "left-to-right context" mean?

A) The prediction at each step only depends on future tokens, not past ones
B) The hidden state at each step is influenced only by tokens that came before it in the sequence
C) The network reads the entire sequence in reverse
D) Context has no effect on the RNN's hidden state

**47.** What does "unfolding" an RNN across time mean?

A) Reshaping the input into a 2D array
B) Representing the same recurrent cell (with shared weights) as a chain of copies, one per time step, to visualize/compute the sequence
C) Removing the recurrent connections from the network entirely
D) Splitting the RNN into multiple independent networks with different weights per step

**48.** Backpropagation Through Time (BPTT) refers to:

A) Backpropagation applied to the unfolded RNN, propagating gradients backward across all time steps
B) A method that skips gradient computation for recurrent layers
C) A technique used only for convolutional neural networks
D) A way to increase the batch size dynamically during training

**49.** What advantage does a Bidirectional RNN have over a standard (unidirectional) RNN?

A) It processes the sequence twice as fast
B) It combines information from both past (left-to-right) and future (right-to-left) context at each time step
C) It eliminates the need for backpropagation
D) It can only be used for image classification tasks

**50.** Connectionist Temporal Classification (CTC) is primarily used to:

A) Reduce the number of layers in an RNN
B) Train sequence models (e.g., speech recognition) when the alignment between input frames and output labels is unknown, without requiring explicit frame-level labels
C) Replace the need for activation functions
D) Perform clustering on time series data

---

*End of Exam — 50 Questions*
