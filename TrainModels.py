import pandas as pd
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data from phishing.csv
df = pd.read_csv('phishing.csv')

# Separate features (X) and target variable (y)
X = df.drop(columns=['class'])
y = df['class']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the training and testing sets to separate files (optional)
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

# Initialize the scaler
scaler = StandardScaler()
scaler.fit(X_train)

# Preprocess features
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize SVM model
svm_model = SVC(kernel='linear', random_state=42)
# Train SVM model
svm_model.fit(X_train_scaled, y_train)

# Initialize Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# Train Random Forest model
rf_model.fit(X_train_scaled, y_train)

# Initialize Decision Tree model
dt_model = DecisionTreeClassifier(random_state=42)
# Train Decision Tree model
dt_model.fit(X_train_scaled, y_train)

# Make predictions using the trained models
y_pred_svm = svm_model.predict(X_test_scaled)
y_pred_rf = rf_model.predict(X_test_scaled)
y_pred_dt = dt_model.predict(X_test_scaled)

# Evaluate model performance
accuracy_svm = accuracy_score(y_test, y_pred_svm)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
accuracy_dt = accuracy_score(y_test, y_pred_dt)

print('SVM Accuracy:', accuracy_svm)
print('Random Forest Accuracy:', accuracy_rf)
print('Decision Tree Accuracy:', accuracy_dt)
