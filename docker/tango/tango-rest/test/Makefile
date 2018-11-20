all: test

test:
	[ -f /.dockerenv ] && sudo apt-get update && sudo apt-get -y install --no-install-recommends curl || true
	/usr/local/bin/wait-for-it.sh tango-rest:8080 --timeout=30 --strict -- curl --user tango-cs:tango http://tango-rest:8080/tango/rest/rc4/hosts/databaseds/10000/devices/sys/tg_test/1/attributes/boolean_scalar/value

.PHONY: all test

