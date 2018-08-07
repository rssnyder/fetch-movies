import urllib
import urllib2
from bs4 import BeautifulSoup

# Given text, returns a link to the top youtube search result
def getLink(textToSearch):
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    # To get all videos...
    # for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    #     print 'https://www.youtube.com' + vid['href']
    return 'https://www.youtube.com' + soup.find(attrs={'class':'yt-uix-tile-link'})['href']
