from pymongo import MongoClient

class Model():
	
	def __init__(self) :
		self.client = MongoClient("mongodb+srv://roshan:mrk0099mrk@cluster0.al8qd.mongodb.net/checking?retryWrites=true&w=majority")
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
