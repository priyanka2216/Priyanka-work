from flask import Flask, request, jsonify
from flask_cors import CORS
from url_checker import check_url_for_phishing

app = Flask(__name__)
CORS(app)

@app.route('/CheckUrl', methods=['POST'])
def check_url():
    try:
        # Call check_url_for_phishing to get predictions and probabilities
        url = request
        svm_prediction, rf_prediction, dt_prediction, svm_proba, rf_proba, dt_proba = check_url_for_phishing(url)

        if svm_prediction == 1 or rf_prediction == 1 or dt_prediction == 1:
            message = "Phishing URL detected!"
        else:
            message = "URL is safe "

        response_data = {
            "message": message,
            "svm_probability": svm_proba.tolist()[0] if svm_proba is not None else None,
            "rf_probability": rf_proba.tolist()[0] if rf_proba is not None else None,
            "dt_probability": dt_proba.tolist()[0] if dt_proba is not None else None
        }
        status_code = 200  # Success
    except Exception as e:
        response_data = {
            "message": "Error processing URL: " + str(e),
            "svm_prediction": None,
            "svm_probability": None,
            "rf_probability": None,
            "dt_probability": None
        }
        status_code = 500  # Internal Server Error

    return jsonify(response_data), status_code

if __name__ == "__main__":
    app.run(debug=True)
