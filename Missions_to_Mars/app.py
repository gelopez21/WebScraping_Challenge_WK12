from flask import Flask, render_template, jsonify, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsData_db")
# db = marsData_db
# collection = db.mars_collection

@app.route("/")
def home():
    mars_collection = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars_collection=mars_collection)

@app.route('/scrape')
def scrape():
    mars_results = scrape_mars.scrape()
    mars_collection = mongo.db.mars_collection
    
    mars_collection.update({},mars_results, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)