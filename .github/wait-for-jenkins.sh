##!/bin/bash
#
#set -e
#
#times=25
#while ! curl -sSL 'http://localhost:8080/login?from=%2F' 2>&1 \
#             | grep 'Username' >/dev/null; do
#    echo 'Waiting for the Jenkins'
#    sleep 10
#    times=$(($times - 1))
#
#    if [ $times -le 0 ]; then
#        echo 'Time out'
#        exit 1
#    fi
#done
#
#echo 'The Jenkins is up'

#!/bin/bash

set -e

times=40

while true; do
    response=$(curl -u "$JENKINS_USERNAME:$JENKINS_PASSWORD" \
        -s -o /dev/null -w "%{http_code}" \
        http://localhost:8080/crumbIssuer/api/json)

    if [ "$response" = "200" ]; then
        echo "Jenkins is fully ready"
        break
    fi

    echo "Waiting for Jenkins API... status=$response"

    sleep 10
    times=$((times - 1))

    if [ $times -le 0 ]; then
        echo "Timeout waiting for Jenkins"
        exit 1
    fi
done