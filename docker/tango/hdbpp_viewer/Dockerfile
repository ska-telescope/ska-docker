FROM nexus.engageska-portugal.pt/ska-docker/tango-java:latest
USER root
RUN apt-get update
RUN apt-get install -y --force-yes wget

RUN mkdir hdbpp_viewer \
 && cd hdbpp_viewer \
 && ls \
 && wget -O jython.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jython.jar \
 && wget -O HDBPP.jar https://bintray.com/tango-controls/maven/download_file?file_path=org%2Ftango%2Flibhdbpp-java%2F1.25%2Flibhdbpp-java-1.25.jar \
 && wget -O ATKCore.jar ftp://ftp.esrf.eu/pub/cs/tango/Atk/ATKCore.jar \
 && wget -O ATKWidget.jar ftp://ftp.esrf.eu/pub/cs/tango/Atk/ATKWidget.jar \
 && wget -O jcalendar.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jcalendar.jar \
 && wget -O jhdbviewer.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jhdbviewer.jar \
 && wget -O JTango.jar https://sourceforge.net/projects/tango-cs/files/JTango/JTango-9.0.3/JTango-9.0.3.jar/download \
 && ls
RUN ls
ADD hdbpp_viewer_script hdbpp_viewer
RUN cd hdbpp_viewer \
 && ls
RUN find . -iname HDBPP.jar
RUN find . -iname ATKCore.jar



