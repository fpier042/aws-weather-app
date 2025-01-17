import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

class WeatherDashboard:
    def validate_api_key(self):
        """Validating the OpenWeather API key by making a test call"""
        test_url = "http://api.openweathermap.org/data/2.5/weather"
        test_params = {"q": "London", "appid": self.api_key, "units": "imperial"}

        try:
            response = requests.get(test_url, params=test_params)
            if response.status_code == 401:  # Invalid API key
                print("Invalid OpenWeather API Key. Please check your .env file.")
                return False
            elif response.status_code == 200:
                print("OpenWeather API Key is valid.")
                return True
            else:
                print(f"Unexpected response while validating API key: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error validating API key: {e}")
            return False


    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
@@ -69,6 +90,10 @@ def save_to_s3(self, weather_data, city):

def main():
    dashboard = WeatherDashboard()

    # Validate the OpenWeather API Key
    if not dashboard.validate_api_key():
        return  # Exit if API key is invalid

    # Create bucket if needed
    dashboard.create_bucket_if_not_exists()
    
    cities = ["Philadelphia", "Seattle", "New York"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = dashboard.fetch_weather(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
            
            # Save to S3
            success = dashboard.save_to_s3(weather_data, city)
            if success:
                print(f"Weather data for {city} saved to S3!")
        else:
            print(f"Failed to fetch weather data for {city}")
if __name__ == "__main__":
    main()
