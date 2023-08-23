# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local app.py file into the container at /app
COPY app.py .

# If you have additional dependencies, you'd install them here:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD ["python", "./app.py"]
