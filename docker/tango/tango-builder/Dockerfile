FROM ubuntu:latest

RUN apt-get update
RUN buildDeps='make bash git curl python-pip apt-transport-https ca-certificates curl software-properties-common'
RUN apt-get install -y $buildDeps && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update && \
    apt-get install -y docker-ce && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
RUN export LC_ALL=C
RUN pip install docker-compose
RUN pip install pytest

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This image illustrates the tango-builder." \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.1.0" \
    website="http://github.com/ska-telescope/ska-docker"
