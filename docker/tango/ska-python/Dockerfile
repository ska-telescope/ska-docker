#
# This Dockerfile creates a Python image containing libraries required by SKA
# projects.
#
ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest

USER root

# Permanently install Python and PyTango runtime dependencies:
#
# * libboost-python1.62.0 is required by PyTango;
# * make is required to manage execution of the tests inside the container
# * python3 is required as this image is intended for running Python Tango
#   devices.
#
RUN runtimeDeps='libboost-python1.62.0 \
                 make \
                 python3' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/*

# Temporarily install build dependencies:
#
# * virtualenv is required to create a new Python virtualenv environment
#
# With the dependencies installed, create a new virtual environment into which
# all default SKA dependencies will be installed.
#
# Once the dependencies are installed, uninstall the build dependencies and
# delete apt caches to reduce the size of the intermediate image.
#
# Finally, change the ownership of the /venv directory within the build
# procedure rather than a separate 'RUN chown...' step, as otherwise the image
# size increases by the size of every file that is touched.
#
RUN buildDeps='virtualenv' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps \
    && virtualenv -p /usr/bin/python3 /venv \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf /var/lib/apt/lists/* /tmp/* \
    && chown -R tango:tango /venv

# Copy the Pipfile across to the image so that pipenv knows which dependencies
# to install.
WORKDIR /app
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# Set environment variables for pipenv execution:
#
# * LC_ALL and LANG: Pipenv (specifically, its Click dependency) exits with an
#   error unless the language encoding is set.
# * PIPENV_TIMEOUT: increased Pipenv timeout as locking dependencies takes
#   *forever* inside a Docker container.
# * PATH: puts virtualenv python/pip/pipenv first on path
# * VIRTUAL_ENV: for completeness. This environment variable would have been
#   set by 'source /venv/bin/activate'
# * PIPENV_VERBOSITY: hides warning about pipenv running inside a virtualenv.
# * PIPENV_NOSPIN: disables animated spinner for cleaner CI logs
#
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIPENV_TIMEOUT=900 \
    PATH=/venv/bin:$PATH \
    VIRTUAL_ENV=/venv \
    PIPENV_VERBOSITY=-1 \
    PIPENV_NOSPIN=1

# Install build dependencies temporarily:
#
# * build-essential is required to build pytango C extensions;
# * libboost-python-dev is required to build pytango;
# * pkg-config is required for the pytango build to locate the libraries that
#   that it requires.
#
# Install pipenv, and then use pipenv to install all project dependencies
# inside the virtualenv located at /venv.
#
# Then, remove the build dependencies to reduce the size of the intermediate
# image.
#
# Finally, change the ownership of the /venv and /app directories within the
# build procedure rather than a separate 'RUN chown...' step, as otherwise the
# image size increases by the size of every file that is touched.
#
RUN buildDeps='build-essential \
               libboost-python-dev \
               pkg-config' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps \
    && pip install pipenv \
    && pipenv install --dev \
    && rm -fr ~/.local ~/.cache \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R tango:tango /venv /app

USER tango

ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

ONBUILD RUN buildDeps='build-essential \
                       libboost-python-dev \
                       pkg-config' \
    && sudo DEBIAN_FRONTEND=noninteractive apt-get update \
    && sudo apt-get -y install --no-install-recommends $buildDeps \
    && pipenv install --dev \
    && rm -fr ~/.local ~/.cache \
    && sudo apt-get purge -y --auto-remove $buildDeps \
    && sudo rm -rf /var/lib/apt/lists/*

ONBUILD COPY . /app