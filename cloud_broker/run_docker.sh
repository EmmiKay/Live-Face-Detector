#!/usr/bin/env bash

docker run --name cloud_broker \
--network hw03 \
-p 1883:1883 \
--rm -ti \
cl_broker
