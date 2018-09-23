# list can have different thing inside
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []

>>> print(cheeses[0]])

#list are mutbale string is immutable


#Traversing a list
#The most common way to traverse the elements of a list is with a for loop. The syntax is the same as for strings:

for cheese in cheeses:
    print(cheese)
#This works well if you only need to read the elements of the list. But if you want to write or update the elements, you need the indices. A common way to do that is to combine the functions range and len:

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2



    #The + operator concatenates lists:

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]



    # List slices
    # The slice operator also works on lists:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']


#append adds a new element to the end of a list:

>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print(t)
['a', 'b', 'c', 'd']

#extend takes a list as an argument and appends all of the elements:

>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
This example leaves t2 unmodified.


# Deleting elements
# There are several ways to delete elements from a list. If you know the index of the element you want, you can use pop:

>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b

# in or not in the list




#sort arranges the elements of the list from low to high:

>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']

#list and string
>>> s = 'pining for the       fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']
>>> print(t[2])
the
