# https://www.py4e.com/html3/07-files
# the file handle is sequence of strings
fhand = open('stuff.txt')
print(fhand)
#<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>

#new line ####################################### this in the file
 stuff = 'Hello\nWorld!'
# >>> stuff
# 'Hello\nWorld!'
print(stuff)
Hello
World!
stuff = 'X\nY'
print(stuff)
# X
# Y
len(stuff)
#3


#reading .......................
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# reading the whole file
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
From stephen.marquar

# print all the lines start with From: and strip off the newline in the file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Code: http://www.py4e.com/code3/search2.py

# bad file names handling
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Code: http://www.py4e.com/code3/search7.py


"""
7.1 Write a program that prompts for a file name,
then opens that file and reads through the file,
and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.rstrip()
    print(line.upper())


"""

Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:

X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.


"""
