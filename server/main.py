from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS
import database as db
import random
app = Flask(__name__)
CORS(app)

user_tokens = {}

@app.route('/sign-up', methods = ['POST'])
def sign_up():
	try:
		email = str(request.form['email'])
		password = str(request.form['password'])
		name = str(request.form['name'])
		try:
			age = int(request.form['age'])
		except Exception:
			return jsonify(result = 0)

		location = str(request.form['location'])
		gender = str(request.form['gender'])
		reddit = str(request.form['reddit'])
		
		result = db.add_user(email, password, name, age, location, gender, reddit)
		return jsonify(result = result)
	except Exception:
		return jsonify(result = 0)


@app.route('/login', methods = ['POST'])
def login():
	try:
		email = str(request.form['email'])
		password = str(request.form['password'])
		if (db.authenticate(email, password)):
			user_tokens[email] = ''.join([random.choice('0123456789abcdef') for n in xrange(30)])
			return jsonify(token = user_tokens[email], result = 1)
		else:
			return jsonify(result = 0)
	except Exception:
		return jsonify(result = 0)