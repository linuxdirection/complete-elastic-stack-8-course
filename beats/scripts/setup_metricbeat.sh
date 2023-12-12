#!/bin/bash

# Update and install Metricbeat
apt-get update && apt-get install metricbeat -y

# Copy the metricbeat.yml and http_ca.crt to their proper locations
cp /tmp/metricbeat.yml /etc/metricbeat/metricbeat.yml

# Enable Metricbeat service (but do not start it yet)
systemctl enable metricbeat

# Start Metricbeat
systemctl start metricbeat
