#BEAUTIFUL SOUP
import sys
#from urllib.request import Request, urlopen
import urllib2
from bs4 import BeautifulSoup as BS

# Get the top torrent on the pirate bay for a given movie, with optional quality specified
def getMagnet(movieName, quality=''):
	# Build the url
	pbURL = 'https://thepiratebay.org/search/' + movieName + ' ' + quality + '/0/99/0'
	pbURL= pbURL.replace(" ", "%20")
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(pbURL,headers=hdr)

	try:
		html = urllib2.urlopen(req)
	except Exception as e:
		print("Could not find " + movieName + " at supplied resolution" + str(e))
		return

	soupPb = BS(html, 'html.parser')
	# Find the top magnet link
	link = soupPb.find(title='Download this torrent using magnet')
	if link:
		print(link.get('href'))
	else:
		# Could not find movie
		print("Could not find " + movieName + " at supplied resolution")

# Get magnet links for each movie in a list
def getList(filePath):
	#Read file line by line, get magnet for each line
	with open(filePath) as f:
		content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content]
	for movie in content:
		getMagnet(movie)

# Get a list of new movies out on dvd
# Format: Movie Title Year : Planet of the Apes 1968
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

def getRarbg(logFile):
	# Build the url
	rarURL = 'https://rarbg.to/torrents.php'
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(rarURL,headers=hdr)

	try:
		html = urllib2.urlopen(req)
	except Exception as e:
		print("Could not fetch rarbg movies " + str(e))
		return

	soup = BS(html, 'html.parser')
	# Find the top magnet link
	section = soup.find('div', {'align': 'center'})
	movies = section.find_all('a')
	for movie in movies:
		movi = str(movie)
		movi = movi[9:]
		download = movi[:movi.find('"')]
		print download

if __name__ == "__main__":
	try:
		filePath = str(sys.argv[1])
	except:
		print "Usage: getMovies.py list-path"
	getRarbg(filePath)
