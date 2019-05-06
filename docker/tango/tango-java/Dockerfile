#
# This Dockerfile builds Tango including Java apps and libraries in an
# intermediate image, then creates a release image containing the compiled
# binaries.
#
ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-dependencies:latest as buildenv

# Remove warnings when using apt-get noninteractively
ARG DEBIAN_FRONTEND=noninteractive

ARG tango_version="9.2.5a"
RUN tango_download_url=https://netcologne.dl.sourceforge.net/project/tango-cs/tango-$tango_version.tar.gz && \
    build_deps='build-essential curl file libmariadbclient-dev libmariadbclient-dev-compat default-jdk pkg-config python libsodium18 libsodium-dev' && \
    # Speed up image builds by adding apt proxy if detected on host
    dockerhost=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` && \
    /usr/local/bin/wait-for-it.sh --host=$dockerhost --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$dockerhost:3142\";" > /etc/apt/apt.conf.d/30proxy && \
    echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" && \
    mkdir -p /usr/share/man/man1 && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $build_deps && \
    mkdir -p /usr/src/tango && \
    cd /usr/src/tango && \
    curl -fsSL "$tango_download_url" -o tango.tar.gz && \
    tar xf tango.tar.gz -C /usr/src/tango --strip-components=1 && \
    ./configure --with-zmq=/usr/local --with-omni=/usr/local --with-mysqlclient-prefix=/usr --enable-static=no && \
    make -C /usr/src/tango -j$(nproc) && \
    make -C /usr/src/tango install && \
    ldconfig && \
    rm -r /usr/src/tango/* && \
    rm -f /etc/apt/apt.conf.d/30proxy && \
    apt-get -y purge --auto-remove $build_deps && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

FROM debian:stretch-slim
COPY --from=buildenv /usr/local /usr/local

RUN runtime_deps='default-jre-headless libmariadbclient18 sudo' && \
    # Speed up image builds by adding apt proxy if detected on host
    dockerhost=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` && \
    mkdir -p /usr/share/man/man1 && \
    /usr/local/bin/wait-for-it.sh --host=$dockerhost --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$dockerhost:3142\";" > /etc/apt/apt.conf.d/30proxy && \
    echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $runtime_deps && \
    rm -f /etc/apt/apt.conf.d/30proxy && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i -e '/^assistive_technologies=/s/^/#/' /etc/java-*-openjdk/accessibility.properties

RUN useradd --create-home --home-dir /home/tango tango

RUN echo "tango ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/tango && \
    chmod 0440 /etc/sudoers.d/tango

USER root

# Extend the java image with Firefox so that Pogo help can be displayed
RUN runtime_deps='firefox-esr' && \
    # Speed up image builds by adding apt proxy if detected on host
    dockerhost=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` && \
    /usr/local/bin/wait-for-it.sh --host=$dockerhost --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$dockerhost:3142\";" > /etc/apt/apt.conf.d/30proxy && \
    echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host" && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $runtime_deps && \
    rm -f /etc/apt/apt.conf.d/30proxy && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER tango

ENTRYPOINT ["/usr/local/bin/pogo"]

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This image builds the TANGO JAVA dependencies" \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.1.2" \
    website="http://github.com/ska-telescope/ska-docker"
