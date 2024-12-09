# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /Agro_space

# Copy the requirements file
COPY requirements.txt /Agro_space/

# Install dependencies
RUN pip install --upgrade pip  
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's files
COPY . /Agro_space/

# Expose port 8000
EXPOSE 8000

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
