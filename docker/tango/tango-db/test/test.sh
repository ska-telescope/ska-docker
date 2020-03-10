#!/bin/bash

result=$(mysql -h $1 -u tango -ptango <<< 'show databases')

if [[ $result =~ "tango" ]]
then
	echo "PASSED"
else
	echo "ERROR"
	exit 1
fi
