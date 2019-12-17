#!/bin/bash

export TANGO_HOST=databaseds:10000

tango_admin --ping-database 20
result=$?

if [ $result -eq 0 ]
then
	echo "PASSED ping database"
else
	echo "ERROR ping database"
	exit 1
fi


tango_admin --check-device sys/tg_test/1
result=$?

if [ $result -eq 0 ]
then
	echo "PASSED check device tg_test"
else
	echo "ERROR check device tg_test"
	exit 1
fi

tango_admin --check-device sys/database/2
result=$?

if [ $result -eq 0 ]
then
	echo "PASSED check device database"
else
	echo "ERROR check device database"
	exit 1
fi
