#list-inbuilt datatype
#list-mutable-means we can add ,update and delete element sof the list the the same memory location
#list is iterable data type
#list is ordered means it will support indexing and slicing
#list is heterogenous
l=[10,20,30,40,"pyhton","java",[100,200,300]]
print(l)
print(type(l))
print(id(l))
#indexing and slicing is same as string
print(l[3])
print(l[-1])
#in this way we can reach elements inside list of a list
print(l[-1][1])
#slicing
print(l[:5])
#reverse  alist
print(l[::-1])
print(l)
l=[100,200,300,400,500]
print(id(l))
for value in l[::2]:
    print(value)
#different methods to add elements to a list
    #1.append()
l.append(700)
print(id(l))
print(l)
   #extend()-if you want to add multiple elements you can use extend method
#when we use extend it will start iterating over the elemnts and it will alos take single argumenty
l.extend([10,20,30])
print(l)
l.append([10,20,30])
print(l)
#for exampple
l.extend("Python")
print(l)
#append and extend add elements at the last of the list
#if we want to add elements at the inbetween
#we use insert(index,value)
l.insert(1,1000)
print(l)
#copy method
l=[10,20,30]
l2=l
print(id(l),id(l2))
print(l,l2)
l.append(20)
print(l,l2)
#for this we use copy it will copy elements at different memory location
l2=l.copy()
print(l2)
print(id(l),id(l2))

