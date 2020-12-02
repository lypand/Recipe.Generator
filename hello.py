from flask import Flask
from recipe_scrapers import scrape_me
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/data')
def hello_world():
    scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
    Title = scraper.title()
    Time = scraper.total_time()
    Quantity = scraper.yields()
    Ingredients = scraper.ingredients()
    ret = json.dumps(scraper.schema.data)
    return (ret)
    