#string:inbuilt datatype
#string immutable-means we can not add or del lements of strings on the same meory location
#string is ordered data structuer
#in python any thing enclosed in "" '' "' "' is string
s="python sample string"
#print(type(s))
#print(id(s))
#s="python"
#print(id(s))
#indentatioon shotcut-ctrl+alt+i
#for comment and uncomment-ctr
#1.indexing
#there are two types of indexing
#l-r 0--
#r-l-1--
s="python sample string"
print(s[0])
print(s[-1])
#print(s[100])
#error index out of range
#sclicing of string--substring-to find substring
print(s[0:5])
print(s[0:6])
print(s[7:])
print(s[:6])
#stride---advanced slicing/after a particular gap/increment
#mmeans after particular cap or multiple
print(s[::2])
print(s[::3])
#reverse string
print(s[::-1])
print(s[6:0])#it will show empty list of slicing
#iterating string
for value in s:
    print(value,end=" ")
for value in s[::2]:
    print(value,end=" ")
#built in functions of string
#format
print()
num1=100
num2=200
print("valueof  num1 is {} value of num2 {}".format(num1,num2))
#{}-placeholder
print("Value of num1 is{1} and value of num2 is{0}".format(num1,num2))
#placeholdaers with keywords
print("value of num1 is{val1} and value of num2 is{val2}".format(val1=num1,val2=num2))
#capitalize
s1="pyhton is good"
s2=s1.capitalize()
print(s2)
#upper,lower and title
s2=s1.title()
print(s2)
s2=s1.upper()
print(s2)
print(s1.isalnum())
#slipt and join
s="HTML,CSS,PYTHON,JAVA,DJANGO"
l=s.split(",")
print(l)
#join-is the opposite of split
s=(",").join(l)
print(s)
#maketrans and translate-make trans do the mapping
#translate do the actual translate
#for example
s1="abcd"
s2="1234"
s3="Python sample string abcd"
table=str.maketrans(s1,s2)
result=s3.translate(table)
print(result)
