ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest

USER root

RUN runtimeDeps='\
    ipython \
    libboost-python1.62.0 \
    make \
    python-concurrent.futures \
    python-dev \
    python-gevent \
    python-numpy \
    python-pip \
    python-pkgconfig \
    python-pkg-resources \
    python-setuptools \
    python-six \
    python-zmq \
    python3 \
    python3-dev \
    python3-gevent \
    python3-numpy \
    python3-pkgconfig \
    python3-pkg-resources \
    python3-setuptools \
    python3-six \
    python3-pip \
    sudo' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/* 

RUN PYTANGO_TAG=v9.2.4 \
    && PYTANGO_URL=https://github.com/tango-cs/pytango.git \
    && buildDeps='build-essential git libboost-python-dev' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/pytango \
    && cd /usr/src/pytango \
    && git clone $PYTANGO_URL \
    && cd pytango \
    && git checkout tags/$PYTANGO_TAG \
    && python setup.py build \
    && python setup.py install \
    && python3 setup.py clean \
    && python3 setup.py build \
    && python3 setup.py install \
    && cd .. \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/pytango

# itango is a separate project from Pytango v9.2.0 on
RUN pip install itango \
    && pip3 install itango

# add sudo so that the tango user can add test dpkgs
RUN echo "tango ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/tango \
    && chmod 0440 /etc/sudoers.d/tango

USER tango

# create ipython profile to so that itango doesn't fail if ipython hasn't run yet
RUN ipython profile create

CMD ["itango"]
