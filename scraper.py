# coding: utf8

from __future__ import unicode_literals

from urlparse import urljoin
from unidecode import unidecode
from bs4 import BeautifulSoup
import requests

def create_soup(url):
    print "\nOpening " + url
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    return soup

def scrape_song(song_url):
    soup = create_soup(song_url)
    soup = soup.find("lyrics")
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    lyrics = soup.get_text()
    print "\nSong scraped :........................" + artist + " - " + song

def get_artist_id(artist_url):
    soup = create_soup(artist_url)
    soup = soup.find("a", {"class":"full_width_button"})
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    tag = soup.a
    url = tag['href']
    artist_id = url.split("=")[1].split("&")[0]
    return artist_id

def get_artist_songs(artist_url):
    artist_id = get_artist_id(artist_url)
    songs_url = BASE_URL + "artists/songs?for_artist_page=" + str(artist_id)
    soup = create_soup(songs_url)
    songs = []
    song_list = soup.find("ul", {"class":"song_list primary_list "})
    song_list = BeautifulSoup(song_list.prettify())
    song_list = song_list.findAll('a')
    # pages = soup.find("div", {"class":"pagination"})
    print song_list[0].

BASE_URL = "http://genius.com/"
artist = "Eminem"
song = "bonjour"
artist_url = BASE_URL + "artists/" + artist + "/"
song_url = BASE_URL + artist + "-" + song + "-lyrics"

get_artist_songs(artist_url)
