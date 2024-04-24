FROM python:3.11.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /todoapp

# Installing the required libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying project files
COPY alembic.ini .
COPY app /todoapp/app

ENV PYTHONPATH=/todoapp/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]