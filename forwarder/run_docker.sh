#!/usr/bin/env bash

docker run --name nx_forward \
--network hw03 \
-p 1883:1883 \
--rm -ti \
forwarder
