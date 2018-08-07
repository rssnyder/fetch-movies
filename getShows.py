#BEAUTIFUL SOUP
import urllib2, sys
from bs4 import BeautifulSoup as BS
import sys
import tvdb_api

def getShows(show, season):
	#t = tvdb_api.Tvdb()
	#theShow = t[show][season]
	#episodes = len(theShow.keys())
	#Do queries for each episode of the season.
	for e in range(1, 50):
		# Build url
		# Need leading 0 for earlier seasons + episodes
		if season < 10:
			s = ' s0'
		else:
			s = ' s'

		if e < 10:
			ep = 'e0'
		else:
			ep = 'e'
		this = show + s + str(season) + ep + str(e)
		pbURL = 'https://thepiratebay.org/search/' + this + '/0/99/0'
		pbURL= pbURL.replace(" ", "%20")
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(pbURL,headers=hdr)
		# Get url
		html = urllib2.urlopen(req)
		soupPb = BS(html, 'html.parser')
		# Find the top magnet link
		link = soupPb.find(title='Download this torrent using magnet')
		if link:
			print link.get('href')
			print '\n\n'
		else:
			exit()
			print "Could not find episode " + e

if __name__ == "__main__":
	# Specify TV Show and Season
	try:
		show = str(sys.argv[1])
		season = int(sys.argv[2])
	except:
		print "Usage: getShows.py \"Show Title\" Season#"
	getShows(show, season)
