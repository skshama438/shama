a=100
b=1000
for x in range(a,b+1):
    sum=0
    temp=x
    while(x!=0):
        s=x%10
        sum=sum+s**3
        x=x//10
    if sum==temp:
        print(temp)