from standards.Conversions import DryMeasures

def convert(vals,key='auto'):
	total = 0
	if(key=='auto'):
		if (vals > 12):
			key = 'cup'
		elif (vals > 3):
			key = 'tbs'
		else:
			key = 'tps'
	if(key == 'cup'):
		while(vals > 48):
			total +=1
			vals-=48
		total = total + round(vals/48,3)
		return([total,key])
	if(key == 'tbs'):
		while(vals > 3):
			total +=1
			vals-=3
		total = total + round(vals/3,3)
		return([total,key])
	if(key == 'tps'):
		total = vals
		return([total,key])


#Cannot convert something like: "3 plum tomatoes"
def CalcUnits(ingred):
	temp = ingred
	units = 0
	for size in DryMeasures:
		correction = 0
		for i in range(0,len(temp)):
			index = i-correction
			if size in temp[index]:
				for word in temp[index].split():
					word = word.lower()
					if word.isdigit():
						units+= int(word)*DryMeasures[size]
					if '/' in word:
						num, denom = word.split('/')
						units+=round(float(int(num)/int(denom))*DryMeasures[size],2)
				correction+=1
				del temp[index]
	#Temp should catch all values that do not have standard measurement values
	print(temp)
	return(units,temp)


if __name__ == '__main__':
	ingredients = ['1 1/2 cup ground ginger','1 plum tomatoe','1 tbs ginger', '3 tablespoons ginger', '5 cups ginger']
	tot_units = CalcUnits(ingredients)
	print(tot_units)
	print(convert(tot_units[0]))
	print(convert(tot_units[0],'cup'))
	print(convert(tot_units[0],'tbs'))
	print(convert(tot_units[0],'tps'))
