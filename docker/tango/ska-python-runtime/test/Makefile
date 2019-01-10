all: test

test:
    # It takes several seconds for the Tango database to be populated from
    # scratch, so pause until DB is created and the device we test against is
    # responsive. If the Tango DB volume already exists, there'll be no delay
    # at all and the test will run immediately.
	retry -- tango_admin --check-device sys/tg_test/1
	pytest SimpleTest.py

.PHONY: all test
