ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-buildenv:latest as buildenv
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-runtime:latest

USER root

RUN apt-get update
RUN apt-get install -y software-properties-common apt-transport-https wget gnupg libx11-xcb1 libasound2 x11-apps libice6 libsm6 libxaw7 libxft2 libxmu6 libxpm4 libxt6 x11-apps xbitmaps
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
RUN apt-get update
RUN apt-get -y install code

CMD ["/usr/bin/code"]