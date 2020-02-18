SHELL = /bin/bash
.SHELLFLAGS = -o pipefail -c

all: test

test:
	retry --max=10 -- tango_admin --ping-device archiving/hdbpp/eventsubscriber01 && \
	pytest SimpleTest.py

.PHONY: all test
