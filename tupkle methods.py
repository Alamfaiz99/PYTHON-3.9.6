#Tuple is immutable datastructure
#because we cannot add,modify and delete elements of tuple at same same memmory location
#tuple is iterative adaty type
#tuple is ordered data type means it supports indexing and slicing
#tuple:
t=(10,20,20,20,30,30,40)
#print(type(t),t)
#help(tuple)
print(t[0])#first elemet
print(t[-1])#last element
#slicing
print(t[:3])
#index method
#count mnethod
#these methods return values
print(t.index(20))
print(t.count(20))
#Tuples are mainly used when you pass data from one fun to another fun
#example how python uses tuple
l=[10,20,30,40]
for index,value in enumerate(l):
    print(index,value)
#enumerate functiion actually return a tuple
for t in enumerate(l):
    print(t)
#if you ahve a list how can you convert into tuple
#we use type caste method
l=[10,20,30,40]
t=tuple(l)
print(t)
#now if you ahve tuple and wants to convert imto list
t=(10,20,30,40,50)
l=list(t)
print(l)
