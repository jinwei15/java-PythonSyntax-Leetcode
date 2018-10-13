# regular expression
import re

# re.search() to used to see if a string match a regular expression
#similar using find()

#re.findall() is like extration finding and pulling out.

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


"""
is the replace of:::

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
"""

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):  # the ^F mean I want the F form the begining of the line
        print(line)

"""
is the replace of:::

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)
"""

# -------------------------------------------------------------------------------------------------
# . means any character
# * means zero or more (many times)
# + means zero or more. (once or more times)
# \S means non-white space charater

# ^X.*:  it means I am looking a word that start with X follow by any number of characters follow by colum
"""
X-adfhjkah:
X-safdf$$$:
"""
# ^X-\S+:  I am looking a string that 1:start with X    2:follow by dash  3. follow by any non-white space
# characters one or more time. 4. follow by a colum

"""
X-asdf:   right
X-palce jj: wrong
"""


# -------------------------------------------------------------------------------------------------
# matching and extracting Data
# [ ] description of one character can have list range digits
# [0-9] + one or more digit

x = 'My 2 faverate number are 14 and 89'
y= re.findall('[0-9]+',x) # return list
print(y) # ['2' '14' '89']

y=re.findall('[AEIOU]+',x) # at least one A or E or ...
print(y) # empty list
