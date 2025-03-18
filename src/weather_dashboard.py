import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template_string

app = Flask(__name__)

class WeatherDashboard:
    def __init__(self):
        required_vars = [
            'OPENWEATHER_API_KEY', 'AWS_BUCKET_NAME', 
            'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_DEFAULT_REGION'
        ]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_DEFAULT_REGION')
        )

    def create_bucket_if_not_exists(self):
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} exists")
        except self.s3_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                print(f"Creating bucket {self.bucket_name}")
                self.s3_client.create_bucket(Bucket=self.bucket_name)
            else:
                print(f"Error checking bucket: {e}")

    def fetch_weather(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": self.api_key, "units": "imperial"}
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data for {city}: {e}")
            return {"error": str(e)}

    def save_to_s3(self, weather_data, city):
        if not weather_data or "error" in weather_data:
            return False
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"
        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved JSON data for {city} to S3")
            return True
        except Exception as e:
            print(f"Error saving JSON to S3: {e}")
            return False

    def generate_html(self, weather_data_list):
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Weather Dashboard</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                table { border-collapse: collapse; width: 100%; max-width: 800px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>Weather Dashboard</h1>
            <table>
                <tr>
                    <th>City</th>
                    <th>Temperature (°F)</th>
                    <th>Feels Like (°F)</th>
                    <th>Humidity (%)</th>
                    <th>Conditions</th>
                    <th>Timestamp</th>
                </tr>
        """
        for data in weather_data_list:
            if "error" not in data:
                city = data.get('name', 'Unknown')
                temp = data['main'].get('temp', 'N/A')
                feels_like = data['main'].get('feels_like', 'N/A')
                humidity = data['main'].get('humidity', 'N/A')
                description = data['weather'][0].get('description', 'N/A') if data.get('weather') else 'N/A'
                timestamp = data.get('timestamp', 'N/A')
                html_content += f"""
                <tr>
                    <td>{city}</td>
                    <td>{temp}</td>
                    <td>{feels_like}</td>
                    <td>{humidity}</td>
                    <td>{description}</td>
                    <td>{timestamp}</td>
                </tr>
                """
        html_content += """
            </table>
        </body>
        </html>
        """
        return html_content

    def save_html_to_s3(self, html_content):
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-dashboard-{timestamp}.html"
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=html_content.encode('utf-8'),
                ContentType='text/html'
            )
            print(f"Successfully saved HTML dashboard to S3 as {file_name}")
            return True
        except Exception as e:
            print(f"Error saving HTML to S3: {e}")
            return False

def fetch_and_save():
    dashboard = WeatherDashboard()
    dashboard.create_bucket_if_not_exists()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cities_file = os.path.join(script_dir, '..', 'data', 'cities.json')
    try:
        with open(cities_file) as file_input:
            data = json.load(file_input)
            cities = data['cities']
    except (FileNotFoundError, json.JSONDecodeError):
        print("cities.json not found or invalid, using default cities")
        cities = ["Philadelphia", "Seattle", "New York"]

    weather_data_list = []
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = dashboard.fetch_weather(city)
        if weather_data and "error" not in weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
            dashboard.save_to_s3(weather_data, city)
        weather_data_list.append(weather_data)

    html_content = dashboard.generate_html(weather_data_list)
    dashboard.save_html_to_s3(html_content)
    return weather_data_list

@app.route('/')
def display_weather():
    weather_data_list = fetch_and_save()
    html = """
    <h1>Weather Dashboard</h1>
    <table border="1">
        <tr><th>City</th><th>Temp (°F)</th><th>Feels Like (°F)</th><th>Humidity (%)</th><th>Conditions</th></tr>
        {% for data in weather_data %}
            {% if "error" not in data %}
                <tr>
                    <td>{{ data.name }}</td>
                    <td>{{ data.main.temp }}</td>
                    <td>{{ data.main.feels_like }}</td>
                    <td>{{ data.main.humidity }}</td>
                    <td>{{ data.weather[0].description }}</td>
                </tr>
            {% endif %}
        {% endfor %}
    </table>
    """
    return render_template_string(html, weather_data=weather_data_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
