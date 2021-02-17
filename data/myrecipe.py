import mongoengine


class MyRecipe(mongoengine.Document): 

    username = mongoengine.StringField()
    name = mongoengine.StringField()
    imageUrl = mongoengine.StringField()
    calories = mongoengine.StringField()
    ingredients = mongoengine.ListField()
    instructions = mongoengine.ListField()
    categories = mongoengine.ListField()
    key = mongoengine.StringField()
    
    meta = {
        'db_alias': 'core',
        'collection': 'recipe'
    }