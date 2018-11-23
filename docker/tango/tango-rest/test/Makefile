all: test

test:
	[ -f /.dockerenv ] && sudo apt-get update && sudo apt-get -y install --no-install-recommends curl || true
    # It takes several seconds for the Tango database to be populated from
    # scratch, so pause until DB is created and the device we test against is
    # responsive. If the Tango DB volume already exists, there'll be no delay
    # at all and the test will run immediately.
	retry -- tango_admin --check-device sys/tg_test/1
	/usr/local/bin/wait-for-it.sh rest:8080 --timeout=30 --strict -- curl --user tango-cs:tango http://rest:8080/tango/rest/rc4/hosts/databaseds/10000/devices/sys/tg_test/1/attributes/boolean_scalar/value

.PHONY: all test

