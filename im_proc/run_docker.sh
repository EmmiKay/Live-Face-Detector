#!/usr/bin/env bash

sudo s3fs mids-251-hw3-eb /s3/bucket -o iam_role=mids-hw-3-role

docker run --name im_proc \
--privileged = true \
--network hw03 \
--rm -ti \
-v /mnt/mids-251-hw3-eb:/mnt/mids-251-hw3-eb:rw \
-ti image_proc
