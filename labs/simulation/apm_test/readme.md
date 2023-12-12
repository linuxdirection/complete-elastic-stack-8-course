# Flask Application with Elastic APM and MySQL

This is a Flask application that demonstrates the integration of Elastic APM and MySQL. It includes routes for simulating various types of errors and transactions.

## Installation

```bash
pip install Flask elasticapm mysql-connector-python

## Configuration
ELASTIC_APM_SERVICE_NAME=MyApp
ELASTIC_APM_SERVER_URL=http://replace_me_with_apm_server_ip:8200
ELASTIC_APM_SECRET_TOKEN=replace_me_with_secret_token
ELASTIC_APM_ENVIRONMENT=test

## Usage
python app.py

## Routes

* `/`: Fetch data from the MySQL database and simulate a delay.
* `/complex-query`: Execute a complex query on the MySQL database and return the results.
* `/failed-transaction`: Simulate a failed database transaction.
* `/internal-error`: Raise an internal server error.
* `/not-found`: Simulate a 404 Not Found error.

## Elastic APM

The application uses Elastic APM to monitor and trace its performance. Elastic APM can be used to identify and troubleshoot performance issues in your application.

## MySQL

The application connects to a MySQL database named `testdb` using the credentials `apm_user` and `replace_me_with_db_password`.

