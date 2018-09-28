##list and dictonary are similar so
lst = list()
lst.append(21)
lst.append(183)   #key is 0,1,2,3  value is 21,183...

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)    #key is age,course..  value is 21,183...

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

#Dictionary as a set of counters
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)


>>> counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
>>> print(counts.get('jan', 0))
100
>>> print(counts.get('tim', 0))
0
#We can use get to write our histogram loop more concisely. Because the get
# method automatically handles the case where a key is not in a dictionary, w
# e can reduce four lines down to one and eliminate the if statement.

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)


# We will write a Python program to read through the lines of the file,
# break each line into a list of words, and then loop through each of the words
# in the line and count each word using a dictionary


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Looping and dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# list of keys
print(list(counts))

# list of keys
print(counts.keys())

#list of values
print(counts.values())

#list of tuples
print(counts.items())

for kkk, vvv in counts.items():
    print(kkk,vvv)


# 9.4 Write a program to read through the mbox-short.txt and figure out who has the
#  sent the greatest number of mail messages. The program looks for 'From ' lines
#  and takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary that maps the sender's mail address
#  to a count of the number of times they appear in the file. After the dictionary
#  is produced, the program reads through the dictionary using a maximum loop to
#  find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    # print (line)
    if line.startswith('From:'):
        person = line.split()[1]
        counts[person] = counts.get(person,0) + 1

lstKeys = list(counts.keys())
lstValue = list(counts.values())
index = None
maxNum = 0
for i in range(len(lstValue)):
    if lstValue[i] > maxNum:
        maxNum = lstValue[i]
        maxIndex = i

print(lstKeys[maxIndex], maxNum)


# print all the words and lines in a files

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open (fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    words = lin.split()
    #print(wds)

    # for w in words:
    #     if w in di :
    #         di[w] = di[w] + 1
    #         print('***Existing***')
    #     else:
    #         di[w] = 1
    #         print('***NEW***')
    #     print(di[w])

    for w in wds:
        di[w] = di.get(w,0) + 1

print(di)

largest = -1
theWord = None
for k,v in di.items():
    print(k,v)
    if v > largest :
        larget = v
        theWord = k

print(larget , theWord)
