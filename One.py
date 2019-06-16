
fuel = True
speed = 167
miles = 153.5
location = 16.789 + 12323.45j
car = "Mustang"

# type() function returns the datatype of variable.

print(fuel, type(fuel))
print(speed, type(speed))
print(miles, type(miles))
print(location, type(location))
print(car, type(car))

#.format().function 
print("---------------------------")
name = "Agent 47"
code_number = 1011010
message = "Hey {}, your code number is {}.".format(name, code_number)
print(message)

#data structures in Python(Lists, Tuples, Dictionaries)

world_tour = ["Paris", "New York", "Melbourne", "Swiss"]
print(type(world_tour))
print(world_tour)
print(world_tour[0])
print(world_tour[1])
print(world_tour[-1])
#Note: Negative indices starts from the end of the list with index value -1.

#several methods on lists
stationery_list = ["Pen", "Pencil", "Notepad"]
stationery_list.append("Eraser")
# Adds new item at the end of the list
print(stationery_list)
stationery_list.insert(2, "Files")

print(stationery_list)
stationery_list.index("Pen")

#Tuples
#Tuples are ordered, immutable sequence of values. Declaring tuples 
#is similar to lists we just enclose the values in pair of parentheses.
#my_tuple = (item_1, item_2, item_3)
#Tuples are immutable which means we cannot add or delete items in the tuple, and also tuples have no index methods.

atmosphere = ("Oxygen", "Hydrogen", "Nitrogen")
print(type(atmosphere))
print(atmosphere)
#Why use tuples?
#Tuples are faster than lists and safer.They are written -protected 
#we cannot add new items once the declaration is made.

#Dictionary
#my_dictionary = {key_1 : value1, key_2 : value2 , key_3 : value3}

code_name = {"jack": 4098, "sape": 4139, "robb": 2323}
print(type(code_name))
print(code_name)
# You can remove items in the dictionary by using the del keyword.
del code_name["sape"]
print(code_name)
"""
You can update the values of the dictionaries by overriding them.
code_name[‘jack’] = 1212
"""

# The len function returns the number of key-value pairs in the dictionary.
len(code_name)


#Conditionals (if, elif, else)
#if Sample 
temperature = 27
if temperature <= 30:
    print("Let’s go to the party!")

# two possibilities of conditions,
movie_tickets = 4
if(movie_tickets >= 4):
    print("Tickets are available, Let’s go to the movie.")
else:
    print("Let’s have a drink, tickets are not available.")
'''
Multiple conditions
If we have more than two possibilities and we need more than two branches. SO we use chained conditional statements. 
#abbreviation ตัวย่อ
'''
weight = 77
height = 180
bmi = (weight / (height**2)) * 10000
print("Computing...")
print("Your bmi is {}\n".format(bmi))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.99:
    print("Perfect ! Normal weight")
elif 25.00 <= bmi <= 30.00:
    print("Overweight")
elif bmi > 30.00:
    print("Obese")

