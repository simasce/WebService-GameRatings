from flask import Flask, render_template, request, url_for, jsonify, make_response
from flask_cors import CORS
from datetime import datetime
import pymysql
import time

class GameRating:
	def __init__(self, id, name, source, rating, comment):
		self.ID = id
		self.Name = name
		self.Source = source
		self.Rating = rating
		self.Comment = comment
		
	def serialize(self):
		return {
			'id': self.ID, 
			'name': self.Name,
			'source': self.Source,
			'rating': self.Rating,
			'comment': self.Comment,
		}
		
db = None
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
				 
def printd(str):
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")
	print(timestampStr + " : " + str, flush=True)
	
def load_db():
	global db
	db_retries = 20
	while db_retries > 0:
		try:
			db = pymysql.connect('database', 'ratings_user', 'pw_ratings', 'rating_database')
			if db != None:
				break			
		except:
			printd("Retrying database connection: %d retries remaining!" % db_retries)
			db_retries -= 1
			time.sleep(2) #wait 2 seconds				
			
	if db == None:
		raise Exception("Failed to connect to the database!")
	printd("Successful database connection!")
	
def fetch_class(result_rows):
	if len(result_rows) < 1:
		return []
	ret_arr = []
	for row in result_rows:
		if len(row) < 5:
			continue
		try:
			rating_int = row[3]
		except ValueError:
			continue
		
		ret_arr.append(GameRating(row[0], row[1], row[2], rating_int, row[4]))
	return ret_arr
	
@app.route("/swagger_api.json", methods=['GET'])
def send_swagger():  
	return app.send_static_file("swagger_api.json")
	
@app.route("/api/v1/resources/ratings/", methods=["GET"])
def all_ratings():
	cursor = db.cursor()
	sql = "SELECT * FROM ratings"
	cursor.execute(sql)
	results = cursor.fetchall()
	classes = fetch_class(results)
	serialized=[e.serialize() for e in classes]
	return jsonify(serialized)
	
@app.route("/api/v1/resources/ratings/", methods=["POST"])
def add_rating():
	qargs = request.args
	name = qargs.get("name")
	source = qargs.get("source")
	comment = qargs.get("comment")
	if name == None or source == None or comment == None:
		return "Bad request, not enough arguments specified", 400	
	try:
		rating = qargs.get("rating")
		if rating == None:
			return "Bad request, rating not specified", 400
		rating_i = int(rating)
		if rating_i < 0 or rating_i > 5:
			return "Bad request, rating must be between 0 and 5", 400
	except ValueError:
		return "Bad request, rating is not a number", 400	
		
	cursor = db.cursor()
	sql = "INSERT INTO ratings VALUES(DEFAULT, %s,%s,%s,%s)"
	cursor.execute(sql, (name,source,rating,comment))
	db.commit()
	if cursor.lastrowid <= 0:
		return "Could not insert item!", 500
	
	return rating_get(cursor.lastrowid)
	
@app.route("/api/v1/resources/ratings/<int:id>", methods=["PUT"])
def rating_update(id):
	qargs = request.args
	name = qargs.get("name")
	source = qargs.get("source")
	comment = qargs.get("comment")
	if name == None or source == None or comment == None:
		return "Bad request, not enough arguments specified", 400	
	try:
		rating = qargs.get("rating")
		if rating == None:
			return "Bad request, rating not specified", 400
		rating_i = int(rating)
		if rating_i < 0 or rating_i > 5:
			return "Bad request, rating must be between 0 and 5", 400
	except ValueError:
		return "Bad request, rating is not a number", 400	
		
	cursor = db.cursor()
	sql = "UPDATE ratings SET Name=%s,Source=%s,Rating=%s,Comment=%s WHERE ID = %s"
	cursor.execute(sql, (name,source,rating,comment,id))
	db.commit()
	if cursor.rowcount <= 0:
		return "Could not find such item", 404
	return rating_get(id)
	
@app.route("/api/v1/resources/ratings/<int:id>", methods=["GET"])
def rating_get(id):
	try:
		int_test = int(id)
	except ValueError:
		return "Bad request, ID is not a number", 400
		
	cursor = db.cursor()
	sql = "SELECT * FROM ratings WHERE ID = %s"
	cursor.execute(sql, id)
	results = cursor.fetchall()
	if len(results) < 1:
		return "Could not find such item", 404
	
	classes = fetch_class(results)
	serialized=[e.serialize() for e in classes]
	return jsonify(serialized)

@app.route("/api/v1/resources/ratings/<int:id>", methods=["DELETE"])
def rating_delete(id):
	cursor = db.cursor()
	sql = "DELETE FROM ratings WHERE ID = %s"
	cursor.execute(sql, (id))
	db.commit()
	if cursor.rowcount <= 0:
		return "Could not find such item", 404
	return "Item deleted!"
	
@app.route("/")
def index():
	cursor = db.cursor()
	sql = "SELECT * FROM ratings"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("index.html", ratings=results)
	
	
if __name__ == "__main__":
	printd("Starting WebService application!")
	load_db()
	app.run(host="0.0.0.0", port=5000, debug=True)