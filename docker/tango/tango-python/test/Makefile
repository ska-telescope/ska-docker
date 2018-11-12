all: test

test:
#	[ -f /.dockerenv ] && sudo apt-get update && sudo apt-get -y install --no-install-recommends python3-pytest || true
#	/usr/bin/py.test-3 -q SimpleTest.py
# Alternatively, use pip to install test requirements
	pip3 install --user -r requirements.txt
	$(HOME)/.local/bin/pytest SimpleTest.py

.PHONY: all test
