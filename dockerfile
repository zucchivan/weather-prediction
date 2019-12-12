FROM python:3.8.0-alpine
WORKDIR /code
ENV FLASK_APP application/app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code
CMD ["flask", "run"]