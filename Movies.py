#BEAUTIFUL SOUP
import urllib2
from bs4 import BeautifulSoup as BS

#Get the HTML
html = urllib2.urlopen('https://www.moviefone.com/dvd/?sort=release-date&page=1')
soup = BS(html, 'html.parser')
#For each entery in the document, get the tag and sort out the movies
for movie in soup.find_all('a'):
    if(movie.get('title') == ''):
    	print(movie.string)