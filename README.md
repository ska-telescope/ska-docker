# TANGO Docker containers

This project defines a set of Docker images and Docker compose files
that are useful for TANGO control system development.
See the documentation in the 'docs' folder for build and usage
instructions.


## Complete Archiver Implementation

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)


Docker images such as tango-archiver, mariadb and hdb++ viewer are used for archiving various attributes and states of 
tango devices. Containers like mariadb, databaseds, hdbpp-es, hdbpp-cm should be up and running. HDB++ is a historical 
database used to store the archived attributes values. Here maria database with default schema of hdp++ is used to store 
the archived values.
Hdbpp-es is event suscriber device is in charge of gathering the values from the Tango devices and storing them into the
database (mariadb). Hdbpp-cm is a configuration manager server. It configures the attributes to be archived and defines
which Event Subscriber is responsible for a set of Tango attributes to be archived.
Hdbpp-viewer shows the picturial representation of archived attributes, which are stored in maria database.

# Important links
 * [Link for Mariadb container](https://gitlab.com/ska-telescope/ska-docker/tree/story_AT1-422/docker/tango/mariadb_hdbpp)
 * [Link for Tango-archiver container](https://gitlab.com/ska-telescope/ska-docker/tree/story_AT1-422/docker/tango/tango-archiver)
 * [Link for Hdbpp-viewer container](https://gitlab.com/ska-telescope/ska-docker/tree/story_AT1-422/docker/tango/hdbpp_viewer)
 * [Docker-compose yaml](https://gitlab.com/ska-telescope/ska-docker/blob/story_AT1-422/docker/tango/tango-archiver/docker-compose.yml)