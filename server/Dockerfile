FROM python:3.10
LABEL authors="gautam"


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
