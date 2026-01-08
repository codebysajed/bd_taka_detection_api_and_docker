# image
FROM python:3.11-slim

# working directory
WORKDIR /app

# requirments and dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY model/ ./model/

ENV PYTHONPATH=/app

EXPOSE 5000

# COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]