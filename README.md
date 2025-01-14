# 🌤️ AWS (Amazon Web Services) Weather Dashboard-Application ☔️

## 📖 Table of Contents 📖
- [Project Intro](#project-intro)
- [Project Structure](#project-structure)
- [Application Features](#application-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [User Guides](#user-guides)
  - [Installation Process](#installation-process)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Incorporating Docker](#incorporating-docker)
- [Potential Future Improvements](#potential-future-improvements)
- [How to Contribute](#how-to-contribute)
- [License](#license)
- [Contact](#contact)

## 👨🏾‍💻 Project Intro

The following code is for an interactive Python application allowing users to fetch and display current (real-time and location-based) weather data for multiple cities. It utilizes the OpenWeather API (application programming interface) to retrieve factual weather information and stores this data in an AWS S3 bucket.

This project demonstrates how to integrate various technologies and services, including:
- Python programming 🐍
- API integration (OpenWeather) ⛈️
- AWS services (S3, IAM) 🚚
- Environment variable management 🌱
- Asynchronous programming ⛓️‍💥

And this project aims to provide the user valuable insight into how best to create a functional, cloud-integrated application, whether you're a developer learning more about Python and AWS, or someone who simply likes to nerd out about the weather!   

## ⚙️ Project Structure

The project, overall, is organized as follows:

```
└── ./
    ├── src
    │   ├── __init__.py
    │   └── weather_dashboard.py
    ├── check_env_vars.py
    └── requirements.txt
```

- `src/weather_dashboard.py`: The main script containing the WeatherDashboard class and application logic
- `check_env_vars.py`: A utility script to validate environment variables
- `requirements.txt`: A list of Python dependencies required for the project

## ⚡️Application Features

- Retrieves real-time weather data for multiple cities
- Displays temperature (°F), humidity, and various weather conditions
- Automatically stores the weather data in the user's AWS S3 bucket
- Supports weather tracking across multiple cities 
- Provides a timestamp for all data, to assist the user with keeping track of their data history

## 🛠️ Getting Started

### 🔖Prerequisites

Before beginning the project, ensure you have the following set up on your machine/computer 🖥️:

- Python 3.7 or higher
- An OpenWeather API key (sign up at [OpenWeather](https://openweathermap.org/api))
- An AWS account with S3 access
- AWS CLI (command line interface) configured with appropriate permissions
- A GitHub account with SSH authentication [https://docs.github.com/en/authentication/connecting-to-github-with-ssh]
- Docker
  
### 📘 User Guides

And here are some general resources to provide you further context and ground you as you move through the project:

- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html): How to use AWS S3
- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html): How to configure the AWS CLI 
- [Docker Installation Guide](https://docs.docker.com/get-docker/): How to install Docker

## 💾 Installation Process for your IDE (Integrated Developer Environment)

1. Clone the repository:
   ```bash
   git clone https://github.com/fpier042/aws-weather-app.git
   cd weather-dashboard
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add these:
   ```
   OPENWEATHER_API_KEY=your_openweather_api_key
   AWS_BUCKET_NAME=your_s3_bucket_name
   AWS_REGION=your_aws_region
   ```

4. Configure your AWS credentials:

  Reminder: The application utilizes the AWS CLI to interact with AWS S3. Double-check that your AWS credentials are properly set up in 
  the **.env** file.
  ```
   AWS CREDENTIALS
      AWS_ACCESS_KEY_ID=your_aws_secret_key_id
      AWS_SECRET_ACCESS_KEY=your_aws-secret_access_key
      AWS_DEFAULT_REGION=your_aws_default_region
  ```
      
  Then input the following command in your IDE:
  ```
    
      bash copyaws configure 
  ```
   
## 🔋 Usage

To run the Weather Dashboard-Application in Python:

1. Navigate to the project directory
   ```bash
   cd src
   ```

2. Run the main script:
   ```bash
   python weather_dashboard.py
   ```

3. Follow the prompts to enter a city name or use the default list of cities

## 📝 Code Explanation 📝

### weather_dashboard.py

This is the core of the application. Its main components are:

1. `WeatherDashboard` class:
   - Initializes the API key and AWS S3 client.
   - Validates environment variables.
   - Manages S3 bucket creation.

2. `fetch_weather` method:
   - Asynchronously fetches weather data from the OpenWeather API.

3. `fetch_weather_for_cities` method:
   - Concurrently fetches weather data for multiple cities.

4. `save_to_s3` method:
   - Saves the weather data to an S3 bucket with a timestamp.

5. `main` function:
   - Handles user input for city selection.
   - Orchestrates the weather data fetching and saving process.
   - Displays the weather information to the user.

### check_env_vars.py

This is a utility script ensuring that all necessary environment variables are properly set, and is necessary for maintaining the security and overall functionality of the application.

## Incorporating Docker ⚓️

Finally, to run the Weather Dashboard-Application in Docker:
    
1. Build the docker image:

    sh
    docker build -t weather-dashboard 
    
2. Run the docker container:

    sh
    docker run weather-dashboard --name aws-app

## 🚧 Common Issues and Solutions 🚧

Here are some challenges you might encounter:

1. **AWS Credentials Configuration**
   - Issue: AWS credentials are not recognized
   - Solution: Ensure AWS CLI is properly configured with `aws configure` and credentials are stored in `~/.aws/credentials`

2. **S3 Bucket Permission Issues**
   - Issue: Access denied when creating or accessing S3 bucket
   - Solution: Verify IAM user has appropriate S3 permissions (AmazonS3FullAccess or custom policy)

3. **Environment Variables Not Loading**
   - Issue: Application unable to access environment variables
   - Solution: Verify .env file is in the correct location and properly formatted

4. **GitHub SSH Authentication**
   - Issue: Unable to push code to repository
   - Solution: Follow the SSH key setup guide in the prerequisites section

## 🪪License

This is a project licensed under MIT

## 🛸 Potential Future Improvements

1. Implement a graphical user interface (GUI) for a more interactive experience
2. Add historical data analysis and visualization capabilities
3. Integrate with additional weather APIs for more comprehensive data
4. Implement user authentication for personalized experiences
5. Create a web application version with real-time updates
6. Add support for geolocation to automatically detect the user's city
7. Implement weather alerts and notifications
 
## 🫱🏻‍🫲🏾 How to Contribute

Contributions are what allow for the open-source community to serve as a valuable resource for developers to learn various tools, inspire others, and create their best work

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📲 Contact Information

Felton Pierre: [Linkedin](www.linkedin.com/in/felton-pierre-90)

Project Link: https://github.com/fpier042/aws-weather-app/
