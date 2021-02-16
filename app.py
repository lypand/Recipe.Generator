from flask import Flask, request, Response
from recipe_scrapers import scrape_me
import json
from flask_cors import CORS
import random
import time
import data.mongo_setup as mongo_setup
import services.data_service as mongoService

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

@app.route('/myrecipes/<username>', methods = ['GET'])
def getMyRecipes(username):
    mongo_setup.global_init()
    return mongoService.read_my_recipes(username)



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

@app.route('/create-recipe', methods = ['POST'])
def createRecipe():
    mongo_setup.global_init()
    ret = mongoService.create_recipe_new(json.loads(request.json["recipe"]))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/save-my-recipe', methods = ['POST'])
def saveMyRecipe():
    mongo_setup.global_init()
    username = json.loads(request.json["username"])
    ret = mongoService.save_my_recipe(json.loads(request.json["recipe"]),username)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
   

@app.route('/output')
def hello_world():
    ret = '{}'
    while(ret=='{}'):
        ret =GetRandomRecipe()
        i+=1
    #put information into Mongo
    retJson = json.loads(ret)
    mongo_setup.global_init()
    mongoService.create_recipe(retJson)
    return (ret)

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
