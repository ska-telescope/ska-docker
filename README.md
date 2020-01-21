# TANGO Docker containers

This project defines a set of Docker images and Docker compose files
that are useful for TANGO control system development.
See the documentation in the 'docs' folder for build and usage
instructions.


## HDB++ Archiver Implementation

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)


HDB++ is a archiver available in TANGO. It is configured to subscribe to TANGO attributes to be archived. MariaDB 
provides the archival database. HDB++ default schema is used to store the archived data. It consists of the following 
components:
The Hdbpp-es is a event suscriber device which subscribes to the Tango attributes. Multiple instances of the event 
subscriber are deployed to support large number of attributes. These attributes could belong to multiple TANGO Devices.
The Hdbpp-cm provides the configuration manager. It allows to configure the attributes to be archived and defines which
Event Subscriber is responsible for a set of Tango attributes to be archived. 
Hdbpp-viewer shows the graphical representation of the archived data, which is stored in the data archive. 

The archiever solution comprises of the following Docker images:

Tango-archiver(hdbpp-es and hdbpp-cm), Mariadb and Hdb++ viewer 

Containers like mariadb, databaseds, hdbpp-es and hdbpp-cm should be up and running in order to work HDB++ archiver solution. 



# Important links
 * [Link for Mariadb container](https://gitlab.com/ska-telescope/ska-docker/tree/story_AT1-422/docker/tango/mariadb_hdbpp)
 * [Link for Tango-archiver container](https://gitlab.com/ska-telescope/ska-docker/tree/story_AT1-422/docker/tango/tango-archiver)
 * [Link for Hdbpp-viewer container](https://gitlab.com/ska-telescope/ska-docker/tree/story_AT1-422/docker/tango/hdbpp_viewer)
 * [Docker-compose yaml](https://gitlab.com/ska-telescope/ska-docker/blob/story_AT1-422/docker/tango/tango-archiver/docker-compose.yml)