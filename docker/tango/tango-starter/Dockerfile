FROM ska/tango-cpp:latest

USER root

# supervisor is installed so that the TANGO Starter device runs on startup
RUN runtimeDeps='supervisor' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/*

COPY tango_register_device.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/tango_register_device.sh

# Configure supervisord. Ensure supervisord.conf contains entries for your device!
COPY supervisord.conf /etc/supervisor/conf.d/

# Start supervisor as daemon
CMD ["/usr/bin/supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]

