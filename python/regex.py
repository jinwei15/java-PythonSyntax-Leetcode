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
 # [0-9]+ one or more digit

 x = 'My 2 faverate number are 14 and 89'
 y= re.findall('[0-9]+',x) # return list
 print(y) # ['2' '14' '89']

 y=re.findall('[AEIOU]+',x) # at least one A or E or ...
 print(y) # empty list


 # Greedy matching
 x= 'From: using the: characters'
 y = re.findall('^F.+:',x) # it will find the largest string match
 # y = 'From: using the:'

 x= 'From: using the: characters'
 y = re.findall('^F.+?:',x) # it will find the non-greedy string match
 # y = 'From:'

 x= 'From jinweizhang@gmail.com asdf bbb'
 y=re.findall('\S+@\S+',x) # this must be greedy otherwise it will be g@g


 x= 'From jinweizhang@gmail.com asdf bbb'
 y=re.findall('From (\S+@\S+)',x) # ()  this is the thing I want to extract

 # extract  the  host : method_1:find the @ find the space behind cut
 # method_2: split the whole line get the whords[1] split by @ get the result[1]
 y = re.findall('@([^ ]*)') # [^ ] not everything but a space


 # \$ means the real dollor sign


"""

Welcome Jinwei Zhang from Using Python to Access Web Data

Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_133844.txt (There are 79 values and the sum ends with 905)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative
7 and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that
everyone needs to know how to program ...
The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none)
"""

fhand = open('regex_sum_133844.txt')
total = 0
for line in fhand:
	line = line.rstrip()
	lst = re.findall('[0-9]+',line) # at least one A or E or ...

	if len(lst) > 0 :
		#print(lst)
#
		lst = [int(i) for i in lst]
		total = total + sum(lst)

print(total)
