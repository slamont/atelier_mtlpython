# -=- encoding: utf-8 -=-
#!/usr/bin/python 

import urllib
import json
import sys

class Timeline(object):
    url = "http://192.168.144.118:8888/subdir/twitter.json"
    def __init__(self, username):
        self.username = username
        self.tweets = []

    def load(self):
        cnt = urllib.urlopen(self.url % {'count' : 100,
                                   'username' : self.username})
        data = cnt.read()
        try:
            obj = json.loads(data)
        except ValueError, e:
            print u"Oh mama! Le json était pourri!"
            sys.exit(1)  #import sys
        return obj

if __name__ == '__main__':
    t = Timeline('bourgetalexndre')
    print t.username
    data = t.load()



