#!/bin/bash
# PANIC launch script
# Set environment variable PANIC_EMAIL to a non-zero value to enable emails.

if [ -n "$PANIC_EMAIL" ] && [ "$PANIC_EMAIL" -ne 0 ]; then
	echo "Enabling email"
	sudo service exim4 start
fi

exec "$@"
