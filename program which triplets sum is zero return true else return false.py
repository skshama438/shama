a=[[1,2,-3],[4,0,-4],[0,1,-5],[1,1,1],[-2,4,-1]]
b=[]
for x in a:
    sum=0
    for y in x:
        sum=sum+y
    if sum==0:
       b.append(True)
    else:
       b.append(False)
print(b)