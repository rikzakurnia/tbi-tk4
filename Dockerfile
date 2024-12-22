# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required system packages, including OpenJDK 17 and python3-venv
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    python3-venv \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME and JVM_PATH environment variables
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
ENV JVM_PATH="/usr/lib/jvm/java-17-openjdk-amd64/lib/server/libjvm.so"
ENV PATH="${JAVA_HOME}/bin:$PATH"


# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment and install Python dependencies
RUN python3 -m venv env && \
    . env/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application using Gunicorn
CMD [ "sh", "-c", ". env/bin/activate && gunicorn -w 4 -b 0.0.0.0:5000 run:app" ]
