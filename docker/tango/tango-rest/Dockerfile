ARG DOCKER_REGISTRY_HOST
ARG DOCKER_REGISTRY_USER
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest

USER root

RUN runtimeDeps='default-jre supervisor' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/*

RUN MTANGOREST_VERSION=rc4-2.12 \
    && MTANGOREST_DOWNLOAD_URL=https://github.com/Ingvord/mtangorest.server/releases/download/mtangorest.server-$MTANGOREST_VERSION/mtangorest.server-$MTANGOREST_VERSION.jar \
    && buildDeps='curl' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /usr/local/lib/tango \
    && cd /usr/local/lib/tango \
    && curl -fsSL "$MTANGOREST_DOWNLOAD_URL" -o mtangorest.jar \
    && apt-get purge -y --auto-remove $buildDeps

COPY tango_register_device.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/tango_register_device.sh

# Configure supervisord. Ensure supervisord.conf contains entries for your device!
COPY supervisord.conf /etc/supervisor/conf.d/

# Start supervisor as daemon
CMD ["/usr/bin/supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]
