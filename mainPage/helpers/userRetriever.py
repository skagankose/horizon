import tweepy
import datetime
import pytz
from .tweetCleaner import *
from ..models import *

def getUser(userName):

	# Twitter credentials
	consumerKey = "IivwDls7fYU6WTdzatJGxJ4Re"
	consumerSecret = "xwsedLJdvvgT3EaMQwPA24LtYb4067EE2avf3ogCxyfRGJ0kCw"
	accessToken = "4590451846-yWybwxLHOGCpCwEmh5XgqcWgIbi505UvjJ1nP0y"
	accessSecret = "EWq727mJBVid759fqKJWVOacHYqYX4he1AVOeGV7cwkj6"

	# authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessSecret)
	api = tweepy.API(auth)

	try:
		user = api.get_user(screen_name=userName)

		exist = TwitterAccount.objects.filter(userID=int(user.id)).exists()

		if not exist:

			# create database table
			newAccount  = TwitterAccount()
			newAccount.userID = int(user.id)
			newAccount.screenName = str(user.screen_name)
			newAccount.fullName = str(user.name)
			newAccount.joined = str(user.created_at)
			newAccount.description = str(user.description)
			newAccount.url = str(user.url)
			newAccount.likeCount = int(user.favourites_count)
			newAccount.followersCount = int(user.followers_count)
			newAccount.followeeCount = int(user.friends_count)
			newAccount.language = str(user.lang)
			newAccount.listedCount = int(user.listed_count)
			newAccount.location = str(user.location)
			newAccount.twitterCount = int(user.statuses_count)
			newAccount.timeZone = str(user.time_zone)
			newAccount.profileBackground = str(user.profile_background_image_url)

			# there might be no banner
			try:
				newAccount.profileBanner = str(user.profile_banner_url)
			except:
				pass
			newAccount.profileImage = str(user.profile_image_url)
			newAccount.save()

			return("%s is added succesfully." % userName)

		else:
			return("%s is already exists in the database." % userName)

	except Exception as error:
		return("%s" % error)

def getTweet(userName):

    # Twitter credentials
    consumerKey = "IivwDls7fYU6WTdzatJGxJ4Re"
    consumerSecret = "xwsedLJdvvgT3EaMQwPA24LtYb4067EE2avf3ogCxyfRGJ0kCw"
    accessToken = "4590451846-yWybwxLHOGCpCwEmh5XgqcWgIbi505UvjJ1nP0y"
    accessSecret = "EWq727mJBVid759fqKJWVOacHYqYX4he1AVOeGV7cwkj6"

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(screen_name=userName)

        # initialize a list to hold all the tweepy Tweets
        allTweets = []

        # make initial request for most recent tweets (200 is the maximum allowed count)
        newTweets = api.user_timeline(screen_name=userName,count=1)

        # save most recent tweets
        allTweets.extend(newTweets)

        # save the id of the oldest tweet less one
        oldest = allTweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while len(newTweets) > 0:

            # all subsiquent requests use the max_id param to prevent duplicates
            newTweets = api.user_timeline(screen_name=userName,count=1,max_id=oldest)

            # retrieve only lastest tweets
            year = newTweets[-1].created_at.year
            month = newTweets[-1].created_at.month
            nowYear = timezone.now().year
            nowMonth = timezone.now().month

            if year != nowYear or month != nowMonth:
            	break

            allTweets.extend(newTweets)

            # update the id of the oldest tweet less one
            oldest = newTweets[0].id - 1

        print("%s tweet(s) for %s" % (len(allTweets), userName))

        for tweet in allTweets:
            newTweet = Tweet()
            relatedAccount = TwitterAccount.objects.get(userID=int(user.id))
            newTweet.relatedAccount = relatedAccount
            newTweet.tweetID = tweet.id

            # <block>
            # clean tweet text
            try:
            	text = api.get_status(tweet.retweeted_status.id, tweet_mode='extended')._json['full_text']
            except:
            	if tweet.truncated:
            		text = api.get_status(tweet.id, tweet_mode='extended')._json['full_text']
            	else:
            		text = tweet.text
            cleanedText = preCleaner(text)
            cleanedText = punctuationRemover(cleanedText)
            cleanedText = adjuster(cleanedText)
            newTweet.text = text
            newTweet.cleanedText = cleanedText
            # </block>

            newTweet.coordinates = tweet.coordinates
            # newTweet.country = tweet.place.country
            # newTweet.countryCode = tweet.place.country_code
            # newTweet.countryFull = tweet.place.full_name
            # newTweet.placeID = tweet.place.id
            # newTweet.placeType = tweet.place.place_type

            # <block>
            # add time zone
            unaware = tweet.created_at
            aware = pytz.utc.localize(unaware)
            newTweet.createdDate = aware
            # </block>

            newTweet.hashtags = tweet.entities['hashtags']
            newTweet.urls = tweet.entities['urls']
            newTweet.mentions = tweet.entities['user_mentions']
            newTweet.liked = tweet.favorite_count
            newTweet.retweets = tweet.retweet_count
            newTweet.replyUserID = tweet.in_reply_to_user_id
            newTweet.replyTweetID = tweet.in_reply_to_status_id
            # newTweet.retweetTweetID = tweet.retweeted_status.id
            newTweet.language = tweet.lang
            # newTweet.quoteTweetID = tweet.quoted_status.id
            newTweet.save()

        return("%s's tweet(s) retrieved succesfully." % userName)

    except Exception as error:
        print("%s" % error)
        return("%s" % error)
