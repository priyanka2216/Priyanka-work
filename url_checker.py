from urllib.parse import urlparse
import re
import numpy as np
#import whois

from TrainModels import scaler, svm_model, rf_model, dt_model, lr_model

def using_ip(domain):
    return int(bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain)))

# 2. Check if the URL length is greater than 75 characters
def long_url(url):
    length = len(url)
    if (length < 54):
        return -1
    elif (54 <= length <= 75):
        return 0
    else:
        return 1

# 3. Check if the URL length is less than 15 characters
def short_url(url):
    return 0

import regex

# 4. Check if '@' symbol is present in the URL
def symbol_at(url):
    symbol = regex.findall(r'@', url)
    if (len(symbol) == 0):
        return -1
    else:
        return 1

# 5. Check if the URL length is above 25 characters
def long_url_above_25(url):
    return int(len(url) > 54)

# 6. Check if the domain contains a prefix or suffix '-'
def prefix_suffix(domain):
    if '-' in domain:
        return -1
    else:
        return 1

# 7. Count the number of subdomains in the domain
def subdomains(domain):
    if '.' in domain:
        return domain.count('.')
    else:
        return 0

# 8. Check if the URL scheme is HTTPS
def https(scheme):
    if int(scheme == 'https'):
        return 1
    else:
        return -1

# 9. Calculate the length of the domain
def domain_reg_len(netloc):
    return len(netloc)

# 10. Check if 'favicon' is present in the URL
def favicon(url):
    return int('favicon' in url.lower())

# 11. Check if the domain contains a non-standard port
def non_std_port(netloc):
    return int(':' in netloc)

# 12. Check if the domain contains 'https'
def https_domain_url(domain):
    return int('https' in domain)

# 13. Check if 'request' is present in the URL path
def request_url(path):
    return int('request' in path.lower())

# 14. Check if '#' is present in the URL
def anchor_url(url):
    return int('#' in url)

# 15. Check if '<script>' is present in the URL
def links_in_script_tags(url):
    return int('<script>' in url.lower())

# 16. Check if 'server' and 'form' are present in the URL path
def server_form_handler(path):
    return int('server' in path.lower() and 'form' in path.lower())

# 17. Check if 'info@' is present in the URL
def info_email(url):
    return int('info@' in url)

# 18. Check if the domain contains any digits
def abnormal_url(domain):
    return int(any(char.isdigit() for char in domain))

# 19. Check if 'forwarding' is present in the URL path
def website_forwarding(path):
    return int('forwarding' in path.lower())

# 20. Check if 'status' is present in the URL path
def status_bar_cust(path):
    return int('status' in path.lower())

# 21. Check if 'rightclick' is present in the URL path
def disable_right_click(path):
    return int('rightclick' in path.lower())

# 22. Check if 'popup' is present in the URL path
def using_popup_window(path):
    return int('popup' in path.lower())

# 23. Check if 'iframe' is present in the URL path
def iframe_redirection(path):
    return int('iframe' in path.lower())

# 24. Check if the domain has more than one part
def age_of_domain(netloc):
    return int(len(netloc.split('.')) > 1)

# 25. Check if 'dns' is present in the URL path
def dns_recording(path):
    return int('dns' in path.lower())

# 26. Check if 'traffic' is present in the URL path
def website_traffic(path):
    return int('traffic' in path.lower())

# 27. Check if 'pagerank' is present in the URL path
def page_rank(path):
    return int('pagerank' in path.lower())

# 28. Check if 'google' is present in the domain
def google_index(domain):
    return int('google' in domain)

# 29. Check if 'link' is present in the URL path
def links_pointing_to_page(path):
    if int('link' in path.lower()):
        return 1
    else:
        return -1

# 30. Check if 'stats' is present in the URL path
def stats_report(path):
    if 'stats' in path.lower():
        return 1
    else:
        return -1


def getDepth(url):
  s = urlparse(url).path.split('/')
  depth = 0
  for j in range(len(s)):
    if len(s[j]) != 0:
      depth = depth+1
  return depth

# Function to extract features
def extract_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    features = {
        'UsingIP': using_ip(domain),
        'LongURL': long_url(url),
        'ShortURL': short_url(url),
        'Symbol@': symbol_at(url),
        'LongURLAbove25': long_url_above_25(url),
        'PrefixSuffix-': prefix_suffix(domain),
        'SubDomains': subdomains(domain),
        'HTTPS': https(parsed_url.scheme),
        'DomainRegLen': domain_reg_len(parsed_url.netloc),
        'Favicon': favicon(url),
        'NonStdPort': non_std_port(parsed_url.netloc),
        'HTTPSDomainURL': https_domain_url(domain),
        'RequestURL': request_url(path),
        'AnchorURL': anchor_url(url),
        'LinksInScriptTags': links_in_script_tags(url),
        'ServerFormHandler': server_form_handler(path),
        'InfoEmail': info_email(url),
        'AbnormalURL': abnormal_url(domain),
        'WebsiteForwarding': website_forwarding(path),
        'StatusBarCust': status_bar_cust(path),
        'DisableRightClick': disable_right_click(path),
        'UsingPopupWindow': using_popup_window(path),
        'IframeRedirection': iframe_redirection(path),
        'AgeofDomain': age_of_domain(parsed_url.netloc),
        'DNSRecording': dns_recording(path),
        'WebsiteTraffic': website_traffic(path),
        'PageRank': page_rank(path),
        'GoogleIndex': google_index(domain),
        'LinksPointingToPage': links_pointing_to_page(path),
        'StatsReport': stats_report(path),
        'getDepth' : getDepth(url)
    }
    print(features)
    return features

def preprocess_features(features):
    # Convert features to list in the same order as the model expects
    feature_values = [features[feature] for feature in features]
    print("$$$$$$$$$$$$$$$$$$")
    print(feature_values)
    arr = np.array(feature_values).reshape(1, -1)
    print("$$$$$$$$$$$$$$$$$$")
    return arr


def check_url_for_phishing(url):
    features = extract_features(url)
    scaled_features = preprocess_features(features)
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(scaled_features)

    svm_prediction = svm_model.predict(scaled_features)[0]
    print(svm_prediction)
    rf_prediction = rf_model.predict(scaled_features)[0]
    print(rf_prediction)

    dt_prediction = dt_model.predict(scaled_features)[0]
    print(dt_prediction)
    print("@@@@@@@@@%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@")
    svm_proba = svm_model.predict_proba(scaled_features)[0] if hasattr(svm_model, 'predict_proba') else None
    rf_proba = rf_model.predict_proba(scaled_features)[0]
    dt_proba = dt_model.predict_proba(scaled_features)[0]

    print("****************************")
    print("SVM Probability:", svm_proba)
    print("RF Probability:", rf_proba)
    print("DT Probability:", dt_proba)
    print("****************************")
    return svm_prediction, rf_prediction, dt_prediction, svm_proba, rf_proba, dt_proba

def check_phishing(url):
    print("Checking URL:", url)
    svm_prediction, rf_prediction, dt_prediction, svm_proba, rf_proba, dt_proba = check_url_for_phishing(url)

    results = {
        'SVM Prediction': svm_prediction,
        'RF Prediction': rf_prediction,
        'DT Prediction': dt_prediction,
        'SVM Probability': svm_proba,
        'RF Probability': rf_proba,
        'DT Probability': dt_proba
    }
    # print('************************************')
    print("Results:", results)
    # print('********************')
    return results


#===============here is existing code=================
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
#     domain = parsed_url.netloc
#     path = parsed_url.path
#
#     features = {}
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
#
#     # Add missing features with default value 0
#     missing_features = set(range(30)) - set(features.keys())
#     for feature in missing_features:
#         features[feature] = 0
#
#     return features
#
# def preprocess_features(features):
#     return [features[feature] for feature in range(30)]
#
# def check_phishing(url):
#     features = extract_features(url)
#     X_predict = preprocess_features(features)
#
#     svm_rbf_prediction = svm_rbf.predict([X_predict])[0].item()  # Convert int64 to regular integer
#   # Convert int64 to regular integer
#     dt_prediction = dt.predict([X_predict])[0].item()  # Convert int64 to regular integer
#     rf_prediction = rf.predict([X_predict])[0].item()  # Convert int64 to regular integer
#
#     return {
#         'SVM (RBF Kernel)': svm_rbf_prediction,
#         'Decision Tree': dt_prediction,
#         'Random Forest': rf_prediction
#     }
#
# @app.route('/check_url', methods=['POST'])
# def check_url():
#     try:
#         data = request.get_json()
#         if 'url' not in data:
#             return jsonify({"error": "URL attribute missing"}), 400
#
#         url = data['url']
#         results = check_phishing(url)
#
#         # Determine if the majority of models predict phishing or safe
#         num_phishing = sum(results.values())
#         num_safe = len(results) - num_phishing
#         is_phishing = num_phishing > num_safe
#
#         result_message = "Phishing URL detected!" if is_phishing else "URL is safe"
#
#         # Print accuracy of each model in the terminal
#         svm_rbf_accuracy = results['SVM (RBF Kernel)']
#         dt_accuracy = results['Decision Tree']
#         rf_accuracy = results['Random Forest']
#         print("SVM (RBF Kernel) Accuracy:", svm_rbf_accuracy)
#         print("Decision Tree Accuracy:", dt_accuracy)
#         print("Random Forest Accuracy:", rf_accuracy)
#
#         return jsonify({"message": result_message, "predictions": results})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)