# url_checker.py

def check_url_for_phishing(url):
    if "phishing" in url.lower():
        return True
    else:
        return False
