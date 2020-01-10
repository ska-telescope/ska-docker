FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y make bash git curl apt-transport-https ca-certificates curl software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce
RUN export LC_ALL=C
# pip
ENV PIP_VERSION=19.3.1
RUN apt-get install -yq python3-distutils \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py --user pip==${PIP_VERSION}
# /pip
RUN pip3 install docker-compose
RUN pip3 install pytest
