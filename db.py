from pymongo import MongoClient
import os 
class Model():
	
	def __init__(self) :

		self.client = MongoClient(os.environ.get('KEY'))
		self.db = self.client["checking"]
		self.collection = self.db["check"]
	def finding(self,name = "Psycho") :
		data = []
		info = self.collection.find({"title":name},{"_id" : False})
		return list(info)
	def inserting(self,title,plot,rate) :
		pass				
	
	