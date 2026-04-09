# Use a slim Python image to reduce container size
FROM python:3.10-slim

WORKDIR /app

# Install dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code into the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

CMD ["python", "app.py"]
