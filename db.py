from pymongo import MongoClient

class Model():
	
	def __init__(self) :
		self.client = MongoClient("")
		self.db = self.client["checking"]
		self.collection = self.db["check"]
	def finding(self,name = "Psycho") :
		data = []
		info = self.collection.find({"title":name},{"_id" : False})
		return list(info)

	def inserting(self,title,plot,rate) :
		pass				
	
	

# say = {"movie": "james bond", "code" : "007"})

# print(say)
