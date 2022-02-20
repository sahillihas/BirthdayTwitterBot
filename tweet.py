import tweepy
import dbpedia
import urllib
import config
import util
import time


def postTweets():
    client = tweepy.Client(consumer_key=config.api_key,
                           consumer_secret=config.api_key_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret)

    dbResult = dbpedia.getData()
    i=0
    for result in dbResult["results"]["bindings"]:
        name = result["name"]["value"]
        description = result["description"]["value"]
        birth = result["birth"]["value"]
        description = util.trimDescription(description)
        # img_url = result["img"]["value"]
        tweet_data = "#HappyBirthday" + util.removeSpace(name) + "\n Birthdate:" + birth + "\n" + str(description)
        # if len(img_url) != 0:
        #     urllib.request.urlretrieve(img_url, "pic.png")
        print(str(i) + " \n")
        i=i+1
        if len(tweet_data) > 278:
            print("TWEET LENGTH EXCEEDED !!!")
        else:
            print("Name - " + name + "\n Description - " + tweet_data + "\n" + str(len(tweet_data)))
            # response = client.create_tweet(text=tweet_data)
            # print(response)
            time.sleep(300)
