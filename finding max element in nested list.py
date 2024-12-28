a=[[2,3,4,5],[0,4,7]]
for x in a:
    max=a[0][0]
    for y in x:
        if max<y:
            max=y
    print(max)