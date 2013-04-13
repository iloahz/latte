import urllib2

class proto():
    pass

def fetch(url):
    while True:
        res = urllib2.urlopen(url, timeout=5000)
        return res