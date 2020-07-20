ARG http_proxy
ARG https_proxy
FROM nexus.engageska-portugal.pt/ska-docker/ska-python-buildenv:9.3.2

# # # NOTES
# - pip2 crashes if the package we want isn't in the SKA repo,
#     so we temporarily hide the SKA pip.conf 
# - exim4 is used for email alerts (configuration to be applied by user)
# - Format of boost library name was apparently changed between 1.65 and 1.67,
#     so we make a symlink
# - panic uses python 2, but 'python' maps to python3 in our base image,
#     so we use sed to edit the PyAlarm launcher
RUN [ ! -z "$http_proxy" ] && \
        sudo echo "Acquire::http::Proxy \"$http_proxy\";" > /etc/apt/apt.conf.d/30proxy ||  \
        echo "no proxy" && \
    sudo mv /etc/pip.conf /tmp/ska_pip_conf && \
    DEBIAN_FRONTEND=noninteractive && sudo apt update && \
    sudo apt install -y \
        python2.7 \
        python-pip \
        exim4 \
    && rm -rf /var/lib/apt/lists/ && \
    ln -s /usr/lib/x86_64-linux-gnu/libboost_python27.so /usr/lib/x86_64-linux-gnu/libboost_python-py27.so && \
    pip2 install panic && \
    sudo mv /tmp/ska_pip_conf /etc/pip.conf && \
    sudo sed -i.original 's/python/python2/g' `which PyAlarm`

COPY aliases /etc/
COPY update-exim4.conf.conf /etc/exim4/
COPY entrypoint.sh /app/
ENTRYPOINT ["/app/entrypoint.sh"]
