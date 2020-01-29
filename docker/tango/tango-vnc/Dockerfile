#
# This Dockerfile builds Tango including Java apps and libraries in an
# intermediate image, then creates a release image containing the compiled
# binaries.
#
ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-java:latest

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