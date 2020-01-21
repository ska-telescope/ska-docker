# HDB++ Viewer Docker Container

[![Documentation Status](https://readthedocs.org/projects/ska-docker/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-docker/en/latest/?badge=latest)


# 1: Introduction
The HdbViewer GUI visualizes the data stored in the Historical database(HDB). This Java framework, allows 
retrieving the data from Maria database(HDB). It has been written using Swing and needs a JVM higher than 1.7.0. 
[Link to the documentation](https://github.com/tango-controls-hdbpp/hdbpp-viewer) 

# 2: Prerequisites - Installation 
  [Link to hdb++ github repository](https://github.com/tango-controls-hdbpp/hdbpp-viewer)
  
# 3: HDB++ Viewer dockerfile
* Image Location
  * nexus.engageska-portugal.pt/ska-docker/tango-java:latest
* Dependencies
  * TANGO=$BASEDIR/JTango.jar
  * TANGOATK=$BASEDIR/ATKCore.jar:$BASEDIR/ATKWidget.jar
  * HDBVIEWER=$BASEDIR/jhdbviewer.jar
  * HDBPP=$BASEDIR/HDBPP.jar
  * JYTHON=$BASEDIR/jython.jar
  * JCALENDAR=$BASEDIR/jcalendar.jar
* Environment Variables
  * HDB_TYPE=mysql                           //type of database
  * HDB_MYSQL_HOST=archiver-maria-db         //database host (In this case, host is container name) 
  * HDB_MYSQL_PORT=3306                      //database port 
  * HDB_USER=tango                           //database user
  * HDB_PASSWORD=tango                       //user password
  * HDB_NAME=hdbpp                           //database name
* Command line to set the environment variables
  * export HDB_TYPE
  * export HDB_MYSQL_HOST
  * export HDB_USER
  * export HDB_PASSWORD
  * export HDB_NAME
  * export HDB_MYSQL_PORT
  * CLASSPATH=$TANGO:$TANGOATK:$HDBVIEWER:$HDBPP:$JYTHON:$JCALENDAR
  * export CLASSPATH
  
# 4: Container Creation for HDB++ Viewer
nexus.engageska-portugal.pt/ska-docker/hdbpp_viewer image with tag 'latest' is used in the hdbpp-viewer container. 
Databaseds, mariadb, hdbpp-es and hdbpp-cm containers should be up and running to access HDB++ viewer device.
Following are the environment variables set at the time of container creation: XAUTHORITY=${XAUTHORITY}, DISPLAY=${DISPLAY},
TANGO_HOST=${TANGO_HOST}, HDB_TYPE, HDB_MYSQL_HOST, HDB_MYSQL_PORT, HDB_USER, HDB_PASSWORD and HDB_NAME.
Refer the link 
[docker-compose.yaml](https://gitlab.com/ska-telescope/ska-docker/blob/master/docker/tango/tango-archiver/docker-compose.yml)

# 5: Running HDB++ viewer inside docker containers

 HDB++ viewer can run on dockers using following command inside the ./tango-archiver

In order to launch the viewer, execute:

`make test`
