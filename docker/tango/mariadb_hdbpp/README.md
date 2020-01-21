# Mariadb Docker Container

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)

# 1: Introduction
The archiver database provides the repository of historical values of attributes, observation states, alarms and data associated 
with other events generated during the control and monitoring of Telescope. 
Mariadb is the database name, which stores the archived data. It is a separate database, other than the tango database. 
The Tango events are subscribed by the hdbpp-es (hdbpp event subscriber) and written to the archive database. 
Mariadb uses the default schema of HDB++ (refer to 'create_hdb++_mysql.sql' file), for storing archived data. 

# 2: Creating Mariadb docker containers
 nexus.engageska-portugal.pt/ska-docker/mariadb_hdbpp image with 'latest' tag is used to create Mariadb container. 
 MYSQL_DATABASE=hdbpp,  MYSQL_USER=tango, MYSQL_PASSWORD=tango, TANGO_HOST=${TANGO_HOST} are the environment variables set 
 at the time of mariadb container creation. 'archiverdb' is the permanent volume required for storing the database file.

# 3: Running Mariadb inside docker containers

The archiver database is brought up and running on dockers using the following command inside the ./tango-archiver

`make test`
