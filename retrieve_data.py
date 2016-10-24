# coding: utf8
from __future__ import unicode_literals

from bs4 import BeautifulSoup
import requests
from util import *

def scrape_song_lyrics(soup, verbose = False):
    soup = soup.find("lyrics")
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    lyrics = clean_text(soup.text)
    if verbose:
        print "Song scraped"
        print lyrics.encode('utf-8')
    return lyrics

def scrape_song_metadata(soup, verbose = False):
    result = {}
    first_soup = soup.find("div", {"class":"song_header-primary_info"})
    first_soup = BeautifulSoup(soup.prettify(), "html.parser")

    artist = first_soup.find("a", {"class":"song_header-primary_info-primary_artist"})
    artist = clean_text(artist.string)
    if verbose:
        print "Artist : " + artist.encode('utf-8')
    result["artist"] = artist

    song = first_soup.find("h1", {"class":"song_header-primary_info-title"})
    song = clean_text(song.string)
    if verbose:
        print "Song   : " + song.encode('utf-8')
    result["song"] = song

    labels = first_soup.findAll("span", {"class":"song_info-label"})
    labels = [clean_text(l.string) for l in labels]
    contents = first_soup.findAll("span", {"class":"song_info-info"})
    contents = [BeautifulSoup(c.prettify(), "html.parser") for c in contents]
    contents = [c.a for c in contents]
    for i in range(len(labels)):
        if contents[i]:
            if verbose:
                print labels[i].encode('utf-8') + " :"
                print "    " + clean_text(contents[i].string).encode('utf-8')
                print "    " + contents[i]['href']
            result[labels[i]] = {"name" : clean_text(contents[i].string), "link" : geniusify(contents[i]['href'])}

    return result

def get_artist_id(soup):
    soup = soup.find("a", {"class":"full_width_button"})
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    tag = soup.a
    url = tag['href']
    artist_id = url.split("=")[1].split("&")[0]
    return artist_id
