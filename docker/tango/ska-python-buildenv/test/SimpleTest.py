import tango


def test_test_device_is_running():
    tango_test = tango.DeviceProxy("sys/tg_test/1")
    assert tango_test.state() == tango.DevState.RUNNING
