ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest

USER root

# Speed up image builds by adding apt proxy if detected on host
RUN DOCKERHOST=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` \
    && /usr/local/bin/wait-for-it.sh --host=$DOCKERHOST --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$DOCKERHOST:3142\";" > /etc/apt/apt.conf.d/30proxy \
    && echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host"

# Install build dependencies:
#
# * build-essential installs C/C++ compilers and build tools
# * libboost-python-dev is required to bind PyTango to the C++ Tango libs
# * pkg-config is used to locate required libraries
# * virtualenv is required to create a new Python virtualenv environment
#

RUN buildDeps='build-essential \
               libboost-python-dev \
               pkg-config \
               git \
               python-setuptools \
               python-pip \
               virtualenv' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps

RUN python2 -m pip install -U pip
COPY pip.conf /etc/pip.conf

# install numpy before pytango, since pytango compilation
# checks for presence of numpy
RUN python2 -m pip install wheel numpy==1.16.6
RUN python2 -m pip install pytango==9.3.2
RUN python2 -m pip install --no-cache-dir python-dsconfig==1.2.5
COPY json2tango .
ENV PATH $PATH:/json2tango
# RUN chmod +x ./json2tango.sh if needed
