ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-buildenv:latest as buildenv
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-runtime:latest

USER root

ARG SSH_PASSWORD=vscodessh

ENV ssh_cmd tango:$SSH_PASSWORD

RUN echo $ssh_cmd

RUN apt-get update && apt-get install -y \
  openssh-server \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd
RUN echo $ssh_cmd | chpasswd

RUN apt-get update && apt-get install -y curl net-tools git software-properties-common \
    apt-transport-https wget gnupg libx11-xcb1 libasound2 x11-apps libice6 libsm6 \
    libxaw7 libxft2 libxmu6 libxpm4 libxt6 x11-apps xbitmaps

RUN pipenv run pip install docker-compose yamllint yamale

ENV KUBE_LATEST_VERSION="v1.16.2"
ENV HELM_VERSION="v3.1.1"
ENV DEBIAN_FRONTEND="readline"
ENV RUNLEVEL="1"
ENV PYTEST_REQUIREMENTS="https://gitlab.com/ska-telescope/skampi/raw/60ad4e45f9e7e716d1abd23e520b63c3711dba99/test-requirements.txt"

RUN wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm

RUN wget -q https://github.com/helm/chart-testing/releases/download/v2.4.0/chart-testing_2.4.0_linux_amd64.tar.gz -O /tmp/ct.tar.gz \
    && cd /tmp \
    && tar -xf ct.tar.gz \
    && mv ct /usr/local/bin/ct

RUN pipenv run pip install -r ${PYTEST_REQUIREMENTS}
RUN pipenv run pip install pytest pytest-cov pytest-json-report pycodestyle pytest-bdd elasticsearch \ 
    kubernetes pytest-runner sphinx recommonmark

RUN printf "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d 

# Allows the SSH user to pass environment variables into their SSH session
# For this stage of development this is useful as it allows the TANGO_HOST
# to be overwritten by the user.
RUN echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config

RUN echo "X11UseLocalhost no" >> /etc/ssh/sshd_config

RUN echo "if [[ ! -d ~/skampi ]] " >> /home/tango/.bashrc
RUN echo "then" >> /home/tango/.bashrc
RUN echo "  git clone https://gitlab.com/ska-telescope/skampi.git" >> /home/tango/.bashrc
RUN echo "fi" >> /home/tango/.bashrc
RUN echo "source /venv/bin/activate" >> /home/tango/.bashrc

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
