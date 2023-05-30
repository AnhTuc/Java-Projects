from flask import Flask
#To run flask app with python
#M1: python -m flask --app file_name run
#M2: flask --app filename run

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "</p>Hello, World!</p>"