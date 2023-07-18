# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose the Django development server port (adjust if necessary)
EXPOSE 1234

# Define the command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:1234"]