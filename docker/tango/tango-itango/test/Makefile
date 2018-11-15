all: test

test:
	[ -f /.dockerenv ] && sudo apt-get update && sudo apt-get -y install --no-install-recommends expect || true
	./script.exp

.PHONY: all test
