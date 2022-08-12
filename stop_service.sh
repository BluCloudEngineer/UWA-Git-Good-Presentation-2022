#!/bin/bash

# This bash script is used during the DeployCode stage of
# the pipeline. The AWS CodeDeploy agent uses this script to
# kill all running Docker containers, if none are present
# output the following text: "No running Docker containers"

docker stop $(docker ps -a -q) || echo "No running Docker containers"
