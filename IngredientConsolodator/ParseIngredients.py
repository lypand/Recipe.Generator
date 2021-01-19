from standards.Conversions import *

def AddItemToMaster(AddItem,MasterList):
	#Parse the ingredients here so we can easily add to master list
	identifier = False
	Ingred = ''
	Measure = ''
	for word in AddItem.split():
		if identifier and word not in CommonAdj:
			if Ingred == '':
				Ingred=word
			else:
				Ingred+= " " + word
		else:
			if Measure=='':
				Measure=word
			else:
				Measure+= " " + word
		if word in DryMeasures:
			identifier = True
	if Ingred == 'egg':
		Ingred = 'eggs'
	if Ingred != '':
		#Creates a list and adds the additem to it, but checks if key is already populated in dictionary
		MasterList[Ingred] = MasterList.get(Ingred,[]) + [Measure]
	else:
		Measure = ''
		if AddItem in NoParsePhrase:
			MasterList[AddItem] = 'No Measure'
		else:
			for word in AddItem.split():
				if word.isdigit():
					Measure += word
				else:
					Ingred+= word + ''
			if Measure != '':
				MasterList[Ingred] = MasterList.get(Ingred,[]) + [Measure]
			else:
				MasterList[Ingred] = 'No Measure'

#Take in list of ingredients and a global master list
def ParseIngredients(InputRecipe,MasterList):
	for index in range(0,len(InputRecipe)):
		AddtoList = ""
		for commaCheck in InputRecipe[index].split(','):
			#There is a comma, so check for adjectives
			if commaCheck != InputRecipe[index]:
				RemoveSecondPart = False
				for word in commaCheck.split():
					word=word.lower()
					if word in CommonAdj:
						RemoveSecondPart = True
				if RemoveSecondPart == False:
					AddtoList += commaCheck
			else:
				AddtoList = commaCheck

		AddItemToMaster(AddtoList,MasterList)





if __name__ == '__main__':
	TrialList = {'dog':15}
	print('duck' in TrialList)
	print('dog' in TrialList)
	#ParseIngredients()
	MasterList = {}
	InputRecipe=["1 cup warm milk (120 to 130 degrees F)",
"1 teaspoon white sugar",
"2 ½ teaspoons rapid-rise yeast",
"2 eggs, room temperature",
"⅓ cup unsalted butter, melted and cooled",
"2 ½ cups all-purpose flour",
"1 ½ cups whole wheat flour",
"½ cup white sugar",
"1 teaspoon salt",
"2 cups all-purpose flour",
'3 eggs','salt and pepper to taste'
]

	ParseIngredients(InputRecipe,MasterList)
	print(MasterList)
