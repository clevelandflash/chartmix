import os
import urllib2
import urllib
import simplejson as json
import feedparser
import re

def buildSearchList(entries):
    searchList = []
    for entry in entries:
        title =  entry.title
        originalTitle = title
        title = stripFeaturing(title)
        title = stripIndex(title)
        title = stripAsterisks(title)
        print 'Changing ' + originalTitle + '\n\tto ' + title
        title = urllib.quote_plus(title)
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
    print("javascript: window.Grooveshark.addSongsByID([")
    delim=''
    for item in searchList:
        req = urllib2.Request("http://tinysong.com/s/" + item + "?format=json&key=" + os.environ['TINYSONG_KEY'], None)
        opener = urllib2.build_opener()
        f = opener.open(req)
        x = json.load(f)
        if len(x) == 0:
            continue
        else:
            print(delim + str(x[0]['SongID']))
        delim=','
    print("])")


source = feedparser.parse("http://www1.billboard.com/rss/charts/hot-100")
entries = source.entries

print 'Building search list...'
searchList = buildSearchList(entries)
print 'Done building search list'
buildPlaylist(searchList)

