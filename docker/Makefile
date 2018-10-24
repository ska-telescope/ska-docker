DIRS = tango
BUILDDIRS = $(DIRS:%=build-%)
PUSHDIRS = $(DIRS:%=push-%)

.DEFAULT_GOAL := help

build: $(DIRS)  ## build all images
$(DIRS): $(BUILDDIRS)
$(BUILDDIRS):
	$(MAKE) -C $(@:build-%=%) build

push: $(PUSHDIRS)  ## push images to Docker hub
$(PUSHDIRS):
	$(MAKE) -C $(@:push-%=%) push

help:  ## show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(BUILDDIRS)
.PHONY: subdirs $(PUSHDIRS)
.PHONY: build push help
