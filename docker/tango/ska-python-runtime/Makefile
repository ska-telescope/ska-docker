include ../../make/Makefile

# defines the image to test
IMAGE_TO_TEST = $(DOCKER_REGISTRY_HOST)/$(DOCKER_REGISTRY_USER)/ska-python-runtime:latest

piplock: build  ## overwrite Pipfile.lock with the image version
	docker run $(IMAGE_TO_TEST) cat /app/Pipfile.lock > $(CURDIR)/Pipfile.lock
