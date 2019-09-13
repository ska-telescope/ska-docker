#
# This Dockerfile compiles Tango dependencies (ZeroMQ and OmniORB) in an
# intermediate image, then creates a release image containing the compiled
# binaries.
#
FROM debian:buster-slim as buildenv

# Copy across files that are used to help orchestrate container compositions
# and test execution sequences
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
COPY retry.sh /usr/local/bin/retry

RUN DOCKERHOST=`awk '/^[a-z]+[0-9]+\t00000000/ { printf("%d.%d.%d.%d", "0x" substr($3, 7, 2), "0x" substr($3, 5, 2), "0x" substr($3, 3, 2), "0x" substr($3, 1, 2)) }' < /proc/net/route` \
    && /usr/local/bin/wait-for-it.sh --host=$DOCKERHOST --port=3142 --timeout=3 --strict --quiet -- echo "Acquire::http::Proxy \"http://$DOCKERHOST:3142\";" > /etc/apt/apt.conf.d/30proxy \
    && echo "Proxy detected on docker host - using for this build" || echo "No proxy detected on docker host"

RUN ZEROMQ_DOWNLOAD_URL=https://github.com/zeromq/libzmq/archive/v4.3.2.tar.gz \
    && buildDeps='autoconf automake build-essential ca-certificates curl libkrb5-dev libtool pkg-config unzip' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /usr/src/zeromq \
    && cd /usr/src/zeromq \
    && curl -kfsSL "$ZEROMQ_DOWNLOAD_URL" -o zeromq.tar.gz \
    && tar xf zeromq.tar.gz -C /usr/src/zeromq --strip-components=1 \
    && ./autogen.sh \
    && ./configure --enable-static=no \
    && make -C /usr/src/zeromq -j$(nproc) \
    && make -C /usr/src/zeromq install \
    && rm -r /usr/src/zeromq


RUN CPPZMQ_DOWNLOAD_URL=https://github.com/zeromq/cppzmq/archive/v4.4.1.tar.gz \
    && buildDeps='autoconf automake build-essential ca-certificates curl libkrb5-dev libtool pkg-config unzip cmake' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /usr/src/cppzmq \
    && cd /usr/src/cppzmq \
    && curl -kfsSL "$CPPZMQ_DOWNLOAD_URL" -o cppzmq.tar.gz \
    && tar xf cppzmq.tar.gz -C /usr/src/cppzmq --strip-components=1 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j4 install \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/cppzmq

RUN OMNIORB_DOWNLOAD_URL=https://nexus.engageska-portugal.pt/repository/raw/omniorb/omniORB-4.2.3.tar.bz2 \
    && buildDeps='build-essential ca-certificates curl python-dev python-pkgconfig' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/omniorb \
    && cd /usr/src/omniorb \
    && curl -kfsSL "$OMNIORB_DOWNLOAD_URL" -o omniorb.tar.bz2 \
    && tar xf omniorb.tar.bz2 -C /usr/src/omniorb --strip-components=1 \
    && ./configure --enable-static=no \
    && make -C /usr/src/omniorb -j$(nproc) \
    && make -C /usr/src/omniorb install \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/omniorb

FROM debian:buster-slim
COPY --from=buildenv /usr/local /usr/local

