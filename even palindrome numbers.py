a=[44,51,22,12,101,202]
b=[]
for x in a:
    reverse=0
    temp=x
    while(x!=0):
        s=x%10
        reverse=reverse*10+s
        x=x//10
    if(temp==reverse)&(temp%2==0):
        b.append(temp)
print(b)