a=0
b=1
n=20
for x in range(1,n+1):
    c=a+b
    a=b
    b=c
    print(a)