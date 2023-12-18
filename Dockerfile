FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY /app/static /app/static

EXPOSE 8000
  
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app.app:app"]