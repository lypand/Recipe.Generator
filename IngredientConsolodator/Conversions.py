#Dry measurement conversitions with base unit of teaspoon
DryMeasures = {'cup':48,'tablespoon':3,'tbs':3,'tbsp':3,'tsp':1,'teaspoon':1}

#1 pound carrots, 

#Used when parsing through ingredients to find similar ones
#Try to look at finding these identifiers after a comma
#i.e "1 onion, cut into thin strips"
#Works as long as not something like "2 skinless, bonesless chicken breasts"
CommonAdj = ['baked','cut','peeled','coarsely','softened','diced','sliced','minced','seeded','cut','chopped','roasted','grated','beaten','melted','mashed','crushed']

#Difficult phrase to parse, but common in recipes
NoParsePhrase = ['salt and pepper to taste']

#Keyword for new parse
CannedGood = ['can', 'cans','canned','package','packages','bottle','bottles','bar','bars']

#After a comma, we can assume it is adjective?


#½ cup chopped, unsalted dry-roasted peanuts
