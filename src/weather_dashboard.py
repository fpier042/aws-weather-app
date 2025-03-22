import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template_string

app = Flask(__name__)

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
