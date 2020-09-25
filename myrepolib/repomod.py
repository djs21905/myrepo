from flask import Flask, render_template, request, redirect
from google.cloud import bigquery
#import os 
#from flask import jsonify



def myfunc():
    return 1

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    #abspath = os.path.abspath(__file__)
    #dname = os.path.dirname(abspath)
    #os.chdir(dname)
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service_key.json'
    client = bigquery.Client()
    QUERY = (
    'SELECT country_name FROM `myrepo-290018.434project.covid` WHERE date = "2020-07-14" LIMIT 1')
    query_job = client.query(QUERY) 
    result = query_job.result() 
    for item in result:
        a = item[0] 
    return render_template('hello.html', a = a)

@app.route('/test', methods=["GET", "POST"])
def test():
    if request.method == 'POST':
        param1 =  request.form['Param1']
        param2 =  request.form['Param2']
        param3 =  request.form['Param3']
        param4 =  request.form['Param4']
        result= [param1,param2,param3,param4]

        #Send this data to GCP AutoML and have it return the prediction
    return render_template('test.html', result=result)
    
if __name__ == '__main__':
    app.run()