from flask import Flask, request, Response
from recipe_scrapers import scrape_me
import json
from flask_cors import CORS
import random
<<<<<<< HEAD
import time
=======
import data.mongo_setup as mongo_setup
import services.data_service as mongoService
>>>>>>> c6b0fc54e21d27c42188ae5b7d08e6cd84e15d1a

app = Flask(__name__)
CORS(app)


def GetRandomRecipe():
    WebURL = 'https://www.allrecipes.com/recipe/'
    ID = random.randint(100,19999)
    WebURL = WebURL + str(ID)
    scraper = scrape_me(WebURL)
    return(json.dumps(scraper.schema.data))

@app.route('/read')
def read_recipe_by_category():

    #Whenever url comes in as: localhost:5000/input/?name=INSERTNAME&size=INSERTSIZE
    #You can add more inputs as well, just seperate in url with '&'

    if 'category' in request.args:
        category = request.args['category']
    mongo_setup.global_init()
    return mongoService.read_recipe_by_category(category)

@app.route('/random')
def read_recipe_random():
    mongo_setup.global_init()
    return mongoService.read_recipe_random()


@app.route('/populate')
def populate():
    mongo_setup.global_init()
    for lp in range(100):
        ret =GetRandomRecipe()
        if(ret!='{}'):
            retJson = json.loads(ret)
            mongoService.create_recipe(retJson)


    return (ret)
    

@app.route('/output')
def hello_world():
    ret = '{}'
    while(ret=='{}'):
        ret =GetRandomRecipe()
<<<<<<< HEAD
    print(ret)
    time.sleep(10)
    return ('hello World')
=======
        i+=1
    
    #put information into Mongo
    retJson = json.loads(ret)
    mongo_setup.global_init()

    mongoService.create_recipe(retJson)


    return (ret)
>>>>>>> c6b0fc54e21d27c42188ae5b7d08e6cd84e15d1a

@app.route('/input/')
def BufferTesting():
    
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
