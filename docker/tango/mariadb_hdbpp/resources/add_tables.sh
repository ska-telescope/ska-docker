#!/bin/bash

echo "Adding tables to MariaDB"
echo "Adding HDB++..."
mysql -u root -D hdbpp < /usr/share/libhdb++mysql/create_hdb++_mysql.sql
