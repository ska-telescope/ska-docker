TRGTS = tango-dependencies tango-db tango-cpp tango-java tango-python tango-starter tango-pogo

.PHONY: build tango-dependencies tango-db tango-cpp tango-java tango-python tango-starter tango-starter tango-pogo
.DEFAULT_GOAL := help

build: $(TRGTS)  ## build all images

tango-dependencies:  ## build base dependency image
	$(MAKE) -C tango-dependencies

tango-db:  ## build ska/tango-db image
	$(MAKE) -C tango-db

tango-cpp: tango-dependencies  ## build ska/tango-cpp image
	$(MAKE) -C tango-cpp

tango-java: tango-dependencies  ## build ska/tango-java image
	$(MAKE) -C tango-java

tango-python: tango-dependencies  ## build ska/tango-python image
	$(MAKE) -C tango-python

tango-starter: tango-cpp  ## build ska/tango-starter image
	$(MAKE) -C tango-starter

tango-pogo: tango-java  ## build ska/tango-pogo image
	$(MAKE) -C tango-pogo

help:  ## show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
