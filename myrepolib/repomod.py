from flask import Flask
from flask import jsonify
from google.cloud import bigquery
import os
#from google.auth import exceptions
#



def myfunc():
    return 1

app = Flask(__name__)

'''try:
    #client = bigquery.Client()

    # Perform a query.
    QUERY = (
    'SELECT country_name FROM `myrepo-290018.434project.covid` WHERE date = '2020-07-07' LIMIT 1)
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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service_key.json'
    client = bigquery.Client()
    QUERY = (
    'SELECT country_name FROM `myrepo-290018.434project.covid` WHERE date = "2020-07-07" LIMIT 1')
    query_job = client.query(QUERY) 
    result = query_job.result()  
    return jsonify(value = "Hello 434 class!", test=result)
if __name__ == '__main__':
    app.run()