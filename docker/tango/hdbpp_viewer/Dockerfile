ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-java:latest

USER root

ENV DEBIAN_FRONTEND="noninteractive"
ENV HDBPP_DOWNLOAD_URL="https://nexus.engageska-portugal.pt/repository/raw/tango-cs/hdbpp_viewer/hdbpp_viewer_resources_20200527.tgz"

RUN apt-get update \
    && apt-get install -y wget

# Untarring this will create the `hdbpp_viewer` folder.
# Inside the tarball is a README detailing the source files.
RUN wget "$HDBPP_DOWNLOAD_URL" -O hdbpp_viewer_resources.tgz \
    && tar zxvf hdbpp_viewer_resources.tgz \
    && rm hdbpp_viewer_resources.tgz

ADD hdbpp_viewer_script hdbpp_viewer

RUN find . -iname HDBPP.jar
RUN find . -iname ATKCore.jar

USER tango
