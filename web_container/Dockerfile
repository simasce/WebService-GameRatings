FROM python:3.10.0a6-buster

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

COPY /templates /app/templates/
COPY /static /app/static/

RUN pip install -r requirements.txt

CMD ["python3","-u","app.py"]
