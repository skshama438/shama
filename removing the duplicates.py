a=[3,4,5,5,4,2]
c=[]
for x in a:
    if x not in c:
        c.append(x)
print("the list after removed the duplicates",c)