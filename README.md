# 🌤️ Dynamic Weather Dashboard ☔️ (Flask-Based Weather Application)

## 📖 Table of Contents 📖

- [Project Intro](#project-intro)
- [Project Structure](#project-structure)
- [Application Features](#application-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation Process](#installation-process)
- [User Guides](#user-guides)
  - [Application Usage](#application-usage)
- [Code Explanation](#code-explanation)
- [Incorporating Docker](#incorporating-docker)
- [Common Issues and Solutions](#common-issues-and-solutions)
- [Potential Future Improvements](#potential-future-improvements)
- [How to Contribute](#how-to-contribute)
- [License](#license)
- [Contact Information](#contact-information)

## 👨🏾‍💻 Project Intro

This Weather Dashboard is a Flask-based web application that provides users with real-time weather information for multiple cities. The application uses the OpenWeather API to fetch current weather data and displays it in an easy-to-read format. Users can search for cities, track extreme weather events, and maintain a history of their searches.

Overall, the project demonstrates how to integrate various technologies and services, including:

- Python programming 🐍
- API integration (OpenWeather) ⛈️
- Environment variable management 🌱
- Web application development, with Flask 🌐
- Session management and caching 💾
- Docker containerization ⚓️

And aims to provide the user valuable insight, whether you're a developer learning more about Python and web development (like myself), or someone who simply likes to nerd out about the weather!

## ⚙️ Project Structure

```
dynamic-weather-dashboard/
│
├── weather_dashboard.py        # Main application file
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── static/                     # Static files
│   ├── css/
│   │   └── styles.css          # CSS styling
│   ├── js/
│   │   └── script.js           # JavaScript functionality
│   └── images/                 # Image assets
│
└── templates/                  # HTML templates
    ├── base.html               # Base template with common elements
    ├── home.html               # Home page template
    └── search_results.html     # Search results template
```

## ⚡️ Application Features

- **Real-time Weather Data**: Get current weather conditions for any city (temperature (°F), humidity, wind speed, and various weather conditions). Also includes timestamp information for all weather data
- **Search Functionality**: Quick and intuitive city search
- **Multi-City Dashboard**: Track weather for multiple cities simultaneously
- **Regional Weather Highlights**: View weather highlights for specific regions and different continents
- **Extreme Weather Tracking**: Monitor cities experiencing extreme weather conditions (hottest, coldest, windiest, most humid)
- **User History**: Session-based tracking of your search history, for easy reference
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **City Removal**: Easily remove cities from your dashboard

## 🛠️ Getting Started

### 🔖 Prerequisites

- Python 3.7+
- Flask
- OpenWeather API key
- Git (for cloning the repository)

### 💾 Installation Process

1. Clone the repository:
```bash
git clone https://github.com/fpier042/dynamic-weather-dashboard.git
cd dynamic-weather-dashboard
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```
OPENWEATHER_API_KEY=your_openweather_api_key
SECRET_KEY=your_secret_key_for_flask_sessions
```

5. Run the application:
```bash
python weather_dashboard.py
```

6. Open your browser and navigate to http://localhost:5000

## 📘 User Guides

And here are some general resources to provide you further context and ground you as you move through the project:

- OpenWeather API Documentation: [https://openweathermap.org/api/one-call-api] 
- Flask Documentation: [https://flask.palletsprojects.com/en/stable/]
- Python Requests Library, for API calls: [https://docs.python-requests.org/en/latest/]
- Docker Installation Guide: [https://docs.docker.com/get-started/get-docker/]

### 🔋 Application Usage

1. **Home Page**: Upon loading, you'll see the dashboard with any previously saved cities
2. **Adding Cities**: Use the search bar at the top to find and add new cities
3. **City Weather Cards**: Each city is displayed as a card with the following information:
   - City name and country
   - Current temperature
   - Weather condition with icon
   - Humidity, wind speed, and pressure
4. **Removing Cities**: Click the "X" button on any city card to remove it from your dashboard
5. **Regional Weather**: Explore weather highlights by region
6. **Extreme Weather**: View cities experiencing extreme weather conditions
7. **Weather History**: Track the cities you've searched for in your current session

## 📝 Code Explanation 📝

### weather_dashboard.py
This is the core of the application. Its main components are:

#### WeatherService class:
- Initializes the API key
- Handles weather data fetching from OpenWeather API
- Formats response data with timestamps

#### Helper functions:
- get_random_cities: Selects random cities for display
- fetch_weather_data: Retrieves weather information for multiple cities
- get_weather_highlights: Gets weather data by geographical region
- get_extreme_weather: Identifies cities with extreme weather conditions

#### Flask application routes:
- /: Home route displaying dashboard with regional highlights, random cities, and extreme weather
- /search: Handles city search and displays results
- /refresh: Refreshes the dashboard data
- /remove_city: Removes a city from search history

#### Session management:
- Stores user's search history
- Caches dashboard data temporarily
- Maintains user preferences across requests

The application uses:
- Flask sessions to store user data temporarily
- The OpenWeather API to fetch current weather data
- Bootstrap for responsive styling
- JavaScript for dynamic interactions

## ⚓️ Incorporating Docker

To containerize this application with Docker:

1. Create a `Dockerfile` in the root directory:
```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=weather_dashboard.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
```

2. Build and run the Docker container:
```bash
docker build -t weather-dashboard .
docker run -p 5000:5000 --env-file .env weather-dashboard
```

## 🚧 Common Issues and Solutions 🚧

### API Key Issues
**Problem**: "Unable to fetch weather data" error message.
**Solution**: Verify your OpenWeather API key in the `.env` file is correct and activated.

### City Not Found
**Problem**: Search returns "City not found" error.
**Solution**: Check the spelling of the city name or try adding the country code (e.g., "London,UK").

### Session Storage
**Problem**: Cities disappear after server restart.
**Solution**: This is expected behavior as the app uses session storage. For persistent storage, consider implementing a database solution.

### API Key Configuration
**Problem**: OpenWeather API key is not recognized.
**Solution**: Double-check your .env file contains the correct API key and is properly loaded.

### Flask Application Not Accessible
**Problem**: Cannot access the web interface after starting the application.
**Solution**: Check that you're using the correct port and that no other applications are using it.

### Weather Data Not Loading
**Problem**: Weather information not displaying or showing errors.
**Solution**: Check your internet connection and verify the OpenWeather API service status.

## 🛸 Potential Future Improvements

- Implement weather forecast data for upcoming days
- Add weather maps and radar visualization
- Create user accounts for personalized experiences
- Add support for different temperature units (°C/°F)
- Implement geolocation to automatically detect the user's city
- Add weather alerts and notifications
- Create mobile-responsive design for better experience on smartphones
- Implement dark/light mode toggle
- Add historical weather data charts and trends
- Integrate with additional weather APIs for more comprehensive data

## 🫱🏻‍🫲🏾 How to Contribute

Contributions are what allow for the open-source community to serve as a valuable resource for developers to learn various tools, inspire others, and create their best work

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🪪 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📲 Contact Information

Felton Pierre: Linkedin [www.linkedin.com/in/felton-pierre-90]

Project Link: https://github.com/fpier042/dynamic-weather-dashboard/
