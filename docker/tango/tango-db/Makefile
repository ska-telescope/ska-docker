include ../../make/Makefile

CACHE_VOLUME = tango-db-test-cache

IMAGE_TO_TEST = $(DOCKER_REGISTRY_HOST)/$(DOCKER_REGISTRY_USER)/tango-db:latest

DOCKER_COMPOSE_COMMAND = PWD=$(CURDIR) \
						 DOCKER_REGISTRY_HOST=$(DOCKER_REGISTRY_HOST) \
						 DOCKER_REGISTRY_USER=$(DOCKER_REGISTRY_USER) \
						 docker-compose \
						 -f docker-compose.yml

make = tar -c test/ | \
	   ./test/wait-for-it.sh -t 30 `docker inspect -f \
	   '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(notdir $(CURDIR))_tangodb_1`:3306 --\
	   docker run -i --rm --network=$(notdir $(CURDIR))_default \
	   -v `pwd`/test/:/test \
	   -v $(CACHE_VOLUME):/home/tango/.cache \
	   -v /build -w /build $(DOCKER_RUN_ARGS) $(IMAGE_TO_TEST) \
	   /test/test.sh $(notdir $(CURDIR))_tangodb_1 \

pre-build:
	@echo do some stuff before the docker build

post-build:
	@echo do some stuff after the docker build

all: test

test: DOCKER_RUN_ARGS = --volumes-from=$(BUILD)
test:
	$(INIT_CACHE)
	$(DOCKER_COMPOSE_COMMAND) up -d
	$(call make,test); \
	  status=$$?; \
	  docker rm -f -v $(BUILD); \
	  $(DOCKER_COMPOSE_COMMAND) down; \
	  exit $$status

.PHONY: all test


# Creates Docker volume for use as a cache, if it doesn't exist already
INIT_CACHE = \
	docker volume ls | grep $(CACHE_VOLUME) || \
	docker create --name $(CACHE_VOLUME) -v $(CACHE_VOLUME):/cache $(IMAGE_TO_TEST)

# http://cakoose.com/wiki/gnu_make_thunks
BUILD_GEN = $(shell docker create -v /build $(IMAGE_TO_TEST))
BUILD = $(eval BUILD := $(BUILD_GEN))$(BUILD)
