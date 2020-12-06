import mongoengine

class Recipe(mongoengine.Document): 

    name = mongoengine.StringField()
    imageUrl = mongoengine.StringField()
    calories = mongoengine.StringField()
    ingredient = mongoengine.ListField()
    instructions = mongoengine.ListField()
    categories = mongoengine.ListField()
    
    meta = {
        'db_alias': 'core',
        'collection': 'recipe'
    }