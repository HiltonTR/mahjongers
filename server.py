from main import main
from flask import Flask
from flask import render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select")
def select():
    return render_template("select.html")

@app.route("/form",  methods=['POST'])
def restaurants():
    content = request.json
    print(content)
    #process content and return content content should be a dictionary
    #data = main(content)
    response = jsonify(data) #data
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


