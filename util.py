# coding: utf8

from __future__ import unicode_literals

from bs4 import BeautifulSoup
import requests

BASE_URL = "http://genius.com"

def create_soup(url):
    print "Opening " + url
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    return soup

def get_artist_url(artist):
    return BASE_URL + "/artists/" + artist + "/"

def get_song_url(song):
    return BASE_URL + '/' + artist + "-" + song + "-lyrics"
