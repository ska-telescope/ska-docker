FROM ubuntu:latest

RUN build_deps='make bash git curl python-pip apt-transport-https ca-certificates software-properties-common gnupg' && \
    apt-get update && \
<<<<<<< HEAD
    apt-get install -y --no-install-recommends $build_deps

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
=======
    apt-get install -y --no-install-recommends $build_deps && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
>>>>>>> 7c98c00a2baa042896d2250ce6f6038b86017783
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends docker-ce && \
    apt-get -y purge --auto-remove $build_deps && \
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
    version="0.1.1" \
    website="http://github.com/ska-telescope/ska-docker"
