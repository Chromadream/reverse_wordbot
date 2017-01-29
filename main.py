from twitter import *
from nltk.corpus import words
import time
import random
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
