# coding: utf8
from __future__ import unicode_literals

from flask import Flask, jsonify, render_template
app = Flask(__name__)

from util import *
from find_songs import *
from retrieve_data import *
from analytics import *

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/<artist>/<song>/")
def dataset(artist, song):
    s = get_song_url(artist, song.replace(' ', '-'))
    soup = create_soup(s)
    data = scrape_song_metadata(soup)
    data["lyrics"] = scrape_song_lyrics(soup).encode('utf-8')
    data["frequencies"] = get_frequencies(data["lyrics"])
    return jsonify(**data)

if __name__ == "__main__":
    app.run()
