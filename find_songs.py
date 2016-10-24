# coding: utf8
from __future__ import unicode_literals

from bs4 import BeautifulSoup

from util import *
from retrieve_data import *

def get_all_songs_in_page(url):
    print "Finding all songs in page " + url
    soup = create_soup(url)
    song_list = soup.find("ul", {"class":"song_list primary_list "})
    song_list = BeautifulSoup(song_list.prettify(), "html.parser")
    song_list = song_list.findAll('a')
    song_list = [BeautifulSoup(s.prettify(), "html.parser") for s in song_list]
    songs = [s.a['href'] for s in song_list]
    for s in songs:
        print "Song found :........................" + s
    return songs

def get_artist_songs(artist_url):
    artist_id = get_artist_id(artist_url)
    songs_url = BASE_URL + "/artists/songs?for_artist_page=" + str(artist_id)
    soup = create_soup(songs_url)
    songs = get_all_songs_in_page(songs_url)
    print "Finding all other pages"
    pages = soup.find("div", {"class":"pagination"})
    pages = pages.findAll("a")
    pages = [BeautifulSoup(s.prettify(), "html.parser") for s in pages]
    pages = [BASE_URL + p.a['href'] for p in pages]
    for p in pages:
        songs += get_all_songs_in_page(p)
    print len(songs)
    return songs
