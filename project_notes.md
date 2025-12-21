
# End to End project

Data  - Housing Price Prediction

# Split The data
Valid_data, Test_data, Train_data =  split(10, 20, 70)

# Using stratified sampling


# Using Data we train a model.
X, y = Train_data[:-1], Train_data[-1]

# Descriptive analyses / Visual analyis



# Do we need to remove duplicates or redundant? 



# Convert non-numeric values to numbers
## One hot encoding
Model   ->  Ford_model  Maruti      Toyota 
Ford        1           0           0
Maruti      0           1           0
Toyota      0           0           1
Ford        1           0           0


# What if there are dates?
## Convert it into M, Y, D, h, minute
## time since epoch - number
## Check if it was a holday? Was it a weekend?
## Convert data into Weather -> Winter, Summer, Spring, Autumn -> one hot encoding.
## Convert it into weather -> humidiy, temperature, etc

# What if there is time?
## Convert Morning, Night, Noon, Evening
## Brightness -> Sun light 
## 00:00 to 23:59 -> Sin(time*360/24)
## 

# What to do with the location?
# Is the place near railway station?
# City -> One hot encoding
# City -> humidity, temperat etc.

## Text -> LLM based embedding
## or words counts based encoding - TFIDF - terms frequency inverse document frequency

# Impute - fix the missing values - delete row/col or fill 0s, mean, median or use some other method
## Nan errors

# Normalize the data
models = [SGDRegressor(), SVMRegressor(), RandomForrestRegressor(), NeuralNetwork()]
for model in models:
    model.fit(X_train, y_train)
    model.evaluate(X_valid, y_valid)

# Pick the ones that are performing best
# parameter tuning of the model

# If you have multiple model which are performing equally # ensemble
Create a team of these model and take the average of the result

# Using Model we will predict the house prices.
y = model.predict(X)

========
pd.read_csv
.head()
.info()
.describe()
.value_counts()
