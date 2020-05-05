Interacting with TANGO applications and devices
===============================================

Command line interactions
-------------------------

``itango`` can be used for command line interactions with the system. To
make itango available, launch the itango service and attach the terminal
to the itango container. An example session follows:

::

   # start the tangotest device, which we'll connect to using itango
   make start tangotest
   # start the itango container
   make start itango
   # attach to the itango container
   docker attach itango
   In [1]: dev = DeviceProxy('sys/tg_test/1')

   In [2]: dev.string_scalar
   Out[2]: 'Default string'

   ...

To detach from the session without quitting the itango session, press
the key combination <CTRL+P><CTRL+Q>.

GUI interactions
----------------

Graphical applications such as Jive and Pogo can be run in a container,
sending their output to an X11 server running on the host machine.
Note that for Linux, you'll probably need to turn off X server security.

::

   # if on Linux, you need to turn off some security
   xhost +

   # run Jive, using the default IP address determined by the Makefile
   make start jive
   # run Pogo
   make start pogo

   # it's prudent to turn security back on
   xhost -

GUI applications send X11 traffic to an IP address determined by the
makefile. This IP address can be overridden by passing a ``DISPLAY``
variable to make, e.g.,

::

   # run Jive, sending X11 output to 172.16.10.120:0
   make DISPLAY=172.16.10.120:0 start jive

Note that the IP address is evaluated inside the Docker container, hence
127.0.0.1 would direct output to the container itself.

Exporting Pogo output
---------------------

The Pogo service mounts your home directory as ``/hosthome``. Save Pogo
output to the ``/hosthome`` directory to make it available outside the
container.

REST interactions
-----------------

The ``rest`` docker-compose service makes a REST proxy to the TANGO system
running in the containers available at http://tango-rest:8080/tango/rest/rc4
from inside the container network, and http://localhost:8080/tango/rest/rc4
from the container host. The REST service uses plain HTTP authentication, with
username=tango-cs password=tango.

The database device server for the container system is located at
databaseds:10000, hence the root URL to use the REST proxy to interact with
the container environment is

http://<hostname>:8080/tango/rest/rc4/databaseds/10000

Below is an example session that reads an attribute value from the TANGO test
device:

.. code-block:: console

  $ # start the TANGO test device and REST proxy
  $ make start tangotest
  $ make start rest
  $ # retrieve an attribute value from the TANGO test device. Output follows.
  $ curl --user tango-cs:tango  http://localhost:8080/tango/rest/rc4/hosts/databaseds/10000/devices/sys/tg_test/1/attributes/boolean_scalar/value
  {"name":"boolean_scalar","value":true,"quality":"ATTR_VALID","timestamp":1541603849178}

