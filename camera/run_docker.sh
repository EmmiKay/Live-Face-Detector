#!/usr/bin/env bash

xhost +
docker run --name nx_cam \
--network hw03 \
-e DISPLAY --privileged -v /tmp:/tmp --rm -ti detector
