import requests
from bs4 import BeautifulSoup
import json

def ScrapeRecipe(URL):
	#Initialize Scrape Attempts counter
	Attempts = 0
	#Set page to Null
	page = None
	#Only attempt 5 times
	while page == None and Attempts < 5:
		#Try to get page data
		try:
			page = requests.get(URL)
		#If page unreachable, wait 1 second and try again
		except:
			time.sleep(1)
			Attempts +=1

	#Page Data could not be scraped succesfully
	if page == None:
		print("Could Not Connect to URL")
		return (None)

	#Initialize the return object and begin parsing return data
	Recipe_Object = {}
	soup = BeautifulSoup(page.content, 'html.parser')

	#Scrape Ingredients
	Ingredients_Section = soup.find_all(class_='ingredients-item-name')
	Ingredients = [] 
	for items in Ingredients_Section:
		Ingredients.append(items.text.strip())
	Recipe_Object['Ingredients'] =Ingredients
	
	#Scrape Instructions
	Instruction_Section = soup.find_all(class_='subcontainer instructions-section-item')
	Instructions = [] 
	for items in Instruction_Section:
		Instructions.append(items.text.strip())
	Recipe_Object['Instructions'] = Instructions
	
	#Scrape Nutrition
	Nutrition = soup.find(class_='nutrition-section container')
	Recipe_Object['Nutrition'] = Nutrition.find(class_='section-body').text
	
	#Scrape the URL for Image and Title of Recipe
	PhotoLink = soup.find(class_='image-container')
	Image_And_Title = str(PhotoLink.img).split('"')
	
	#Parse Title
	Recipe_Object['Title'] = Image_And_Title[1] #Title
	
	#Parse Image URL
	Recipe_Object['Image'] = Image_And_Title[3] #JPG
	
	#Return data as Json
	return(json.dumps(Recipe_Object))


if __name__ == '__main__':

	URL = 'https://www.allrecipes.com/recipe/91836/ds-whole-wheat-challah/'
	print(ScrapeRecipe(URL))