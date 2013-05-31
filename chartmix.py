import os
import urllib2
import urllib
import simplejson as json
import feedparser
import re
from pprint import pprint

def buildSearchList(entries):
    searchList = []
    for entry in entries:
        title =  entry.title
        originalTitle = title
        title = stripFeaturing(title)
        title = stripIndex(title)
        title = stripAsterisks(title)
        print 'Changing ' + originalTitle + '\n\tto ' + title
        searchList.append(title)
    return searchList

def stripFeaturing(val):
    rfindIndex = val.lower().rfind('featuring')
    if rfindIndex > 0:
        val = val[:rfindIndex].strip()
    return val

def stripIndex(val):
    stripLeftIndex = val.find(': ')
    return val[stripLeftIndex+2:]

def stripAsterisks(val):
    return re.sub(r'[^ ]*\*+[^ ]*', '', val)

def buildPlaylist(searchList):
    notFound = []
    print("javascript: window.Grooveshark.addSongsByID([")
    delim=''
    for item in searchList:
        itemToSearch = urllib.quote_plus(item)
        req = urllib2.Request("http://tinysong.com/s/" + itemToSearch + "?format=json&key=" + os.environ['TINYSONG_KEY'], None)
        opener = urllib2.build_opener()
        f = opener.open(req)
        x = json.load(f)
        if len(x) == 0:
            notFound.append(item)
            continue
        else:
            print(delim + str(x[0]['SongID']))
        delim=','
    print("])")
    print "Could not find the following songs:"
    pprint(notFound)


source = feedparser.parse("http://www1.billboard.com/rss/charts/hot-100")
entries = source.entries

print 'Building search list...'
searchList = buildSearchList(entries)
print 'Done building search list'
buildPlaylist(searchList)

