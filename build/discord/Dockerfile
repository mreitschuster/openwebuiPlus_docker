# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Discord bot script and env file
COPY discord_bot.py .
#COPY .env .

# Expose port 8080 for outgoing HTTP connections (e.g., to Open-WebUI)
EXPOSE 8080

# Set environment variables from .env file
#ENV DISCORD_BOT_TOKEN $DISCORD_BOT_TOKEN

# Run the bot script when the container starts
CMD ["python", "discord_bot.py"]