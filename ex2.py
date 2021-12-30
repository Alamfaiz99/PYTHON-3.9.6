ne=0
no=0
numbers=(1,2,3,4,5,6,7,8,9)
for value in numbers:
    if(value%2==0):
        ne+=1
    else:
        no+=1
print("total even numbers:",ne)
print("total odd numbers:",no)
