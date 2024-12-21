# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN python -m venv env && \
    . env/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application using Gunicorn
CMD [ "sh", "-c", ". env/bin/activate && gunicorn -w 4 -b 0.0.0.0:5000 run:app" ]