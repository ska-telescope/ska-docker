ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-cpp:latest

USER root

RUN apt-get update && \
    apt-get install -y ca-certificates

RUN echo "deb http://deb.debian.org/debian buster-backports main contrib non-free" >> /etc/apt/sources.list && \
    more /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
        checkinstall \
        git \
        cmake \
        make \
        g++ \
        libomniorb4-dev \
        libzmq3-dev \
        libcos4-dev \
        mariadb-server \
        libmariadb-dev-compat libmariadb-dev \
        libmariadbclient-dev 

RUN git clone -b v1.0.0 --depth 1 https://github.com/tango-controls-hdbpp/libhdbpp.git

RUN cd libhdbpp \
 && mkdir build \
 && cd build \
 && cmake .. -DHDBPP_DEV_INSTALL=ON -DCMAKE_INCLUDE_PATH=/usr/local/include/tango \
 && make -j4

RUN cd libhdbpp/build \
 && checkinstall \
    --install=yes \
    --fstrans=no \
    --showinstall=no \
    --backup=no \
    --type=debian \
    --pkgsource="https://github.com/tango-controls-hdbpp/libhdbpp" \
    --pkglicense="LGPLv3" \
    --deldesc=no \
    --nodoc \
    --strip \
    --stripso \
    --maintainer="tango" \
    --pkgarch=$(dpkg --print-architecture) \
    --pkgversion="1.0.0" \
    --pkgrelease="SNAPSHOT" \
    --pkgname="libhdbpp" \
    --requires="libzmq5,libomniorb4-2,libcos4-2,libomnithread4" \
    make install

RUN git clone -b v1.1.0 --depth 1 https://github.com/tango-controls-hdbpp/libhdbpp-mysql.git

RUN cd libhdbpp-mysql \
 && make TANGO_INC=/usr/local/include/tango

RUN cd libhdbpp-mysql \
 && checkinstall \
    --install=yes \
    --fstrans=no \
    --showinstall=no \
    --backup=no \
    --type=debian \
    --pkgsource="https://github.com/tango-controls-hdbpp/libhdbpp-mysql" \
    --pkglicense="LGPLv3" \
    --deldesc=no \
    --nodoc \
    --strip \
    --stripso \
    --maintainer="tango" \
    --pkgarch=$(dpkg --print-architecture) \
    --pkgversion="1.1.0" \
    --pkgrelease="SNAPSHOT" \
    --pkgname="libhdbpp-mysql" \
    --requires="libmariadbclient-dev" \
    make install

RUN git clone -b v1.0.1 --depth 1 https://github.com/tango-controls-hdbpp/hdbpp-es.git

RUN cd hdbpp-es \
 && make TANGO_INC=/usr/local/include/tango

RUN cd hdbpp-es \
 && checkinstall \
    --install=yes \
    --fstrans=no \
    --showinstall=no \
    --backup=no \
    --type=debian \
    --pkgsource="https://github.com/tango-controls-hdbpp/hdbpp-es" \
    --pkglicense="GPLv3" \
    --deldesc=no \
    --nodoc \
    --strip \
    --stripso \
    --maintainer="tango" \
    --pkgarch=$(dpkg --print-architecture) \
    --pkgversion="1.0.1" \
    --pkgrelease="SNAPSHOT" \
    --pkgname="hdbpp-es" \
    --requires="libzmq5,libomniorb4-2,libcos4-2,libomnithread4" \
    make install

RUN git clone -b v1.0.0 --depth 1 https://github.com/tango-controls-hdbpp/hdbpp-cm.git

RUN cd hdbpp-cm \
 && make TANGO_INC=/usr/local/include/tango

RUN cd hdbpp-cm \
 && checkinstall \
    --install=yes \
    --fstrans=no \
    --showinstall=no \
    --backup=no \
    --type=debian \
    --pkgsource="https://github.com/tango-controls-hdbpp/hdbpp-cm" \
    --pkglicense="GPLv3" \
    --deldesc=no \
    --nodoc \
    --strip \
    --stripso \
    --maintainer="tango" \
    --pkgarch=$(dpkg --print-architecture) \
    --pkgversion="1.0.0" \
    --pkgrelease="SNAPSHOT" \
    --pkgname="hdbpp-cm" \
    --requires="libzmq5,libomniorb4-2,libcos4-2,libomnithread4" \
    make install


RUN apt-get update && \
    apt-get install -y \
    build-essential && \
    apt-get clean

RUN dpkg -i /libhdbpp/build/libhdbpp_1.0.0-SNAPSHOT_amd64.deb
RUN dpkg -i /libhdbpp-mysql/libhdbpp-mysql_1.1.0-SNAPSHOT_amd64.deb
RUN dpkg -i /hdbpp-es/hdbpp-es_1.0.1-SNAPSHOT_amd64.deb
RUN dpkg -i /hdbpp-cm/hdbpp-cm_1.0.0-SNAPSHOT_amd64.deb

RUN ldconfig

RUN mv /usr/local/bin/hdb++cm-srv /usr/local/bin/hdbppcm-srv
RUN mv /usr/local/bin/hdb++es-srv /usr/local/bin/hdbppes-srv
