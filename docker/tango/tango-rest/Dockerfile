ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-dependencies:latest as buildenv

RUN MTANGOREST_DOWNLOAD_URL=https://github.com/tango-controls/rest-server/releases/download/rest-server-1.14/rest-server-1.14.jar \
    && DOCKERHOST=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` \
    && /usr/local/bin/wait-for-it.sh --host=$DOCKERHOST --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$DOCKERHOST:3142\";" > /etc/apt/apt.conf.d/30proxy \
    && echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" \
    && buildDeps='ca-certificates curl' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /usr/local/lib/tango \
    && cd /usr/local/lib/tango \
    && curl -fsSL "$MTANGOREST_DOWNLOAD_URL" -o mtangorest.jar \
    && apt-get purge -y --auto-remove $buildDeps

FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-java:latest

COPY --from=buildenv /usr/local/lib/tango/mtangorest.jar /usr/local/lib/tango/mtangorest.jar

USER root

RUN runtimeDeps='supervisor' \
    && mkdir -p /usr/share/man/man1 \
    && DOCKERHOST=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` \
    && /usr/local/bin/wait-for-it.sh --host=$DOCKERHOST --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$DOCKERHOST:3142\";" > /etc/apt/apt.conf.d/30proxy \
    && echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/30proxy

COPY tango_register_device.sh /usr/local/bin/

# Configure supervisord. Ensure supervisord.conf contains entries for your device!
COPY supervisord.conf /etc/supervisor/conf.d/

# Start supervisor as daemon
CMD ["/usr/bin/supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]
