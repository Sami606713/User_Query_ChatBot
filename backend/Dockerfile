# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /backend

# Copy the entire backend folder except ignored files (use .dockerignore)
COPY . .

# Copy requirements file
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port for uvicorn
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]