FROM python:3.12.0

ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend

COPY ./backend .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
