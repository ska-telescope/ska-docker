ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-java:latest

USER root

# Extend the java image with Firefox so that Pogo help can be displayed
RUN runtimeDeps='firefox-esr' \
    && DOCKERHOST=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` \
    && /usr/local/bin/wait-for-it.sh --host=$DOCKERHOST --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$DOCKERHOST:3142\";" > /etc/apt/apt.conf.d/30proxy \
    && echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/30proxy

# Pogo is included in tango source distribution, but replace with a newer version
# Official source:  https://bintray.com/tango-controls/maven/Pogo/_latestVersion
RUN buildDeps='wget' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $buildDeps \
    && POGO_DOWNLOAD_URL=https://nexus.engageska-portugal.pt/repository/raw/tango-cs/pogo/Pogo-9.6.31.jar \
    && cd /usr/local/share/java \
    && rm -f Pogo-*.jar \
    && wget --no-check-certificate "$POGO_DOWNLOAD_URL" -O Pogo-9.6.31.jar \
    && ln -sf Pogo-9.6.31.jar Pogo.jar

USER tango

CMD ["/usr/local/bin/pogo"]

