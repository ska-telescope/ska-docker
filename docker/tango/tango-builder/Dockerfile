FROM ubuntu:18.04

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get install -y make bash git curl apt-transport-https ca-certificates curl software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce
RUN export LC_ALL=C
# pip
RUN apt-get update && apt-get install -yq python3-distutils \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py
COPY pip.conf /etc/pip.conf
# /pip
RUN python3 -m pip install docker-compose
RUN python3 -m pip install pytest
