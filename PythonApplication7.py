#creating a dictionary
country_capital = {"United States": "Washington D.C", "Itlay": "Rome","England": "London"}

#printing the dictionarry
print(country_capital)

#Valid dictionnary

mydict = {
          1: "Hello",
          2: "Hello Hi",
          3: [1,2,3]
         }

#get dictionary's lenght
print(len(country_capital))

Dict = dict({1: 'Just', 2: 'For', 3: 'Geeks'})
print ("\nDictionary with each item as a pair")
print (Dict)
print(Dict[1])

#   Key unmutable but valu mutable
#Add an item with a key
country_capital["Germany"] = "Berlin"

#delete an item
del country_capital["United States"]
#print dictionarry keys
for country in country_capital:
    print(country)
    
print ("---------")

for keys,values in country_capital.items() :
    print (country_capital.keys())
    print (country_capital.values())
    
dict1 ={1: "Python", 2: "Java", 3:"Ruby", 4: "Scala"}

#copy methode
dict2 = dict1.copy()

#pop method
dict2.pop(4)
print (dict2)

#pop the last item
dict2.popitem()
print(dict2)

#update() methode
dict2.update({3: "Scala"})
print(dict2)

#List ordered and changeable, tupper ordered and unchangeable, dictionary ordered and changeable (but no duplicate), set unordered un changeable and unindexed

cities =('Paris', 'Athens', 'Madrid')

continent = 'Europe'

mydictionary = dict.fromkeys(cities, continent)

print(mydictionary)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]

capital = {}

for i in range (3):
    capital[keys[i]] = values[i]
print(capital)

#Créer un dictionnaire à partir de deux liste
#zip prend deux listes et en fait un tupple
res_dict = dict(zip(keys, values))
print(res_dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty' : 40}
dict1.update(dict2)
print (dict1)

#Autre moyen
dict3 = {**dict1,**dict2}
print (dict3)
print (dict3)

sampleDict = {"class": {"student":{"name" : "Mike", "marks" : {"physics": 70, "history": 80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res = dict.fromkeys (employees, defaults)
print (res)

#Individual data
print(res["Kelly"])

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}

sample_dict.pop("name")
sample_dict.pop("salary")
print(sample_dict)

adict = {
    'emp1': {'name': 'Jhon', 'salary':7500}, 'emp2': {'name': 'Emma', 'salary':8000}, 'emp3': {'name': 'Brad', 'salary':500}}
adict.update({'emp3': {'salary' : 8500}})
print (adict)