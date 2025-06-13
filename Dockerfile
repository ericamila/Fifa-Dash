# Use a base image with Python 3.13
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
	&& pip install --no-cache-dir -r requirements.txt \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["streamlit", "run", "1_🏠_home.py"]