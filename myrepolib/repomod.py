from flask import Flask
from flask import jsonify
#from google.cloud import bigquery
from google.auth import exceptions
#


def myfunc():
    return 1

app = Flask(__name__)

try:
    #client = bigquery.Client()

    # Perform a query.


    @app.route('/')
    def hello():
        return jsonify(value = "Hello 434 class! test")
except exceptions.DefaultCredentialsError: 
    @app.route('/')
    def hello():
        return jsonify(value = "Hello 434 class!")

if __name__ == '__main__':
    app.run()