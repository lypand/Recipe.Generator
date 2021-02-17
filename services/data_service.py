from data.recipes import Recipe
from data.myrecipe import MyRecipe
import mongoengine
import json
import uuid

def create_recipe(retJson) -> Recipe: 
    recipe = Recipe()

    recipe.name = retJson["name"]
    recipe.imageUrl = retJson["image"]["url"]
    recipe.calories = retJson["nutrition"]["calories"]
    recipe.ingredients = retJson["recipeIngredient"]
    recipe.instructions = extractInstructions(retJson["recipeInstructions"])
    recipe.categories = retJson["recipeCategory"]
    recipe.save()
    return recipe

def create_recipe(retJson) -> Recipe: 
    recipe = Recipe()

    recipe.name = retJson["name"]
    recipe.imageUrl = retJson["image"]["url"]
    recipe.calories = retJson["nutrition"]["calories"]
    recipe.ingredients = retJson["recipeIngredient"]
    recipe.instructions = extractInstructions(retJson["recipeInstructions"])
    recipe.categories = retJson["recipeCategory"]
    recipe.save()
    return recipe

def extractInstructions(instructions):
    extractedInstructions = []
    for instruction in instructions:
        extractedInstructions.append(instruction['text'])
    return extractedInstructions

def create_recipe_new(retJson) -> Recipe: 
    recipe = Recipe()
    recipe.name = retJson["name"]
    recipe.imageUrl = retJson["imageUrl"]
    recipe.calories = retJson["calories"]
    recipe.ingredients = retJson["ingredients"]
    recipe.instructions = retJson["instructions"]
    recipe.save()
    return recipe    

def read_recipe_by_category(category: str) -> Recipe:
    recipe = Recipe.objects(categories= category).first()
    return recipe.to_json()


def read_recipe_random() -> Recipe: 
    doc_collection = Recipe._get_collection()
    random_oids = get_random_oids(doc_collection, 1)
    return Recipe.objects(id__in=random_oids).to_json()

def get_random_oids(collection, sample_size):
    pipeline = [{"$project": {'_id': 1}}, {"$sample": {"size": sample_size}}]
    return [s['_id'] for s in collection.aggregate(pipeline)]


#My recipe 
def read_my_recipes(username) -> MyRecipe: 
    recipe = MyRecipe.objects(username=username)
    return recipe.to_json()

#My recipe 
def delete_my_recipe(key) -> MyRecipe: 
    recipe = MyRecipe()
    recipe = MyRecipe.objects(key=key).delete()
    return recipe

def save_my_recipe(retJson, username) -> MyRecipe: 
    recipe = MyRecipe()
    recipe.username = username
    recipe.name = retJson["name"]
    recipe.imageUrl = retJson["imageUrl"]
    recipe.calories = retJson["calories"]
    recipe.ingredients = retJson["ingredients"]
    recipe.instructions = retJson["instructions"]
    recipe.key = uuid.uuid4().hex
    recipe.save()
    return recipe 
    