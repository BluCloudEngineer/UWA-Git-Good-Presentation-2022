#!/bin/bash
flaskId=$(ps aux | grep -i python | grep -i flask | awk '{print $2}')
kill $flaskId
exit 0
