# This is week 6 tuples:

# looks just like list but we use partences 

#index start from 0 as well.

x=('gem'.'sally','John')

print(x[2])

y=(1,2.3)
print(y)
print(max(y))

for iter in y:
	print(iter)


#tuple are immutable 

#list:
x = [3,4,5]
x[0]=8

#tuple
x=(3,4,5)
x[0] = 9
#this will cause trace back 

#string 
x='123'
x[0]=8
#this will cause trace back as well.

#things can not do to a tuple
x=('1,2,3')
x.sort()
x.append(5)
x.reverve()
#all trace back

#all the function that list can do
l = list()
dir(l)
#append count extend index insert pop remove reverse sort 
t= tuple()
#count index //but mroe effieicent


#tuple can do 2 assignment 
(x,y)=(4,'friend')
print(y)
#friend

(x,y)=5
#this is wrong track back 


#tuples and dictionary 
d=dict()
d['jinwei'] = 2
d['yong'] = 5
#items isa list of two itens  tuples
for (k,v) in d.items():
	print(k,v)

"""
jiwnei 2
yong 5
""" 

tup = d.items()
print(tup)




#tuple is compareable
(0,3,3) < 5,2,3()#true
('john','Zed')>('john','ian')#true!
# it willcompare the john if match look at  Zed





#sort dict based on key
d= {'a':10,'b':1, 'c':22}
d.items()

sorted(d.items())
#[('a',10),('b',1),('c',22)]

for k,v in sorted(d.items):
	print(k,v)

#sort by value 
c = {'a':10,'b':1'c':22}
temp = list()
for k,v in c.items():
	temp.append((v,k))#each item in the list is a tuple 
print(temp)

temp = sorted(tmp, reverse= True)
print(temp)
	


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#ten most common words. more advanced. Please understand each pieces of code by yourself
#constructing the dictionary 
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
#reverse the key and the value as a tuple 
lst = list()
for key,val in counts.items()
	newTuple = (val,key)
	lst.append(newTuple)
# sort the lst of tuple based on the value
lst = sorted(lst,reverse = True)

#print out the first item in the list and in a normal way 
for val,key in lst[:10]:
	print(key,value)













