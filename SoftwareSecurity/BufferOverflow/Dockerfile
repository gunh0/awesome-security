# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the badfile_generator.py script into the container
COPY badfile_generator.py /app/

# Run the script when the container launches
CMD ["python", "./badfile_generator.py"]
