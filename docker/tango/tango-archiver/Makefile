include ../../make/Makefile

# name of the Docker volume used to cache eggs and wheels
CACHE_VOLUME = tango-archiver-test-cache

# defines the image to test
IMAGE_TO_TEST = $(DOCKER_REGISTRY_HOST)/$(DOCKER_REGISTRY_USER)/tango-itango:latest

THIS_HOST := $(shell ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p' | head -n1)

ifneq ($(CI_JOB_ID),)
NETWORK_MODE := tangonet-$(CI_JOB_ID)
CONTAINER_NAME_PREFIX := $(CI_JOB_ID)-
else
# ********
# Patch Matteo 20/02/2020 network mode cannot be host in this case. 
# For enabling the host network, it is necessary to template the archiver-devices.json configuration file.
NETWORK_MODE := tangonet-local
CONTAINER_NAME_PREFIX := local-
# ********
endif

#
# When running in network=host mode, point devices at a port on the host
# machine rather than at the container.
#
ifeq ($(OS),Windows_NT)
    $(error Sorry, Windows is not supported yet)
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		DISPLAY ?= :0.0
		NETWORK_MODE ?= host
		XAUTHORITY_MOUNT := /tmp/.X11-unix:/tmp/.X11-unix
		XAUTHORITY ?= /hosthome/.Xauthority
		# /bin/sh (=dash) does not evaluate 'docker network' conditionals correctly
		SHELL := /bin/bash
	endif
	ifeq ($(UNAME_S),Darwin)
		IF_INTERFACE := $(shell netstat -nr | awk '{ if ($$1 ~/default/) { print $$6} }')
		DISPLAY := $(shell ifconfig $(IF_INTERFACE) | awk '{ if ($$1 ~/inet$$/) { print $$2} }'):0
		# network_mode = host doesn't work on MacOS, so fix to the internal network
		NETWORK_MODE ?= tangonet
		XAUTHORITY_MOUNT := $(HOME)/.Xauthority:/hosthome/.Xauthority:ro
		XAUTHORITY := /hosthome/.Xauthority
	endif
endif

#
# When running in network=host mode, point devices at a port on the host
# machine rather than at the container.
#
ifeq ($(NETWORK_MODE),host)
	TANGO_HOST := $(shell hostname):10000
	MYSQL_HOST := $(shell hostname):3306
else
	TANGO_HOST := $(CONTAINER_NAME_PREFIX)databaseds:10000
	MYSQL_HOST := $(CONTAINER_NAME_PREFIX)tangodb:3306
endif

DOCKER_COMPOSE_ARGS := PWD=$(CURDIR) DOCKER_REGISTRY_HOST=$(DOCKER_REGISTRY_HOST) \
		DOCKER_REGISTRY_USER=$(DOCKER_REGISTRY_USER) DISPLAY=$(DISPLAY) XAUTHORITY=$(XAUTHORITY) TANGO_HOST=$(TANGO_HOST) \
		NETWORK_MODE=$(NETWORK_MODE) XAUTHORITY_MOUNT=$(XAUTHORITY_MOUNT) MYSQL_HOST=$(MYSQL_HOST) \
		CONTAINER_NAME_PREFIX=$(CONTAINER_NAME_PREFIX) COMPOSE_IGNORE_ORPHANS=true

make = tar -c test/ | \
	   docker run -i --rm --network=$(NETWORK_MODE) \
	   $(DOCKER_RUN_ARGS) $(IMAGE_TO_TEST) \
	   bash -c "tar x --strip-components 1 --warning=all && \
	   make TANGO_HOST=$(TANGO_HOST) $1"

all: test

test:
ifneq ($(NETWORK_MODE),host)
	docker network inspect $(NETWORK_MODE) &> /dev/null || ([ $$? -ne 0 ] && docker network create $(NETWORK_MODE))
endif
	$(DOCKER_COMPOSE_ARGS) docker-compose up -d
	$(call make,test); \
	  status=$$?; \
	  docker-compose logs; \
	  $(DOCKER_COMPOSE_ARGS) docker-compose down; \
	  exit $$status

.PHONY: all test
