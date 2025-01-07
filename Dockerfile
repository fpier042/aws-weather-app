FROM python:3.9-slim

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y awscli 

COPY .env .
COPY data ./data
COPY src/ ./src  

CMD ["python", "src/__init__.py"]
