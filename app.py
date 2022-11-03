from control.controlDB import controlDB
from control.transformDataFrame import transfomDataFrame
from control.generateFeedRss import generateFeedRss

from flask import Flask, render_template


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("not-found.html"), 404

@app.route("/feed/<group_id>/<users_id_lastupdater>")
def feed(group_id, users_id_lastupdater):
    valuesDB = controlDB(group_id, users_id_lastupdater).getData()
    convertData = transfomDataFrame()
    df = convertData.transform(valuesDB)
    xml = generateFeedRss().create(df)
    return(xml)

@app.route("/feed/<group_id>")
def feed_just_group(group_id):
    valuesDB = controlDB(group_id).getData()
    convertData = transfomDataFrame()
    df = convertData.transform(valuesDB)
    xml = generateFeedRss().create(df)
    return(xml)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)