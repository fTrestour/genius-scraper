# coding: utf8

from __future__ import unicode_literals

from urlparse import urljoin
from bs4 import BeautifulSoup
import requests

def create_soup(url):
    print "Opening " + url
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    return soup

def scrape_song_lyrics(song_url):
    soup = create_soup(song_url)
    soup = soup.find("lyrics")
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    lyrics = soup.get_text()
    print "Song scraped :........................" + artist + " - " + song

def scrape_song_metadata(song_url):
    soup = create_soup(song_url)
    first_soup = soup.find("div", {"class":"song_header-primary_info"})
    first_soup = BeautifulSoup(soup.prettify(), "html.parser")
    artist = first_soup.find("a", {"class":"song_header-primary_info-primary_artist"})
    artist = artist.string
    print "Artist : " + artist
    song = first_soup.find("h1", {"class":"song_header-primary_info-title"})
    song = song.string
    print "Song   : " + song
    labels = first_soup.findAll("span", {"class":"song_info-label"})
    labels = [l.string for l in labels]
    contents = first_soup.findAll("span", {"class":"song_info-info"})
    # contents = [c.string for c in contents]
    for i in range(len(labels)):
        if contents[i]:
            print labels[i] + " : "
            print contents[i]

def get_artist_id(artist_url):
    soup = create_soup(artist_url)
    soup = soup.find("a", {"class":"full_width_button"})
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    tag = soup.a
    url = tag['href']
    artist_id = url.split("=")[1].split("&")[0]
    return artist_id

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

BASE_URL = "http://genius.com"
artist = "Vald"
song = "bonjour"
artist_url = BASE_URL + "/artists/" + artist + "/"
song_url = BASE_URL + '/' + artist + "-" + song + "-lyrics"

scrape_song_metadata(song_url)
