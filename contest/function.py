import urllib2

class proto():
    pass

def fetch(url):
    while True:
        try:
            req = urllib2.Request(url)
            res = urllib2.urlopen(req, timeout=10000).read()
            return res
        except:
            pass