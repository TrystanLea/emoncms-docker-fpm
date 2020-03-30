FROM python:3.8-slim

ARG EMONHUB_DIR

RUN apt-get update && apt-get install -y git python3-pip
RUN pip3 install configobj paho-mqtt requests serial

RUN git clone -b python3 https://github.com/openenergymonitor/emonhub.git ${EMONHUB_DIR}
