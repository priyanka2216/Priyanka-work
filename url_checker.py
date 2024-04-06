from sklearn.preprocessing import StandardScaler
from urllib.parse import urlparse
import re

from TrainModels import scaler, svm_model, rf_model ,dt_model

def extract_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    
    features = {}
    # Assign numerical values directly where applicable
    features['Index'] = 1  # Example numerical value
    features['UsingIP'] = bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))
    features['LongURL'] = int(len(url) > 75)
    features['ShortURL'] = int(len(url) < 25)
    features['Symbol@'] = int('@' in url)
    features['Redirecting//'] = int('//' in url)
    features['PrefixSuffix-'] = int('-' in domain)
    features['SubDomains'] = domain.count('.')
    features['HTTPS'] = int(parsed_url.scheme == 'https')
    features['DomainRegLen'] = len(parsed_url.netloc)
    features['Favicon'] = int('favicon' in url.lower())
    features['NonStdPort'] = int(':' in parsed_url.netloc)
    features['HTTPSDomainURL'] = int('https' in domain)
    features['RequestURL'] = int('request' in path.lower())
    features['AnchorURL'] = int('#' in url)
    features['LinksInScriptTags'] = int('<script>' in url.lower())
    features['ServerFormHandler'] = int('server' in path.lower() and 'form' in path.lower())
    features['InfoEmail'] = int('info@' in url)
    features['AbnormalURL'] = int(any(char.isdigit() for char in domain))
    features['WebsiteForwarding'] = int('forwarding' in path.lower())
    features['StatusBarCust'] = int('status' in path.lower())
    features['DisableRightClick'] = int('rightclick' in path.lower())
    features['UsingPopupWindow'] = int('popup' in path.lower())
    features['IframeRedirection'] = int('iframe' in path.lower())
    features['AgeofDomain'] = int(len(parsed_url.netloc.split('.')) > 1)
    features['DNSRecording'] = int('dns' in path.lower())
    features['WebsiteTraffic'] = int('traffic' in path.lower())
    features['PageRank'] = int('pagerank' in path.lower())
    features['GoogleIndex'] = int('google' in domain)
    features['LinksPointingToPage'] = int('link' in path.lower())
    features['StatsReport'] = int('stats' in path.lower())

    return features

def preprocess_features(features):
    # Convert numerical features to list
    feature_values = [features[feature] for feature in features]
    scaled_features = scaler.transform([feature_values])
    return scaled_features

def check_url_for_phishing(url):
    features = extract_features(url)
    scaled_features = preprocess_features(features)
    # Make predictions using SVM, Random Forest, and Decision Tree models
    svm_prediction = svm_model.predict(scaled_features)[0]
    rf_prediction = rf_model.predict(scaled_features)[0]
    dt_prediction = dt_model.predict(scaled_features)[0]
    return svm_prediction, rf_prediction, dt_prediction
