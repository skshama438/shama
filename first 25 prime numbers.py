a=25
for x in range(1,a+1):
    count=0
    for y in range(1,x):
        if x%y==0:
            count=count+1
    if count==1:
        print(x)