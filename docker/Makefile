.PHONY: tango help
.DEFAULT_GOAL := help

build:  ## build all SKA TANGO docker images
	$(MAKE) -C tango build

help:  ## show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
