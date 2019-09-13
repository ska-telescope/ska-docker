#
# This Dockerfile builds Tango including Java apps and libraries in an
# intermediate image, then creates a release image containing the compiled
# binaries.
#
ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-dependencies:latest

RUN JAVA_DOWNLOAD_URL=https://nexus.engageska-portugal.pt/repository/raw/java/jre-8u221-linux-x64.tar.gz \
    && mkdir /usr/java \
    && cd /usr/java \
    && buildDeps='wget sudo libxrender1 libxtst6 libxi6' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $buildDeps \
    && wget --no-check-certificate "$JAVA_DOWNLOAD_URL" -O java.tar.gz \
    && tar zxvf java.tar.gz \
    && update-alternatives --install /usr/bin/java java /usr/java/jre1.8.0_221/bin/java 0 \
    && update-alternatives --set java /usr/java/jre1.8.0_221/bin/java \
    && rm /usr/java/java.tar.gz

RUN TANGO_DOWNLOAD_URL=https://github.com/tango-controls/TangoSourceDistribution/releases/download/9.3.3-rc2/tango-9.3.3-rc2.tar.gz \
    && DOCKERHOST=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` \
    && /usr/local/bin/wait-for-it.sh --host=$DOCKERHOST --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$DOCKERHOST:3142\";" > /etc/apt/apt.conf.d/30proxy \
    && echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" \
    && mkdir -p /usr/share/man/man1 \
    && buildDeps='build-essential curl file libmariadbclient-dev libmariadbclient-dev-compat pkg-config python libmariadb3' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/tango \
    && cd /usr/src/tango \
    && curl -fsSL -k "$TANGO_DOWNLOAD_URL" -o tango.tar.gz \
    && tar xf tango.tar.gz -C /usr/src/tango --strip-components=1 \
    && ./configure --with-zmq=/usr/local --with-omni=/usr/local --with-mysqlclient-prefix=/usr --enable-static=no \
    && make -C /usr/src/tango -j$(nproc) \
    && make -C /usr/src/tango install \
    && ldconfig \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/tango

RUN LOG4J=https://nexus.engageska-portugal.pt/repository/raw/java/log4j-1.2.17.tar.gz \
    && cd /usr/java \
    && wget --no-check-certificate "$LOG4J" -O log4j.tar.gz \
    && tar zxvf log4j.tar.gz \
    && mv apache-log4j-1.2.17/log4j-1.2.17.jar /usr/local/share/java/log4j-1.2.17.jar \
    && apt-get purge -y --auto-remove wget \
    && rm /usr/java/log4j.tar.gz

RUN useradd --create-home --home-dir /home/tango tango

RUN echo "tango ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/tango \
    && chmod 0440 /etc/sudoers.d/tango

USER tango
