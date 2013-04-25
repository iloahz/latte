import urllib2
import time

class proto():
    pass

def fetch(url):
    start = time.time()
    while True:
        try:
            req = urllib2.Request(url)
            res = urllib2.urlopen(req, timeout=10).read()
            return res
        except:
            end = time.time()
            if end - start > 60:
                return ''