import urllib2, sys, re
from bs4 import BeautifulSoup as BS
from getMovies import getMagnet
import sys

def rottenList(listURL):
    # Get the link of the list
    listURL = sys.argv[1]
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(listURL,headers=hdr)

    # Get html doc
    html = urllib2.urlopen(req)
    page = BS(html, 'html.parser')

    # Find the html list that holds each movie in this list
    theMovies = page.find_all('div', {'class': 'col-sm-20 col-full-xs'})
    
    # For each movie in the list, get the top torrent
    for thing in theMovies:
        #getMagnet(thing.img['alt'])
	movie = BS(str(thing), 'html.parser').find('div', {'class': 'article_movie_title'}).text.replace("(", "").replace(")", "").replace("'", "")
        print getMagnet(movie)

if __name__ == "__main__":
    try:
        listURL = str(sys.argv[1])
    except:
	print 'Please specify list url'
	exit()
    rottenList(listURL)
