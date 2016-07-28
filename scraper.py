# coding: utf8

from __future__ import unicode_literals

from urlparse import urljoin
from unidecode import unidecode
from bs4 import BeautifulSoup
import requests


BASE_URL = "http://genius.com/"
artist = "Vald"
song = "bonjour"
artist_url = BASE_URL + "artists/" + artist + "/"
song_url = BASE_URL + artist + "-" + song + "-lyrics"

print "\nOpening " + song_url
response = requests.get(artist_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
content = unidecode(response.text)
soup = BeautifulSoup(content, 'html.parser')

lyrics = soup.findAll("lyrics")
print lyrics

# find_all("div", class_="sister")

# print "\nLyrics"
# lyrics = soup.find('lyrics')
# print lyrics
