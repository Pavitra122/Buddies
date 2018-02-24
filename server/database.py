import pymongo
import personality as pn
from pymongo import MongoClient

client = MongoClient('mongodb://107.170.2.182:27017/')

# Creates user if the user does not exist
# email: string
# name: string
# age: number
# location (city name): string
# gender: string
# reddit (username): string
def add_user(email, name, age, location, gender, reddit):
	db = client.buddy
	users = db.users
	
	# Get information from reddit account first
	personality = pn.get_personality(pn.get_reddit_comments(reddit))

	users.insert_one({
		'email': email,
		'name': name,
		'age': age,
		'location': location,
		'gender': gender,
		'reddit': reddit,
		'personality': personality,
		'description': '',
		'interest': {}
	})

# Sets the user's values to the new values
# email: string
# name: string
# age: number
# location (city name): string
# gender: string
# reddit (username): string
# description: string
# interest: JSON object
def update_user(email, name, age, location, gender, reddit, description, interests):
	if (users.find_one({'email': email}).reddit != reddit):
		personality = pn.get_personality(pn.get_reddit_comments(reddit))
		users.find_one_and_update({'email': email}, {'$set': {'reddit': reddit, 'personality': personality}})

	users.find_one_and_update({'email': email}, {'$set': {
		'name': name,
		'age': age,
		'location': location,
		'gender': gender,
		'description': description,
		'interest': interests
	}})


def get_user(email):
	return users.find_one({'email': email})

if __name__ == '__main__':
	update_user("<email>", "<name>", 18, "<town>", "Male", "<reddit username>")