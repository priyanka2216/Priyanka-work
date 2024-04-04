from flask import Flask, request, jsonify
from flask_cors import CORS
from url_checker import check_url_for_phishing

app = Flask(__name__)
CORS(app)

@app.route('/CheckUrl/<string:url>', methods=['POST'])
def check_url(url):
    print("Received URL:", url)
    
    # Call check_url_for_phishing to get predictions
    svm_prediction, rf_prediction = check_url_for_phishing(url)

    if svm_prediction == 1 or rf_prediction == 1:
        message = "Phishing URL detected!"
    else:
        message = "URL received successfully"

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
