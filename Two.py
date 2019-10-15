#Control Flow

    #Syntax of for loop
'''
for variable in sequence:
    statement(s)
'''
colors = ['Red', 'Black', 'Blue', 'White', 'Pink']
for color in colors:
    print(color)

print('\n-------------------------------------')
for index in [1, 2, 3, 4, 5]:
    print("{} times 5 is {}".format(index, index * 5))
print('\n------------------------------------')

#The While loop
#Syntax of While loop
'''
while condition:
    statement(s)
'''
flag = 10
while 0 < flag:
    print(flag)
    flag = flag - 1
print('Go !!')
print('\n-------------------------------------')

'''
    #The Range Function
The range function in Python generates a list of numbers, 
which can be used to iterate over for loops and in other few cases.
'''
# range(n)
# range(begin, end)
for number in range(1,7):
    square = number * number 
    print(square)

#Declaring a function
'''
def function_name(formal parameters):
    statement(s)
'''
def greet():
    print("Hello !Welcome to the python ")
print('\n-------------------------------------')
greet()

#Functions with parameters.
def greet2(name):
    print("Hello [{}] How are you today?".format(name))

greet2("Natthanon")
greet2("Fern")
greet2("Biew")

print('\n---------------------------------')

def num_factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factory does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else: 
        for i in range(1,num + 1):
            factorial = factorial * i
            print("i {} factorial {}".format(i,factorial))
    print("I {} The factorial of number is {}".format(i,factorial))


num_factorial(5)

name = input('Please enter Name ')
print(name);