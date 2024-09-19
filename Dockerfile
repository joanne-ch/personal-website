# Use the official Python image from the Docker Hub
FROM python:3.9

# Install AWS CLI v2

# RUN apt-get update && apt-get install -y \
#     docker.io \
#     awscli \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

# RUN apt-get update && apt-get install -y \
#     docker.io \
#     awscli \
#     unzip \
#     curl \
#     && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
#     && unzip awscliv2.zip \
#     && ./aws/install \
#     && rm -rf /var/lib/apt/lists/* awscliv2.zip aws/


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Run pytest when the container launches
ENTRYPOINT ["pytest"]
