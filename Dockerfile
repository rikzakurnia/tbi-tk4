# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required system packages, including the JDK
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME and JVM_PATH environment variables
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV JVM_PATH="/usr/lib/jvm/java-11-openjdk-amd64/jre/lib/amd64/server/libjvm.so"
ENV PATH="$JAVA_HOME/bin:$PATH" 

# Verify Java installation (optional)
RUN java -version
RUN find / -name 'libjvm.so'

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN python -m venv env && \
    . env/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application using Gunicorn with explicit JAVA_HOME and JVM_PATH
CMD [ "sh", "-c", "export JAVA_HOME='/usr/lib/jvm/java-11-openjdk-amd64' && export JVM_PATH='/usr/lib/jvm/java-11-openjdk-amd64/jre/lib/amd64/server/libjvm.so' && . env/bin/activate && gunicorn -w 4 -b 0.0.0.0:5000 run:app" ]
