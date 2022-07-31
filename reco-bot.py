from http.client import ResponseNotReady
import spotipy
import tweepy
import json
import random

import requests

api_key = ""
api_key_secret = ""
access_token= "-"
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

Client_ID = ""
Client_Secret = ""

resp = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,client_secret=Client_Secret,scope="playlist-modify-public",
                                   redirect_uri="http://example.com/")
sp = spotipy.Spotify(oauth_manager=resp)

################### fetching a random hindi song from spotify###################

playlist = sp.playlist("6WfOMWi9LeJ6lfzE5XgmXi")

hindi_song_data = {}
hindi_song_list = []

for n in range(len(playlist["tracks"]["items"])):
    link =playlist["tracks"]["items"][n]["track"]["external_urls"]["spotify"] 
    hindi_song_data[(playlist["tracks"]["items"][n]["track"]["name"])] = link
    hindi_song_list.append((playlist["tracks"]["items"][n]["track"]["name"]))

random_choice = random.choice(hindi_song_list)
random_choice_link = hindi_song_data[random_choice]
########################################################################################

id = "3v5PC6RPnCP0mCQgv9IMEx"

playlist = sp.playlist(id)

eng_song_data = {}
eng_song_list = []

for n in range(len(playlist["tracks"]["items"])):
    link =playlist["tracks"]["items"][n]["track"]["external_urls"]["spotify"] 
    eng_song_data[(playlist["tracks"]["items"][n]["track"]["name"])] = link
    eng_song_list.append((playlist["tracks"]["items"][n]["track"]["name"]))

random_choice1 = random.choice(eng_song_list)
random_choice_link1 = eng_song_data[random_choice1]


# print(random_choice,random_choice_link)
# print(random_choice1,random_choice_link1)

###############################################################################3



def check_mentions(api, keywords, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet.user.following:
                tweet.user.follow()
            print(tweet.id)
            to = True
            with open("tweets.txt",mode = "r") as file:
                cont = file.readlines()
            # for id in cont:
            #     if '\n' in id:
            #         id.replace('\n',"")
            # print(cont)
            content = cont[0].split(',')
            if f"{tweet.id}" in content:
                pass
            else:
                with open ("tweets.txt", mode="a") as file:
                    file.write(str(tweet.id))
                    file.write(",")
                tweet_text = f"Hey @{tweet.user.screen_name}! How's it going? Try listening to {random_choice} and see how you like it. Here is the spotify link : {random_choice_link}. Enjoy :)"
                print(tweet_text)
                api.update_status(
                    status=tweet_text,
                    in_reply_to_status_id=tweet.id,
                )
    return new_since_id


def check_mentionseng(api, keywords, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet.user.following:
                tweet.user.follow()
            print(tweet.id)
            with open("tweets.txt",mode = "r") as file:
                cont = file.readlines()
            
            content = cont[0].split(',')
            
            # for id in cont:
            #     if '\n' in id:
            #         id.replace('\n',"")
            if f"{tweet.id}" in content:
                pass
            else:
                with open ("tweets.txt", mode="a") as file:
                    file.write(str(tweet.id))
                    file.write(",") 
                tweet_text = f"Hey @{tweet.user.screen_name}! How's it going? Try listening to {random_choice1} and see how you like it. Here is the spotify link : {random_choice_link1}. Enjoy :)"
                print(tweet_text)
                api.update_status(
                    status=tweet_text,
                    in_reply_to_status_id=tweet.id,
                )
    return new_since_id


since_id = 1

since_id = check_mentions(api,["hindi"],since_id)

since_id = check_mentionseng(api,["english"],1)


# print(playlist)
# print(playlist)



