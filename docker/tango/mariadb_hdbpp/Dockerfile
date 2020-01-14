FROM nexus.engageska-portugal.pt/ska-docker/tango-db:latest

COPY resources/create_hdb++_mysql.sql docker-entrypoint-initdb.d/create_db.sql
COPY resources/my.cnf /etc/mysql/conf.d

