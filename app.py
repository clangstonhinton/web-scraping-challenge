# INSTRUCTIONS
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information 
# that was scraped from the URLs above.
# •	Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a 
    # function called scrape that will execute all of your scraping code from above and return one 
    # Python dictionary containing all of the scraped data.
# •	Next, create a route called /scrape that will import your scrape_mars.py script and call your 
    # scrape function.
# • Store the return value in Mongo as a Python dictionary.
# •	Create a root route / that will query your Mongo database and pass the mars data into an HTML 
    # template to display the data.
# •	Create a template HTML file called index.html that will take the mars data dictionary and 
    # display all of the data in the appropriate HTML elements. Use the following as a guide for 
    # what the final product should look like, but feel free to create your own design.




from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars 

app = Flask(__name__)

# setup mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
db = mongo.db.mars_db

# Route to render index.html template using data from Mongo
@app.route("/")
def home(): 

    # Find one record of data from the mongo database and return it
    mars_collection = db.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_collection)

# Route to start the scrape function
@app.route("/scrape")
def scraper():

    # # Create a Mars db in mongo
    # mars_data = mongo.db.mars

    # Call the scrape function
    mars_scrape = scrape_mars.scrape()

    # Update database with scraped data
    db.update_one({}, {"$set": mars_scrape}, upsert=True)

    # Redirect back to home page and pass it the data from Mongo
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
