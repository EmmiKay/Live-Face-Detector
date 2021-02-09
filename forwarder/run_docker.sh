#!/usr/bin/env bash

docker run --name nx_forward \
--network hw03_local \
--rm -ti \
forwarder
