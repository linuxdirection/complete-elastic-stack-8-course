# Elastic Stack Docker Deployment

## Overview
This Docker Compose setup is designed to deploy an Elastic Stack cluster, including Elasticsearch nodes and Kibana, with SSL configuration and user authentication. It's intended for environments where you want to quickly spin up an Elastic Stack cluster with security features enabled.

## Configuration
The deployment can be customized using environment variables defined in the `.env` file. Below are the variables that you can adjust:

- `ELASTIC_PASSWORD`: Password for the `elastic` superuser. Must be at least 6 characters.
- `KIBANA_PASSWORD`: Password for the `kibana_system` user. Must be at least 6 characters.
- `STACK_VERSION`: Version of Elastic Stack components (Elasticsearch, Kibana, etc.) to deploy.
- `CLUSTER_NAME`: Name of your Elasticsearch cluster.
- `LICENSE`: License type for Elastic Stack. Set to `basic` for the free version or `trial` for a 30-day trial of premium features.
- `ES_PORT`: Host port to expose Elasticsearch's HTTP API. Defaults to `9200`.
- `KIBANA_PORT`: Host port to expose Kibana. Defaults to `5601`.
- `MEM_LIMIT`: Memory limit for each service in the cluster, specified in bytes. Adjust based on your host's capacity.

## Starting the Cluster
To start the cluster, navigate to the directory containing the `docker-compose.yml` and `.env` files, and run:

```bash
docker-compose up -d

This command will start all services defined in the `docker-compose.yml` file in detached mode.

## Stopping the Cluster
To stop the cluster, run:

```bash
docker-compose down

This command stops and removes the containers, networks, and volumes created by `docker-compose up`.

## Caution
This setup includes an initial service (`setup`) to generate SSL certificates and set user passwords.
Ensure the `.env` file is properly configured before starting the services. Also,
be aware that using `docker-compose down` will remove the containers and their data.
For persistent data storage, ensure your data volumes are configured correctly.
