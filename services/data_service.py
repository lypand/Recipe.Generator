from data.recipes import Recipe


def create_recipe(retJson) -> Recipe: 
    recipe = Recipe()

    recipe.name = retJson["name"]
    recipe.imageUrl = retJson["image"]["url"]
    recipe.calories = retJson["nutrition"]["calories"]
    recipe.ingredients = retJson["recipeIngredient"]
    recipe.recipeInstructions = retJson["recipeInstructions"]
    recipe.categories = retJson["recipeCategory"]
    recipe.save()

    return recipe