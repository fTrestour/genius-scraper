# coding: utf8

from __future__ import unicode_literals

from bs4 import BeautifulSoup
import requests
from util import *
from retrieve_data import *
from find_songs import *

artist = "Vald"
artist_url = get_artist_url(artist)
songs_list = get_artist_songs(artist_url)
for s in songs_list:
    metadata = scrape_song_metadata(s)
    lyrics = scrape_song_lyrics(s)
