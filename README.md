# AWS Weather Dashboard:

The following is code allowing the user to build an application that retreives real-time/location-based weather data, from OpenWeather API, and saves this data to their AWS S3 bucket.

## Application Features:

- Retrieves real-time weather data for multiple cities across the U.S
- Displays temperature (°F), humidity, and various weather conditions
- Automatically stores the weather data in the user's AWS S3 bucket
- Supports weather tracking across multiple cities 
- Provides a timestamp for all data, to help with keeping track of data history

## Prerequisites/ Requirements:

The user must have:
- An OpenWeather account and API key
- An AWS account set up, with access keys
- Docker installed on their computer 

## Setup Instructions:

1. Clone the following repository:
  bash git clone https://github.com/fpier042/aws-weather-app.git

2. Install the necessary dependencies:
  bash Copypip install -r requirements.txt

3. Create a (.env) file in the root directory of your terminal (https://dotenvx.com/docs/env-file), and fill in this information:

    OPENWEATHER_API_KEY=your_openweather_api_key
    AWS_BUCKET_NAME=weather-dashboard-${RANDOM}
    # AWS CREDENTIALS
      AWS_ACCESS_KEY_ID=your_aws_secret_key_id
      AWS_SECRET_ACCESS_KEY=your_aws-secret_access_key
      AWS_DEFAULT_REGION=your_aws_default_region

4. Configure the AWS credentials:
   bash Copyaws configure

5. Run the application:
   python src/weather_dashboard.py
    
6. Build the docker image:

    sh
    docker build -t weather-dashboard .
    
7. Run the docker container:

    sh
    docker run weather-dashboard --name aws-app

## Application Uses: 

The application retrieves real-time weather data from the cities added into the json file at **/data/cities.json** file. The weather data automatically saves to the specified AWS S3 bucket.

## AWS Configuration

The application utilizes the AWS CLI (command line interface) to interact with AWS S3. Double-check that your AWS credentials are properly set up in the **.env** file.

## User Resources:

- [OpenWeather API Documentation](https://openweathermap.org/api): Here you can learn more about the OpenWeather API
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html): Here is a guide to how to use AWS S3
- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html): Here is a guide for how to configure the AWS CLI. 
- [Docker Installation Guide](https://docs.docker.com/get-docker/): Here is a guide for how to install Docker on your computer

## License: 

This is a project licensed under MIT
