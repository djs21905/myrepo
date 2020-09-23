from flask import Flask
from flask import jsonify
#from google.cloud import bigquery
#from google.auth import exceptions
#


def myfunc():
    return 1

app = Flask(__name__)

'''try:
    #client = bigquery.Client()

    # Perform a query.
    QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)

    @app.route('/')
    def hello():
        return jsonify(value = "Hello 434 class! test")
except exceptions.DefaultCredentialsError: 
    @app.route('/')
    def hello():
        return jsonify(value = "Hello 434 class!")'''

@app.route('/')
def hello():
        return jsonify(value = "Hello 434 class!")
if __name__ == '__main__':
    app.run()