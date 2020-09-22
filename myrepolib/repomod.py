from flask import Flask
from flask import jsonify
from google.cloud import bigquery


logging.basicConfig()
def myfunc():
    return 1

app = Flask(__name__)

try:
    client = bigquery.Client()

    # Perform a query.
    QUERY = (
        'SELECT * FROM `myrepo-290018.434project.covid`'
        'LIMIT 10')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    #for row in rows:
        #print(row.name)

    @app.route('/')
    def hello():
        for row in rows:
            a = row.name
        return jsonify(value = "Hello 434 class!", test=a)
except google.auth.exceptions.DefaultCredentialsError: 
    @app.route('/')
    def hello():
        return jsonify(value = "Hello 434 class!")

if __name__ == '__main__':
    app.run()