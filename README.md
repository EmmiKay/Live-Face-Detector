# 251_HW3
project for MIDS w251 HW3

## Order of operations:
Each of these gets run in a separate terminal window. Make sure to set up the
hw03 network first!
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
```
cd im_proc
./create_image.sh --first time only
./run_docker.sh
```
#### Spin up the camera and face detector on the jetson
```
cd camera
./create_image.sh --first time only
./run_docker.sh
```
