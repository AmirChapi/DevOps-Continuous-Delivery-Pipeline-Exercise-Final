# 1a. Based on Ubuntu latest image
FROM ubuntu:latest

# Update package list and install necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip vim zip unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 1b. Define environment variable VERSION=1.2.0
ENV VERSION="1.2.0"

# 1g. Copy zip_job.py into the image's /tmp folder
# שימו לב: יש לוודא ש-zip_job.py נמצא באותה תיקייה כמו ה-Dockerfile (Final_hw)
COPY zip_job.py /tmp/

# 1h. Once docker container is up, run a command which will print OS type and architecture + verify /tmp/zip_job.py exists
CMD ["bash", "-c", "echo 'OS Type: $(uname)' && echo 'Architecture: $(uname -m)' && ls -l /tmp/zip_job.py"]