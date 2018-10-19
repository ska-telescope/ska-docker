FROM ska/tango-java:latest

USER root

# Extend the java image with Firefox so that Pogo help can be displayed
RUN runtimeDeps='firefox-esr' \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends $runtimeDeps \
    && rm -rf /var/lib/apt/lists/*

USER tango

CMD ["/usr/local/bin/pogo"]

