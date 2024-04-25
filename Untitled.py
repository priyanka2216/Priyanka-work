#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
ds = pd.read_csv("phishing.csv")

# Extract features and target variable
x = ds.iloc[:, 1:31].values
y = ds.iloc[:, -1].values

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Support Vector Machine (RBF Kernel)
svm_rbf = SVC(kernel='rbf')
svm_rbf.fit(x_train, y_train)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
rf.fit(x_train, y_train)

# Save the models
joblib.dump(svm_rbf, 'svm_rbf.pkl')
joblib.dump(dt, 'decision_tree.pkl')
joblib.dump(rf, 'random_forest.pkl')

print("Models trained and saved successfully!")

# Create DataFrame to compare models and display accuracy
models = pd.DataFrame({
    'Model': ['SVM', 'Random Forest', 'Decision Tree'],
    'Accuracy': [svm_rbf, dt, rf]
})
models.sort_values(by='Accuracy', ascending=False)
print(models)

