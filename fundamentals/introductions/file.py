num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # variable declaration
string = 'Hello World' # variable declaration, Data Types, Primitive, Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Lists
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionarys
fruit = ('blueberry', 'strawberry', 'banana') # Tuples
print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') 
print(person['name']) # log statement
person['name'] = 'George' #setting name - john = George
person['eye_color'] = 'blue' #setting (pushing) eye_color - 'blue'
print(fruit[2]) # log statement

if num1 > 45: # conditionals - if
    print("It's greater") # log statement
else: # conditionals - else
    print("It's lower") # log statement

if len(string) < 5: # conditionals - if
    print("It's a short word!") # log statement
elif len(string) > 15: # conditionals - else if
    print("It's a long word!") # log statement
else: # conditionals - else
    print("Just right!") # log statement

for x in range(5): # for loop start
    print(x) # log statement
for x in range(2,5): # for loop start
    print(x) # log statement
for x in range(2,10,3): # for loop start
    print(x) # log statement
x = 0 # Variable Decloration
while(x < 5): # While loop start
    print(x) # log statement
    x += 1 # Variable Decloration

pizza_toppings.pop() # List - delete value
pizza_toppings.pop(1) # list - delete value - index 1   

print(person) #log statements
person.pop('eye_color') #list 
print(person) # Log Statements

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # conditional if
        continue # for loop continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if
        break # for loop break

def print_hello_ten_times(): # function
    for num in range(10): # for loop start
        print('Hello') # log statement

print_hello_ten_times() # function argument

def print_hello_x_times(x): # function - parameter (x)
    for num in range(x): # for loop start
        print('Hello') # log statement

print_hello_x_times(4) # function argument (4)

def print_hello_x_or_ten_times(x = 10): # function 
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # function argument ()
print_hello_x_or_ten_times(4) # function argument (4)


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'pop'