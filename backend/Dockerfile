# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /backend

# Copy only the requirements file (improves build caching)
COPY backend/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY backend/ .

# Expose the port (optional, for documentation)
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]