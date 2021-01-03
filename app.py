from flask import Flask,request,jsonify,render_template,request
import db
from bson import json_util
import json
import bson
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def capitalize(name):
	fix = [i.capitalize() for i in name.split()]
	return " ".join(fix)

@app.route("/")

def home():
	return render_template("index.html")	

@app.route("/<string:name>", methods = ["GET","POST"])

def get(name):
	if request.method == "GET" :
		mongo =db.Model()
		actual_name = capitalize(name)
		details = mongo.finding(actual_name)
		if details != [] :
			print(details)
			return {"details" : details}
		else :
			return "oops couldnt find !!!!!, tip : Try spelling it as it is "	
	else :
		return "<h1>oooppssss....</h1>"		

if __name__ == '__main__':
	app.run(debug=True)

	
