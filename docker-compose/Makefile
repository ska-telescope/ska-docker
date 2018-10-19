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

# find IP addresses of this machine, setting MY_IP to the first address found
MY_IP := $(shell ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p' | head -n1)
DISPLAY = $(MY_IP):0

.PHONY: up down minimal start stop status help
.DEFAULT_GOAL := help

up: minimal  ## start the base TANGO system and prepare all services
	DISPLAY=$(DISPLAY) docker-compose $(COMPOSE_FILE_ARGS) up --no-start

down:  ## stop all services and tear down the system
	DISPLAY=$(DISPLAY) docker-compose $(COMPOSE_FILE_ARGS) down

minimal:  ## start the base TANGO system
	docker-compose -f tango.yml up -d

start: up ## start a service (usage: make start <servicename>)
	DISPLAY=$(DISPLAY) docker-compose $(COMPOSE_FILE_ARGS) start $(SERVICE)

stop:  ## stop a service (usage: make stop <servicename>)
	DISPLAY=$(DISPLAY) docker-compose $(COMPOSE_FILE_ARGS) stop $(SERVICE)

status:  ## show the container status
	DISPLAY=$(DISPLAY) docker-compose $(COMPOSE_FILE_ARGS) ps

clean: down  ## clear all TANGO database entries
	docker volume rm $(BASEDIR)_tangodb

help:   ## show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

