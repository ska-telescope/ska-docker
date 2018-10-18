FROM debian:stretch

RUN runtimeDeps='libmariadbclient18 doxygen' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/* 

RUN ZEROMQ_VERSION=4.0.5 \
    && ZEROMQ_DOWNLOAD_URL=https://archive.org/download/zeromq_$ZEROMQ_VERSION/zeromq-$ZEROMQ_VERSION.tar.gz \
    && buildDeps='autoconf automake build-essential ca-certificates curl libkrb5-dev libtool pkg-config unzip' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /usr/src/zeromq \
    && cd /usr/src/zeromq \
    && curl -fsSL "$ZEROMQ_DOWNLOAD_URL" -o zeromq.tar.gz \
    && tar xf zeromq.tar.gz -C /usr/src/zeromq --strip-components=1 \
    && ./configure --enable-static=no \
    && make -C /usr/src/zeromq -j$(nproc) \
    && make -C /usr/src/zeromq install \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/zeromq

RUN OMNIORB_DOWNLOAD_URL=https://svwh.dl.sourceforge.net/project/omniorb/omniORB/omniORB-4.2.1/omniORB-4.2.1-2.tar.bz2 \
    && OMNIORB_PATCH_URL=http://ftp.esrf.fr/pub/cs/tango/Patches/dii_race.patch \
    && buildDeps='build-essential ca-certificates curl python-dev' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/omniorb \
    && cd /usr/src/omniorb \
    && curl -fsSL "$OMNIORB_DOWNLOAD_URL" -o omniorb.tar.bz2 \
    && curl -fsSL "$OMNIORB_PATCH_URL" -o dii_race.patch \
    && tar xf omniorb.tar.bz2 -C /usr/src/omniorb --strip-components=1 \
    && patch -p0 < dii_race.patch \
    && ./configure --enable-static=no \
    && make -C /usr/src/omniorb -j$(nproc) \
    && make -C /usr/src/omniorb install \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/omniorb

COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
