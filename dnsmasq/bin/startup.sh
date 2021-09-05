#!/bin/bash

# Check if dnsmasq is running, if not, start the dnsmasq service. 

SERVICE="dnsmasq"

if pgrep -x "$SERVICE" > /dev/null
then
    echo "$(date +"%b %d,%Y%l:%M:%S%P"), $SERVICE is active"
else
    echo "$(date +"%b %d,%Y%l:%M:%S%P"), $SERVICE is inactive, starting service."
    systemctl daemon-reload && systemctl start dnsmasq
fi


