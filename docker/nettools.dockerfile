FROM ubuntu
RUN apt-get update
RUN apt-get install -yq traceroute
RUN apt-get install -yq netcat
RUN apt-get install -yq tcpdump
EXPOSE 5555
EXPOSE 6666
EXPOSE 7777
