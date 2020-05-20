# TANGO Docker containers

This project defines a set of Docker images and Docker compose files
that are useful for TANGO control system development.
See the documentation in the 'docs' folder for build and usage
instructions.


## Docker hierarchy and release tagging

When updating Dockerfiles, and especially the tags in the `.release` files,
it is useful to know the hierarchy.  All downstream images must have the release
tags updated.

The release tags should match the underlying dependencies used.  E.g., for the
first release of cppTango 9.3.4-rc4, use the tag `9.3.4-rc4`.  If there are
subsequent modifications to a Dockerfile, but still using that cppTango release,
add a suffix, e.g., `9.3.4-rc4.1`.  Further changes would then incremenent that
suffix: `9.3.4-rc4.2`, etc.

- ubuntu
  - deploy/Dockerfile:FROM ubuntu:18.04
  - tango-builder/Dockerfile:FROM ubuntu:18.04
- debian-buster-slim
  - tango-dependencies/Dockerfile:FROM debian:buster-slim as buildenv
  - tango-dependencies/Dockerfile:FROM debian:buster-slim
    - tango-java/Dockerfile:FROM {nexus}/tango-dependencies:latest
        - hdbpp_viewer/Dockerfile:FROM {nexus}/tango-java:latest
        - tango-jive/Dockerfile:FROM {nexus}/tango-java
        - tango-pogo/Dockerfile:FROM {nexus}/tango-java:latest
        - tango-rest/Dockerfile:FROM {nexus}/tango-dependencies:latest as buildenv
        - tango-rest/Dockerfile:FROM {nexus}/tango-java:latest
        - tango-vnc/Dockerfile:FROM {nexus}/tango-java:latest
    - tango-cpp/Dockerfile:FROM {nexus}/tango-dependencies:latest as buildenv
    - tango-cpp/Dockerfile:FROM debian:buster-slim
      - tango-archiver/Dockerfile:FROM {nexus}/tango-cpp:latest
      - tango-dsconfig/Dockerfile:FROM {nexus}/tango-cpp:latest
      - tango-libtango/Dockerfile:FROM {nexus}/tango-cpp
        - tango-admin/Dockerfile:FROM {nexus}/tango-libtango:latest
        - tango-test/Dockerfile:FROM {nexus}/tango-libtango:latest
        - tango-databaseds/Dockerfile:FROM {nexus}/tango-libtango:latest
      - ska-python-buildenv/Dockerfile:FROM {nexus}/tango-cpp:latest
        - ska-python-runtime/Dockerfile:FROM {nexus}/ska-python-buildenv:latest as buildenv
        - ska-python-runtime/Dockerfile:FROM {nexus}/tango-cpp:latest
          - tango-itango/Dockerfile:FROM {nexus}/ska-python-buildenv:latest as buildenv
          - tango-itango/Dockerfile:FROM {nexus}/ska-python-runtime:latest
          - tango-pytango/Dockerfile:FROM {nexus}/ska-python-buildenv:latest as buildenv
          - tango-pytango/Dockerfile:FROM {nexus}/ska-python-runtime:latest
          - tango-vscode/Dockerfile:FROM {nexus}/ska-python-buildenv:latest as buildenv
          - tango-vscode/Dockerfile:FROM {nexus}/ska-python-runtime:latest
      - tango-starter/Dockerfile:FROM {nexus}/tango-cpp:latest
- mariadb
  - tango-db/Dockerfile:FROM mariadb:10
    - mariadb_hdbpp/Dockerfile:FROM {nexus}/tango-db:latest


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
