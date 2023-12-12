from flask import Flask, abort
from elasticapm.contrib.flask import ElasticAPM
import mysql.connector
import time

app = Flask(__name__)

# Configure Elastic APM
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'MyApp',
    'SECRET_TOKEN': '',  # if APM server requires a token
    'SERVER_URL': 'http://replace_me_with_apm_server_ip:8200',
    'ENVIRONMENT': 'test',
}
apm = ElasticAPM(app)

# MySQL connection details
db_config = {
    'user': 'apm_user',
    'password': 'replace_me_with_db_password',
    'host': '127.0.0.1',
    'database': 'testdb'
}

@app.route('/')
def index():
    # Create a MySQL connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Sample query
    cursor.execute("SELECT * FROM test_table")
    results = cursor.fetchall()

    # Simulating a delay
    time.sleep(2)

    cursor.close()
    conn.close()
    return str(results)

# Route for a complex query to test Latency
@app.route('/complex-query')
def complex_query():
    # Create a MySQL connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Complex query
    cursor.execute("SELECT a.*, b.* FROM test_table a CROSS JOIN test_table b")
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return str(results)

# Route to simulate a failed database transaction
@app.route('/failed-transaction')
def failed_transaction():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Start a transaction
        conn.start_transaction()

        # Deliberately cause a failure (e.g., syntax error, invalid operation)
        cursor.execute("INVALID SQL STATEMENT")

        # Commit the transaction
        conn.commit()
        return "Transaction committed"
    except Exception as e:
        # Rollback in case of failure
        conn.rollback()
        return "Transaction failed: " + str(e)
    finally:
        cursor.close()
        conn.close()

# Route to simulate a 500 Internal Server Error
@app.route('/internal-error')
def internal_error():
    raise Exception("This is a simulated internal server error.")

# Route to simulate a 404 Not Found Error
@app.route('/not-found')
def not_found():
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)