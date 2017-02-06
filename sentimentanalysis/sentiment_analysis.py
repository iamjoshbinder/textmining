#Basic Sentiment Analysis of tweets 

from string import punctuation

#Reading the filesclea
tweets = open('obama_tweets.txt').read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt").read()
positive_words = pos_sent.split('\n')

neg_sent = open("negative.txt").read()
negative_words = neg_sent.split('\n')


#Classifying the type of tweet
"""Remove the punctuation, convert to lower case, 
and examine whether or not 
each word was in the positive or negative words list."""

pt = 0; nt = 0; t = 0
for tweet in tweets_list:
	positive_counter = 0
	negative_counter = 0
	tweet_processed = tweet.lower()
	for p in list(punctuation):	
		tweet_processed = tweet_processed.replace(p,'')
		words = tweet_processed.split(' ')
	for word in words:
		if word in positive_words:
			positive_counter = positive_counter + 1
		if word in negative_words:
			negative_counter = negative_counter + 1
	if(positive_counter > negative_counter):
		pt = pt + 1
		#print('Positive')
	elif(positive_counter < negative_counter):
		nt = nt + 1
		#print('Negative')
	else:
		t = t + 1
		#print('Neutral')

print('Total number of tweets: ', len(tweets_list))
print('Number of positive tweets: ', pt)
print('Number of negative tweets: ', nt)
print('Number of neutral tweets: ', t)