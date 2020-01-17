# Mariadb Docker Container

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)

# 1: Introduction
 Mariadb is a database other than tango database, which is used to store the atrributes , observation states etc of TMC 
 devices which have been archived at the time of command execution or generation of event on hdbpp-es(hdbpp event 
 suscriber). Mariadb uses the default schema of hdb++(refer create_hdb++_mysql.sql file), to store the attributes. 

# 3: Images required for container creation
* tango-db ({DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-db:latest)
* tango-cpp (DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest)
* tango-java ({DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-java:latest)
* mariadb_hdbpp ({DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/mariadb_hdbpp:latest)

# 4: Creating mariadb docker containers
 Image '{DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/mariadb_hdbpp' with tag:latest  is used to create Mariadb 
 container. MYSQL_DATABASE=hdbpp,  MYSQL_USER=tango,  MYSQL_PASSWORD=tango, TANGO_HOST=${TANGO_HOST} are the enviornments
 variables set at the time of mariadb container creation. archiverdb is the permenent volume required.

# 5: Running mariadb inside docker containers

mariadb can run on dockers using following command inside the ./tango-archiver

In order to test , execute:

`make test`
