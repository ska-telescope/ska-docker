FROM mariadb:10

ENV TANGO_VERSION=9.2.5a
ENV TANGO_DOWNLOAD_URL=https://netcologne.dl.sourceforge.net/project/tango-cs/tango-$TANGO_VERSION.tar.gz                                                                    

RUN buildDeps='curl' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/tango \
    && cd /usr/src/tango \
    && curl -fsSL "$TANGO_DOWNLOAD_URL" -o tango.tar.gz \
    && tar xf tango.tar.gz -C /usr/src/tango --strip-components=1 \
    && mkdir -p dbinit/include \
    && cp cppserver/database/create_db.sql.in dbinit/create_db.sql \
    && cp cppserver/database/create_db_tables.sql.in dbinit/include/create_db_tables.sql \
    && cp cppserver/database/stored_proc.sql.in dbinit/include/stored_proc.sql \
    && sed -i "s|@TANGO_DB_NAME@|tango|g" dbinit/create_db.sql \
    && sed -i "s|@TANGO_DB_NAME@|tango|g" dbinit/include/create_db_tables.sql \
    && sed -i "s|@TANGO_DB_NAME@|tango|g" dbinit/include/stored_proc.sql \
    && sed -i "s|^source create_db_tables.sql$|source /docker-entrypoint-initdb.d/include/create_db_tables.sql|g" dbinit/create_db.sql \
    && sed -i "s|^source stored_proc.sql$|source /docker-entrypoint-initdb.d/include/stored_proc.sql|g" dbinit/create_db.sql \
    && sed -i "/CREATE DATABASE tango;/d" dbinit/create_db.sql \
    && cp -r dbinit/* /docker-entrypoint-initdb.d \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /usr/src/tango

COPY sql_mode.cnf /etc/mysql/conf.d
