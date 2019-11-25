FROM registry.gitlab.com/s2innovation/tangobox-docker/tangobox-base:latest AS build

RUN apt update \
 && apt install -y \
    checkinstall \
    git \
    cmake \
    make \
    g++ \
    libomniorb4-dev \
    libzmq3-dev \
    libcos4-dev \
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
    --requires="libmariadbclient18" \
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

FROM registry.gitlab.com/s2innovation/tangobox-docker/tangobox-base:latest

RUN apt update \
 && apt install -y \
    libmariadbclient18 \
    mariadb-client \
    mariadb-server \
 && apt clean

COPY --from=build \
    /libhdbpp/build/libhdbpp_1.0.0-SNAPSHOT_amd64.deb \
    /libhdbpp-mysql/libhdbpp-mysql_1.1.0-SNAPSHOT_amd64.deb \
    /hdbpp-es/hdbpp-es_1.0.1-SNAPSHOT_amd64.deb \
    /hdbpp-cm/hdbpp-cm_1.0.0-SNAPSHOT_amd64.deb \
    /

RUN dpkg -i libhdbpp_*.deb
RUN dpkg -i libhdbpp-mysql_*.deb
RUN dpkg -i hdbpp-es_*.deb
RUN dpkg -i hdbpp-cm_*.deb

RUN ldconfig

COPY resources/create_hdb++.sql /
COPY resources/my.cnf /etc/mysql/
COPY resources/supervisord.conf /etc/supervisord.conf

RUN bash -c "mysqld_safe --defaults-file=/etc/mysql/my.cnf &" \
 && sleep 5 \
 && mysql -u root < /create_hdb++.sql \
 && sleep 10 \
 && mysql -u root -D hdbpp < /usr/local/share/libhdb++mysql/create_hdb++_mysql.sql \
 && sleep 60 \
 && mysql -u root -D hdbpp -e "CREATE USER 'tango'@'%' identified by 'tango';"\
 && sleep 10 \
 && mysql -u root -D hdbpp -e  "GRANT ALL PRIVILEGES ON hdbpp.* To 'tango'@'%' IDENTIFIED BY 'tango' WITH GRANT OPTION;" \
 && sleep 5 \
 && mysql -u root -D hdbpp -e  "FLUSH PRIVILEGES;" \
 && sleep 5

#RUN find / -iname hdb++*
RUN mv /usr/local/bin/hdb++cm-srv /usr/local/bin/hdbppcm-srv
RUN mv /usr/local/bin/hdb++es-srv /usr/local/bin/hdbppes-srv

RUN find / -iname libhdb++*.so*.*

CMD /usr/bin/supervisord -c /etc/supervisord.conf
