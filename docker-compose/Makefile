# Set dir of Makefile to a variable to use later
MAKEPATH := $(abspath $(lastword $(MAKEFILE_LIST)))
BASEDIR := $(notdir $(patsubst %/,%,$(dir $(MAKEPATH))))

COMPOSE_FILES := $(wildcard *.yml)
COMPOSE_FILE_ARGS := $(foreach yml,$(COMPOSE_FILES),-f $(yml))

# If the first make argument is "start" or "stop"...
ifeq (start,$(firstword $(MAKECMDGOALS)))
  SERVICE_TARGET = true
else ifeq (stop,$(firstword $(MAKECMDGOALS)))
  SERVICE_TARGET = true
endif
ifdef SERVICE_TARGET
  # .. then use the rest as arguments for the make target
  SERVICE := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(SERVICE):;@:)
endif


ifeq ($(OS),Windows_NT)
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		DISPLAY ?= :0.0
		TANGO_HOST ?= $(shell hostname):10000
		MYSQL_HOST ?= $(shell hostname):3306
		NETWORK_MODE := host
		XAUTHORITY_MOUNT := /tmp/.X11-unix:/tmp/.X11-unix
		XAUTHORITY ?= /hosthome/.Xauthority
		# /bin/sh (=dash) does not evaluate 'docker network' conditionals correctly
		SHELL := /bin/bash
	endif
	ifeq ($(UNAME_S),Darwin)
		IF_INTERFACE := $(shell netstat -nr | awk '{ if ($$1 ~/default/) { print $$6} }')
		DISPLAY := $(shell ifconfig $(IF_INTERFACE) | awk '{ if ($$1 ~/inet/) { print $$2} }'):0
		# network_mode = host doesn't work on MacOS, so fix to the internal network
		NETWORK_MODE := tangonet
		TANGO_HOST := databaseds:10000
		MYSQL_HOST := tangodb:3306
		XAUTHORITY_MOUNT := $(HOME):/hosthome:ro
		XAUTHORITY := /hosthome/.Xauthority
	endif
endif

DOCKER_COMPOSE_ARGS := DISPLAY=$(DISPLAY) XAUTHORITY=$(XAUTHORITY) TANGO_HOST=$(TANGO_HOST) \
		NETWORK_MODE=$(NETWORK_MODE) XAUTHORITY_MOUNT=$(XAUTHORITY_MOUNT) MYSQL_HOST=$(MYSQL_HOST) \
		COMPOSE_IGNORE_ORPHANS=true

.PHONY: up down minimal start stop status clean pull help
.DEFAULT_GOAL := help

pull: ## pull the images from the Docker hub
	$(DOCKER_COMPOSE_ARGS) docker-compose $(COMPOSE_FILE_ARGS) pull

up: minimal  ## start the base TANGO system and prepare all services
	$(DOCKER_COMPOSE_ARGS) docker-compose $(COMPOSE_FILE_ARGS) up --no-start

down:  ## stop all services and tear down the system
	$(DOCKER_COMPOSE_ARGS) docker-compose $(COMPOSE_FILE_ARGS) down
	docker network inspect tangonet &> /dev/null && ([ $$? -eq 0 ] && docker network rm tangonet) || true

minimal: ## start the base TANGO system
	docker network inspect tangonet &> /dev/null || ([ $$? -ne 0 ] && docker network create tangonet)
	$(DOCKER_COMPOSE_ARGS) docker-compose -f tango.yml up -d

start: up ## start a service (usage: make start <servicename>)
	$(DOCKER_COMPOSE_ARGS) docker-compose $(COMPOSE_FILE_ARGS) start $(SERVICE)

stop:  ## stop a service (usage: make stop <servicename>)
	$(DOCKER_COMPOSE_ARGS) docker-compose $(COMPOSE_FILE_ARGS) stop $(SERVICE)

status:  ## show the container status
	$(DOCKER_COMPOSE_ARGS) docker-compose $(COMPOSE_FILE_ARGS) ps

clean: down  ## clear all TANGO database entries
	docker volume rm $(BASEDIR)_tangodb

help:   ## show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

