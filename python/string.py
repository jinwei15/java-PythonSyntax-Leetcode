"""
string is like a array of chars
you can access it by string fruit[0]
"""
zot = 'abc'
print(zot[0])

# Length of the string
print(len(zot))

#loop through string
######################
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (letter)
    index = index + 1

######################
fruit = 'banana'
for letters in fruit
    print (letter)

# slicing string (cut before this chunk)
s = 'Monkey python'
print (s[0:4])
print (s[6:7])
print (s[:4])# all the way to before 4
print (s[4:])# all the way after 4


#string concatenation:

a = 'Hello'
b = a + ' There'
print(b)


#in statement in string

fruit = 'banana'
if 'a' in fruit :
    print('Found it')

if 'nan' in fruit :
    print('Found it')

#string comparision
word = 'banana'
if word == 'banana' :
    print('YES')

#string library
print('Hellow There'.lower())
greet = 'Hello bob'
zap = greet.lower()
print(zap)
print(greet)

## find what it is capable of
stuff = 'Hello world'
type(stuff)
dir(stuff) #this is what it is capable of
