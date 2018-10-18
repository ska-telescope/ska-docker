# TANGO Docker containers

This repository defines a set of Docker images and Docker compose files that 
are useful for TANGO control system development. 

## Building the Docker images
The Docker images created by this project comprise:

Docker image           | Description
-----------------------|------------
ska/tango-dependencies | A base image containing TANGO's preferred version of ZeroMQ plus the preferred, patched version of OmniORB.
ska/tango-db           | A MariaDB image with TANGO database schema defined. Data is stored separately in a volume 
ska/tango-cpp          | Core C++ TANGO libraries and applications.
ska/tango-java         | As per ska/tango-cpp, plus Java applications and bindings    
ska/tango-python       | Extends ska/tango-cpp, adding pytango Python bindings and itango for interactive TANGO sessions.

To build the images, from the root of this repository execute:

    cd docker
    make build
    
## Launching a TANGO system
The Docker compose files define a set of containers for a TANGO system. In 
addition to the processes to be launched, the files define the connections and 
dependencies between containers, plus the order in which they must be started. 
A minimal TANGO system consisting of a MariaDB database plus TANGO database 
server can be started and stopped with:

    # start a minimal TANGO system with database and TANGO database server
    # Note: omit '-d' if you want the system to launch in the foreground
    docker-compose -f tango.yml up -d
    # stop the system
    docker-compose -f tango.yml down
    
Additional Docker compose files can be added to the composition to add new
new functions. For instance, to start the TANGO test Java server in addition
to the base system, execute:

    docker-compose -f tango.yml -f tangotest.yml up -d  
     

## Interacting with TANGO devices

### Command line interactions
``itango`` can be used for command line interactions with the system. To make
itango available, add it to the system composition, e.g.,

    docker-compose -f tango.yml -f tangotest.yml -f itango.yml up -d
    
An example session that attaches the shell to itango and interacts with the 
Java test device server follows:

    docker attach itango
    In [1]: dev = DeviceProxy('sys/tg_test/1')

    In [2]: dev.string_scalar
    Out[2]: 'Default string'

    ...
    
To detach from the session without quitting the itango session, press the key
combination <CTRL+P><CTRL+Q>.   
    
    
### GUI interactions    
Graphical applications such as Jive can be launched using docker-compose too. 
The Jive container sends X11 traffic to the address defined by the ``MY_IP``
variable, which must be defined before the system composition is started.
Thereafter, Jive can be launched by adding jive.yml to the system composition,
e.g.,

    export MY_IP=172.16.10.120
    docker-compose -f tango.yml -f tangotest.yml -f jive.yml up -d

The IP address information can be persisted by adding it to the .env file in 
this directory.
