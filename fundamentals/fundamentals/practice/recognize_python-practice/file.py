num1 = 42 #variable declaration, number initialized
num2 = 2.3 #variable declaration, decimal/float initialized
boolean = True #variable declaration, boolean initialized
#variable declaration, string initialized
string = 'Hello World'
#variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
# print to console, type check 
print(type(fruit))
# print to colsone, list acces value
print(pizza_toppings[1])
#list, add value
pizza_toppings.append('Mushrooms')
#print to console, dictionary acces value
print(person['name'])
#dictionary, change value
person['name'] = 'George'
#dictionary change value
person['eye_color'] = 'blue'
#print to console, tuple acces value
print(fruit[2])
#conditional if evaluation, print to console, conditional else print to console
if num1 > 45:
    print("It's greater")

else:
    print("It's lower")
#conditional if - elif - else, print to console
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#for loop start 0 end 5 print to console
for x in range(5):
    print(x)
    #for loop start 2 end 5 , print to console
for x in range(2,5):
    print(x)
# for loop start 2 end 10 increment 3 , print to console
for x in range(2,10,3):
    print(x)
#while loop variable declaration 
x = 0
while(x < 5):
    #print to console
    print(x)
    #incrementing x
    x += 1
#list delete value at end 
pizza_toppings.pop()
#list delete value at index
pizza_toppings.pop(1)
#print to console dictionary
print(person)
#ddictionary delete value at index
person.pop('eye_color')
#print to console dictionary
print(person)
#for loop list
for topping in pizza_toppings:
    #conditional if 
    if topping == 'Pepperoni':
        #continues
        continue
        #print to console
    print('After 1st if statement')
    #conditional if 
    if topping == 'Olives':
        #breaks
        break
#function declaration
def print_hello_ten_times():
    #for loop start 0 end 10
    for num in range(10):
        #print to console
        print('Hello')
#function call
print_hello_ten_times()
#function declaration parameter x
def print_hello_x_times(x):
    #for loop 
    for num in range(x):
        #print to console
        print('Hello')
#function call argument 4
print_hello_x_times(4)
#function declaration 
def print_hello_x_or_ten_times(x = 10):
    #for loop until x
    for num in range(x):
        #print to console 
        print('Hello')
#function call end 10
print_hello_x_or_ten_times()
#function call end 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
##variable declaration, number initialized
num3 = 72
#print to console
print(num3)
#tuple change value
fruit[0] = 'cranberry'
#print to console
print(person['favorite_team'])
#print to console
print(pizza_toppings[7])
#print to console
print(boolean)
#tuple add value
fruit.append('raspberry')
#tuple delete value at index
fruit.pop(1)