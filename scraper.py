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

response = requests.get(song_url)
content = response.text
soup = BeautifulSoup(content)
soup = soup.find("lyrics")
soup = BeautifulSoup(soup.prettify())
print soup.get_text()
