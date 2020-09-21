def myfunc():
    return 1

#Testing a pass


from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(value = "Hello 434 class!")

if __name__ == '__main__':
    app.run()