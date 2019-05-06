FROM mariadb:10

# Remove warnings when using apt-get noninteractively
ARG DEBIAN_FRONTEND=noninteractive

ARG tango_version="9.2.5a"
RUN tango_download_url=https://netcologne.dl.sourceforge.net/project/tango-cs/tango-$tango_version.tar.gz && \
    build_deps='curl' && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends $build_deps && \
    mkdir -p /usr/src/tango && \
    cd /usr/src/tango && \
    curl -fsSL "$tango_download_url" -o tango.tar.gz && \
    tar xf tango.tar.gz -C /usr/src/tango --strip-components=1 && \
    mkdir -p dbinit/include && \
    cp cppserver/database/create_db.sql.in dbinit/create_db.sql && \
    cp cppserver/database/create_db_tables.sql.in dbinit/include/create_db_tables.sql && \
    cp cppserver/database/stored_proc.sql.in dbinit/include/stored_proc.sql && \
    sed -i "s|@TANGO_DB_NAME@|tango|g" dbinit/create_db.sql && \
    sed -i "s|@TANGO_DB_NAME@|tango|g" dbinit/include/create_db_tables.sql && \
    sed -i "s|@TANGO_DB_NAME@|tango|g" dbinit/include/stored_proc.sql && \
    sed -i "s|^source create_db_tables.sql$|source /docker-entrypoint-initdb.d/include/create_db_tables.sql|g" dbinit/create_db.sql && \
    sed -i "s|^source stored_proc.sql$|source /docker-entrypoint-initdb.d/include/stored_proc.sql|g" dbinit/create_db.sql && \
    sed -i "/CREATE DATABASE tango;/d" dbinit/create_db.sql && \
    cp -r dbinit/* /docker-entrypoint-initdb.d && \
    rm -r /usr/src/tango/* && \
    apt-get -y purge --auto-remove $build_deps && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY sql_mode.cnf /etc/mysql/conf.d

LABEL \
    author="A Developer <a.developer@.com>" \
    description="This image contains the Tango database" \
    license="Apache2.0" \
    repository="ska-telescope/ska-docker" \
    vendor="SKA Organisation" \
    version="0.1.2" \
    website="http://github.com/ska-telescope/ska-docker"
