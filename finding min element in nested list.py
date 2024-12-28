a=[[2,3,4,5],[0,4,7]]
for x in a:
    min=a[0][0]
    for y in x:
        if min>y:
            min=y
    print(min)