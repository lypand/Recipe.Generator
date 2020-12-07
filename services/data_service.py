from data.recipes import Recipe
import mongoengine
import json


def create_recipe(retJson) -> Recipe: 
    recipe = Recipe()

    recipe.name = retJson["name"]
    recipe.imageUrl = retJson["image"]["url"]
    recipe.calories = retJson["nutrition"]["calories"]
    recipe.ingredients = retJson["recipeIngredient"]
    recipe.instructions = retJson["recipeInstructions"]
    recipe.categories = retJson["recipeCategory"]
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