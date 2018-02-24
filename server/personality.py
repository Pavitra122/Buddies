import praw
import requests

reddit = praw.Reddit(client_id = 'bcvTpNZBqRi6JA', client_secret = '0X9bSPMRqaJEXnX1fkzlUbjx5rA', user_agent = 'Web:app:1.0 (by /u/uiucbuddyapp)')

# Produces a long chained paragraph of a person's Reddit comments
def get_reddit_comments(username):
	person = reddit.redditor(username)
	paragraph = ''
	for comment in person.comments.new(limit = None):
		paragraph += comment.body.replace('\n', ' ') + '. '
	paragraph = paragraph.replace('"', '')
	paragraph = paragraph.replace('\\', '')
	return paragraph.encode('utf-8')

# Returns a JSON array with the 5 personality traits in it (also as JSON objects)
def get_personality(text):
	username = '6857df7a-9739-411c-901f-1a27d8be2ae3'
	password = 'iyUH0PnPtWr0'
	res = requests.post(url = 'https://gateway.watsonplatform.net/personality-insights/api/v3/profile?version=2017-10-13&consumption_preferences=true&raw_scores=true',
		                data = '{"contentItems":[{"content":"' + text + '"}]}',
		                auth = (username, password),
		                headers = {'content-type': 'application/json'})
	return res.json()['personality']

if __name__ == '__main__':
	get_personality(get_reddit_comments("spez"))