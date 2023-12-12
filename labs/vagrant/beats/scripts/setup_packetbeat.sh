#!/bin/bash

# Update and install packetbeat
apt-get update && apt-get install packetbeat -y

# Copy the packetbeat.yml and http_ca.crt to their proper locations
cp /tmp/packetbeat.yml /etc/packetbeat/packetbeat.yml

# Enable packetbeat service (but do not start it yet)
systemctl enable packetbeat

# Start packetbeat
systemctl start packetbeat
