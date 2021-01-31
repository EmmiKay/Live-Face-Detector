#!/usr/bin/env bash

sudo s3fs mids-251-hw3-eb /mnt/mids-251-hw3-eb -o nonempty  -o passwd_file=/home/ubuntu/.s3fs-creds,nonempty -o sigv2 -o use_path_request_style -o url=https://s3.us-east.objectstorage.softlayer.net

docker run --name imgage_proc \
--network hw03 \
--rm -ti \
-v /mnt/mids-251-hw3-eb:/mnt/mids-251-hw3-eb:rw \
persist_msg:latest
