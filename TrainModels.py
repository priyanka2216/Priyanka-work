def predict_phishing(url):
    # Extract features from the URL
    features = extract_features(url)

    # Check conditions based on features
    if features['length'] >= 30 or features['double_slash'] > 1 or features['at_symbol'] == 1 or features[
        'hyphen'] == 1:
        return 1  # Phishing
    elif 20 <= features['length'] <= 25:
        return -1  # Safe
    else:
        return -1  # Safe


def extract_features(url):
    # Calculate URL length
    length = len(url.split('/')[2])

    # Count occurrences of '//' in the URL
    double_slash = url.count('//')

    # Check if '@' symbol is present
    at_symbol = 1 if '@' in url else 0

    # Check if '-' symbol is present
    hyphen = 1 if '-' in url else 0

    return {'length': length, 'double_slash': double_slash, 'at_symbol': at_symbol, 'hyphen': hyphen}


# Example usage
url1 = "https://example.com"  # Safe URL
url2 = "https://gemini.google.com/"  # Phishing URL
url3 = "https://example@phishing.com"  # Phishing URL
url4 = "https://example-long-phishing-url.com"  # Phishing URL with long length
url5 = "https://example-long-phishing-url-with-multiple-slashes.com"  # Phishing URL with multiple slashes

print("Prediction for '{}' is: {}".format(url1, predict_phishing(url1)))
print("Prediction for '{}' is: {}".format(url2, predict_phishing(url2)))
print("Prediction for '{}' is: {}".format(url3, predict_phishing(url3)))
print("Prediction for '{}' is: {}".format(url4, predict_phishing(url4)))
print("Prediction for '{}' is: {}".format(url5, predict_phishing(url5)))

#**********************************

# import pandas as pd
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LogisticRegression
#
# # Load the data from phishing.csv1
# df = pd.read_csv('phishing.csv')
#
# # Separate features (X) and target variable (y)
# X = df.drop(columns=['class'])
# # print(X)
# y = df['class']
# # print(y)
#
# # Split data into training and testing sets (80% train, 20% test)
# # print("============")
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # print(pr)
# # print("============")
# # Save the training and testing sets to separate files (optional)
# X_train.to_csv('X_train.csv', index=False)
# X_test.to_csv('X_test.csv', index=False)
# y_train.to_csv('y_train.csv', index=False)
# y_test.to_csv('y_test.csv', index=False)
#
# # Initialize the scaler
# scaler = StandardScaler()
# # print(scaler)
# scaler.fit(X_train)
#
# # Preprocess features
# X_train_scaled = scaler.transform(X_train)
# # print(X_train_scaled)
#
# X_test_scaled = scaler.transform(X_test)
#
# #*****************************
# lr_model = LogisticRegression(random_state=42)
#
# # Train Logistic Regression model
# lr_model.fit(X_train_scaled, y_train)
#
# # Make predictions using the trained model
# y_pred_lr = lr_model.predict(X_test_scaled)
#
# # Evaluate model performance
# accuracy_lr = accuracy_score(y_test, y_pred_lr)
# # #*************************
#
# # Initialize SVM model
# svm_model = SVC(kernel='linear', random_state=42)
#
# # Train SVM model
# svm_model.fit(X_train_scaled, y_train)
#
# # Initialize Random Forest model
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# # Train Random Forest model
# rf_model.fit(X_train_scaled, y_train)
#
# # Initialize Decision Tree model
# dt_model = DecisionTreeClassifier(random_state=42)
# # Train Decision Tree model
# dt_model.fit(X_train_scaled, y_train)
#
# # Make predictions using the trained models
# y_pred_svm = svm_model.predict(X_test_scaled)
# # print(y_pred_svm)
# y_pred_rf = rf_model.predict(X_test_scaled)
# # print(y_pred_rf)
# y_pred_dt = dt_model.predict(X_test_scaled)
# # print(y_pred_dt)
#
# # Evaluate model performance
# accuracy_svm = accuracy_score(y_test, y_pred_svm)
# accuracy_rf = accuracy_score(y_test, y_pred_rf)
# accuracy_dt = accuracy_score(y_test, y_pred_dt)
#
# print('SVM Accuracy:', accuracy_svm)
# print('Random Forest Accuracy:', accuracy_rf)
# print('Decision Tree Accuracy:', accuracy_dt)
# print('Logistic regression Accuracy:', accuracy_lr)


#=====================here is my existing code========
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import joblib
#
# # Load the dataset
# ds = pd.read_csv("phishing.csv")
#
# # Extract features and target variable
# x = ds.iloc[:, 1:31].values
# y = ds.iloc[:, -1].values
#
# # Split the data into training and testing sets
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
#
# # Support Vector Machine (RBF Kernel)
# svm_rbf = SVC(kernel='rbf')
# svm_rbf.fit(x_train, y_train)
# svm_rbf_accuracy = accuracy_score(y_test, svm_rbf.predict(x_test))
#
# # Decision Tree
# dt = DecisionTreeClassifier()
# dt.fit(x_train, y_train)
# dt_accuracy = accuracy_score(y_test, dt.predict(x_test))
#
# # Random Forest
# rf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
# rf.fit(x_train, y_train)
# rf_accuracy = accuracy_score(y_test, rf.predict(x_test))
#
# # Save the models
# joblib.dump(svm_rbf, 'svm_rbf.pkl')
# joblib.dump(dt, 'decision_tree.pkl')
# joblib.dump(rf, 'random_forest.pkl')
#
# print("Models trained and saved successfully!")
#
# # Create DataFrame to compare models and display accuracy
# models = pd.DataFrame({
#     'Model': ['SVM', 'Random Forest', 'Decision Tree'],
#     'Accuracy': [svm_rbf_accuracy, rf_accuracy, dt_accuracy]})
#
# # Sort models by accuracy
# models = models.sort_values(by='Accuracy', ascending=False)
#
# print(models)
#
#
#
