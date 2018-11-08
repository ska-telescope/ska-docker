from tango import DeviceProxy

# Get proxy on the tango_test1 device
print("Creating proxy to TangoTest device...")
tango_test = DeviceProxy("sys/tg_test/1")

# ping it
print(tango_test.ping())

# get the state
print(tango_test.state())