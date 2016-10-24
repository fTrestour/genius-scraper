# coding: utf8
from __future__ import unicode_literals

from bs4 import BeautifulSoup
import requests
import re

BASE_URL = "http://genius.com"

def create_soup(url):
    print "Opening " + url
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    return soup

def geniusify(url):
    if BASE_URL in url:
        return url
    else:
        return BASE_URL + url

def get_artist_url(artist):
    return geniusify("/artists/" + artist + "/")

def get_song_url(artist, song):
    return geniusify('/' + artist + "-" + song + "-lyrics")

def clean_text(text):
    res = ""
    space = False
    tab = False
    new_line = False
    for c in text:
        if c == ' ':
            if not space:
                res += c
                space = True
        elif c == '\t':
            if not tab:
                res += c
                tab = True
        elif c== '\n':
            if not new_line:
                new_line = True
        elif c.lower()!=c:
            if new_line:
                res += '\n'
            res += c
            space = False
            tab = False
            new_line = False
        else:
            res += c
            space = False
            tab = False
            new_line = False
    while res[0] in [' ', '\t', '\n']:
        res = res[1:]
    while res[-1] in [' ', '\t', '\n']:
        res = res[:-1]
    return re.sub("googletag\.cmd\.push\(function\(\) \{ .*}\);", '', res)
