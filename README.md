# 🌤️ AWS (Amazon Web Services) Weather Dashboard ☔️ (30 Days Dev Ops Challenge)

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
- [Contact](#contact)

## 👨🏾‍💻 Project Intro

The following code is for an interactive Python web application allowing users to fetch and display current (real-time and location-based) weather data for multiple cities. It utilizes the OpenWeather API (application programming interface) to retrieve factual weather information, stores this data in an AWS S3 bucket, and also generates an HTML file of this data.

This project taught me (and demonstrates to other learners) how to integrate various technologies and services, including:

- Python programming 🐍
- API integration (OpenWeather) ⛈️
- AWS services (IAM, S3) 🚚
- Environment variable management 🌱
- Web application development, with Flask 🌐
- Docker containerization ⚓️

And aims to provide the user valuable insight into how best to create a functional, cloud-integrated application, whether you're a developer learning more about Python and AWS (like myself), or someone who simply likes to nerd out about the weather!

## ⚙️ Project Structure

The project, overall, is organized as follows:

```
└── ./
    ├── weather_dashboard.py  # Main Flask application
    ├── data
    │   └── cities.json      # Default cities configuration 
    ├── .env                 # Environment variables
    ├── Dockerfile           # For Docker containerization
    └── requirements.txt     # Python dependencies required
```

## ⚡️Application Features

- Retrieves real-time weather data for multiple cities
- Displays temperature (°F), feels-like temperature, humidity, and various weather conditions
- Automatically stores the weather data in the user's AWS S3 bucket
- Provides a simple web interface to view the current weather data
- Generates and saves an HTML dashboard to S3 for future reference
- Supports weather tracking across multiple cities (configurable via cities.json)
- Provides a timestamp for all data, to assist the user with keeping track of their data history

## 🛠️ Getting Started

### 🔖Prerequisites

Before beginning the project, ensure you have the following set up on your machine/computer 🖥️:

- Python 3.7 or higher
- An OpenWeather API key (sign up at [OpenWeather](https://openweathermap.org/))
- An AWS account with IAM & S3 access
- AWS CLI (command line interface) configured with appropriate permissions
- A GitHub account with SSH authentication [https://docs.github.com/en/authentication/connecting-to-github-with-ssh]
- Basic knowledge of HTML & CSS
- Docker (for containerized deployment)

### 📘 User Guides

And here are some general resources to provide you further context and ground you as you move through the project:

- [AWS IAM Documentatation](https://docs.aws.amazon.com/iam/): How to use AWS IAM
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html): How to use AWS S3
- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html): How to configure the AWS CLI
- [Docker Installation Guide](https://docs.docker.com/get-docker/): How to install Docker
- [Flask Documentation](https://flask.palletsprojects.com/): How to use Flask web framework

### 💾 Installation Process for your IDE (Integrated Developer Environment)

1. Clone the repository:
```
git clone https://github.com/fpier042/aws-weather-app.git
cd aws-weather-app
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Set up your environment variables: Create a `.env` file in the project root, and add these:
```
OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your_s3_bucket_name
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_DEFAULT_REGION=your_aws_region
```

4. Configure your AWS credentials:
   Double-check that your AWS credentials are properly set up in the `.env` file.

Reminder: The application also utilizes the AWS CLI to interact with AWS S3. Use the command 'aws configure' to add it directly to ~/.aws/credentials in AWS CLI.

## 🔋 Usage

### To run the Weather Dashboard in Python:

1. Navigate to the project directory
```
cd aws-weather-app
```

2. Run the main script:
```
python weather_dashboard.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000 (or 5001, 5002, etc, if you run into any issues with the current port)
```

The application will fetch weather data for the default cities (Philadelphia, Seattle, New York) or load cities from a cities.json file, if available. The generated HTML dashboard will also be pushed to your S3 bucket.

## 📝 Code Explanation 📝

### weather_dashboard.py

This is the core of the application. Its main components are:

- **WeatherDashboard class**:
  - Initializes the API key and AWS S3 client
  - Validates environment variables
  - Manages S3 bucket creation

- **fetch_weather method**:
  - Fetches weather data from the OpenWeather API

- **save_to_s3 method**:
  - Saves the weather data to an S3 bucket with a timestamp

- **generate_html method**:
  - Generates an HTML file to visualize weather data

- **save_html_to_s3 method**:
  - Saves the HTML file to an S3 bucket

- **Flask application routes**:
  - Renders the weather dashboard in the web browser
  - Orchestrates the weather data fetching and saving process

## Incorporating Docker ⚓️

To run the Weather Dashboard in Docker:

1. Build the docker image:
```
docker build -t weather-dashboard .
```

2. Run the docker container:
```
docker run --env-file .env -p 5001:5000 -it weather-dashboard
```

3. Access the dashboard in your web browser:
```
http://localhost:5001
```

## 🚧 Common Issues and Solutions 🚧

Here are some challenges you might encounter:

### AWS Credentials Configuration

- **Issue**: AWS credentials are not recognized
- **Solution**: Ensure AWS CLI is properly configured with `aws configure` and credentials are stored in `~/.aws/credentials` or properly set in your `.env` file

### S3 Bucket Permission Issues

- **Issue**: Access denied when creating or accessing S3 bucket
- **Solution**: Verify IAM user has appropriate S3 permissions (AmazonS3FullAccess or a custom policy)

### Environment Variables Not Loading

- **Issue**: Application unable to access environment variables
- **Solution**: Verify `.env` file is in the correct location and properly formatted

### Flask Application Not Accessible

- **Issue**: Cannot access the web interface after starting the application
- **Solution**: Check that you're using the correct port (5001 if using Docker with the command above, or 5000 if running directly)

### GitHub SSH Authentication

- **Issue**: Unable to push code to repository
- **Solution**: Follow the SSH key setup guide in the prerequisites section

## 🛸 Potential Future Improvements

- Implement a more advanced graphical user interface (GUI) for a better user experience
- Add historical data analysis and visualization capabilities
- Integrate with additional weather APIs for more comprehensive data
- Implement user authentication for personalized experiences
- Create a more interactive web application with real-time updates
- Add support for geolocation to automatically detect the user's city
- Implement weather alerts and notifications
- Add a forecast feature to show weather predictions for upcoming days

## 🫱🏻‍🫲🏾 How to Contribute

Contributions are what allow for the open-source community to serve as a valuable resource for developers to learn various tools, inspire others, and create their best work

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🪪License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📲 Contact Information

Felton Pierre: [Linkedin](www.linkedin.com/in/felton-pierre-90)

Project Link: https://github.com/fpier042/aws-weather-app/
