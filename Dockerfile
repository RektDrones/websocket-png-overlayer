FROM ubuntu:15.04
RUN apt-get update && apt-get install -y python-pip virtualenv python2.7-dev
ENV VERSION 3 #dummy version to force a rebuild from here
ADD app /app
WORKDIR /app
RUN /app/install.sh
EXPOSE 5000
USER nobody
ENTRYPOINT  /app/run.sh
