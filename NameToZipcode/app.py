from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/zipcode/<state_name>/<city_name>")
def get_zip_code(state_name, city_name):
    result = requests.get(f'https://api.zippopotam.us/us/{state_name}/{city_name}').json()
    zip_codes = [place['post code'] for place in result['places']]
    zip_code = zip_codes[0] 
    # f"http://hn_weather:8600/weather/{zip_code}"
    weather_url = f"http://hn_weather:8600/weather/{zip_code}"
    weather_res = requests.get(weather_url)
    if weather_res.status_code == 200:
        return f"{weather_res.text}"
    else:
        return f"Request failed with status code: {weather_res.status_code}"
     
    #try:
    #    return f"{zip_codes[0]}"
    #except KeyError:
    #    return f"No zipcode found for {city_name}"
    # Use a free API like the OpenCage API to convert city name to zip code
    #API_KEY = "0179fc6cf2ac46d6b4a9f43c6ab2a8bb"
    #API_URL = f"https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={API_KEY}"
    #response = requests.get(API_URL)
    #data = response.json()
    
    # If there are no results for the given city name, return an error message
    #if len(data["results"]) == 0:
    #    return jsonify({"error": "No results found for the given city name"}), 400

    # Extract the zip code from the first result
    #zip_code = data["results"]
    #return jsonify({"zip_code": zip_code})

if __name__ == "__main__":
    app.run(debug=True, port="5000")
