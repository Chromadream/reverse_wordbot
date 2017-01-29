from twitter import *
from nltk.corpus import words
import time
import random
auth = OAuth(consumer_key='z8ZmHH8kChc9XmP9OYI1rL9pE',consumer_secret='ih0tsDeJVmJtnWVL4eDoFfvBzposjX6Y1zhNBUPh7GQSYykeaW',token='825594302390628352-ohzd6I2x0G7l66BC369e7Iw9zfOY472',token_secret='79Zuu6B6P38tjtAtm0fzzVdkat6QkxdCYnEj7oSxKbpu0')
t = Twitter(auth=auth)
wordlist = words.words()
wordLength = len(wordlist)
def tweetRandomGibberish():
    which = random.randrange(wordLength)
    initialWord = wordlist[which]
    toTweet = initialWord[::-1]
    t.statuses.update(status=toTweet)
    print(initialWord)
    return None
def timing():
    tweetRandomGibberish()
    time.sleep(180)

while True:
    timing()