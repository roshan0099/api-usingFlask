from flask import Flask,request,jsonify,render_template,request
import db
from bson import json_util
import json
import bson


app = Flask(__name__)

#funtion to capitalize just the first letter of the input movie name
def capitalize(name):
	fix = [i.capitalize() for i in name.split()]
	return " ".join(fix)

#home page
@app.route("/")

def home():
	return render_template("index.html")	

#function to fetch a particular movie from the database according to the user's need
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

#function to fetch random movies from the database		
@app.route("/random")

def random():
	mongo = db.Model()
	movies = mongo.random_movies()

	return {"details" : movies}


if __name__ == '__main__':
	app.run(debug=True)

	
