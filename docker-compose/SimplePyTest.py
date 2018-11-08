import pytest
import tango
from tango import DeviceProxy

def test_framework():
	tango_test = DeviceProxy("sys/tg_test/1")
	assert tango_test.state() == tango.DevState.RUNNING