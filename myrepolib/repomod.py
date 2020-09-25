from flask import Flask, render_template, request
#from google.cloud import bigquery
from google.cloud import automl_v1beta1
#import os 
#from flask import jsonify



def myfunc():
    return 1

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    '''abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service_key.json'
    client = bigquery.Client()
    QUERY = (
    'SELECT country_name FROM `myrepo-290018.434project.covid` WHERE date = "2020-08-30" LIMIT 1')
    query_job = client.query(QUERY) 
    result = query_job.result() 
    for item in result:
        a = item[0] 
    print(a,result)'''
    return render_template('hello.html') #, a = a) #jsonify(value = "Hello 434 class!", test=a) 



@app.route('/test', methods=["GET", "POST"])
def test():
    '''abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service_key.json'''
    if request.method == 'POST':
        param1 =  request.form['Param1']
        param2 =  request.form['Param2']
        param3 =  request.form['Param3']
        param4 =  request.form['Param4']
        param5 =  request.form['Param5']
        param6 =  request.form['Param6']
        param7 =  request.form['Param7']
        result= [param1,param2,param3,param4,param5,param6,param7]
        labels = ['CGPA','GRE','LOR','Research','SOP','TOEFL','University Rating']

        #Send this data to GCP AutoML and have it return the prediction
        automl_client = automl_v1beta1.TablesClient(project = 'myrepo-290018',region = 'us-central1')
        inputs = {'CGPA':param1,'gre':param2,'LOR':param3,'Research':param4,'SOP':param5,'toefl':param6,'universityrating':param7}
        response = automl_client.predict(model_display_name='admission', inputs=inputs)
        for annotation_payload in response.payload:
            pred_value = annotation_payload.tables.value
            
    return render_template('test.html', result= zip(result,labels), prediction= round(pred_value * 100,2))

if __name__ == '__main__':
    app.run(debug=True)
