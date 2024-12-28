a=int(input("enter a number:345"))
count=0
while(a!=0):
    s=a%10
    count=count+1
    a=a//10
print(count)