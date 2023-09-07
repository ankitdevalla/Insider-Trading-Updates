from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow all origins. In production, you should configure CORS more securely.

@app.route('/')
def get_stocks():
    url = "https://mboum-finance.p.rapidapi.com/v1/sec/form4"
    headers = {
        "X-RapidAPI-Key": "81c06f3ee5msh1a81ae8f9624681p179a68jsn3bc9bf3b7556",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    stocks = data['form_4_filings'][:20]
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
