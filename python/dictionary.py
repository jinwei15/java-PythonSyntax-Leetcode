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
#We can use get to write our histogram loop more concisely. Because the get method automatically handles the case where a key is not in a dictionary, we can reduce four lines down to one and eliminate the if statement.

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
