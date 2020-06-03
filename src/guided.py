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



