from http.client import ResponseNotReady
from turtle import Screen
import spotipy
import tweepy
import requests

api_key = ""
api_key_secret = ""
access_token= ""
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

for follower in (api.get_followers(screen_name = "thebotofviz")):
        print(follower.name)
        if not follower.following:
            print(f"Following {follower.name}")
            follower.follow()