a=248
product=1
count=0
while(a!=0):
    s=a%10
    if s%2!=0:
        product=product*s
        count=1
    a=a//10
if count==1:
    print(product)
else:
    print("0")