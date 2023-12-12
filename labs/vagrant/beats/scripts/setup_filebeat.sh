#!/bin/bash

# Update and install filebeat
apt-get update && apt-get install filebeat -y

# Copy the filebeat.yml and http_ca.crt to their proper locations
cp /tmp/filebeat.yml /etc/filebeat/filebeat.yml

# Enable filebeat service (but do not start it yet)
systemctl enable filebeat

# Start filebeat
systemctl start filebeat
