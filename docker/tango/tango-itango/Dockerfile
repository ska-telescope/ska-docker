ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST

FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-buildenv:latest as buildenv
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/ska-python-runtime:latest

# create ipython profile to so that itango doesn't fail if ipython hasn't run yet

RUN python3 -m pip install itango==0.1.6
RUN ipython profile create

CMD ["itango3"]
