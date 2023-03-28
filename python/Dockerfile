FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements/backend.in


CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
