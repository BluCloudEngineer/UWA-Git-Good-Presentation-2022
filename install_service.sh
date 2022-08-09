#!/bin/bash
pwd
ls -lha
env
docker build -t uwagitgoodwebapp -f /tmp/webapp/Dockerfile .
