from flask import Flask
from recipe_scrapers import scrape_me
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
    Title = scraper.title()
    Time = scraper.total_time()
    Quantity = scraper.yields()
    Ingredients = scraper.ingredients()
    ret = json.dumps(scraper.schema.data)
    return (ret)


class Recipe():
    def __init__(self, Title, Time, Quantity, ):
        self._Title=Title
        self._Time = str(Time)
        self._Quantity = str(Quantity)
    