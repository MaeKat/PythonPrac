#Inclass and on my own python testing
#takes an input name and outputs the name and then changes the name to uppercase and outputsname
print('Enter your name')
x = input()
print ('Hello, ' + x)
x=x.upper()
print('HELLO, '+ x)

import datetime
d= datetime.datetime.now()
print("The time is: ")
print( d)

#Array A
a = [1,2,3,4]
print("Array A: is")
print(a)
print(type(a))

#Array B
b = ['red','blue','green','yellow']
print("Array B: is")
print(b)
print(type(b))

#Array C
c = list("hello world!")
print("Array C: is")
print(c)
print(type(c))

#Array D
d=a
#Array D with 6
d.append(6)
print(d)
print(type(c))
#Array D with hello
d.append('hello')
print(d)
print(type(c))


#R
#range makes a list 3-18 that counts by 3 (not upper bound inclusive)
r= list(range(3,18,3))
print (r)
print(type(r))
#find length
print("The lenght of r is: ")
print(len (r))
#check if 12 is in r
print("is 12 in r?")
print (12 in r)
#check if 13 is in r
print("is 13 in r?")
print (13 in r)

#s - Splitting prac
s = "This is a sentence that can be split."
print(s)
words = s.split()
print (words)

#e
e= [1,2,3,3]
#e before append
print(e)
e.append(4)
#e after append
print(e)
#e extend
e.extend([5,6,7,8])
print(e)
#e insert 5.5. at 5
e.insert (5,5.5)
print(e)
#e pop
print(e.pop())
print(e)
#e pop sepecific
print(e.pop(4))
print(e)

#f sorting
f =[23, 12, 500, 3.3, 42, 92, 7]
#f before sort
print(f)
f.sort()
#f after sort
print(f)

#Aliasing 
first = [20,31,42]
second = first
#print first and second
print(first)
print(second)
#add 53 to second
second.append(53)
#adds to both 
print(second)
print(first)
#to not have an alias and treat seperate
third = list(first)
print(third)
#ADD 55 to third
third.append(55)
print(third)
print(first)#both lists are diff

#checking diff
print("Is first equal to second?")
print(first==second)
print("Is first equal to third?")
print(first == third)
print("Is first the same as second?")
print(first is second)
print("Is first the same as third?")
print(first is third)
print("Pop 55!")
third.pop()
print("Is first equal to third?")
print(first==third)
print("Is first the same as third?")
print(first is third)


#Capitals dictionary
capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
print(capitals)
print(type(capitals))
print(capitals['Italy'])
#Add madrid
capitals['Spain'] = 'Madrid'
print(capitals)
#is Germany in capitals
print('Germany' in capitals)
#is Italy in capitals
print('Italy' in capitals)

morecapitals = {'Germany': 'Berlin','United Kingdom': 'London'}
print(morecapitals)
capitals.update(morecapitals)
print(capitals)
print("Length")
print(len(capitals))

