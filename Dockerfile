FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip vim zip unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV VERSION="1.2.0"

COPY zip_job.py /tmp/

CMD ["bash", "-c", "echo 'OS Type: $(uname)' && echo 'Architecture: $(uname -m)' && ls -l /tmp/zip_job.py"]