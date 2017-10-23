#BEAUTIFUL SOUP
import urllib2, sys
from bs4 import BeautifulSoup as BS

# Specify TV Show and Season
show = 'Rick and Morty'
season = 3

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
	pbURL = 'https://thepiratebay.org/search/' + this + ' /0/99/0'
	pbURL= pbURL.replace(" ", "%20")
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(pbURL,headers=hdr)
	# Get url
	html = urllib2.urlopen(req)
	soupPb = BS(html, 'html.parser')
	# Find the top magnet link
	link = soupPb.find(title='Download this torrent using magnet')
	if link:
		print this + '\n' + link.get('href')
		print '\n\n'
	else:
		#If we cant find this episode, this must be the end of avalible episodes
		break
