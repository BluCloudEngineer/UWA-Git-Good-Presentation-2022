#!/bin/bash

# This bash script is used during the DeployCode stage of
# the pipeline. The AWS CodeDeploy agent uses this script to
# run the Docker container on the EC2 instance

docker run -d --rm -p 80:5000 uwagitgoodwebapp:latest
