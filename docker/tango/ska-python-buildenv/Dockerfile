#
# This Dockerfile creates a Docker image containing a build environment for SKA
# python projects. This image is intended to be used as an intermediate layer,
# where it can be used to compile C extensions to be copied into a final
# release image.
#
# This image caches a compilation of PyTango bindings so that child images
# need not recompile it.
#
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
# * git is required for Python packages using katversion for release info
#
RUN buildDeps='build-essential \
               libboost-python-dev \
               pkg-config \
               python3-distutils \
               python3-pip \
               zlib1g-dev \
               curl \
               git' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
COPY pip.conf /etc/pip.conf

RUN python3 -m pip install setuptools \
    wheel

WORKDIR /app

# Install numpy manually before PyTango and other requirements to ensure we
# build PyTango with numpy support.
RUN python3 -m pip install numpy==1.17.2

COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r /requirements.txt

RUN mkdir /venv && ln -s /usr/* /venv/  && ln -s /usr/local/bin/itango3 /venv/bin/itango3
