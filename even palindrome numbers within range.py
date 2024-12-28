a=100
b=[]
for x in range(1,a):
    reverse=0
    temp=x
    while(x!=0):
        s=x%10
        reverse=reverse*10+s
        x=x//10
    if(temp==reverse)&(temp%2==0):
        b.append(temp)
print(b)