#set mutable---we can add,update or del elements of set
#all the elements should be unique
#you can add immutable datatypes in set--int,float,tuple,str
#set---unordered datastructure
#indexing and slicing is not possible
#s1={10,20,30,40,20,40,40}#printing {40,10,20,30}--because unordered datastructe
#print(s1,type(s1))
#s2={100,200,300,400}

#add elemt to a set
#add()--add single element to set
#s2.add(500)
#print(s2)

#set operations
#union intersection difference---bw two set
#symmetric_difference()---all elements of sets except common elemnts
#s1={10,20,30,40,50,60}
#s2={40,50,60,70,80,90}
#s3=s1.union(s2)
#s4=s1.intersection(s2);
#print(s3,s4)
#s5=s1.difference(s2)
#print(s5)
#s6=s1.symmetric_difference(s2)
#print(s6)


#update method()--updates the original set
s1={10,20,30,40}
s2={50,60,70,80}
#s1.update(s2)
print(s1)
#intersection_update()--
s1.intersection_update(s2)
print(s1)
#difference_update()--
s1.difference_update(s2)
print(s1)
#symmetric_difference_update()--
s1.symmetric_difference_update(s2)
print(s1)

#to check subset or nrnot
#issubset()
#issuperset
s3={100,200,300,400}
s4={100,200,300}

print(s2.issubset(s1))

print(s1.issuperset(s1))


#how to typecast
l=[100,200,300,400,500]
s11=set(l)
print(s11)


l1=[100,200,300,400]
l2=[50,100,150,200,500,45,30,25]

#sorting a list
s1=set(l1)
s2=set(l2)
s3=s1.union(s2)
print(s3)

l3=list(s3)
print(l3)
l3.sort()
print(l3)

#detelte operations of set datatype

#pop--it will atke a random no and delete and return the deleted value
#remove--del a particular value and not rfeturns only deletes
#discerd--same as remove but if element is notv present it does not throw any error
#clear--remove all the elements
#del--del the memory location
s={100,200,300,400,500,600}
#r=s.pop()
#print(s,r)
#s.remove(100)
#print(s)
#s.discard(100)
#print(s)
#s.clear()
#print(s)
del s
print(s)
