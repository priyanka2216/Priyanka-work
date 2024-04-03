from flask import Flask, request, jsonify
from flask_cors import CORS
from url_checker import check_url_for_phishing  # Import the check_url_for_phishing function

app = Flask(__name__)
CORS(app)

@app.route('/CheckUrl/<string:url>', methods=['POST'])
def check_url(url):
    print("Received URL:", url)

    # Call the check_url_for_phishing function from url_checker.py
    is_phishing = check_url_for_phishing(url)

    if is_phishing:
        message = "Phishing URL detected!"
    else:
        message = "URL received successfully"

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
