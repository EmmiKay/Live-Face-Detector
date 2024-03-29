# Live Face Detector
Built on the Jetson Xavier NX

This project was built as a mostly unguided project for the UC Berkeley Masters in Information and Data Science. The project was practice in using trained models running remotely on an IoT device to detect faces. A camera was plugged into the Jetson which would recognize faces, clip them from the video feed, and drop them into an Amazon S3 bucket.

## Order of operations:
Each of these gets run in a separate terminal window. Make sure to set up the
hw03 network on the jetson and in the cloud first!
#### Spin up the broker on the Jetson
```
cd jetson_broker
./create_image.sh --first time only
./run_docker.sh
```
#### Spin up the broker on the cloud
```
cd cloud_broker
./create_image.sh --first time only
./run_docker.sh
```
#### Spin up the message forwarder on the Jetson
```
cd forwarder
./create_image.sh --first time only
./run_docker.sh
```
#### Spin up the image processor on the cloud
Also need to download s3fs to your EC2 instance and mount the bucket there.
```
cd im_proc
./create_image.sh --first time only
./run_docker.sh

s3fs mids-251-hw3-eb /s3/bucket -o passwd_file=/etc/passwd-s3fs
df -h
cd im_proc
python3 im_proc.py
```
#### Spin up the camera and face detector on the jetson
```
cd camera
./create_image.sh --first time only
./run_docker.sh
```
