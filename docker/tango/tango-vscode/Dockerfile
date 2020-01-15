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

RUN apt-get install -y software-properties-common apt-transport-https wget gnupg libx11-xcb1 libasound2 x11-apps libice6 libsm6 libxaw7 libxft2 libxmu6 libxpm4 libxt6 x11-apps xbitmaps

# Allows the SSH user to pass environment variables into their SSH session
# For this stage of development this is useful as it allows the TANGO_HOST
# to be overwritten by the user.
RUN echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
