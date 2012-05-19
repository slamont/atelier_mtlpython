# -=- encoding: utf-8 -=-
# tweetaroo.py
import urllib
import json
import sys

class Timeline(object):
    #url = "http://api.twitter.com/1/statuses/user_timeline.json?count=%(count)d&screen_name=%(username)s"
    url = "http://192.168.144.118:8888/subdir/twitter.json"
    def __init__(self, username):
        self.username = username
        self.tweets = []
    def load(self):
        cnt = urllib.urlopen(self.url % {'count': 100,
                                         'username': self.username})
        data = cnt.read()
        try:
            obj = json.loads(data)
        except ValueError, e:
            print "Oh mama! Le json était pourri"
            sys.exit(1)  # import sys
        self.tweets = [ Tweet(item) for item in obj ]

    def calc_obsession(self):
        word_count = {}
        for tweet in self.tweets:
            for word in tweet.get_words():
                word_count[word] = word_count.get(word, 0) + 1
        return sorted(word_count.iteritems(), key=lambda x: x[1])


stopwords = set([line.strip() for line in open('stopwords.txt')]) 

class Tweet(object):
    def __init__(self, item):
        self.item = item
        self.text = item['text']
    def get_words(self):
        words = self.text.lower().split()
        return [ word for word in words if word not in stopwords  ]

if __name__ == '__main__':
    t = Timeline('AUsernameOfTwitterGoesHere')
    print t.username
    data = t.load()
    print t.calc_obsession()


