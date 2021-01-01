from flask import Flask,request,jsonify
import db
from bson import json_util
import json
import bson
from flask_restful import Api,Resource,reqparse,abort

app = Flask(__name__)

api = Api(app)

# schema = reqparse.RequestParser(bundle_errors=True)
# schema.add_argument("name", type=str, required=True, help = "type your name and its kinda mandatory")
# schema.add_argument("job", type=str, required=True,help = "type your Job and its kinda mandatory")


# schemaf = reqparse.RequestParser(bundle_errors=True)
# schemaf.add_argument("title", type=str, required=True, help = "type your name and its kinda mandatory")


def capitalize(name):
	fix = [i.capitalize() for i in name.split()]
	return " ".join(fix)

class Hey(Resource):
	def get(self,name):
		mongo =db.Model()
		actual_name = capitalize(name)
		details = mongo.finding(actual_name)
		if details != [] :
			return details
		else :
			return "oops couldnt find !!!!!, tip : Try spelling it as it is "	

	# def put(self,name):
	# 	arrgs = schema.parse_args()
	# 	return{'we got': arrgs}


	# def post(self,name):
	# 	arrgs = schema.parse_args()
	# 	collection.insert_one(arrgs)
	# 	lol.append(arrgs)
	# 	# collection.insert_one(arrgs)
	# 	return {'your msg': "cool" }

api.add_resource(Hey,"/<string:name>")

# if __name__ == '__main__':
#  	app.run(debug=True) 


	
