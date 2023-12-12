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

## MySQL Setup on Ubuntu

This README provides instructions on how to install MySQL on Ubuntu, create a new database and user, and source a database schema from a `schema.sql` file.

## Installing MySQL on Ubuntu

Follow these steps to install MySQL on your Ubuntu system:

1. **Update Package Index:**
   ```bash
   sudo apt update
   ```

2. **Install MySQL Server:**
   ```bash
   sudo apt install mysql-server
   ```

3. **Secure MySQL Installation (Optional but Recommended):**
   This step involves setting a root password, removing anonymous users, disallowing remote root login, and removing the test database.
   ```bash
   sudo mysql_secure_installation
   ```

## Creating a MySQL Database and User

After installing MySQL, you can create a new database and a user with specific privileges:

1. **Log in to MySQL:**
   ```bash
   sudo mysql
   ```

2. **Create a New Database:**
   Replace `your_database_name` with your desired database name.
   ```sql
   CREATE DATABASE your_database_name;
   ```

3. **Create a New User with a Password:**
   Replace `your_username` and `your_password` with your desired username and password.
   ```sql
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   ```

4. **Grant Privileges to the New User:**
   ```sql
   GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
   ```

5. **Flush Privileges and Exit:**
   ```sql
   FLUSH PRIVILEGES;
   EXIT;
   ```

## Sourcing Database from `schema.sql`

To source your database schema from a file named `schema.sql`, follow these steps:

1. **Navigate to the Directory Containing `schema.sql`:**
   ```bash
   cd /path/to/directory
   ```

2. **Source the Schema File:**
   Make sure you replace `your_database_name` with the name of your database.
   ```bash
   mysql -u your_username -p your_database_name < schema.sql
   ```

   When prompted, enter the password for `your_username`.

## Verifying the Setup

To verify that your database has been set up correctly:

1. **Log in to MySQL:**
   ```bash
   mysql -u your_username -p
   ```

2. **Select Your Database:**
   ```sql
   USE your_database_name;
   ```

3. **Show Tables in the Database:**
   ```sql
   SHOW TABLES;
   ```

This process will confirm whether the tables have been created successfully from the `schema.sql` file.

---

