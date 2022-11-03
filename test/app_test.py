from control.controlDB import controlDB
from control.transformDataFrame import transfomDataFrame

from json import loads
from dicttoxml import dicttoxml
import json
from flask import Flask, render_template
import os
import pandas as pd

import rfeed 


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("not-found.html"), 404

@app.route("/api/<group_id>")
def json_return(group_id):
    valuesDB = controlDB(group_id).getData()
    convertData = transfomDataFrame()
    df = convertData.transfom(valuesDB)
    json = df.to_json()
    return json

@app.route("/rss/<group_id>")
def rss_return(group_id):    
    valuesDB = controlDB(group_id).getData()
    convertData = transfomDataFrame()
    df = convertData.transform(valuesDB)
    xml = df.to_xml()
    return xml

@app.route("/feed")
def feed():
    return render_template("feed.xml")

@app.route("/feed-test")
def test_feed():
    group_id = 271
    valuesDB = controlDB(group_id).getData()
    convertData = transfomDataFrame()
    df = convertData.transform(valuesDB)
    xml = generateFeedRss().create(df)
    return(xml)

if __name__ == '__main__':
    #print(json_return(271))
    #print(rss_return(271))
    print(test_feed())
    #app.run(host="0.0.0.0", port=8081, debug=True)