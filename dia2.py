import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read the dataset
df = pd.read_csv('C:/Users/manoj/Desktop/diabets/dia.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Splitting data into features (x) and target (y)
x = df.iloc[:, df.columns != 'Outcome']
y = df.iloc[:, df.columns == 'Outcome']

# Splitting data into training and testing sets
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42) # 20% for testing

# Creating a Random Forest model
model = RandomForestClassifier(random_state=42)

# Training the model
model.fit(xtrain, ytrain.values.ravel())

# Predicting outcomes on the test set
predict_output = model.predict(xtest)

# Calculating accuracy
acc = accuracy_score(predict_output, ytest)
print('The accuracy score for Random Forest:', acc)
