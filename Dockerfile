# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /user/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Set the entrypoint command to run your Flask app
ENTRYPOINT ["python", "app.py"]
