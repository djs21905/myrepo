from flask import Flask
from flask import jsonify
from google.cloud import bigquery
#import os 




def myfunc():
    return 1

app = Flask(__name__)

@app.route('/')
def hello():
    #abspath = os.path.abspath(__file__)
    #dname = os.path.dirname(abspath)
    #os.chdir(dname)
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service_key.json'
    client = bigquery.Client()
    QUERY = (
    'SELECT country_name FROM `myrepo-290018.434project.covid` WHERE date = "2020-07-08" LIMIT 1')
    query_job = client.query(QUERY) 
    result = query_job.result() 
    for item in result:
        a = item[0] 
    print(a,result)
    return jsonify(value = "Hello 434 class!", test= a)
if __name__ == '__main__':
    app.run()