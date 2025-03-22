FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask requests python-dotenv
EXPOSE 5000
CMD ["python", "weather_dashboard.py"]