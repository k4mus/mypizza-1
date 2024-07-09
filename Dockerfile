# Use the official Python image with Alpine Linux
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY /mypizza/ /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run any commands needed to set up your application


# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
