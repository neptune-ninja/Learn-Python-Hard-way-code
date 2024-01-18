#create a mapping of states to there Abbrevations
states = {
	
	'Karnataka' : 'KA',
	'Maharashtra' : 'MH',
	'Tamilnadu' : 'TN',
	'Kerala' : 'KL',
	'Delhi' : 'DL'
}

#Create a basic set of cities in the states
cities = {
	
	'KA' : 'Bengaluru',
	'MH' : 'Mumbai',
	'TN' : 'Chennai'
}
#Adding few more cities to the list
cities['DL'] = 'Delhi'
cities['KL'] = 'Kochi'

#print out some cities

print('-' * 15)

print("Karnataka State has ", cities['KA'])
print("Maharashtra state has",cities['MH'])

#print some state abbrevations
print('-' * 15)

print("Kerala's abbrevation is ",states['Kerala'])
print("Delhi's abbrevation is ", states['Delhi'])

#print it by using state then cities dict
print('-' * 15)

print("Kerala state has ", cities[states['Kerala']])
print("Delhi state has ", cities[states['Delhi']])

#print every state abbrevation
print('-' * 15)

for state,abbre in list(states.items()):
	print(f"{state} is abbrevated as {abbre}")

#print every city in state
print('-' * 15)

for abbre,city in list(cities.items()):
	print(f"{abbre} has the city {city} ")

#now do both state and city in single
print('-' * 15)

for state,abbre in list(states.items()):
	print(f"{state} is abbrevated as {abbre}")
	print(f"and has city {cities[abbre]}")

print('-' * 15)

#get the state which does not have abbrevation

state = states.get('Sikkim')

if not state:
	print("Sorry not Sikkim")

#get the city with default value
city = cities.get('SK','Does not exists')
print(f"The city for the state of 'SK' is ,{city}")


















