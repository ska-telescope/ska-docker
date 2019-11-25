import tango

def test_test_device_is_running():
    tango_test = tango.DeviceProxy("archiving/hdbpp/eventsubscriber01")
    assert tango_test.state() == tango.DevState.RUNNING