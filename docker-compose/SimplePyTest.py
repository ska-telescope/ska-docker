import pytest
from tango import DeviceProxy

def test_tango_test():
	# Get proxy on the tango_test1 device
	print("Creating proxy to TangoTest device...")
	tango_test = DeviceProxy("sys/tg_test/1")
	# ping it
	print(tango_test.ping())
	# get the state
	assert tango_test.state() == tango.DevState.RUNNING