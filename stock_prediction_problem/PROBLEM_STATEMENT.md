# Stock Price Prediction with a Deep Neural Network

## 1. Goal

Your goal is to build a supervised learning model that predicts the next stock closing price of a company using the previous 20 closing prices.

You will use historical daily stock prices for **Apple Inc. (AAPL)**. The dataset has already been downloaded for you as:

```text
data/aapl_daily.csv
```

The task is intentionally simple at first: convert the raw stock price series into many training examples of the form:

```text
20 previous closing prices  ->  21st closing price
```

Then build a deep neural network that takes 20 numeric inputs and predicts 1 numeric output.

---

## 2. Dataset

### File

```text
data/aapl_daily.csv
```

### Company

Apple Inc. stock, ticker symbol: **AAPL**

### Source

The CSV was downloaded from a public GitHub-hosted historical stock dataset based on Yahoo Finance data.

### Columns

The dataset contains the following columns:

| Column | Meaning |
|---|---|
| Date | Trading date |
| Open | Opening stock price for that day |
| High | Highest stock price during that day |
| Low | Lowest stock price during that day |
| Close | Closing stock price for that day |
| Adj Close | Adjusted closing price |
| Volume | Number of shares traded |

For this exercise, use only:

```text
Date
Close
```

The `Close` column is the target time series.

---

## 3. Machine Learning Problem

You are given a sequence of daily closing prices:

```text
p1, p2, p3, p4, ..., pn
```

You must convert this single long sequence into many supervised learning samples.

Each input sample should contain **20 consecutive closing prices**.

The target output should be the **next closing price**, meaning the 21st value.

### Example

Suppose the closing prices are:

```text
[100, 102, 101, 105, 107, ..., 120]
```

A training example should look like:

```text
Input X:  [price_day_1, price_day_2, ..., price_day_20]
Output y: price_day_21
```

Then the next training example shifts forward by one day:

```text
Input X:  [price_day_2, price_day_3, ..., price_day_21]
Output y: price_day_22
```

This is called a **sliding window** dataset.

---

## 4. Required Data Transformation

Create a new dataset from the `Close` column using a window size of 20.

For every valid position `i`, create:

```text
X[i] = [Close[i], Close[i+1], ..., Close[i+19]]
y[i] = Close[i+20]
```

If the original dataset has `n` closing prices, the transformed dataset should have:

```text
n - 20
```

supervised examples.

### Expected Shapes

After transformation:

```text
X shape: (number_of_examples, 20)
y shape: (number_of_examples,)
```

For example, if there are 1,258 stock price rows:

```text
X shape: (1,238, 20)
y shape: (1,238,)
```

---

## 5. Train/Test Split

Because this is time-series data, do **not** randomly shuffle the dataset before splitting.

Use the earlier data for training and the later data for testing.

Suggested split:

```text
80% training data
20% testing data
```

Example:

```text
train_size = int(0.8 * len(X))

X_train = X[:train_size]
y_train = y[:train_size]

X_test = X[train_size:]
y_test = y[train_size:]
```

---

## 6. Scaling Requirement

Stock prices can have large numeric values, and neural networks usually train better when inputs are scaled.

Scale the input values before training.

You may use one of the following:

1. `MinMaxScaler`
2. `StandardScaler`
3. Manual normalization

Important rule:

Fit the scaler only on the training data, then use the same scaler to transform the test data.

Do not fit the scaler on the full dataset, because that leaks information from the future test period into the training process.

---

## 7. Model Requirement

Build a **deep neural network** that takes exactly 20 input values and predicts the 21st value.

This should be a standard feed-forward neural network, also called a multilayer perceptron.

### Input Layer

The model input should have shape:

```text
20
```

Each input feature represents one previous closing price.

### Output Layer

The model should output one number:

```text
predicted next closing price
```

### Suggested Architecture

You may start with this architecture:

```text
Input: 20 values
Dense layer: 64 neurons, ReLU activation
Dense layer: 32 neurons, ReLU activation
Dense layer: 16 neurons, ReLU activation
Output layer: 1 neuron, linear activation
```

The final layer should not use softmax or sigmoid because this is a regression problem, not a classification problem.

---

## 8. Training Requirement

Train the model to minimize prediction error.

Use a regression loss function such as:

```text
Mean Squared Error, MSE
```

or

```text
Mean Absolute Error, MAE
```

Suggested optimizer:

```text
Adam
```

Suggested starting values:

```text
epochs = 50
batch_size = 32
validation_split = 0.1
```

You may tune these values after observing model performance.

---

## 9. Evaluation

Evaluate the model on the test set.

Report at least two of the following metrics:

| Metric | Meaning |
|---|---|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| MAPE | Mean Absolute Percentage Error |

Recommended minimum evaluation:

```text
MAE
RMSE
```

Also create a plot comparing:

```text
Actual closing prices vs Predicted closing prices
```

on the test set.

---

## 10. Questions to Answer

After training your model, answer these questions:

1. What is the shape of your `X` dataset after creating sliding windows?
2. What is the shape of your `y` dataset?
3. Why should the time-series train/test split not be randomly shuffled?
4. What loss function did you use, and why?
5. What was your test MAE?
6. What was your test RMSE?
7. Does the predicted line follow the real stock price trend?
8. Is predicting stock prices from only the previous 20 prices reliable in real life? Why or why not?

---

## 11. Deliverables

Submit the following:

1. A notebook or Python script that loads `data/aapl_daily.csv`.
2. Code that extracts the `Close` column.
3. Code that converts the close prices into `20 values -> 21st value` supervised examples.
4. A train/test split that preserves time order.
5. A deep neural network with 20 inputs and 1 output.
6. Training logs or a plot of training loss.
7. Test-set evaluation metrics.
8. A plot of actual vs predicted closing prices.
9. Short written answers to the questions in Section 10.

---

## 12. Optional Extensions

After completing the basic version, try one or more of these improvements:

1. Use `Adj Close` instead of `Close`.
2. Predict percentage return instead of raw price.
3. Compare window sizes such as 5, 10, 20, 50, and 100.
4. Add more input features such as `Open`, `High`, `Low`, and `Volume`.
5. Compare the neural network against a naive baseline:

```text
Tomorrow's predicted price = today's closing price
```

6. Try an LSTM or 1D CNN model after finishing the simple dense network.

---

## 13. Success Criteria

Your solution is successful if:

1. You correctly create sliding-window examples using 20 previous closing prices.
2. Your neural network accepts 20 inputs and produces 1 output.
3. You train only on earlier dates and test on later dates.
4. You report meaningful test metrics.
5. You visualize actual vs predicted prices.

The most important part of this exercise is not achieving perfect predictions. The goal is to learn how to convert time-series data into a supervised learning problem and train a neural network for regression.
