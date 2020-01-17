# Hdbpp_viewer Docker Container

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)


# 1: Introduction
The HdbViewer GUI visualizes the data stored in the Historical database(HDB). This Java framework, allows 
retrieving the data from Maria database(HDB). It has been written using Swing and need a JVM higher than 1.7.0. 
Link to the documentation: 

# 2: Prerequisites - Installation 
  [Link to hdb++ github repository](https://github.com/tango-controls-hdbpp/hdbpp-viewer)
  
# 3: HDB++ viewer dockerfile
* Base image 
  * nexus.engageska-portugal.pt/ska-docker/tango-java:latest
* Dependencies
  * TANGO=$BASEDIR/JTango.jar
  * TANGOATK=$BASEDIR/ATKCore.jar:$BASEDIR/ATKWidget.jar
  * HDBVIEWER=$BASEDIR/jhdbviewer.jar
  * HDBPP=$BASEDIR/HDBPP.jar
  * JYTHON=$BASEDIR/jython.jar
  * JCALENDAR=$BASEDIR/jcalendar.jar
* Enviornment Variables
  * HDB_TYPE=mysql
  * HDB_MYSQL_HOST=archiver-maria-db
  * HDB_MYSQL_PORT=3306
  * HDB_USER=tango
  * HDB_PASSWORD=tango
  * HDB_NAME=hdbpp
* Command line to set the environment variables
  * export HDB_TYPE
  * export HDB_MYSQL_HOST
  * export HDB_USER
  * export HDB_PASSWORD
  * export HDB_NAME
  * export HDB_MYSQL_PORT
  * CLASSPATH=$TANGO:$TANGOATK:$HDBVIEWER:$HDBPP:$JYTHON:$JCALENDAR
  * export CLASSPATH
  
# 4: Container creation for HDB++ archiver
For HDB++ container, image {DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/hdbpp-viewer with tag latest is used for creation. The containers such as databaseds, mariadb, hdbpp-es and hdbpp-cm should be up and running.
XAUTHORITY=${XAUTHORITY}, DISPLAY=${DISPLAY}, TANGO_HOST=${TANGO_HOST}, HDB_TYPE=mysql, HDB_MYSQL_HOST=archiver-maria-db, HDB_MYSQL_PORT=3307, HDB_USER=tango, HDB_PASSWORD=tango, and HDB_NAME=hdbpp are the enviornment variables set at the time of creating this container.
Volume for this container is {XAUTHORITY_MOUNT}.

# 5: Running HDB++ viewer inside docker containers

 HDB++ viewer can run on dockers using following command inside the ./tango-archiver

In order to test , execute:

`make test`
