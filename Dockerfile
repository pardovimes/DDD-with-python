FROM python:3.7-slim-buster

WORKDIR /app

ENV FLASK_APP app/app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl \
    # Clean cache
    && apt-get clean && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
