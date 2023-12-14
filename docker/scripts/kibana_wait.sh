#!/bin/bash
set -e

# Function to check Elasticsearch health
check_es_health() {
  response=$(curl -s -k --cacert config/certs/ca/ca.crt https://es01:9200 -I | grep "401 Unauthorized")
  if [ -n "$response" ]; then
    echo "Elasticsearch is up but requires authentication (401)."
    return 0
  else
    echo "Elasticsearch is not ready or not returning a 401 status."
    return 1
  fi
}

echo "Waiting for Elasticsearch to be up..."
until check_es_health; do
  echo "Elasticsearch is unavailable - sleeping"
  sleep 10
done

echo "Elasticsearch is up - executing command"
exec /usr/local/bin/kibana-docker
