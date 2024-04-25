from flask import Flask, request, jsonify
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('phishing.csv')

# Separate features (X) and target variable (y)
X = df.drop(columns=['class'])
y = df['class']

# Initialize the SVM model
svm_model = SVC(kernel='linear', random_state=42)
# Train the SVM model
svm_model.fit(X, y)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    # Get URL from the JSON payload
    url = request.json.get('url')

    # Extract features from the URL
    features = extract_features(url)

    # Predict using SVM model
    svm_prediction = int(svm_model.predict([features])[0])
    if svm_prediction == -1:
        svm_message = "URL is predicted to be safe!!"
    else:
        svm_message = "URL is predicted to be phishing!!"

    # Predict using RandomForest model
    rf_prediction = int(rf_model.predict([features])[0])
    if rf_prediction == -1:
        rf_message = "URL is predicted to be safe!!"
    else:
        rf_message = "URL is predicted to be phishing!!"

    # Predict using DecisionTree model
    dt_prediction = int(dt_model.predict([features])[0])
    if dt_prediction == -1:
        dt_message = "URL is predicted to be safe!!"
    else:
        dt_message = "URL is predicted to be phishing!!"

    # Convert SVM accuracy to a regular Python float
    svm_accuracy = float(svm_model.score(X, y))

    # Convert RandomForest accuracy to a regular Python float
    rf_accuracy = float(rf_model.score(X, y))

    # Convert DecisionTree accuracy to a regular Python float
    dt_accuracy = float(dt_model.score(X, y))

    # Return the predictions, message, and accuracies as JSON response
    return jsonify({'svm_prediction': svm_prediction, 'svm_message': svm_message, 'svm_accuracy': svm_accuracy,
                    'rf_prediction': rf_prediction, 'rf_message': rf_message, 'rf_accuracy': rf_accuracy,
                    'dt_prediction': dt_prediction, 'dt_message': dt_message, 'dt_accuracy': dt_accuracy})


def extract_features(url):
    # Initialize feature values
    using_ip = 0
    long_url = 0
    short_url = 0
    symbol_at = 0
    redirecting_slash = 0
    prefix_suffix = 0

    # Check if IP address is used in the URL
    if 'http://' in url or 'ip' in url:
        using_ip = 1

    # Check if URL length is greater than 30
    if len(url) > 40:
        long_url = -1

    # Check if URL length is less than 10
    if len(url) <= 40:
        short_url = 1
    # if 10 < len(url) <= 40:
    #     short_url = -1

    # Check if "@" symbol is present in the URL
    if '@' in url:
        symbol_at = 1

    # Check if "Redirecting//" feature is present
    if url.count('//') > 1:
        redirecting_slash = 1

    # Check if "PrefixSuffix-" feature is present
    if '-' in url:
        prefix_suffix = 1

    # Return extracted features as list
    # print(using_ip, long_url, short_url, symbol_at, redirecting_slash, prefix_suffix)
    return [using_ip, long_url, short_url, symbol_at, redirecting_slash, prefix_suffix]


if __name__ == '__main__':
    app.run(host='192.168.1.26', debug=True)


#---------------------------------------------

#*****************************************

# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# def predict_phishing(url):
#     # Extract features from the URL
#     features = extract_features(url)
#
#     # Check conditions based on features
#     if features['length'] >= 30 or features['double_slash'] > 1 or features['at_symbol'] == 1 or features['hyphen'] == 1:
#         return 1  # Phishing
#     elif 20 <= features['length'] <= 25:
#         return -1  # Safe
#     else:
#         return -1  # Safe
#
# def extract_features(url):
#     # Calculate URL length
#     length = len(url.split('/')[2])
#
#     # Count occurrences of '//' in the URL
#     double_slash = url.count('//')
#
#     # Check if '@' symbol is present
#     at_symbol = 1 if '@' in url else 0
#
#     # Check if '-' symbol is present
#     hyphen = 1 if '-' in url else 0
#
#     return {'length': length, 'double_slash': double_slash, 'at_symbol': at_symbol, 'hyphen': hyphen}
#
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get URL from the JSON payload
#     url = request.json.get('url')
#
#     # Predict whether the URL is phishing or safe
#     prediction = predict_phishing(url)
#
#     # Determine message based on prediction
#     if prediction == -1:
#         message = "URL is predicted to be safe!!"
#     else:
#         message = "URL is predicted to be phishing!!"
#
#     # Return the prediction and message as JSON response
#     return jsonify({'prediction': prediction, 'message': message})
#
# if __name__ == '__main__':
#     app.run(debug=True)


#--------phishing url------------------

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from url_checker import check_url_for_phishing
#
# app = Flask(__name__)
# CORS(app)
#
# @app.route('/check_url', methods=['POST'])
# def check_url():
#     try:
#         # Call check_url_for_phishing to get predictions and probabilities
#         url = request.json.get('url')
#         # print(url)
#         svm_prediction, rf_prediction, dt_prediction, svm_proba, rf_proba, dt_proba = check_url_for_phishing(url)
#         print(svm_prediction, rf_prediction, dt_prediction)
#         if svm_prediction == 1 or rf_prediction == 1 or dt_prediction == 1:
#
#             message = "Phishing URL detected!"
#         else:
#             message = "URL is safe "
#
#         response_data = {
#             "message": message,
#             "svm_probability": svm_proba.tolist()[0] if svm_proba is not None else None,
#             "rf_probability": rf_proba.tolist()[0] if rf_proba is not None else None,
#             "dt_probability": dt_proba.tolist()[0] if dt_proba is not None else None
#         }
#         print(response_data, "******************")
#         status_code = 200  # Success
#     except Exception as e:
#         response_data = {
#             "message": "Error processing URL: " + str(e),
#             "svm_prediction": None,
#             "svm_probability": None,
#             "rf_probability": None,
#             "dt_probability": None
#         }
#         status_code = 500  # Internal Server Error
#
#     return jsonify(response_data), status_code
#
#
# if __name__ == "__main__":
#     app.run(host='192.168.1.9', debug=True)

#=================here is my existing code===============

# import joblib
# from flask import Flask, request, jsonify
# from urllib.parse import urlparse
# import re
# import numpy as np
#
# app = Flask(__name__)
#
# # Load the models
# svm_rbf = joblib.load('svm_rbf.pkl')
# dt = joblib.load('decision_tree.pkl')
# rf = joblib.load('random_forest.pkl')
#
# def extract_features(url):
#     parsed_url = urlparse(url)
#     print("***********************")
#     print(parsed_url)
#     print("***********************")
#     domain = parsed_url.netloc
#     path = parsed_url.path
#     features = {}
#
#     features['UsingIP'] = bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))
#     features['LongURL'] = int(len(url) > 75)
#     features['ShortURL'] = int(len(url) < 25)
#     features['Symbol@'] = int('@' in url)
#     features['Redirecting//'] = int('//' in url)
#     features['PrefixSuffix-'] = int('-' in domain)
#     features['SubDomains'] = domain.count('.')
#     features['HTTPS'] = int(parsed_url.scheme == 'https')
#     features['DomainRegLen'] = len(parsed_url.netloc)
#     features['Favicon'] = int('favicon' in url.lower())
#     features['NonStdPort'] = int(':' in parsed_url.netloc)
#     features['HTTPSDomainURL'] = int('https' in domain)
#     features['AnchorURL'] = int('#' in url)
#     features['LinksInScriptTags'] = int('<script>' in url.lower())
#     features['InfoEmail'] = int('info@' in url)
#     features['AbnormalURL'] = int(any(char.isdigit() for char in domain))
#     features['WebsiteForwarding'] = int('forwarding' in path.lower())
#     features['DisableRightClick'] = int('rightclick' in path.lower())
#     features['UsingPopupWindow'] = int('popup' in path.lower())
#     features['IframeRedirection'] = int('iframe' in path.lower())
#     features['AgeofDomain'] = int(len(parsed_url.netloc.split('.')) > 1)
#     features['DNSRecording'] = int('dns' in path.lower())
#     features['PageRank'] = int('pagerank' in path.lower())
#     features['GoogleIndex'] = int('google' in domain)
#     features['LinksPointingToPage'] = int('link' in path.lower())
#     features['StatsReport'] = int('stats' in path.lower())
#     print(features)
#     # Add missing features with default value 0
#     missing_features = set(range(30)) - set(features.keys())
#
#     for feature in missing_features:
#         features[feature] = 0
#
#     return features
#
# def preprocess_features(features):
#     pre = [features[feature] for feature in range(30)]
#     return pre
#
# def check_phishing(url):
#     features = extract_features(url)
#     X_predict = preprocess_features(features)
#
#     print("/////////////////////////////////")
#     svm_rbf_prediction = svm_rbf.predict([X_predict])[0].item()  # Convert int64 to regular integer
#     print(svm_rbf_prediction)
#     dt_prediction = dt.predict([X_predict])[0].item()  # Convert int64 to regular integer
#     print(dt_prediction)
#     rf_prediction = rf.predict([X_predict])[0].item()  # Convert int64 to regular integer
#     print(rf_prediction)
#     print("/////////////////////////////////")
#     # Map model predictions to appropriate labels
#     results = {
#         'SVM (RBF Kernel)': -1 if svm_rbf_prediction == 0 else 1,
#         'Decision Tree': -1 if dt_prediction == 0 else 1,
#         'Random Forest': -1 if rf_prediction == 0 else 1
#     }
#     print(results)
#     print("@@@@@@@@@@@@")
#
#     return results
#
# # def check_phishing(url):
# #     features = extract_features(url)
# #     X_predict = preprocess_features(features)
# #
# #     print("/////////////////////////////////")
# #     svm_rbf_prediction = svm_rbf.predict([X_predict])[0].item()# Convert int64 to regular integer
# #     print(svm_rbf_prediction)
# #     dt_prediction = dt.predict([X_predict])[0].item()  # Convert int64 to regular integer
# #     print(dt_prediction)
# #     rf_prediction = rf.predict([X_predict])[0].item()  # Convert int64 to regular integer
# #     print(rf_prediction)
# #     print("/////////////////////////////////")
# #     # Map model predictions to appropriate labels
# #     results = {
# #         'SVM (RBF Kernel)': 1 if svm_rbf_prediction == 1 else -1,
# #         'Decision Tree': 1 if dt_prediction == 1 else -1,
# #         'Random Forest': 1 if rf_prediction == 1 else -1
# #         # 'SVM (RBF Kernel)': -1 if svm_rbf_prediction == 0 else 1,
# #         # 'Decision Tree': -1 if dt_prediction == 0 else 1,
# #         # 'Random Forest': -1 if rf_prediction == 0 else 1
# #     }
# #     print(results)
# #     print("@@@@@@@@@@@@@")
# #
# #     return results
#
# @app.route('/check_url', methods=['GET', 'POST'])
# def check_url():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             if 'url' not in data:
#                 return jsonify({"error": "URL attribute missing"}), 400
#
#             url = data['url']
#             results = check_phishing(url)
#             # print(results)
#             # print("###################")
#
#             # Determine if the majority of models predict phishing or safe
#             num_phishing = sum(1 for result in results.values() if result == 1)
#             # print("**************")
#             # print(num_phishing)
#             # print("**************")
#             num_safe = sum(1 for result in results.values() if result == -1)
#             # print(num_safe)
#             # print("**************")
#             is_phishing = num_phishing > num_safe
#             # print(is_phishing)
#
#             result_message = "Phishing URL detected!" if is_phishing else "URL is safe"
#
#             return jsonify({"message": result_message, "predictions": results})
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
#     else:
#         return jsonify({"error": "Method not allowed"}), 405
#
# if __name__ == '__main__':
#     app.run(host='192.168.1.12', debug=True)
