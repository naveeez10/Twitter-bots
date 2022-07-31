from http.client import ResponseNotReady
import tweepy

import requests

api_key = ""
api_key_secret = ""
access_token= ""
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
	"X-RapidAPI-Key": "f69cc3a052mshb654ea92294198ep1c3577jsnef1137d7f11a"
}
flag = 0
while(True):
	response = requests.request("GET", url, headers=headers)

	data = response.json()

	while(True):
		try:
			joke = (data["body"][0]["setup"])
			joke += "\n"
			joke += (data["body"][0]["punchline"])
			break
		except:
			flag = 0
		  	
	if "*" in joke:
		joke.replace("*","")
		
	try:
		api.update_status(joke)
		break
	except:
		print(f"Joke not printed \n {joke}")
    
print(joke)


