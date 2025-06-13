# Use a base image with Python 3.13
FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "1_🏠_home.py"]