ARG http_proxy
ARG https_proxy
FROM nexus.engageska-portugal.pt/ska-docker/ska-python-buildenv:9.3.2

# # # NOTES
# - pip2 crashes if the package we want isn't in the SKA repo,
#     so we temporarily hide the SKA pip.conf 
# - python-qt4 is needed for the panic gui (but not PyAlarm)
# - pip doesn't automically install lxml (needed for GUI but not PyAlarm)
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
        python-qt4 \
    && rm -rf /var/lib/apt/lists/ && \
    ln -s /usr/lib/x86_64-linux-gnu/libboost_python27.so /usr/lib/x86_64-linux-gnu/libboost_python-py27.so && \
    pip2 install panic lxml && \
    sudo mv /tmp/ska_pip_conf /etc/pip.conf && \
    sudo sed -i.original 's/python/python2/g' `which PyAlarm`

# now the VNC stuff (ref. tango-vnc image in ska-docker repo)

USER root

RUN apt-get update && apt-mark hold iptables && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      dbus-x11 \
      psmisc \
      xdg-utils \
      x11-xserver-utils \
      x11-utils && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      xfce4 && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      gtk3-engines-xfce \
      libgtk-3-bin \
      mousepad \
      xfce4-notifyd \
      xfce4-taskmanager \
      xfce4-terminal && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      xfce4-battery-plugin \
      xfce4-clipman-plugin \
      xfce4-cpufreq-plugin \
      xfce4-cpugraph-plugin \
      xfce4-diskperf-plugin \
      xfce4-datetime-plugin \
      xfce4-fsguard-plugin \
      xfce4-genmon-plugin \
      xfce4-indicator-plugin \
      xfce4-netload-plugin \
      xfce4-notes-plugin \
      xfce4-places-plugin \
      xfce4-sensors-plugin \
      xfce4-smartbookmark-plugin \
      xfce4-systemload-plugin \
      xfce4-timer-plugin \
      xfce4-verve-plugin \
      xfce4-weather-plugin \
      xfce4-whiskermenu-plugin && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      libxv1 \
      mesa-utils \
      mesa-utils-extra && \
    sed -i 's%<property name="ThemeName" type="string" value="Xfce"/>%<property name="ThemeName" type="string" value="Raleigh"/>%' /etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml

RUN apt-get update && apt-get install -y \ 
    git \
    x11vnc \
    software-properties-common \
    unzip \
    curl \
    slim \
    xvfb \ 
    novnc \
    python-websockify

#Expose port 5920 to view display using VNC Viewer
EXPOSE 5920
EXPOSE 6081

ENV DISPLAY=:20

CMD Xvfb :20 -screen 0 1366x768x16 & x11vnc -passwd TestVNC -display :20 -N -forever & startxfce4 & websockify --web /usr/share/novnc 6081 localhost:5920 
