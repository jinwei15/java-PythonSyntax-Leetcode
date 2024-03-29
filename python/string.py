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
for letters in fruit:
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
up = greet.upper()
print(zap)
print(greet)

## find what it is capable of
stuff = 'Hello world'
type(stuff)
dir(stuff) #this is what it is capable of


# replace string
sentence = 'Hello Bob'
sentence.replace('Bob','Jane')
print(sentence) #Hello Jane
sentence.replace('o','X') #HellX BXb


#remove white space
greeting  = '       Hello Bob   '
greeting.lstrip()#'Hello Bob   '
greeting.rstrip()#'       Hello Bob'
greeting.strip()#'Hello Bob'  remove both left and right space


#start with something
line = 'Please have a nice day'
line.startswith('Please') #true
line.startswith('P') #true

#phrasing and extracting
data = 'From jinwei.zhang18@imperial.ac.uk Sat Jan 5 150'
atpos = data.find('@')  # 19
addpos = data.find(' ',atpos) #find the space after atpos which is 34

host = data[atpos+1:addpos]


"""
Exercises
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
"""




"""
Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional."""
