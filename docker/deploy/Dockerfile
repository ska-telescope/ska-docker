FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y make bash git curl apt-transport-https ca-certificates wget software-properties-common 
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
    && python3 get-pip.py pip==${PIP_VERSION}
# /pip

RUN pip install docker-compose
RUN pip install yamllint yamale

ENV KUBE_LATEST_VERSION="v1.16.2"
ENV HELM_VERSION="v3.1.1"
ENV DEBIAN_FRONTEND="readline"
ENV RUNLEVEL="1"
ENV PYTEST_REQUIREMENTS="https://gitlab.com/ska-telescope/skampi/raw/8204ac53ef67941bf22e9f259be1910b2a9636a5/test-requirements.txt"

RUN wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm

RUN wget -q https://github.com/helm/chart-testing/releases/download/v3.0.0-beta.1/chart-testing_3.0.0-beta.1_linux_amd64.tar.gz -O /tmp/ct.tar.gz \
    && cd /tmp \
    && tar -xf ct.tar.gz \
    && mv ct /usr/local/bin/ct

RUN pip install -r ${PYTEST_REQUIREMENTS}
RUN pip install pytest

RUN apt-get update
RUN apt-get install -y python software-properties-common net-tools
RUN apt-add-repository --yes --update ppa:ansible/ansible 
RUN printf "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d 
RUN apt-get -y install ansible ssh python-apt
