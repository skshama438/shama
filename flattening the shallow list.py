a=[[1, 2, 3], [4, 5, 6], 7, 8]
c=[]
for x in a[:]:
    if type(x)==list:
        for y in x:
           c.append(y)
    else:
        c.append(x)
print(c)