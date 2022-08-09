#!/bin/bash
docker stop $(docker ps -a -q) || echo "No running Docker containers"
