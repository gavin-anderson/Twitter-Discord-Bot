import json
import discord_message
import pandas as pd


def json_message(json_string):
        
    enter_tweet = json.loads(json_string)
    exit_tweet =  'https://twitter.com/twitter/status/'+enter_tweet['data']['id']
    print(exit_tweet)
    discord_message.run_bot(exit_tweet)

 
    