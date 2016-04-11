from twython import Twython, TwythonError
import time

#Api info goes here
APP_KEY = 'XXXXXXXXX'
APP_SECRET = 'XXXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXXX'

#Use Twython to set up api access to twitter
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	#Read the things we need to tweet
	with open('tweets.txt', 'r+') as tweetsfile:
		tweets = tweetsfile.readlines()

	#Dictionary to maintain all tweets done
	dict = {}

	#Loop through all the tweets
	for line in tweets[:]:
		#Api does not support empty line, duplicate status and tweets > 140, thus ignoring those lines
		if (line not in ['\n','\r\n']) and (line not in dict) and (len(line) <= 140):
			#What are we tweeting
			print ("Trying to tweet " + line)
			#Attempt to send the tweet, converted line to string type
			api.update_status(status=str(line))
			#Add it to dictionary
			dict[line]=1
			#Rate limit 
			time.sleep(1)
	#Yey it worked
	print ("I have tweeted AllTheThings!") 

except TwythonError, e:
	#in case it didn't work
	print("Something Broke :(")  
	print('Failed '+ str(e))

	
