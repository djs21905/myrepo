from flask import Flask
from flask import jsonify
from google.cloud import bigquery
from google.auth import exceptions
#


def myfunc():
    return 1

app = Flask(__name__)

try:
    client = bigquery.Client()

    # Perform a query.
    '''QUERY = (
        'SELECT * FROM `myrepo-290018.434project.covid`'
        'LIMIT 10')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish'''

    @app.route('/')
    def hello():
        print("the master branch")
        return jsonify(value = "Hello 434 class! test")
except exceptions.DefaultCredentialsError: 
    print("the non master branch")
    @app.route('/')
    def hello():
        return jsonify(value = "Hello 434 class!")

if __name__ == '__main__':
    app.run()