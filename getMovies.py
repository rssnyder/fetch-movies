#BEAUTIFUL SOUP
import urllib2, sys
from bs4 import BeautifulSoup as BS

# Get the top 1080p torrent on the pirate bay for a given movie
def getMagnet(movieName):
	movie = movieName.encode('utf-8')
	# Try for 1080p version
	pbURL = 'https://thepiratebay.org/search/' + movie + ' 1080p/0/99/0'
	pbURL= pbURL.replace(" ", "%20")
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(pbURL,headers=hdr)
	# Get url
	try:
		html = urllib2.urlopen(req)
	except:
		print "Could not find " + movie
		return

	soupPb = BS(html, 'html.parser')
	# Find the top magnet link
	link = soupPb.find(title='Download this torrent using magnet')
	if link:
		print link.get('href')
	else:
		# Try for 720p version
		pbURL = 'https://thepiratebay.org/search/' + movie + ' 720p/0/99/0'
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


# Get a list of new movies out on dvd
def getMovies():
    # Dic for return
    movies = []
    count = 0;
    #Get the HTML
    html = urllib2.urlopen('https://www.moviefone.com/dvd/?sort=release-date&page=1')
    soup = BS(html, 'html.parser')
    #For each entery in the document, get the tag and sort out the movies
    for movie in soup.find_all('a'):
        if(movie.get('title') == ''):
            movies.insert(count, movie.string)
            count += 1
    return movies
