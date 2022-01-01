#l=[100,200,300,400,500]
#mathematical functions
#sum(l)--argument must be iterable data type
#max(l)--iterable
#min(l)--iterable
#print(sum(l))
#print(max(l))
#print(min(l))

#round(num)--round off a particular no.
num1=25.555
print(round(num1,2))

#these are present in built i nmodule
#print(dir(__builtins__))
 #if you wants dis. also
#help(__builtins__)


#working on math module
#firstly we have to import it
import math

l=[0.1]*10
print(l)
print(sum(l))#get wrong ans sum works on integer


#for floating addition
#if you use any module function than you have to write module name foloed by .
print(math.fsum(l))

#15 16
#floor()--lower bound
#ceil--upper bound

print(math.floor(15.5559),math.ceil(15.5559))


#sqrt(num)--gives the square root

print(math.sqrt(49))

#factorial(num)--gives the factorial of number

print(math.factorial(1000))

#modf()--seperates decimal and integer parts

num1=15.5559
print(math.modf(num1))

d,i=math.modf(num1)
print(d,i)

#power of any number

print(math.pow(10,2))

#math module also mprovides the loagrithmic methods as well

print(math.log(10,2))#log 10 base 2

print(math.log10(2))
print(math.log2(10))

#for trigonometri nctions pythom provides the trigo

#sin,cos tan--takes input in radian

print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))

#help(math)
#print(dir(math))



#for generating random numbers we use random module
#first we have to import it

import random
#random()--always getrandom no. betw 0-1
print(random.random())
#choice method--to chose random no. from list
l=[1,2,3,4,5,6]
print(random.choice(l))

#randint(10,100)--to get random no. bw the range
#end is inclusive
print(random.randint(10,100))

#randrange()--end is not inclusive

print(random.randrange(10,100))


#uniform()--generate floating point randon number

print(random.uniform(10,100))
























