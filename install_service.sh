#!/bin/bash

# This bash script is used during the DeployCode stage of
# the pipeline. The AWS CodeDeploy agent uses this script to
# build the Docker container on the EC2 instance

cd /tmp/webapp
docker build -t uwagitgoodwebapp .
