Launching TANGO applications and services in containers
=======================================================

The docker-compose directory contains a set of files that can be used to
run a TANGO system in Docker containers. The following services are
defined:

+-----------------+------------------------------------------------+
| Docker service  | Description                                    |
+=================+================================================+
| tangodb         | MariaDB database holding TANGO database tables |
+-----------------+------------------------------------------------+
| databaseds      | TANGO database device server                   |
+-----------------+------------------------------------------------+
| tangotest       | TANGO test device                              |
+-----------------+------------------------------------------------+
| jive            | Container running Jive application             |
+-----------------+------------------------------------------------+
| logviewer       | Container running TANGO log viewer             |
+-----------------+------------------------------------------------+
| pogo            | Pogo TANGO application                         |
+-----------------+------------------------------------------------+
| astor           | Astor application                              |
+-----------------+------------------------------------------------+
| starter-example | Example service running TANGO Starter device   |
+-----------------+------------------------------------------------+
| itango          | interactive itango session                     |
+-----------------+------------------------------------------------+
| rest            | REST proxy to the TANGO system running in the  |
|                 | containers                                     |
+-----------------+------------------------------------------------+

To pull pre-built images from the Docker hub, execute:

.. code-block:: console

   cd docker-compose
   # download official SKA images
   make pull

Optional: the images can be pulled from an alternative registry and/or
account by supplying the DOCKER_REGISTRY_HOST and DOCKER_REGISTRY_USER
Makefile variables respectively, e.g.,

.. code-block:: console

   cd docker-compose
   # download foo/tango-cpp, foo/tango-jive, etc. from a registry at
   # localhost:5000
   make DOCKER_REGISTRY_HOST=localhost:5000 DOCKER_REGISTRY_USER=foo pull

To start and stop a minimal TANGO system (database and databaseds
server), execute:

.. code-block:: console

   cd docker-compose
   # start a minimal TANGO system with database and TANGO database server
   make up

Optional applications and device servers can be launched by calling the
*start* make target followed by the name of the service. Note that for
Linux, you'll probably need to turn off X server security.

For example:

.. code-block:: console

   # still in the docker-compose directory..
   
   # if on Linux, you need to turn off some security
   xhost +   

   # run Jive
   make start jive

   # it's prudent to turn security back on
   xhost -

   # run tangotest
   make start tangotest

Running services can be stopped individually or as a whole using the
*stop* make target or *down* make target respectively. For instance,

.. code-block:: console

   # stop just the tangotest device server, leaving other services running
   make stop tangotest
   # stop all services and tear down the system
   make down

.. note::
    On Linux, the Docker containers make their services available on the host
    network and not on a separate container-only network. That is, you can
    effectively set TANGO_HOST=localhost:10000 and use Tango as though the
    services are installed and running on your machine rather than inside
    containers.

    On Windows and MacOS, the host network mode is not available, and services
    will execute on a separate network partition internal to the Docker
    containers.
