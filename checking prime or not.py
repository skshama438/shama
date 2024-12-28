a=10
count=0
for x in range(1,a+1):
    if a%x:
        count=count+1

if count==1:
    print("it is a prime number")
else:
    print("it is not a prime number")