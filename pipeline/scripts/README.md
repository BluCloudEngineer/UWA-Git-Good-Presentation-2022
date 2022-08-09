# Pipeline Scripts README

## Overview

These scripts are to be used as part of the `DeployCode` stage of the pipeline and are used by AWS CodeDeploy. You do not need to run these scripts on your local machine, but you can if you want.

## Scripts Overview

| Script Name        | Description                                    |
| ------------------ | ---------------------------------------------- |
| install_service.sh | Build the Docker image on the EC2 Instance     |
| start_service.sh   | Run the built Docker image on the EC2 Instance |
| stop_service.sh    | Stop all Docker images on the EC2 Instance     |
