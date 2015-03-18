from flask import render_template, request, send_from_directory, send_file, Response, url_for
import json
from twitter_api import get_trending, get_popular
#import decorators


from scape import app

@app.route('/')
def index():
    trends = get_trending()
    return render_template("index.html", trends=trends)

@app.route('/api/<term>')
#@decorators.accept("application/json")
def get_tweets(term):
    tweets = get_popular(term)
    data = json.dumps(get_popular(term))
    #headers = {"Location": url_for("get_tweets")}
    return Response(data, 201, mimetype="application/json")

#static js files
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('scape/static/js', path)

@app.route('/api/trends')
def trends():
    pass
    