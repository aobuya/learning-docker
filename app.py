from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_KEY = '9e6b16500amsh87f6e6039041672p1f7721jsn0d66bfad716f'
RAPIDAPI_HOST = 'open-weather13.p.rapidapi.com'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    location = request.form.get('location')
    print(f"Received location: {location}")  # Debugging: Print location
    weather_data, error_message = fetch_weather(location)
    print(f"Weather data: {weather_data}")  # Debugging: Print weather data
    if weather_data:
        return render_template('index.html', weather=weather_data, location=location)
    else:
        return render_template('index.html', error=error_message)

def fetch_weather(location):
    url = f"https://open-weather13.p.rapidapi.com/city/{location}/EN"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    print(f"Making API request to: {url}")  # Debugging: Print URL
    response = requests.get(url, headers=headers)
    print(f"API response status code: {response.status_code}")  # Debugging: Print status code
    print(f"API response text: {response.text}")  # Debugging: Print response text
    if response.status_code == 200:
        return response.json(), None
    else:
        return None, f"Error {response.status_code}: {response.text}"

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test endpoint working"})

if __name__ == '__main__':
    app.run(debug=True, port=8081)
