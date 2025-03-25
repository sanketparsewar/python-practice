# xxxxxxxxxxxxx-------------HashMap in python is called Dictionary ------------xxxxxxxxxxxxxxx


# ------Dictionary = elements are in form of key value pairs
# d={'mon':2,'tue':3,'wed':4,'thu':6,'fri':9,'sat':10}
# print(d.keys())
# print(d.values())
# print(d)
'''Methods in dictionary: 
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary'''


# ------Dictionary and different methods
'''
weather={'jan1':27,'jan2':31,'jan3':23,'jan4':34,'jan5':37,'jan6':38,'jan7':29,'jan8':30,'jan9':35,'jan10':30}
print(weather)
avg_1stweek=0
count=0
for i in weather:
    if count<=6:
        avg_1stweek+=weather[i]
        count+=1
max_list=[]
for i in weather:
    max_list.append(weather[i])
print('The average temperature in first week of Jan:',avg_1stweek/7)
print('The maximum temperature in first 10 days of Jan:',max(max_list))
print('The temperature on Jan 9:',weather['jan9'])
print('The temperature on Jan 4:',weather['jan4'])
'''

#---------- get count of words from given text
'''
p=input("Enter Text: ")
poem=p.split(' ')
counts=[]
for i in poem:
    c=poem.count(i)
    counts.append(f'{i}:{c},')

counts1=set(counts)
for i in counts1:
    print(i)
'''


# -------------expenses of months using dictionary ------------------  
'''
expense={"January" : 2200, "February" : 2350, "March":2600, "April":2130, "May":2190}
print(expense)
print('expense["February"]-expense["January"]=',expense["February"]-expense["January"])
sum=0
for values in expense:
    sum=sum+expense[values]
print('Total expense =', sum)
'''


# --------- Python | Sort Python Dictionaries by Key or Value
'''
month = {'jan': 2, 'feb': 3, 'march': 5, 'april': 9, 'may': 6, 'june': 8}
month_key=month.keys()
month_key_li=list(month_key)
month_key_li.sort()
month_d=[]
for i in month_key_li:
    month_dict_item=(i,month[i])
    month_d.append(month_dict_item)
month_dict=dict(month_d)
print(month_dict)
'''

# -------Handling missing keys in Python dictionaries
'''
month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8}
try:
    key=input("enetr key to get value ")
    print(key, month[key])
except :
    print("key not found")
'''


# ----Python dictionary with keys having multiple inputs
'''
month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8}
num=int(input("number of keys "))
for i in range(num):
    key=input("enter key ")
    print(key,month[key])
'''

# -------Python program to find the sum of all items in a dictionary
'''
month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8}
month_value=month.values()
month_value_li=list(month_value)
print('sum',sum(month_value_li))
'''

# ------python program to find the size of a Dictionary
'''
month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8,'july':17,'august':13}
print(month.__sizeof__(),'bytes')
'''