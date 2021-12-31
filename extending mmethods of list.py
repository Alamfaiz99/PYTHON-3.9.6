#update and delete elements of a list
#update elements
l=[10,20,30,40,50]
l[2]=300
print(l)
#delete-various methods
#1.pop,remove,clear,del
#pop works on LIFO
r=l.pop()
print(l)
print(r)
#pop with particular index
r=l.pop(1)
print(l,r)
#want to remove on the basis of values
#remove method
r=l.remove(10)
print(l)
#for example if we jhave multiple occurance of any element
#still remove method removes only one at a time
#if we want to remove all the lements we use clear method
l.clear()
print(l)
#if you want to remove list form memory location
#use del operator
del l
#print(l)
#it will throw error
#built iin function for list
l=[50,40,30,30,20,10]
#sort method
l.sort()
print(l)
#reverse
print(l[::-1])
#reverse method is present
l.reverse()
print(l)
#for sorting we have another method
#sorted() returns sorted list
#it will work on any data type
r=sorted(l)
print(r)
print(l.index(30))
#it will tell the index of 30
#count-counts total no of occurances
print(l.count(30))
#concatenate two lists
l=[10,20,30,40]
l2=[100,200,300]
print(l+l2)
l=[0.1]
print(l*10)
