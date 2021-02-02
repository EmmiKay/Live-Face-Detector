#!/usr/bin/env bash

docker run --name nx_forward \
--network hw03 \
--rm -ti \
forwarder
