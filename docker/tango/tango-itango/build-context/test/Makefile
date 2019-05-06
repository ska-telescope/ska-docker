all: test

test:
	[ -f /.dockerenv ] && sudo apt-get update && sudo apt-get -y install --no-install-recommends expect || true
    # It takes several seconds for the tango database to be populated from
    # scratch, so pause until DB is created and the device we test against is
    # responsive. If the Tango DB volume already exists, there'll be no pause
    # delay at all and the test will run immediately.
	retry -- tango_admin --check-device sys/tg_test/1
	./script.exp

.PHONY: all test
