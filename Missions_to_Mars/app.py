from flask import Flask, render_template, jsonify, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_collection")
db = client.mars_db
collection = db.mars_collection


@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    print("\n\n\n")
    db.mars_collection.insert_one(mars)
    return "scrapped data"

@app.route("/")
def home():
    mars = list(db.mars_collection.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)