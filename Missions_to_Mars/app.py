from flask import Flask, render_template, jsonify, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsinfo_data.mars_data")
db = marsinfo_data
collection = mars_data


@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    print("\n\n\n")
    db.mars_collection.insert_one(mars)
    return "scrapped data"

@app.route("/")
def home():
    mars = list(mars_data.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)