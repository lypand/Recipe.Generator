from flask import Flask, request
from recipe_scrapers import scrape_me
import json
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


def GetRandomRecipe():
    WebURL = 'https://www.allrecipes.com/recipe/'
    WebURL = WebURL + str(random.randint(100,19999))
    scraper = scrape_me(WebURL)
    return(json.dumps(scraper.schema.data))



@app.route('/output')
def hello_world():
    i = 1
    ret = GetRandomRecipe()
    while(ret=='{}'):
        ret =GetRandomRecipe()
        i+=1
    return (str(i) + ret)

@app.route('/input/')
def Testing():
    
    #Whenever url comes in as: localhost:5000/input/?name=INSERTNAME&size=INSERTSIZE
    #You can add more inputs as well, just seperate in url with '&'

    if 'name' in request.args:
        name = request.args['name']
    else:
        name = 'No Name Specified'
    if 'size' in request.args:
        size = request.args['size']
    else:
        size = 'No size Specified'
        
    return(name+size)



if __name__ == '__main__':
    app.run(debug=True)
