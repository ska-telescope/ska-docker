ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
ARG SKA_PYTHON_BUILDENV_TAG=latest
ARG SKA_PYTHON_RUNTIME_TAG=latest

FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-buildenv:${SKA_PYTHON_BUILDENV_TAG} as buildenv

FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-runtime:${SKA_PYTHON_RUNTIME_TAG}

# create ipython profile to so that itango doesn't fail if ipython hasn't run yet
RUN ipython profile create

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This image illustrates itango cli." \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.1.2" \
    website="http://github.com/ska-telescope/ska-docker"

CMD ["itango3"]
