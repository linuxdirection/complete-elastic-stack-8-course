#!/bin/bash

# Update and upgrade packages
apt-get update
apt-get upgrade -y

# Install necessary package
apt-get install apt-transport-https -y

# Check if Public Signing Key is already added
if ! apt-key list | grep -q "Elasticsearch"; then
    # Download and install the Public Signing Key
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
fi

# Check if repository definition already exists
if ! grep -q "deb https://artifacts.elastic.co/packages/8.x/apt stable main" /etc/apt/sources.list.d/elastic-8.x.list 2> /dev/null; then
    # Save the repository definition
    echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-8.x.list
fi

# Check if /etc/certs directory exists
if [ ! -d /etc/certs ]; then
    # If it does not exist, create it
    mkdir /etc/certs
    cp /tmp/http_ca.crt /etc/certs/http_ca.crt
else
    # If it exists, print a message
    echo "/etc/certs directory already exists."
fi
