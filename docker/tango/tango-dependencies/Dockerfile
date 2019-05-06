#
# This Dockerfile compiles Tango dependencies (ZeroMQ and OmniORB) in an
# intermediate image, then creates a release image containing the compiled
# binaries.
#
FROM debian:stretch-slim as buildenv

# Copy across files that are used to help orchestrate container compositions
# and test execution sequences
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
COPY retry.sh /usr/local/bin/retry

RUN dockerhost=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` && \
    /usr/local/bin/wait-for-it.sh --host=$dockerhost --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$dockerhost:3142\";" > /etc/apt/apt.conf.d/30proxy && \
    echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host"

ARG omniorb_version="4.2.1-2"
RUN omniorb_download_url=https://svwh.dl.sourceforge.net/project/omniorb/omniORB/omniORB-4.2.1/omniORB-$omniorb_version.tar.bz2 && \
    omniorb_patch_url=http://ftp.esrf.fr/pub/cs/tango/Patches/dii_race.patch && \
    build_deps='build-essential ca-certificates curl python-dev python-pkgconfig' && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $build_deps && \
    mkdir -p /usr/src/omniorb && \
    cd /usr/src/omniorb && \
    curl -fsSL "$omniorb_download_url" -o omniorb.tar.bz2 && \
    curl -fsSL "$omniorb_patch_url" -o dii_race.patch && \
    tar xf omniorb.tar.bz2 -C /usr/src/omniorb --strip-components=1 && \
    patch -p0 < dii_race.patch && \
    ./configure --enable-static=no && \
    make -C /usr/src/omniorb -j$(nproc) && \
    make -C /usr/src/omniorb install && \
    apt-get -y purge --auto-remove $build_deps && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ARG zeromq_version="4.0.5"
RUN zeromq_download_url=https://archive.org/download/zeromq_$zeromq_version/zeromq-$zeromq_version.tar.gz && \
    build_deps='autoconf automake build-essential ca-certificates curl libkrb5-dev libtool pkg-config unzip libsodium18 libsodium-dev' && \
    apt-get -y update && \
    apt-get -y install $build_deps --no-install-recommends && \
    mkdir /usr/src/zeromq && \
    cd /usr/src/zeromq && \
    curl -fsSL "$zeromq_download_url" -o zeromq.tar.gz && \
    tar xf zeromq.tar.gz -C /usr/src/zeromq --strip-components=1 && \
    ./configure --enable-static=no && \
    make -C /usr/src/zeromq -j$(nproc) && \
    make -C /usr/src/zeromq install && \
    apt-get -y purge --auto-remove $build_deps && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

FROM debian:stretch-slim
COPY --from=buildenv /usr/local /usr/local
