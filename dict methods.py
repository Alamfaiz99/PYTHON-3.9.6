#Dictionary datastructue in python
#mutable datatype--we can add,update and delete elements from dictionary at the same memory location
#dict---{}
#key should be unique
#keys should be immutable
#-------when we create a dictionary in the background python creates hash ttable---
#unordered datastructure--means indexing and slicing is not possible
#time complexity----O(1)
#dictionary is nothing but key value pair
#keys supports datastructure immutable :int,float,str,tuple
#d={"emp_id":"100","name":"faizan","Email":"faizanalam986@gmail.com",[10,20]:100,[10,20,30]:200}
#print(d)
#error is unhashable type because ew can update list
d={"emp_id":"100","name":"faizan","Email":"faizanalam986@gmail.com"}
print(d)
#add new keys
d["Contact_no"]=123456780
print(d)
#if we want the value we have to write key
print(d["emp_id"])
#if ew search for key which doesnot exist
#it will through error key is not found---key error
#because it will not support indexing
#print(d[0])
#built in functions
#get
#setdefault
print(d.get("emp_id"))
#if key is not available it willlllllshow none
#you can use this approach also
print(d.get("player",-1))
#setdefault method
#diffrence bw get and setdefault method
#in setdefault method will key doesnot exit it will add particular key to dic
#and set the value to none you can also get another value otherwise if exist
#returns the value
print(d.setdefault("emp_id"))
print(d.setdefault("father","Masood Alam"))
print(d)
#iterate over dictionar
for key in d:
    print(key,d[key])
d1={}
#1 :1,2:4,3:9,4:16.......10:100
for value in range(1,11):
    d1[value]=value*value
print(d1)
#keys,value,items
#keys()---print all the keys of the dictionary
print(d1.keys())
#values()--print all the values of keys
print(d1.values())
#items()--print key value pairs
print(d1.items())
for t in d.items():
    print(t)

