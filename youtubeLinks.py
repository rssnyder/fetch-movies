# from __future__ import unicode_literals
import urllib
import urllib2
from bs4 import BeautifulSoup
import youtube_dl
import sys

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

def downloadMP3(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # 'logger': MyLogger(),
        # 'progress_hooks': [my_hook],
        'outtmpl': '%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# Get m3u playlist
with open(sys.argv[1]) as f:
    content = f.readlines()
# Clean file
songs = []
for x in content:
    x = x.strip()
    # Forget comments
    if x[0] == '#':
        comments = 0
    else:
        # Remove Album and .mp3 at the end
        songs.append(x.replace('.mp3', '').split('/', 1)[-1])

for song in songs:
    link = getLink(song)
    downloadMP3(link)
