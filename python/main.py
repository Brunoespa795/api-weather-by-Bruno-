from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_response(question):
    api_key = "bc5018a6325c8e4268f85617f400bd22"
    api_endpoint = "http://api.weatherstack.com/current"
    params = {"query": question, "access_key": api_key}

    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch response."}

@app.route('/')
def index():
    return 'Hello, please go to /ask to ask a question.'

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form.get('question')
    elif request.method == 'GET':
        question = request.args.get('question')
    else:
        return 'Unsupported method.'

    if question:
        response = get_response(question)
        return jsonify(response)
    else:
        return 'Please provide a question.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
