from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "c12c00ca2fae6a11009ce36f6d0f6720"
    api_endpoint = "https://api.weatherstack.com/current"
    params = {"access_key": api_key, "query": city}
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch weather data."}

@app.route('/')
def index():
    return 'Hello, please go to /weather to check weather.'

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if city:
        weather_data = get_weather(city)
        return jsonify(weather_data)
    else:
        return 'Please provide a city parameter.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
