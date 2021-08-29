FROM python:3.8

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]