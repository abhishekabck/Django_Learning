# Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files at build time (optional)
RUN python manage.py collectstatic --noinput

# Run Gunicorn as WSGI server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]# Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files at build time (optional)
RUN python manage.py collectstatic --noinput

# Run Gunicorn as WSGI server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]# Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files at build time (optional)
RUN python manage.py collectstatic --noinput

# Run Gunicorn as WSGI server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:9000"]
