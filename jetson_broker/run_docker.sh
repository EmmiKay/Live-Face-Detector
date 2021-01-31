#!/usr/bin/env bash

#make sure bridge is there
./create_network_bridge.sh > /dev/null 2>&1

docker run --name nx_broker \
--network hw03 \
-p 1883:1883 \
--rm -ti \
mqtt_broker
