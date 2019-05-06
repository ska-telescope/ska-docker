# This Dockerfile creates a Docker image intended to be a base runtime for SKA
# python projects. This image should be used as an intermediate layer
# alongside the ska-python-buildenv image.

ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-buildenv:latest as buildenv

# The application Pipfile and lock are pulled into the build environment here
# and installed within this build image
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest

# Remove warnings when using apt-get noninteractively
ARG DEBIAN_FRONTEND=noninteractive

USER root

# Permanently install Python and PyTango runtime dependencies:
#
# * libboost-python1.62.0 is required by PyTango;
# * make is required to manage execution of the tests inside the container
# * python3 is required as this image is intended for running Python Tango
#   devices.
RUN runtime_deps='libboost-python1.62.0 make python3' && \
    # Speed up image builds by adding apt proxy if detected on host
    dockerhost=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` && \
    /usr/local/bin/wait-for-it.sh --host=$dockerhost --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$dockerhost:3142\";" > /etc/apt/apt.conf.d/30proxy && \
    echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $runtime_deps && \
    rm -f /etc/apt/apt.conf.d/30proxy && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER tango

# When building an extension of this runtime image, copy the python virtual environment from the build image into the extending image
ONBUILD COPY --from=buildenv --chown=tango:tango /venv /venv
ONBUILD ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIPENV_TIMEOUT=900 \
    PATH=/venv/bin:$PATH \
    VIRTUAL_ENV=/venv \
    PIPENV_VERBOSITY=-1 \
    PIPENV_NOSPIN=1
# Now copy the application Pipfile and lock across from the build image.
ONBUILD COPY --from=buildenv --chown=tango:tango /app /app
# Copy the application source code across, in the process overwriting the old Pipfile and lock
ONBUILD COPY --chown=tango:tango . /app
# Overwrite the 'stale' user Pipfile.lock with the fresh version from the build image, so that the hashes in the final image reflect what's installed in the extending image
ONBUILD COPY --from=buildenv --chown=tango:tango /app/Pipfile.lock /app/Pipfile.lock

# subtlety: this has to come after the copy, otherwise /app is created root:root and the tango user cannot create new files
ONBUILD WORKDIR /app

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This Dockerfile creates a Docker image intended to be a base runtime for SKA python projects" \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.1.2" \
    website="http://github.com/ska-telescope/ska-docker"
