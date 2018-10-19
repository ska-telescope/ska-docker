# TANGO Docker containers

This repository defines a set of Docker images and Docker compose files that 
are useful for TANGO control system development. 

## Building the Docker images
The following Docker images are built by this project:

Docker image           | Description
-----------------------|------------
ska/tango-dependencies | A base image containing TANGO's preferred version of ZeroMQ plus the preferred, patched version of OmniORB.
ska/tango-db           | A MariaDB image including TANGO database schema. Data is stored separately in a volume. 
ska/tango-cpp          | Core C++ TANGO libraries and applications.
ska/tango-java         | As per ska/tango-cpp, plus Java applications and bindings    
ska/tango-python       | Extends ska/tango-cpp, adding PyTango Python bindings and itango for interactive TANGO sessions.
ska/tango-pogo         | Image for running Pogo and displaying Pogo help. Pogo output can be persisted to a docker volume or to the host machine.
ska/tango-starter      | Example image that demonstrates how to package the Starter device in an image.

To build the images, from the root of this repository execute:

    cd docker
    make 
    
## Launching TANGO applications and services
The docker-compose directory contains a set of files that can be used to run a
TANGO system in Docker containers. The following services are defined:

Docker service  | Description
----------------|------------
tangodb         | MariaDB database holding TANGO database tables
databaseds      | TANGO database device server
tangotest       | TANGO test device
jive            | Container running Jive application
pogo            | Pogo TANGO application
astor           | Astor application
starter-example | Example service running TANGO Starter device
itango          | interactive itango session

To start and stop a minimal TANGO system (database and databaseds server),
execute:

    cd docker-compose
    # start a minimal TANGO system with database and TANGO database server
    make up 

Optional applications and device servers can be launched by calling the 
_start_ make target followed by the name of the service. For example:

    # still in the docker-compose directory..
    # run Jive
    make start jive
    # run tangotest
    make start tangotest
    
Running services can be stopped individually or as a whole using the _stop_
make target or _down_ make target respectively. For instance,

    # stop just the tangotest device server, leaving other services running
    make stop tangotest
    # stop all services and tear down the system
    make down

## Interacting with TANGO applications and devices

### Command line interactions
``itango`` can be used for command line interactions with the system. To make
itango available, launch the itango service and attach the terminal to the 
itango container. An example session follows:

    # start a container running itango
    make start itango
    
    # attach to the itango container
    docker attach itango
    In [1]: dev = DeviceProxy('sys/tg_test/1')

    In [2]: dev.string_scalar
    Out[2]: 'Default string'

    ...
    
To detach from the session without quitting the itango session, press the key
combination <CTRL+P><CTRL+Q>.   
    
### GUI interactions    
Graphical applications such as Jive and Pogo can be run in a container, 
sending their output to an X11 server running on the host machine. 

    # run Jive, using the default IP address determined by the Makefile
    make start jive
    # run Pogo
    make start pogo
    
GUI applications send X11 traffic to an IP address determined by the makefile. 
This IP address can be overridden by passing a ``DISPLAY`` variable to make, 
e.g.,

    # run Jive, sending X11 output to 172.16.10.120:0
    make DISPLAY=172.16.10.120:0 start jive

Note that the IP address is evaluated inside the Docker container, hence
127.0.0.1 would direct output to the container itself.  

#### Exporting Pogo output
The Pogo service mounts your home directory as ``/hosthome``. Save Pogo 
output to the ``/hosthome`` directory to make it available outside the 
container. 