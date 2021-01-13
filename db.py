from pymongo import MongoClient
import os 
class Model():
	
	def __init__(self) :

		self.client = MongoClient("mongodb+srv://roshan:mrk0099mrk@cluster0.al8qd.mongodb.net/checking?retryWrites=true&w=majority")
		# self.client = MongoClient(os.environ.get('KEY'))
		self.db = self.client["checking"]
		self.collection = self.db["check"]

	#function to find a particular movie 	
	def finding(self,name = "Psycho") :
		info = self.collection.find({"title":name},{"_id" : False})
		return list(info)

	#function to insert movie details 	
	def inserting(self,title,plot,rate) :
		pass				
	
	#funtion to fetch random movies from the database
	def random_movies(self):
		random_movies_list = self.collection.aggregate([{"$sample": {"size" : 1}}])

		redefined_list = list(random_movies_list)

		#removing the ObjectId from the response so as to avoid the "json" error 
		redefined_list[0].pop('_id')
		return(redefined_list)
