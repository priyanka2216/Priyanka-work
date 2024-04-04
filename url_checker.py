from operator import index
from sklearn.preprocessing import StandardScaler
from urllib.parse import urlparse
import re

from TrainModels import scaler, svm_model, rf_model

def extract_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    
    features = {}
    features['Index'] = index
    features['UsingIP'] = bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))
    features['LongURL'] = len(url) > 75
    features['ShortURL'] = len(url) < 25
    features['Symbol@'] = '@' in url
    features['Redirecting//'] = '//' in url
    features['PrefixSuffix-'] = '-' in domain
    features['SubDomains'] = domain.count('.')
    features['HTTPS'] = parsed_url.scheme == 'https'
    features['DomainRegLen'] = len(parsed_url.netloc)
    features['Favicon'] = 'favicon' in url.lower()
    features['NonStdPort'] = ':' in parsed_url.netloc
    features['HTTPSDomainURL'] = 'https' in domain
    features['RequestURL'] = 'request' in path.lower()
    features['AnchorURL'] = '#' in url
    features['LinksInScriptTags'] = '<script>' in url.lower()
    features['ServerFormHandler'] = 'server' in path.lower() and 'form' in path.lower()
    features['InfoEmail'] = 'info@' in url
    features['AbnormalURL'] = any(char.isdigit() for char in domain)
    features['WebsiteForwarding'] = 'forwarding' in path.lower()
    features['StatusBarCust'] = 'status' in path.lower()
    features['DisableRightClick'] = 'rightclick' in path.lower()
    features['UsingPopupWindow'] = 'popup' in path.lower()
    features['IframeRedirection'] = 'iframe' in path.lower()
    features['AgeofDomain'] = len(parsed_url.netloc.split('.')) > 1
    features['DNSRecording'] = 'dns' in path.lower()
    features['WebsiteTraffic'] = 'traffic' in path.lower()
    features['PageRank'] = 'pagerank' in path.lower()
    features['GoogleIndex'] = 'google' in domain
    features['LinksPointingToPage'] = 'link' in path.lower()
    features['StatsReport'] = 'stats' in path.lower()

    return features

def preprocess_features(features):
    feature_values = [int(features[feature]) for feature in features]
    scaled_features = scaler.transform([feature_values])
    return scaled_features

def check_url_for_phishing(url):
    features = extract_features(url)
    scaled_features = preprocess_features(features)
    # Make predictions using SVM and Random Forest models
    svm_prediction = svm_model.predict(scaled_features)[0]
    rf_prediction = rf_model.predict(scaled_features)[0]
    return svm_prediction, rf_prediction
