a=[11,22,33]
b=[]
for x in a:
    sum=0
    while(x!=0):
        s=x%10
        sum=sum+s
        x=x//10
    b.append(sum)
print(b)