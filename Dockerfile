# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy project
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Run the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
