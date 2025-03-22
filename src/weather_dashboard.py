import os
import json
import requests
import random
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, jsonify, redirect, url_for

load_dotenv()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.getenv('SECRET_KEY', 'dev_secret_key')

POPULAR_CITIES = [
    "New York", "London", "Tokyo", "Paris", "Sydney", "Berlin", "Toronto", 
    "Rome", "Madrid", "Dubai", "Singapore", "Hong Kong", "Bangkok", "Istanbul",
    "Moscow", "Beijing", "Seoul", "Mexico City", "Rio de Janeiro", "Cairo",
    "Mumbai", "Cape Town", "Buenos Aires", "San Francisco", "Chicago", "Seattle",
    "Miami", "Boston", "Philadelphia", "Dallas", "Austin", "Denver", "Atlanta",
    "Las Vegas", "Vancouver", "Montreal", "Amsterdam", "Vienna", "Stockholm",
    "Prague", "Barcelona", "Lisbon", "Athens", "Dublin", "Helsinki", "Zurich",
    "Auckland", "Jerusalem", "Honolulu", "Havana"
]

WEATHER_REGIONS = {
    "North America": ["New York", "Chicago", "Los Angeles", "Toronto"],
    "Europe": ["London", "Paris", "Berlin", "Rome"],
    "Asia": ["Tokyo", "Beijing", "Singapore", "Mumbai"],
    "Oceania": ["Sydney", "Auckland", "Melbourne", "Wellington"],
    "Africa": ["Cairo", "Cape Town", "Nairobi", "Lagos"],
    "South America": ["Rio de Janeiro", "Buenos Aires", "Lima", "Santiago"]
}

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            raise ValueError("Missing OPENWEATHER_API_KEY")
    
    def fetch_weather(self, city):
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": self.api_key, "units": "imperial"}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {city}: {e}")
            return {"error": str(e), "city": city}

weather_service = WeatherService()

def get_random_cities(count=4):
    return random.sample(POPULAR_CITIES, min(count, len(POPULAR_CITIES)))

def fetch_weather_data(cities):
    return [weather_service.fetch_weather(city) for city in cities]

def get_weather_highlights():
    highlights = {}
    for region, cities in WEATHER_REGIONS.items():
        city = random.choice(cities)
        weather_data = weather_service.fetch_weather(city)
        if weather_data and "error" not in weather_data:
            highlights[region] = weather_data
    return highlights

def get_extreme_weather():
    sample_cities = [city for cities in WEATHER_REGIONS.values() for city in cities[:2]]
    all_weather = [d for d in fetch_weather_data(sample_cities) if "error" not in d]
    if not all_weather:
        return {}
    return {
        "hottest": max(all_weather, key=lambda x: x.get('main', {}).get('temp', -999)),
        "coldest": min(all_weather, key=lambda x: x.get('main', {}).get('temp', 999)),
        "windiest": max(all_weather, key=lambda x: x.get('wind', {}).get('speed', -999)),
        "most_humid": max(all_weather, key=lambda x: x.get('main', {}).get('humidity', -999))
    }

@app.route('/')
def home():
    # Always get fresh extreme weather data
    extreme_weather = get_extreme_weather()
    
    if 'random_cities' not in session:
        session['random_cities'] = get_random_cities()
    if 'region_highlights' not in session:
        session['region_highlights'] = get_weather_highlights()
    
    current_time = datetime.now().strftime('%A, %B %d, %Y %I:%M %p')
    return render_template(
        'home.html',
        current_time=current_time,
        random_cities=session['random_cities'],
        region_highlights=session['region_highlights'],
        extreme_weather=extreme_weather  # Use the freshly generated data
    )

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        city = request.args.get('city', '').strip()
    else:
        city = request.form.get('city', '').strip()
    if not city:
        return redirect(url_for('home'))
    
    weather_data = fetch_weather_data([city])
    if 'cities' not in session:
        session['cities'] = []
    if city.lower() not in [c.lower() for c in session['cities']]:
        session['cities'].append(city)
        if len(session['cities']) > 8:
            session['cities'].pop(0)
    
    city_weather_data = fetch_weather_data([c for c in session['cities'] if c.lower() != city.lower()])
    current_time = datetime.now().strftime('%A, %B %d, %Y %I:%M %p')
    return render_template(
        'search_results.html',
        city=city,
        weather=weather_data[0] if weather_data else None,
        city_weather_data=city_weather_data,
        random_cities=session.get('random_cities', get_random_cities()),
        current_time=current_time
    )

@app.route('/refresh')
def refresh():
    session.pop('region_highlights', None)
    session.pop('random_cities', None)
    return redirect(url_for('home'))

@app.route('/remove_city/<city>', methods=['POST'])
def remove_city(city):
    if 'cities' in session and city in session['cities']:
        session['cities'].remove(city)
        session.modified = True
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.template_filter('now')
def filter_now(format_string):
    return datetime.now().strftime(format_string) if format_string != 'year' else datetime.now().year

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)