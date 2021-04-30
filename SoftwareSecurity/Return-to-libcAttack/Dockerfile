# Use the official Ubuntu 18.04 base image
FROM ubuntu:18.04

# Set the working directory inside the container
WORKDIR /app

# Install Python3 and xxd
RUN apt-get update && \
    apt-get install -y python3

# Copy the exploit script (exploit.py) into the container
COPY exploit.py /app/exploit.py

# CMD specifies the default command to run when the container starts
CMD ["python3", "/app/exploit.py"]
