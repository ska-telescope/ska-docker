FROM python:3.5-slim

# Remove warnings when using apt-get noninteractively
ARG DEBIAN_FRONTEND=noninteractive

# Remove warnings when adding apt-key
ARG APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN runtime_deps='make git apt-transport-https ca-certificates curl gnupg2 software-properties-common' && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $runtime_deps && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends docker-ce && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN export LC_ALL=C && \
    pip install docker-compose && \
    pip install pytest

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This image illustrates the tango-builder." \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.2.1" \
    website="http://github.com/ska-telescope/ska-docker"
