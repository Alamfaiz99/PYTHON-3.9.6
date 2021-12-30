#finding factorial of n
n=3
fact=1
if n==0 or n==1:
    fact=1
else:
    while n>1:
       fact*=n
       n-=1
print(fact)
    
