#
# This Dockerfile creates a Docker image containing a build environment for SKA
# python projects. This image is intended to be used as an intermediate layer,
# where it can be used to compile C extensions to be copied into a final
# release image.
#
# This image caches a compilation of PyTango bindings so that child images
# need not recompile it.
ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
ARG TANGO_CPP_TAG=latest

FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:${TANGO_CPP_TAG}

USER root

# Speed up image builds by adding apt proxy if detected on host
RUN dockerhost=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` && \
    /usr/local/bin/wait-for-it.sh --host=$dockerhost --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$dockerhost:3142\";" > /etc/apt/apt.conf.d/30proxy && \
    echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host"

# Remove warnings when using apt-get noninteractively
ARG DEBIAN_FRONTEND=noninteractive

# Install runtime dependencies:
#
# * build-essential installs C/C++ compilers and build tools
# * libboost-python-dev is required to bind PyTango to the C++ Tango libs
# * pkg-config is used to locate required libraries
# * virtualenv is required to create a new Python virtualenv environment
RUN runtime_deps='build-essential libboost-python-dev pkg-config virtualenv' && \
    mkdir -p /usr/share/man/man1 && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $runtime_deps && \
    rm -f /etc/apt/apt.conf.d/30proxy && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

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
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIPENV_TIMEOUT=900 \
    PATH=/venv/bin:$PATH \
    VIRTUAL_ENV=/venv \
    PIPENV_VERBOSITY=-1 \
    PIPENV_NOSPIN=1

# Create the virtual environment into which we'll install PyTango
RUN virtualenv -p /usr/bin/python3 /venv
WORKDIR /app

# Install pipenv into the new virtual environment
RUN pip install pipenv

# Copy the Pipfile and frozen hashes (Pipfile.lock) across to the image so
# that pipenv knows what to install
COPY --chown=tango:tango Pipfile Pipfile
COPY --chown=tango:tango Pipfile.lock Pipfile.lock

# Install PyTango et al. into the virtual environment.
RUN pipenv install --dev

# The following commands are executed when extending this image.
# Copy the Pipfile across to the image so that pipenv knows which dependencies
# to install.
ONBUILD COPY --chown=tango:tango Pipfile Pipfile
ONBUILD COPY --chown=tango:tango Pipfile.lock Pipfile.lock
ONBUILD RUN pipenv install --dev

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This image creates the python build environment image with the PyTango bindings" \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.1.2" \
    website="http://github.com/ska-telescope/ska-docker"
