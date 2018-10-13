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
# * means zero or more

# ^X.*:  it means I am looking a word that start with X follow by any number of characters follow by colum


"""
X-adfhjkah:
X-safdf$$$:
"""
