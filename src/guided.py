# print hello world
print("hello, world!")

#declare a variable

name = "matt"

#print a variable
print(name)

#string concatenation

print("hello " + name)

#`hello ${name}`

print(f'Hello {name}')

#data structures

#array are lists

p = [10,60,20,5,"string","another string"]
print(p)

p.append(77)

print(p)

#for loop

for element in p:
    print(element)


#let's print the index and the element at the index of P

for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]}')



#list comprehensions
#another way to create a list

numbers = [1,2,4,5,6,7,5,4]

#make a new list of squares from the numbers list
squares = []

for num in numbers:
    squares.append(num*num)
print(squares)

# lets use List Comprehensions
#for each element from numbers multiply the number by itself and add to cooler_squares
# [*what you want returned* for variable in some_list]

cooler_squares = [num*num for num in numbers]
print(cooler_squares) 

# let's create a list of just even numbers
evens = [num*num for num in numbers if num % 2 == 0]
print(evens)


names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

s_names = [name.capitalize() for name in names if name[0].lower() == "s" ]
print(s_names)