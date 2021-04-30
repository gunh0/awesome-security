# Use the official Ubuntu 18.04 base image
FROM ubuntu:18.04

# Set the working directory inside the container
WORKDIR /app

# Install Python3
RUN apt-get update && \
    apt-get install -y python3

# Copy the exploit script (exploit.py) into the container
COPY exploit.py /app/exploit.py

# Specify the entry point for the container
CMD ["sh", "-c", "echo 'Exploit script is running...'; python3 exploit.py; echo 'Exploit script finished.'"]
