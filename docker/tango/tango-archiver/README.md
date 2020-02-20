# Tango-archiver Docker Containers

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)


# 1: Introduction
The EventSubscriber TANGO device server, or Archiver, is the archiving system engine. It contains mainly two components 
Event Subscriber and Configuration Manager. It subscribes to archive events on request by the Configuration Manager 
device and stores the configuration into the TANGO database. The EventSubscriber is designed to start archiving all 
the already configured attributes, even if the Configuration Manager is not running. Moreover, being a TANGO device, the
EventSubscriber configuration can be managed with Jive.

# 2: Prerequisites - Installation
* HDB++ library: libhdbpp
* HDB++ mysql library: libhdbpp-mysql
* HDB++ configuration manager: hdbpp-cm
* HDB++ event subscriber: hdbpp-es
* HDB++ viewer: hdbpp-viewer
* [HDB++ Installation Manual](https://docs.google.com/document/d/1QP3pU62j1v7RWvHeX72JG3s8FqgsCg-bD74xDLP2bSY/edit#heading=h.pqr2e1svlqll) 
* [Link to HDB++ github repository](https://github.com/tango-controls-hdbpp)

# 3: Creating docker containers for archiver
## 3.1: hdbpp-es 
hdbpp-es is a Event Suscriber device server container.
[Link to hdbpp-es github repository](https://github.com/tango-controls-hdbpp/hdbpp-es)
nexus.engageska-portugal.pt/ska-docker/tango-archiver image with tag 'latest' is used for creating hdbpp-es container.
TANGO_HOST=${TANGO_HOST}, HdbManager=archiving/hdbpp/confmanager01 are the environment variables set at the time of 
creating this container. The containers such as databaseds, archiver-dsconfig and maria-db should be up and running, 
for the hdbpp-es container to start.
 
## 3.2: hdbpp-cm
hdbpp-cm is a Configuration manager device server container.
[Link to hdbpp-cm github repository](https://github.com/tango-controls-hdbpp/hdbpp-cm)
nexus.engageska-portugal.pt/ska-docker/tango-archiver image with tag 'latest' is used to create hdbpp-cm container. 
TANGO_HOST=${TANGO_HOST}, HdbManager=archiving/hdbpp/confmanager01 are the environment variables set at the time of 
creating this container. The containers such as databaseds, archiver-dsconfig and maria-db should be up and running,
for the hdbpp-cm container to start.

## 3.3: dsconfig
The data file, 'archiver-devices.json' runs in this container to configure all the TMC devices properties. 
nexus.engageska-portugal.pt/ska-docker/tango-dsconfig image with tag 'latest' is used in this container.
TANGO_HOST=${TANGO_HOST} is the environment variable set inside this container at the time of creation.

# 4: Running tango-archiver inside docker containers

The tango-archiver is tested on dockers using the following command inside the ./tango-archiver

`make test`
