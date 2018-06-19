import urllib2, sys
from bs4 import BeautifulSoup as BS
from getMovies import getMagnet
import sys

letternoxdList(listURL):
    # Get the link of the list
    listURL = sys.argv[1]
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(listURL,headers=hdr)

    # Get html doc
    html = urllib2.urlopen(req)
    page = BS(html, 'html.parser')

    # Find the html list that holds each movie in this list
    theList = page.find_all('ul', {'class': 'poster-list -p125 -grid film-list'})
    theMovies = BS(str(theList[0]), 'html.parser').find_all('li');

    # For each movie in the list, get the top torrent
    for thing in theMovies:
        getMagnet(thing.img['alt'])

if __name__ == "__main__":
    try:
		listURL = str(sys.argv[1])
	except:
		print "Usage: letterboxd.py list-URL"
	letternoxdList(listURL)
