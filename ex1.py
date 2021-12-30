#program to find numbers divisible by 7 and 5 bw 1500 and 2700(both included)
for value in range(1500,2701):
    if(value%7==0 and value%5==0):
        print(value,end=" ")
    else:
        continue
