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
<<<<<<< HEAD
    
=======
    #hELLP

class Recipe():
    def __init__(self, Title, Time, Quantity, ):
        self._Title=Title
        self._Time = str(Time)
        self._Quantity = str(Quantity)
    
>>>>>>> aa44af91c9869f59d65927c912f42795bba5d562
