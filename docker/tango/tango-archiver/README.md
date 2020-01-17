# Tango-archiver Docker Container

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)


# 1: Introduction
The EventSubscriber TANGO device server, or Archiver, is the archiving system engine. It contains mainly two components 
EventSuscriber and Configuration manager. It will subscribe to archive  events on request by the ConfigurationManager 
device. The EventSubscriber is designed to start archiving all the already configured Attributes, even if the 
ConfigurationManager is not running. Moreover, being a TANGO device, the EventSubscriber configuration can be managed 
with Jive.

# 2: Prerequisites - Installation
* Linux/Ubuntu (18.04 LTS)
* Python 3.6
* [python3-pip](https://packages.ubuntu.com/xenial/python3-pip)
* [Tango (9.2.5a)](https://docs.google.com/document/d/1TMp5n380YMvaeqeKZvRHHXa7yVxT8oBn5xsEymyNFC4/edit?usp=sharing)
* [PyTango (9.2.4)](https://docs.google.com/document/d/1DtuIs1PeYGHlDXx8RyOzZyRQ-_Eiup-ncqeDDCtcNxk/edit?usp=sharing)
* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) (for running the prototype in a containerised environment)
* HDB++ library libhdbpp.
* For complete installation, refer the link: [Link to HDB++ github repository](https://github.com/tango-controls-hdbpp)

# 3: Images required for container creation
* tango-db ({DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-db:latest)
* tango-cpp (DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest)
* tango-java ({DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-java:latest)
* tango-archiver ({DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/archiver:latest)
* tango-dsconfig (nexus.engageska-portugal.pt/ska-docker/tango-dsconfig:latest)

# 4: Creating docker containers for archiver
## 4.1: hdbpp-es 
hdbpp-es is a Event Suscriber device server container.
[Link to hdbpp-es github repository](https://github.com/tango-controls-hdbpp/hdbpp-es)
{DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/archiver image  with tag latest is used for creating hdbpp-es container.
TANGO_HOST=${TANGO_HOST}, HdbManager=archiving/hdbpp/confmanager01  are the enviornments variables set at the time of 
creating this container. The containers such as databaseds, archiver-dsconfig and maria-db should be up and running , 
so that hdbpp-es container will start.
 
## 4.2: hdbpp-cm
hdbpp-cm is a Configuration manager device server container.
[Link to hdbpp-cm github repository](https://github.com/tango-controls-hdbpp/hdbpp-cm)
{DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/archiver image with tag latest is used for creating hdbpp-cm container. 
TANGO_HOST=${TANGO_HOST}, HdbManager=archiving/hdbpp/confmanager01 are the enviornments variables set at the time of 
creating this container. The containers such as databaseds, archiver-dsconfig and maria-db should be up and running ,
so that hdbpp-cm container will start.

## 4.3: archiver-dsconfig
The data file, archiver-devices.json file runs in this container to configure all the TMC devices properties. Image 
nexus.engageska-portugal.pt/ska-docker/tango-dsconfig:latest is used in this container.
TANGO_HOST=${TANGO_HOST} is the eviornment variable set inside this container at the time of creation.

# 5: Running tango-archiver inside Docker containers

 tango-archiver can run on dockers using following command inside the ./tango-archiver

In order to test , execute:

`make test`
