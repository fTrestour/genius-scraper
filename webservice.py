# coding: utf8
from __future__ import unicode_literals

from flask import Flask, render_template, json
from flask import request
app = Flask(__name__)

from util import *
from find_songs import *
from retrieve_data import *
from analytics import *

@app.route("/", methods=['POST', 'GET'])
@app.route("/index/", methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        artist = request.form['artist']
        song = request.form['song']

        s = get_song_url(artist, song.replace(' ', '-'))
        soup = create_soup(s)
        data = scrape_song_metadata(soup)
        data["lyrics"] = scrape_song_lyrics(soup)
        data["frequencies"] = get_frequencies(data["lyrics"])
        data = json.dumps(data).encode('utf-8')
        # js_script = render_template("viz.js", data=data)
        # print js_script

    return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run()
