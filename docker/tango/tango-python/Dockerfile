ARG DOCKER_REGISTRY_USER
FROM ${DOCKER_REGISTRY_USER}/tango-cpp:latest

USER root

RUN runtimeDeps='ipython libboost-python1.62.0 python-concurrent.futures python-gevent python-numpy python-six python-zmq python-pkgconfig python-pkg-resources python3 python3-gevent python3-numpy python3-six python3-pkgconfig python3-pkg-resources' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/* 

RUN PYTANGO_TAG=v9.2.4 \
    && PYTANGO_URL=https://github.com/tango-cs/pytango.git \
    && buildDeps='build-essential ca-certificates git libboost-python-dev python-dev python-setuptools python3-dev python3-setuptools' \
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
RUN buildDeps='python-dev python-pip python-setuptools python3-dev python3-pip python3-setuptools' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && pip install itango \
    && pip3 install itango \
    && apt-get purge -y --auto-remove $buildDeps

USER tango

# create ipython profile to so that itango doesn't fail if ipython hasn't run yet
RUN ipython profile create

CMD ["itango"]
