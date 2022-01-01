l1=[1,2,3,4,5]
l2=[1,4,9,16,25]
#how to create dict out of list
#zip()---combine elements with same index
#typecast into dict
d=dict(zip(l1,l2))
print(d)
#fromkeys()----method makes dict of keys set to default value none
#l=[1,2,3,4,5]
#d1=dict.fromkeys(l,0)
#print(d1)


d1={1:1,2:4,3:9,4:16}
d2={5:25,6:36,7:49}

#we want to merge both dict
#update()---to merge two dict
d1.update(d2)
print(d1)

#delete items of dict
#pop--pop taken key value as argument 
#popitem--will not take the argument--randomly takes an rgumrnt and del it
#clear--clear whole dict
#del--it deletes the memory loc of dict
d3={1:1,2:4,3:9,4:16}
r=d3.pop(2)
print(d3)
r1=d3.popitem()
print(d3,r1)
print(d3.clear())
del d3
print(d3)

